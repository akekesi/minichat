#!/bin/bash

venv=.venv_minichat

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv

# message
echo
echo "'$venv' is unset."
