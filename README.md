# jiralogreporter
jiralogreporter is a shell for Kubernetes users and administrators.


[![PyPi](https://img.shields.io/pypi/v/jiralogreporter.svg?style=flat-square)](https://pypi.python.org/pypi/jiralogreporter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

Planned features:

- Status bar:

- Kubernetes query commands:
  - [ ] list pods
  - [X] list namespaces
  - [X] list nodes

## How to use it

## Run from  the docker image
```bash
docker run --privileged -v "$HOME/.kube/config":/app/kube_config -it joaompinto/jiralogreporter
```

## Install using Python3.6+

## How to install
```sh
# Last Release
pip3 install --user jiralogreporter
# Development Release
pip3 install --user https://github.com/joaompinto/jiralogreporter/archive/master.zip
```
