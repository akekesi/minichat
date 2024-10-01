# MiniChat
![Status](https://img.shields.io/badge/status-in_progress-yellow.svg)

## Table of Contents
1. [About](#about)
1. [Usage](#usage)
1. [ToDo](#todo)

## About
Please note that this project is a work in progress. Some features may not be fully implemented or documented yet.

## Usage
### Python 3.12.0
```
https://www.python.org/downloads/release/python-3120/
```
### OpenAI API Key
```
https://platform.openai.com/api-keys
```
### Python Packages  
- With Virtual Environment (using shell script):
```
$ . venv_setup.sh arg1 arg2
```
&emsp;&emsp;&emsp;*arg1*:&emsp;the first suffix of the name of the virtual environment  
&emsp;&emsp;&emsp;*arg2*:&emsp;if it equals "dev"*, the second suffix will be "dev" and the requirements_dev.txt will be installed too.  
-  Without Virtual Environment:
```
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ pip install -r requirements_dev.txt
```
### Run MiniChat:
```
$ python -m src.minichat
```
### Execute pylint (only with requirements_dev.txt):
```
$ pylint src/<name_of_file>
```
### Execute single unittest (only with requirements_dev.txt):
```
$ python -m test.test_logger_00
$ python -m test.<name_of_test_file>
```
### Execute every unittest (only with requirements_dev.txt):
```
$ python -m unittest discover test
```
### Execute coverage using unittest (only with requirements_dev.txt):
```
$ python -m coverage run -m unittest discover test
$ python -m coverage report
$ python -m coverage html
```
### Coverage html report: htmlcov\class_index.html

## ToDo
- [ ] tests for GUI (using mocks)
- [ ] tests for logger (stdout)
- [ ] add video about usage
- [ ] finish README.md

<!--
just ideas:
1. [Description](#description)
1. [Getting Started](#getting_started)
1. [Installation](#installation)
1. [Authors](#authors)
1. [ToDo](#todo)
-->
<!--
just ideas:
## About/Description
## Demo

## Getting Started
### Dependencies
### Installing
### Executing program/Usage

## Help
## Authors
## Version History
## License
## Acknowledgments
## ToDo
-->
