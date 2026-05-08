#!/bin/bash

# Check if setup or cleanup arg
if [[ "$1" == "setup" ]]; then
    echo "Setting up the environment..."
    # Set up venv/ virtual environment and activete it
    python -m venv venv
    # Check if windows or linux
    if [[ "$OSTYPE" == "msys" ]]; then
        source venv/Scripts/activate
    else
        source venv/bin/activate
    fi

    # Ensure pip and all required packages are installed
    #python -m pip install --upgrade pip    
    python -m pip install -r requirements.txt


elif [[ "$1" == "cleanup" ]]; then
    echo "Cleaning up the environment..."
    # Check if windows or linux
    if [[ "$OSTYPE" == "msys" ]]; then
        deactivate
    else
        deactivate
    fi  
else
    echo "Usage: $0 [setup|cleanup]"
fi

