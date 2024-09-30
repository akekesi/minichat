#!/bin/bash

# arguments
suffix=""
if [ "$1" != "" ]; then
    suffix="_$1"
fi

# variables
name="minichat$suffix"
venv=".venv_minichat_exe$suffix"
python_required="Python 3.12.0"
python_current=$(python --version 2>&1)
requirements="requirements.txt"
requirements_dev="requirements_dev.txt"

# python version check
if [[ "$python_current" != *"$python_required"* ]]; then
    echo "Virtual environment '$venv' is not created."
    echo "Python version current:  $python_current"
    echo "Python version required: $python_required"
    return 0
fi

# create directory if it doesn't exist
if [ ! -d "./exe/$name" ]; then
    mkdir -p "./exe/$name"
else
    echo "Directory 'exe/$name' already exists."
    return 0
fi

# create virtual environment
if [ ! -d "$venv" ]; then
    python -m venv "$venv"
else
    echo "Virtual environment '$venv' already exists."
    return 0
fi

# activate virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    . "$venv/Scripts/activate"
else
    echo "Virtual environment '$venv' is already activated."
    return 0
fi

# upgrade pip and install requirements
python -m pip install --upgrade pip > /dev/null 2>&1
pip install -r "$requirements" > /dev/null 2>&1
pip install -r "$requirements_dev" > /dev/null 2>&1

# build executable with pyinstaller
pyinstaller --noconfirm --onedir --windowed \
    --icon "ico/minichat.ico" \
    --add-data "ico;ico/" \
    --add-data "list;list/" \
    --add-data "log;log/" \
    --add-data "png;png/" \
    --distpath "exe/$name" \
    "src/minichat.py" > /dev/null 2>&1

# deactivate virtual environment
if [[ ! -z "$VIRTUAL_ENV" ]]; then
    deactivate
fi

# delete the virtual environment after use
rm -rf "$venv"

# wait for 3 seconds to avoid 'permission denied' of the next mv commands
sleep 3

# move and rename exe and dependencies
rm -rf ./exe/"$name"/minichat/_internal/log/*
mv ./exe/"$name"/minichat/* ./exe/"$name"/
mv ./exe/"$name"/minichat.exe ./exe/"$name"/"$name".exe
rm -rf ./exe/"$name"/minichat
rm -rf ./build
rm -rf ./minichat.spec

# message indicating completion
echo
echo "Executable 'exe/$name/$name.exe' is created."
