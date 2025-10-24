pushd ../pymaterialx
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -lf 'libraries' -al
python mtlx_nodedef_inspect.py -op ../documents/source_reference/ -lf 'libraries' -al
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -ip downloaded_release_libraries/v1.39.4/MaterialX-1.39.4 -lf 'libraries' -al
python mtlx_nodedef_inspect.py -op ../documents/source_reference/ -ip downloaded_release_libraries/v1.39.4/MaterialX-1.39.4 -lf 'libraries' -al
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -ip downloaded_release_libraries/v1.39.3/MaterialX-1.39.3 -lf 'libraries' 
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -ip downloaded_release_libraries/v1.39.2/MaterialX-1.39.2 -lf 'libraries' 
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -ip downloaded_release_libraries/v1.39.1/MaterialX-1.39.1 -lf 'libraries' 
python mtlx_nodedef_inspect.py -ng -op ../documents/source_reference/ -ip externalLibraries
popd
python mdhtml.py ../documents_internal/TreeVisualizer.html -t template.html --top ".." -o ../documents -of TreeVisualizer.html
cp ../documents_internal/TreeVisualizer.js ../documents/TreeVisualizer.js
