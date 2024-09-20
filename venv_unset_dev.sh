#!/bin/bash

# arguments
suffix=""
if [ "$1" != "" ]; then
    suffix+=_$1
fi
if [ "$2" == "dev" ]; then
    suffix+=_$2
fi

# variables
venv=".venv_minichat$suffix"

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# delete venv
rm -rf $venv

# message
echo
echo "'$venv' is unset."
