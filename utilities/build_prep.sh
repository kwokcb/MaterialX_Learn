
if [ -z "$1" ]; then
    echo "No argument supplied. Please provide the path the MaterialX package."
    return
else
    PYTHON_PACKAGE_LOCATION=$1
fi

echo "--------- Building Python Package"
pushd "$PYTHON_PACKAGE_LOCATION"
pip install .
popd

echo "--------- Copying Python files to ../pymaterialx/python"
rm -rf ../pymaterialx/python
cp -R "$PYTHON_PACKAGE_LOCATION" ../pymaterialx/
rm -rf ../pymaterialx/python/MaterialX.egg-info/
rm -rf ../pymaterialx/python/build/
rm -rf ../pymaterialx/python/dist/
echo "--------- Finished copying Python files to ../pymaterialx/python"

