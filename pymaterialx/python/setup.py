from setuptools import setup
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def getRecursivePackageData(root):
    packageData = []
    for dirpath, dirnames, filenames in os.walk(root):
        relpath = os.path.relpath(dirpath, root)
        packageData.append(os.path.join(relpath, '*.*'))
    return packageData

setup(name='MaterialX',
      url='www.materialx.org',
      version='1.39.4',
      packages=['MaterialX'],
      package_data={'MaterialX' : getRecursivePackageData('MaterialX')},
      zip_safe = False)
