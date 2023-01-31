'''
    Test example to check that MaterialX modules are available
    and will run.
'''
import MaterialX as mx

def main():
    # Create a document
    doc = mx.createDocument()

    # Print the version
    print('Hello MaterialX (Version %s)' % doc.getVersionString())    

if __name__ == '__main__':
    main()
