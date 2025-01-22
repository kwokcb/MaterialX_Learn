#pip install bpy --upgrade
#pip install usd-core --upgrade --quiet
#pip install xmltodict --quiet
#for file in *.ipynb; do
#    echo "------------------- Running notebook: $file.. --------------"
#    python -m jupyter execute --allow-errors --inplace "$file" 
#    echo "------------------------------------------------------------"
#done
#for file in *.ipynb; do
#    echo "Creating html $file..."
#    python -m jupyter nbconvert --to html "$file" > html_log.txt
#done
for file in *.ipynb; do
    echo "Creating Python $file..."
    python -m jupyter nbconvert --to python "$file" > python_log.txt
done
