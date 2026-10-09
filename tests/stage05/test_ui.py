"""Browser tests for the stage05 UI (requires: playwright install chromium)."""
import pytest
from playwright.sync_api import Page, expect

from app.stage05 import data

pytestmark = pytest.mark.ui


@pytest.fixture
def map_page(page: Page, live_server_url):
    # Tiles are irrelevant to behaviour and slow/flaky; block them.
    page.route("**/tile.openstreetmap.org/**", lambda route: route.abort())
    page.goto(live_server_url + "/")
    try:
        page.wait_for_selector(".pint-icon", timeout=15000)
    except Exception:
        pytest.skip("Leaflet CDN unreachable")
    return page


def set_slider(page: Page, slider_id: str, value):
    page.evaluate(
        """([id, v]) => {
            const el = document.getElementById(id);
            el.value = v;
            el.dispatchEvent(new Event('input'));
        }""",
        [slider_id, value],
    )


def test_title_and_subtitle(map_page):
    expect(map_page.locator("h1")).to_have_text("Merseyside Real Ale Pubs")
    expect(map_page).to_have_title("Merseyside Real Ale Pubs")


def test_one_pint_icon_per_pub(map_page):
    total = len(data.load_pubs())
    expect(map_page.locator(".pint-icon")).to_have_count(total)
    expect(map_page.locator("#count")).to_have_text(f"Showing {total} of {total} pubs")


def test_map_fills_remaining_window(map_page):
    box = map_page.locator("#map").bounding_box()
    assert box["height"] > 400 and box["width"] >= 1000


def test_legend_is_visible(map_page):
    legend = map_page.locator(".legend")
    expect(legend).to_be_visible()
    expect(legend).to_contain_text("Colour = review rating")
    expect(legend).to_contain_text("Size = real ales")


def test_icons_vary_in_size_and_colour(map_page):
    sizes = map_page.eval_on_selector_all(
        ".pint-icon svg", "els => els.map(e => e.getAttribute('width'))")
    fills = map_page.eval_on_selector_all(
        ".pint-icon svg path:nth-of-type(2)", "els => els.map(e => e.getAttribute('fill'))")
    assert len(set(sizes)) > 1
    assert len(set(fills)) > 1
    assert min(map(int, sizes)) == 28 and max(map(int, sizes)) == 56


def test_min_rating_filter_hides_pubs(map_page):
    pubs = data.load_pubs()
    threshold = 9.0
    expected = sum(p["review_rating"] >= threshold for p in pubs)
    assert 0 < expected < len(pubs)
    set_slider(map_page, "minRating", threshold)
    expect(map_page.locator(".pint-icon")).to_have_count(expected)
    expect(map_page.locator("#count")).to_have_text(
        f"Showing {expected} of {len(pubs)} pubs")


def test_min_ales_filter_hides_pubs(map_page):
    pubs = data.load_pubs()
    threshold = 8
    expected = sum(p["real_ales_available"] >= threshold for p in pubs)
    assert 0 < expected < len(pubs)
    set_slider(map_page, "minAles", threshold)
    expect(map_page.locator(".pint-icon")).to_have_count(expected)


def test_filters_combine_and_reset(map_page):
    pubs = data.load_pubs()
    set_slider(map_page, "minRating", 9.0)
    set_slider(map_page, "minAles", 8)
    expected = sum(p["review_rating"] >= 9.0 and p["real_ales_available"] >= 8 for p in pubs)
    expect(map_page.locator(".pint-icon")).to_have_count(expected)
    set_slider(map_page, "minRating", 0)
    set_slider(map_page, "minAles", 0)
    expect(map_page.locator(".pint-icon")).to_have_count(len(pubs))


def test_hover_shows_tooltip_with_details(map_page):
    map_page.locator(".pint-icon").first.hover(force=True)
    tooltip = map_page.locator(".leaflet-tooltip.pub-tooltip")
    expect(tooltip).to_be_visible()
    expect(tooltip).to_contain_text("Real Ales Available")
    expect(tooltip).to_contain_text("Review Rating")


def test_click_opens_pinned_popup_and_closes(map_page):
    map_page.locator(".pint-icon").first.click(force=True)
    popup = map_page.locator(".leaflet-popup")
    expect(popup).to_be_visible()
    expect(popup.locator(".hdr")).not_to_be_empty()
    expect(popup).to_contain_text("Location")
    # The hover tooltip is dismissed while the popup is open.
    expect(map_page.locator(".leaflet-tooltip")).to_have_count(0)
    map_page.locator(".leaflet-popup-close-button").click()
    expect(popup).to_have_count(0)


def test_no_javascript_errors(page: Page, live_server_url):
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.route("**/tile.openstreetmap.org/**", lambda route: route.abort())
    page.goto(live_server_url + "/")
    page.wait_for_timeout(1500)
    assert errors == []


@pytest.mark.parametrize("size", [(1200, 800), (1000, 600), (390, 700)])
def test_every_tooltip_stays_inside_map(page: Page, live_server_url, size):
    page.set_viewport_size({"width": size[0], "height": size[1]})
    page.route("**/tile.openstreetmap.org/**", lambda route: route.abort())
    page.goto(live_server_url + "/")
    try:
        page.wait_for_selector(".pint-icon", timeout=15000)
    except Exception:
        pytest.skip("Leaflet CDN unreachable")
    page.wait_for_timeout(500)
    map_box = page.locator("#map").bounding_box()
    tooltip = page.locator(".leaflet-tooltip")
    for i in range(page.locator(".pint-icon").count()):
        page.mouse.move(0, 0)
        expect(tooltip).to_have_count(0)
        page.locator(".pint-icon").nth(i).hover(force=True)
        expect(tooltip).to_have_count(1)
        page.wait_for_timeout(100)
        box = tooltip.bounding_box()
        name = tooltip.locator(".hdr").inner_text()
        assert box["x"] >= map_box["x"], f"{name} overflows left"
        assert box["y"] >= map_box["y"], f"{name} overflows top"
        assert box["x"] + box["width"] <= map_box["x"] + map_box["width"], f"{name} overflows right"
        assert box["y"] + box["height"] <= map_box["y"] + map_box["height"], f"{name} overflows bottom"
