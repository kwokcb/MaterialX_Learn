#!/usr/bin/env python
'''
Print out all node types grouped by node group for all nodedefs in library definition documents
under a given root folder.
'''

import sys, os, argparse
import MaterialX as mx
import inspect
import pprint
import pydoc

def parseArgs():
    parser = argparse.ArgumentParser(description="Print out all node types grouped by node group for all nodedefs in library definition documents under a given root folder.")
    
    parser.add_argument('--interactive', action='store_true', default=False)
    (args, rest) = parser.parse_known_args()
    if args.interactive:
        try: readline.read_history_file()
        except: pass
        rest += input("Arguments: ").split(" ")  # Get input args
        try: readline.write_history_file()
        except: pass    

    print(rest)
    
    parser.add_argument(dest="inputFolder", help="Root folder for MaterialX definition documents.")
    opts = parser.parse_args(rest)
    return opts

# Find all MaterialX files
def getFiles(rootdir):
    filelist = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('mtlx'):
                filelist.append(os.path.join(subdir, file)) 
    return filelist

# Create a dictionary with node group as the primary key for a list of associated
# node types
def getNodeDictionary(inputFilenames):

    doc = mx.createDocument()
    for inputFilename in inputFilenames:
        try:
            mx.readFromXmlFile(doc, inputFilename)
        except mx.ExceptionFileMissing as err:
            print(err)
            sys.exit(0)

    nodegroups = { "" } 
    nodetypes = { "" }
    nodegroupdict = {}
    for nd in doc.getNodeDefs():
        nodestring = nd.getNodeString() 
        nodetypes.add( nodestring )
        nodegroup = nd.getNodeGroup()
        if not nodegroup:
            nodegroup = "no group"
        nodegroups.add( nodegroup )
        if not nodegroup in nodegroupdict.keys():
            nodegroupdict[nodegroup] = { nodestring }
        else:
            nodegroupdict[nodegroup].add(nodestring)

    return nodegroupdict;

# ------------------------------------------------------------
# pybind11 helpers
# ------------------------------------------------------------

def is_pybind_descriptor(value):
    return (
        hasattr(value, '__get__') and
        value.__class__.__module__ == 'pybind11_builtins'
    )


def resolve_static_value(cls, name):
    try:
        return getattr(cls, name)
    except Exception as e:
        return f"<unavailable: {e}>"


def format_value_old(value):
    try:
        return repr(value)
    except Exception:
        return "<unrepresentable>"
    
def format_value_old2(value):
    return_value = value
    try:
        mx_val = mx.Value.createValue(value)
        return_value =  mx_val.getValueString()
        print('------------- Use mx to create and get string value !!!!!!!!!!!!!!!', value, '-->', return_value)
    except Exception:
        print("------------- Failed to use mx to create and get string value !!!!!!!!!!!!!!!", value    )
        pass

    try:
        return_value = repr(value)
        print('------------- Use repr to get string value !!!!!!!!!!!!!!!', value, '-->', return_value)
    except Exception:
        print("------------- Failed to use repr to get string value !!!!!!!!!!!!!!!", value    )
        return_value = "<unrepresentable>"

    print('format_value:', return_value)
    return return_value


def format_value(value):
    # 1. Try MaterialX Value path (works for scalars, lists, tuples)
    try:
        mx_val = mx.Value.createValue(value)
        return mx_val.getValueString()
    except Exception:
        pass

    #print('******************** format value class name:', value.__class__.__name__)

    if not value or not value.__class__ or not value.__class__.__name__:
        return ''

    # 2. MaterialX matrix types...
    class_name = value.__class__.__name__

    if not class_name or class_name == 'NoneType':
        return ''
    
    #for attr in dir(value):
    #    print(f'   Attribute: {attr}')
    if class_name == 'dict':
        # Just get the keys
        keys = value.keys() 
        return '{ ' + ', '.join(f'{k}' for k in keys) + ' }'

    if class_name == 'tuple':
        return '( ' + ', '.join(v for v in value) + ' )'
    
    if value.__class__.__name__ in ('Matrix33', 'Matrix44'):
        return f'[ {value} ]'

    if value.__class__.__name__ in ('str'):
        return '\'' + value + '\''

    # 3. MaterialX vector / color types
    if hasattr(value, '__len__') and hasattr(value, '__getitem__'):
        return value
    
    # If it's a dict then get keys
    if isinstance(value, dict):
        keys = value.keys()
        return '{ ' + ', '.join(f'{k}' for k in keys) + ' }'
    if isinstance(value, (list, set)):
        return '[ ' + ', '.join(format_value(v) for v in value) + ' ]'

    # 4. Fallback
    try:
        if isinstance(value, property):
            doc = value.fget.__doc__ if hasattr(value, 'fget') and value.fget.__doc__ else 'no doc'
            # remove newlines and extra spaces
            doc_lines = doc.split('\n')
            stripped_lines = [line.strip() for line in doc_lines if line.strip()]
            joined_doc = ' '.join(stripped_lines)
            return f'property: {joined_doc}'

        repr_value = repr(value)
        if 'object at' in repr_value:
            return f' {type(value).__name__} instance'
        return repr(value)
    except Exception:
        return repr(value)



# ------------------------------------------------------------
# Introspection helpers
# ------------------------------------------------------------

def print_class_header(cls):
    indent = ' ' * 4
    print()
    print('# class', cls.__name__)

    if cls.__doc__:
        doc_lines = cls.__doc__.split('\n')
        print('#   Description:', doc_lines[0].strip())
        for line in doc_lines[1:]:
            print('# ', line.strip())

    print('#   Module:', cls.__module__)
    print(f'def {cls.__name__}():')
    #print(f'{indent}# Public members')


def print_method(cls, name, value):
    indent = ' ' * 4

    func = value
    if isinstance(value, (staticmethod, classmethod)):
        func = value.__func__

    try:
        argspec = inspect.getfullargspec(func)
        annotations = getattr(func, '__annotations__', {})
        arg_names = argspec.args

        if arg_names and arg_names[0] in ('self', 'cls'):
            arg_names = arg_names[1:]

        args = []
        for arg in arg_names:
            if arg in annotations:
                ann = annotations[arg]
                ann_name = ann.__name__ if hasattr(ann, '__name__') else str(ann)
                args.append(f"{arg}: {ann_name}")
            else:
                args.append(arg)

        arg_str = ', '.join(args)
    except Exception:
        arg_str = ''

    if arg_str:
        arg_str = 'self, ' + arg_str
    else:
        arg_str = 'self'

    print(f'\n{indent}#  Method: {name}')

    if func.__doc__:
        for line in func.__doc__.split('\n'):
            print(f'{indent}#   {line.strip()}')

    print(f'{indent}def {name}({arg_str}):')
    print(f'{indent*2}pass')


def print_data_member(cls, name, value):
    indent = ' ' * 4
    doc = value.__doc__ if hasattr(value, '__doc__') else ''
    #print(f'{indent}# Data member: {name}')
    if doc:
        print(f'{indent}# Description: {doc.strip()}')
    if is_pybind_descriptor(value):
        #print(f'>>>>>>>>>>>>>>>>>>>> class: {cls.__name__}, static property: {name}')
        actual = resolve_static_value(cls, name)
        #print(f' --------- actual value for static property {name}: {actual}')
        print(f'{indent}{name} = {format_value(actual)}')
        #print(f' ---- formattted value for static property {name}: {format_value(actual)}')
        #print('-------------------------------')
        return

    val_repr = format_value(value)

    if 'property:' in val_repr:
        # remove 'property:' prefix
        prop_doc = val_repr.replace('property:', '').strip()
        cls_name = value.__class__.__name__
        #print(f'  {name}  # Reference to <"{cls_name}" instance>. Value: "{val_repr}"')
        print(f'{indent}{name} # "{prop_doc}"')
    else:
        print(f'{indent}{name} = {val_repr}')


# ------------------------------------------------------------
# Main MaterialX inspection
# ------------------------------------------------------------

def parsePythonLib(module):
    use_pydoc = False

    for _, obj in inspect.getmembers(module, inspect.isclass):

        # Skip private/internal classes
        if obj.__name__.startswith('_'):
            continue

        if use_pydoc:
            print(pydoc.render_doc(obj))
            continue

        print_class_header(obj)

        class_dict = obj.__dict__

        for name, value in class_dict.items():

            if name == '_pybind11_conduit_v1_':
                continue

            if name.startswith('__') and name.endswith('__') and name not in ('__init__', '__new__'):
                continue

            if callable(value):
                print_method(obj, name, value)
                continue

            if inspect.isclass(value) or inspect.ismodule(value):
                continue

            print_data_member(obj, name, value)


# Parse python
def parsePythonLib_old(mx):
    print_private = False
    use_pydoc = False
    indent = ' ' * 4

    for o in inspect.getmembers(mx): 
        if inspect.isclass(o[1]):
            if (o[1].__name__ == 'Exception'):
            #pp.pprint(o[1].__dict__)
                print(o[1].__dict__)
            if use_pydoc:
                print(pydoc.render_doc(o[1], renderer=pydoc.HTMLDoc()))
            else:
                print(" ")
                print('# class ', o[1].__name__)
                doc_lines = o[1].__doc__.split('\n') if o[1].__doc__ else []
                first_line = True
                for line in doc_lines:
                    if first_line:
                        first_line = False  
                        print('#   Description:', line.strip())
                    else:
                        print('# ', line.strip())
                print('#   Module:', o[1].__module__)
                #print('#   Module:', o[1].__subclasses__)
                print('def', o[1].__name__, '():')
                print(f'{indent}# Public members')
                # Only include members defined directly on the class
                class_dict = o[1].__dict__
                for name, value in class_dict.items():
                    # Skip known internal members and unwanted dunder attributes
                    if name == '_pybind11_conduit_v1_':
                        continue
                    if name.startswith('__') and name.endswith('__') and name not in ('__init__', '__new__'):
                        continue
                    # Print all callable members (functions, methods, staticmethods)
                    if callable(value):
                        try:
                            func = value
                            if isinstance(value, staticmethod) or isinstance(value, classmethod):
                                func = value.__func__
                            argspec = inspect.getfullargspec(func)
                            annotations = func.__annotations__ if hasattr(func, '__annotations__') else {}
                            arg_names = argspec.args[1:] if argspec.args and argspec.args[0] in ('self', 'cls') else argspec.args
                            arg_strs = []
                            for arg in arg_names:
                                if arg in annotations:
                                    arg_strs.append(f"{arg}: {annotations[arg].__name__ if hasattr(annotations[arg], '__name__') else str(annotations[arg])}")
                                else:
                                    arg_strs.append(arg)
                            arg_str = ', '.join(arg_strs)
                        except (ValueError, TypeError):
                            arg_str = ''

                        if arg_str:
                            arg_str = 'self, ' + arg_str
                        else:
                            arg_str = 'self'

                        doc_string = func.__doc__ if hasattr(func, '__doc__') else ''
                        print('\n  #  Method:', name)
                        if doc_string:
                            doc_string_lines = doc_string.split('\n') if doc_string else []
                            for line in doc_string_lines:
                                print(f'  #   {line.strip()}')

                        print(f'  def {name}({arg_str}):')
                        print('    pass')
                        
                    # Print data members (skip class itself, modules, etc.)
                    elif not inspect.isroutine(value) and not inspect.isclass(value) and not inspect.ismodule(value):
                        # Handle pybind11_static_property to get the actual value
                        actual_value = ''
                        if value.__class__.__name__ == 'pybind11_static_property':
                            try:
                                actual_value = getattr(o[1], name)
                                val_repr = repr(actual_value)
                            except Exception:
                                val_repr = '<unavailable>'
                        else:
                            actual_value = value
                            val_repr = repr(value)
                        # If it's a MaterialX object instance, print as <ClassName instance>
                        if 'object at' in val_repr:
                            class_name = value.__class__.__name__ if hasattr(value, '__class__') else 'instance'
                            print(f'  {name} # Reference to <{class_name} instance>. Value: {val_repr}')
                        else:
                            #mx_value = mx.Value.getValueString(value) 
                            #print('------------------- mx value -------------------', mx_value)
                            print(f'  {name} = {val_repr}')


                if print_private:
                    print('  # Private members')
                    for i in inspect.getmembers(o[1]):
                        if (i[0] == '_pybind11_conduit_v1_'):
                            continue
                        if i[0].startswith('_') and not i[0].startswith('__'):
                            if not inspect.ismethod(i[1]):
                                if not i[0] not in o[1].__dict__:
                                    print(' ', i[0] + '()')            
                    #print(o[1].__dict__)

    #print(dir(mx))
    #pp = pprint.PrettyPrinter(indent=4)    

# Print out dictionary in Markdown format
def printNodeDictionary(nodegroupdict):
    for ng in nodegroupdict:
        print('### Node Group: ' + ng)
        for n in nodegroupdict[ng]:
            print('* ' + n)

def main():
    #opts = parseArgs()    
    #filelist = getFiles("d:/Work/materialx/bernard_materialX/libraries")
    #nodedict = getNodeDictionary(filelist)
    #printNodeDictionary(nodedict)
    parsePythonLib(mx)



if __name__ == '__main__':
    main()