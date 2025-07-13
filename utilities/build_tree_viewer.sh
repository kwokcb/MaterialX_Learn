pushd ../pymaterialx
python mx_nodef_introspection.py -ng
python mx_nodef_introspection.py
popd
cp ../pymaterialx/nodedef_introspection.json ../documents/nodedef_introspection.json
python mdhtml.py ../documents_internal/TreeVisualizer.html -t template.html --top ".." -o ../documents -of TreeVisualizer.html
cp ../documents_internal/TreeVisualizer.js ../documents/TreeVisualizer.js
