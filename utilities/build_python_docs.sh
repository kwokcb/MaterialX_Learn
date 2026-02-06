echo "Building Python Documentation"
echo "- Note: This script shoudl be run on Mac to include Python docs for MSL"
python ../pymaterialx/mtlx_python_docs2.py -o ../documents_internal
python mdhtml.py ../documents_internal/Python_1_39_5_documentation.html -t template.html --top ".." -o ../documents -of documents/Python_1_39_5_documentation.html --removeMermaid True

