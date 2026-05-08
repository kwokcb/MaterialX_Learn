#!/bin/bash

# Rebuils RST files
python makerst.py

# Build the documentation
python -m sphinx -b html . ../../documents/python_docs/html

