#!/bin/bash

# Ensure pip and all required packages are installed
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Build the documentation
python -m sphinx -b html sphinx sphinx/_build/html