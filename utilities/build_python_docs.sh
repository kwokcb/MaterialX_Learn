echo "Building Python Documentation"
#echo "- Note: This script shoudl be run on Mac to include Python docs for MSL"
#python ../pymaterialx/mtlx_python_docs2.py -o ../documents_internal
#python mdhtml.py ../documents_internal/python_docs/html/index.html -t template.html --top ".." -o ../documents -of documents/python_docs/html/index.html --removeMermaid True
pushd .
cd ../pymaterialx/sphinx
source build_it.sh
popd
