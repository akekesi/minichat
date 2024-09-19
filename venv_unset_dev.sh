#!/bin/bash

venv_name=.venv_minichat_dev

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv_name

# message
echo
echo "'$venv' is unset."
