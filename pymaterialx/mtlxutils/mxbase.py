import MaterialX as mx

def haveVersion(major, minor, patch):
    """
    Check if the current vesion matches a given version
    """ 
    imajor, iminor, ipatch = mx.getVersionIntegers()
    if imajor < major:
        return False
    if iminor < minor:
        return False
    if ipatch < patch:
        return False
    return True
