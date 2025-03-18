import MaterialX
import os
import argparse

def getMaterialXLocation():
    ini_location = MaterialX.__file__
    folder_path = os.path.dirname(ini_location)
    print('Found MaterialX at: ' + folder_path)
    return folder_path

def main():
    getMaterialXLocation()

if __name__ == '__main__':
    main()