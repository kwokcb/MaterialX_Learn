python ../pymaterialx/compareVersions.py ../resources/libraries_1.39.1 --sourceLibrary ../pymaterialx/python/MaterialX/libraries > ../resources/mtlx_1391_vs_1392.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.39.0 --sourceLibrary ../resources/libraries_1.39.1 > ../resources/mtlx_1390_vs_1391.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.0 --sourceLibrary ../resources/libraries_1.39.0 > ../resources/mtlx_1380_vs_1390.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.9 --sourceLibrary ../resources/libraries_1.39.0 > ../resources/mtlx_1389_vs_1390.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.8 --sourceLibrary ../resources/libraries_1.38.9 > ../resources/mtlx_1388_vs_1389.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.7 --sourceLibrary ../resources/libraries_1.38.8 > ../resources/mtlx_1387_vs_1388.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.6 --sourceLibrary ../resources/libraries_1.38.7 > ../resources/mtlx_1386_vs_1387.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.5 --sourceLibrary ../resources/libraries_1.38.6 > ../resources/mtlx_1385_vs_1386.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.4 --sourceLibrary ../resources/libraries_1.38.5 > ../resources/mtlx_1384_vs_1385.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.3 --sourceLibrary ../resources/libraries_1.38.4 > ../resources/mtlx_1383_vs_1384.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.2 --sourceLibrary ../resources/libraries_1.38.3 > ../resources/mtlx_1382_vs_1383.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.1 --sourceLibrary ../resources/libraries_1.38.2 > ../resources/mtlx_1381_vs_1382.md
python ../pymaterialx/compareVersions.py ../resources/libraries_1.38.0 --sourceLibrary ../resources/libraries_1.38.1 > ../resources/mtlx_1380_vs_1381.md

python mdhtml.py ../resources/mtlx_1391_vs_1392.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1390_vs_1391.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1380_vs_1390.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1389_vs_1390.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1388_vs_1389.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1387_vs_1388.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1386_vs_1387.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1385_vs_1386.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1384_vs_1385.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1383_vs_1384.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1382_vs_1383.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1381_vs_1382.md -t template.html --top ".." -o ../documents
python mdhtml.py ../resources/mtlx_1380_vs_1381.md -t template.html --top ".." -o ../documents