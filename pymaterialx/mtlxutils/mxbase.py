import MaterialX as mx
'''
    Base MaterialX utilities
    - version checking

    Requires: MaterialX package
'''
def haveVersion(major, minor, patch):
    '''
    Check if the current vesion matches a given version
    ''' 
    imajor, iminor, ipatch = mx.getVersionIntegers()
    if imajor < major:
        return False
    if iminor < minor:
        return False
    if ipatch < patch:
        return False
    return True
