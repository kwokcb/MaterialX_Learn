rm -rf ./mtlxutils
cp -R ../pymaterialx/mtlxutils .
python mxdoclib.py --compareLib ../resources/ --docType html --nodegraph --outputPath ../documents/definitions --outputFile all_definitions ../pymaterialx/python/MaterialX/libraries
python mxdoclib.py --compareLib ../resources/ --docType html --nodegraph --outputPath ../documents/definitions  ../pymaterialx/python/MaterialX/libraries --outputFile definitions_by_group --separateFiles True

python mxdoclib.py --docType md --nodegraph --outputPath ../documents/definitions  ../pymaterialx/python/MaterialX/libraries/stdlib --outputFile stdlib_doc
python mxdoclib.py --docType md --nodegraph --outputPath ../documents/definitions  ../pymaterialx/python/MaterialX/libraries/pbrlib --outputFile pbrlib_doc 
python mxdoclib.py --docType md --nodegraph --outputPath ../documents/definitions  ../pymaterialx/python/MaterialX/libraries/bxdf --outputFile bxdf_doc 

source build_compare.sh

python mdhtml.py ../documents_internal/index.html -t template.html --top "." -o ../ -of index.html --removeMermaid True
python mdhtml.py ../documents_internal/about.html -t template.html --top ".." -o ../documents -of about.html
cp ../documents_internal/about.md ../
python mdhtml.py ../documents_internal/presentations.md -t template.html --top ".." -o ../documents -of presentations.html
python mdhtml.py ../documents_internal/design.html -t template.html --top ".." -o ../documents -of design.html
python mdhtml.py ../documents_internal/workflow_gltf.html -t template.html --top ".." -o ../documents -of workflow_gltf.html
python mdhtml.py ../documents_internal/workflow_ocio.html -t template.html --top ".." -o ../documents -of workflow_ocio.html
python mdhtml.py ../documents_internal/workflow_usd.html -t template.html --top ".." -o ../documents -of workflow_usd.html
python mdhtml.py ../documents_internal/implementation.html -t template.html --top ".." -o ../documents -of implementation.html
python mdhtml.py ../documents_internal/documents.html -t template.html --top ".." -o ../documents -of documents.html
python mdhtml.py ../documents_internal/hosting.html -t template.html --top ".." -o ../documents -of hosting.html
python mdhtml.py ../documents_internal/mtlx_utilities.html -t template.html --top ".." -o ../documents -of mtlx_utilities.html
python mdhtml.py ../documents_internal/mermaidChecker.html -t template.html --top ".." -o ../documents -of mermaidChecker.html
python mdhtml.py ../documents_internal/using_library.html -t template.html --top ".." -o ../documents -of using_library.html
python mdhtml.py ../documents_internal/jupyter_example.html -t template.html --top ".." -o ../documents -of jupyter_example.html
python mdhtml.py ../documents_internal/nodes_and_nodegraphs.html -t template.html --top ".." -o ../documents -of nodes_and_nodegraphs.html
python mdhtml.py ../documents_internal/python_MaterialX.html -t template.html --top ".." -o ../documents -of python_MaterialX.html
python mdhtml.py ../documents_internal/node_definitions.html -t template.html --top ".." -o ../documents -of node_definitions.html
python mdhtml.py ../documents_internal/gltfViewer.html -t template.html --top ".." -o ../documents -of gltfViewer.html
python mdhtml.py ../documents_internal/property_editor_ui.md -t template.html --top ".." -o ../documents -of property_editor_ui.html

rm -rf ./mtlxutils