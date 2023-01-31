'''
    Test example to load in libraries and print out
    the library files loaded.
'''
import sys, os, argparse
import MaterialX as mx

def main():
    parser = argparse.ArgumentParser(description="Test loading libraries.")
    parser.add_argument("--libraryPath", help="Path for MaterialX libraries.")

    opts = parser.parse_args()

    # Assuming we are running from the install localtion for MaterialX
    # This will loade in all files found under the `libraries` folder
    # into a document called `stdlib`
    libraryPath = mx.FilePath('libraries')
    # Check for library path on input args
    if opts.libraryPath:
        libraryPath = opts.libraryPath
    stdlib = mx.createDocument()
    searchPath = mx.FileSearchPath()
    libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

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
