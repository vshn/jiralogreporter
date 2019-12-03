# jiralogreporter

Print all JIRA worklog entries updated in the last month

## Requirements:
Python3.6+


## Install from this repository

```sh
pip3 install --user jiralogreporter
```

## Install the stable  release

```sh
pip3 install --user jiralogreporter
```

```sh
## How to use

# Create a JIRA env file
cat > jira_env << _EOF_
export JIRA_USERNAME=your_jira_username
export JIRA_SERVER=your_jira_server
_EOF_

# Load your env
source jira_env

# Run the report tool
jiralogreporter

```
