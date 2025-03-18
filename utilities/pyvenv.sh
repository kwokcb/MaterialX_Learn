#!/bin/bash
echo "Setting up virtual environment"

# Check if virtualenv is installed
if ! pip show virtualenv > /dev/null 2>&1; then
    echo "- Installing virtualenv"
    pip install virtualenv
else
    echo "- virtualenv already installed"
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "- Creating new virtual environment"
    virtualenv venv
else
    echo "- Using existing virtual environment (venv)"
fi

# Activate or deactivate the virtual environment based on the argument
if [ "$1" == "0" ]; then
    echo "- Deactivating virtual environment"
    deactivate
else
    echo "- Activating virtual environment"
    source venv/Scripts/activate
fi