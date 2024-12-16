pushd ../pymaterialx
rm -rfv ../resources/mtlx/nodedef_materials/*.mtlx
echo "Building MaterialX documents for nodedefs..."
python genMaterialsFromDefs.py ./python/MaterialX/libraries/ --outputPath ../resources/mtlx/nodedef_materials
echo "Rendering MaterialX documents for nodedefs..."
python renderDocuments.py ../resources/mtlx/nodedef_materials 
echo "Done rendering."
popd