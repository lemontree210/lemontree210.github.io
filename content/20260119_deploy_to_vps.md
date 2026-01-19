Title: Automating deployment to VPS from GitHub 
Date: 2026-01-19 11:00
Category: Automation
Tags: Automation, CI/CD, GitHub Actions, Workflow Automation, Deployment, VPS, Nginx, systemd

In [my previous post](20260111_repository_dispatch.md), I described a workflow that connects data with an app that visualizes the data.

There's one step left: automatically deploying the web app from GitHub to a server after every push to the repo's default branch.

<!-- PELICAN_END_SUMMARY -->

I will not describe the details of setting up Nginx and generating an SSL certificate, as I did it in [my post about n8n](20250615_n8n.md).

To keep things simple on my server, I set up my web app as a systemd-managed service.

The main task in this workflow was enabling GitHub Actions to trigger an update on the server.

There are several possible ways of doing it. I chose to let a GitHub Action access the server over SSH and run the update as if I had logged in and executed the script manually.

To do so, I generated a dedicated SSH key pair for GitHub Actions, stored the private key as a GitHub Actions secret, and added the public key to the deploy user’s `authorized_keys` on the VPS.

Next, I allowed a user on the VPS that my GitHub Action logs in as to run one `sudo` command without a password prompt: `sudo systemctl restart <name of service>`. Without this, the jobs would fail because `sudo` would prompt for a password.

To do so, I edited sudoers by running 

```commandline
sudo visudo
```
and adding this line:
```ini
<username> ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart <name of my service>
```

So now, GitHub Actions can connect to my server, run commands for checking out the latest version of my repo and then run a bash script for re-loading the web app.

### Resulting workflow

Items 1-3 on the list are from [the previous post](20260111_repository_dispatch.md)

1. [The trigger half of the workflow in the data repo](https://github.com/Jazyki-Mira/langworld_db_data/blob/master/.github/workflows/dispatch-web.yml) runs on every push to the `master` branch.
1. It sends a [`repository_dispatch`](https://docs.github.com/actions/learn-github-actions/events-that-trigger-workflows#repository_dispatch) event to [`Jazyki-Mira/langworld_db_pyramid`](https://github.com/Jazyki-Mira/langworld_db_pyramid). It uses Peter Evans's [Repository Dispatch](https://github.com/peter-evans/repository-dispatch) GitHub Action that calls the [GitHub API](https://docs.github.com/en/rest/repos/repos#create-a-repository-dispatch-event).
1. In [the web repo workflow](https://github.com/Jazyki-Mira/langworld_db_pyramid/blob/master/.github/workflows/update-langworld-subtree.yml), I catch the event and run an update of the git subtree, then create a new commit in the web repo. Note `on: repository_dispatch` at the top of the YAML file.
1. In [another web repo workflow](https://github.com/Jazyki-Mira/langworld_db_pyramid/blob/master/.github/workflows/deploy-prod.yml) I log into my VPS (note that all sensitive data is provided via secrets) and run my bash script that performs necessary operations (like applying database migrations, populating the database, compiling strings for i18n).

The result: The time from pushing to the data repo to the web app being updated on the server is **just under 1 minute**. With no manual intermediate operations from my side.

### Example

Manual action:

- Made [a commit](https://github.com/Jazyki-Mira/langworld_db_data/commit/3db911f7ef7e7ee6a799b4e6d62fa21006f6918d) in the **data** repo to fix a typo in the data.

Subsequent automatic actions:

- [GitHub Action](https://github.com/Jazyki-Mira/langworld_db_data/actions/runs/21059018003/job/60560903175) was run in the **data** repo to dispatch an update to `langworld_db_pyramid`. **Run time: 4 seconds**.
- [GitHub Action](https://github.com/Jazyki-Mira/langworld_db_pyramid/actions/runs/21058683781) was triggered by the `repository_dispatch` event and run in the **web** repo. **Run time: 18 seconds**.
- [GitHub Action](https://github.com/Jazyki-Mira/langworld_db_pyramid/actions/runs/21059027305) was triggered by a push to the main branch in the **web** repo and deployed the updated code to the VPS. **Run time: 32 seconds**.

**Total run time: 54 seconds**.

I can only guess how much time and procrastination it would have taken me to do this without my 12-week-year plan.
