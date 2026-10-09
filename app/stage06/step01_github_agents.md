# Step 1 – Set up Copilot agents on GitHub

**Goal:** Show how GitHub works with Copilot by setting up the cloud agent on the repository. No application code changes in this stage.

## Do
1. In the repository, open **Settings → Copilot** and confirm the Copilot cloud agent is enabled.
2. Add `.github/copilot-instructions.md` with the project conventions, for example "Python 3, run tests with `python -m pytest`, keep the app in `app/`".
3. Add `.github/workflows/copilot-setup-steps.yml` with a job named `copilot-setup-steps` that checks out the repo, sets up Python and runs `pip install -r requirements.txt`. This preinstalls the tools the agent needs.
4. Create an issue describing a small change, such as "Add a filter by rating to the map".
5. Assign the issue to **Copilot**, then watch the session log as it works.
6. Review the pull request it opens: read the diff, leave a comment asking for a change, and merge when happy.

## Say
"We describe the work in an issue, and the agent plans, codes and opens a pull request for us to review, the same as for any teammate."

## Next
Step 2 – automate running the tests on GitHub with Actions.
