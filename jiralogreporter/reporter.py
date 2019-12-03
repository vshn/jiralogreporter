#!/usr/bin/python3
import subprocess
import os
from getpass import getpass
from jira import JIRA


def print_log():
    username = os.environ["JIRA_USERNAME"]
    jira_server = os.environ["JIRA_SERVER"]
    # TODO: Document the passwordless feature
    password = subprocess.getoutput(f"secret-tool lookup username {username}")
    if not password:
        password = getpass("Enter your JIRA Password:")
    if not password:
        exit(0)
    options = {"server": jira_server}
    user = username.split("@", 1)[0]
    jira = JIRA(options=options, auth=(user, password))
    search_query = "updated > startOfMonth() order by updated desc"

    for issue in jira.search_issues(search_query, fields="worklog", maxResults=1000):
        for log in issue.fields.worklog.worklogs:
            print(log.author.name, issue, log.started, log.timeSpent)
