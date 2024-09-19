#!/bin/bash

# variables
venv=.venv_minichat_dev
python_required="Python 3.12.0"
python_current=$(python --version 2>&1)
requirements=requirements.txt
requirements_dev=requirements_dev.txt

# python version
if [[ $python_current != *"$python_required"* ]]; then
    echo "Virtual environment '$venv' is not created."
    echo "Python version current:  $python_current"
    echo "Python version required: $python_required"
    return 0
fi

# create venv
if [ ! -d $venv ]; then
    python -m venv $venv
else
    echo "Virtual environment '$venv' already exists."
    return 0
fi

# activate venv
if [[ -z $VIRTUAL_ENV ]]; then
    . $venv/Scripts/activate
else
    echo "Virtual environment '$venv' is already activated."
    return 0
fi

# pip install
python -m pip install --upgrade pip > /dev/null
pip install -r $requirements > /dev/null
pip install -r $requirements_dev > /dev/null

# deactivate venv
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

# message
echo
echo "'$venv' is setup."
echo "Command to activate or deactivate '$venv':"
echo "Activation:   . $venv/Scripts/activate"
echo "Deactivation: deactivate"
