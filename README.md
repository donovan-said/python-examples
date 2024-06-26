# python-examples

A repository to play around with the python, create examples, and collate useful
snippets found online.

- [python-examples](#python-examples)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [pipenv](#pipenv)
    - [pre-commit](#pre-commit)
  - [Examples](#examples)

## Requirements

| Tool                                       | Description                               |
| :----------------------------------------- | :---------------------------------------- |
| [Pipenv](https://pypi.org/project/pipenv/) | Required to manahe pip packages           |
| [pre-commit](https://pre-commit.com/)      | Used to ensure standards prior to commits |

## Setup

### pipenv

Pipenv is used to manage all python dependencies.

```shell
pip install pipenv
```

```shell
pipenv install -d
```

```shell
pipenv shell
```

### pre-commit

[pre-commit](https://pre-commit.com/) is used to enforce standards on this repository prior to committing any changes. This forms part of
our [Contributing](../CONTRIBUTING.md) standards. Please also see the
[pre-commit-config.yaml](../.pre-commit-config.yaml) file.

This is installed via the Pipfile, though this has to be initialised within this repository by running the below
command:

```shell
pre-commit install
```

## Examples

| Samples Code                                    | Description                               |
| :---------------------------------------------- | :---------------------------------------- |
| [Dictionaries](src/dictionaries/)               | Working with dictionaries                 |
| [List Comprehensions](src/list-comprehensions/) | Working with list comprehensions          |
| [HTTP](src/http/)                               | Working with the HTTP protocol            |
| [Websocket](src/websockets/)                    | Working with the Websockets protocol      |
| [Lambda](src/lambda/)                           | Working with lambda (anonymous) functions |
