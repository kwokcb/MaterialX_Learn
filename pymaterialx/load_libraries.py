'''
    Test example to load in libraries and print out the library files loaded.
'''
import sys, os, argparse
import MaterialX as mx

def main():
    parser = argparse.ArgumentParser(description="Test loading libraries.")
    parser.add_argument("--libraryPath", help="Path for MaterialX libraries.")

    opts = parser.parse_args()

    stdlib = mx.createDocument()
    libFiles = mx.loadLibraries(mx.getDefaultDataLibraryFolders(), mx.getDefaultDataSearchPath(), stdlib)

    # Create main document and import the library document
    doc = mx.createDocument()
    doc.importLibrary(stdlib)

    # Print out the names of the library files loaded
    if libFiles:
        for libFile in libFiles:
            print('Loaded library file: %s' % libFile)
    else:
        print('No library files loaded.')

if __name__ == '__main__':
    main()
