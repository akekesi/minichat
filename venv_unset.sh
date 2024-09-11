#!/bin/bash

venv_name=.venv_minichat

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv_name

# message
echo
echo "'$venv' is unset."
