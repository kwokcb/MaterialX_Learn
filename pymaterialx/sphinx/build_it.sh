#!/bin/bash

# Create the RST files used by Sphinx
echo "Generating RST files..."
python makerst.py

# Build the documentation
echo "Building HTML documentation..."
python -m sphinx -b html . ../../documents/python_docs/html

echo "Finished building documentation."
