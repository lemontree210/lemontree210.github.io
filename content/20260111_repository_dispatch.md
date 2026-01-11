Title: Connecting data to representation with GitHub Actions 
Date: 2026-01-11 12:20
Category: Automation
Tags: Automation, CI/CD, GitHub Actions, Workflow Automation

In any project that shows data to users, be it documentation or a linguistic database, data must be separated from its representation.

This is almost an axiom. You have to keep your data in an easy-to-edit, non-proprietary format, while the tools with which you show the data to users can be as complex as needed. Tools tend to get outdated, and your data cannot depend on them.
<!-- PELICAN_END_SUMMARY -->
In my [Jazyki Mira project](https://github.com/Jazyki-Mira), I have two actively maintained repositories: one for [data](https://github.com/Jazyki-Mira/langworld_db_data), one for [a web app](https://github.com/Jazyki-Mira/langworld_db_pyramid) that visualizes the data.

The web app could access the data via an API, and that would be the default workflow for many cases, but I decided against it as it would require an additional web server.

I went with `git subtree` (could have been `git submodule` as well): the web repo includes the data repo as a subtree.

When I update the data, I update the subtree, and the web app has fresh data to show. But, until recently, I did it manually. Now it's time to automate the process.

I used the `repository_dispatch` event to notify the web app repo of changes in the data repo. Here's how it works:

### Prerequisites

For the workflow to work, a secret is required, which I called `LANGWORLD_WEB_UPDATE_PAT`.

1. In Developer Settings of the organization, I created a fine-grained Personal Access Token (PAT) `LANGWORLD_WEB_UPDATE_PAT` with access to `Jazyki-Mira/langworld_db_pyramid` only and repository permissions `Contents: Read and write`.
1. I then added an Actions repository secret with the same name in both `langworld_db_data` and `langworld_db_pyramid`. The value of the secret is the value of the token that I pasted manually.
1. I will have to update secrets in both repos every year, once the token expires.

> #### Side notes
> 
> - Since I paste the value of the PAT manually, the name of the secret doesn't have to match the name of the PAT, but it's more convenient this way.
> - I can switch to an organizational secret, which would mean that I would only need to update the secret in one place instead of two.

### Workflow setup

1. [The trigger half of the workflow in the data repo](https://github.com/Jazyki-Mira/langworld_db_data/blob/master/.github/workflows/dispatch-web.yml) runs on every push to the `master` branch.
1. It sends a [`repository_dispatch`](https://docs.github.com/actions/learn-github-actions/events-that-trigger-workflows#repository_dispatch) event to [`Jazyki-Mira/langworld_db_pyramid`](https://github.com/Jazyki-Mira/langworld_db_pyramid). It uses Peter Evans's [Repository Dispatch](https://github.com/peter-evans/repository-dispatch) GitHub Action that calls the [GitHub API](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event).
1. In [the web repo workflow](https://github.com/Jazyki-Mira/langworld_db_pyramid/blob/master/.github/workflows/update-langworld-subtree.yml), I catch the event and run an update of the git subtree, then create a new commit in the web repo. Note `on: repository_dispatch` at the top of the YAML file.

> Note: `repository_dispatch` will only trigger a workflow run in `langworld_db_pyramid` if the workflow there is set up on the **default branch**.

### Example

Manual action:

- Made [a commit](https://github.com/Jazyki-Mira/langworld_db_data/commit/06bb2629f90a7e4d303e759209d0602950f62a2f) in the **data** repo to fix a typo in the data.

Subsequent automatic actions:

- [GitHub Action](https://github.com/Jazyki-Mira/langworld_db_data/actions/runs/20877364699) was run in the **data** repo to dispatch an update to `langworld_db_pyramid`.
- [GitHub Action](https://github.com/Jazyki-Mira/langworld_db_pyramid/actions/runs/20877366062) was triggered and run in the **web** repo.
- [A new commit was created](https://github.com/Jazyki-Mira/langworld_db_pyramid/commit/e8318e71a02c1190b5df171d93f7f36ef9ab0163)  in the **web** repo to reflect the change.

## What's next

Now I have to set up my web server to automatically pull the latest changes from the web repo and reinitialize the web app.

That's for the next post.
