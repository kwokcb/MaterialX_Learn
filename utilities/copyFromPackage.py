import MaterialX
import os
import argparse

def getMaterialXLocation():
    ini_location = MaterialX.__file__
    folder_path = os.path.dirname(ini_location)
    return folder_path

def copyMaterialXFiles(input_location, output_location):
    # Remove output location if it exists
    if os.path.exists(output_location):
        print("Removing existing output location")
        os.system('rm -rf ' + output_location)

        # Create the output location if it doesn't exist
        os.makedirs(output_location)
        
    # Copy all files in the MaterialX folder to the output location with a singe command
    print(f"Copying from: {input_location} to: {output_location}")
    os.system('cp -r ' + input_location + ' ' + output_location)

def main():
    # Get output location to copy files to using argparse


    parser = argparse.ArgumentParser(description='Copy installed MaterialX package to a specified location')
    parser.add_argument(dest='outputPath', help='Output Location.')
    args = parser.parse_args()

    output_location = args.outputPath
    input_location = getMaterialXLocation()
    copyMaterialXFiles(input_location, output_location)

# Call main()
if __name__ == '__main__':
    main()

