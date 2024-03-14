# %% [markdown]
# ## Usage Checker
# 
# This notebook demonstrates how to check the usage of node definitions for node libraries.
# 
# The utility scans one or more libraries
#     * Each definition is examined to see if it is implemented as a node graph. 
#         * If it is the list of nodes it uses is returned.
#         * For each node that is used a list of node definitions that use it is returned.
#     * A list of definitions which are not implemented as graphs as well as a list of nodes that are missing implementations are returned.
# 
# The utility also provides usage rate for node definitions and a hint of complexity of a node definition which uses other nodes by providing a count of
# the number of unique nodes it uses.

# %%
import MaterialX as mx
import mtlxutils.mxfile as mxf
from IPython.display import display_markdown

stdlib = mx.createDocument()
searchPath = mx.getDefaultDataSearchPath()
libraryFolders = mx.getDefaultDataLibraryFolders() 
try:
    libFiles = mx.loadLibraries(libraryFolders, searchPath, stdlib)
    print('Loaded %s standard library definitions for version %s' % (len(stdlib.getNodeDefs()), mx.getVersionString()))
except mx.Exception as err:
    print('Failed to load standard library definitions: "', err, '"')

doc = mx.createDocument()
doc.importLibrary(stdlib)


# %% [markdown]
# ## Utility Methods

# %%

def getNodeDefUsage(doc, libraryFilter=None):
    
    # List of nodes used by another node
    nodes_use = dict()
    nodes_used_by = dict()
    nongraph_nodes = []
    unimplemented = []

    for nodedef in doc.getNodeDefs():
        found = True
        if libraryFilter:
            found = False
            for lib in libraryFilter:
                if lib in nodedef.getSourceUri():
                    found = True
                    break
        if not found:
            continue

        nodename = nodedef.getNodeString()
        impl = nodedef.getImplementation()
        if impl:
            nodes_use_list = [] 
            for node in impl.getChildrenOfType(mx.Node):
                #print('scan:', node.getName())
                nd = node.getNodeDef()
                if nd:
                    ns = nd.getNodeString()
                    if ns not in nodes_use_list:                    
                        nodes_use_list.append(ns)

                    # Look for ns key in nodes_used_by dictionary
                    if ns not in nodes_used_by:
                        nodes_used_by[ns] = []

                    if nodename not in nodes_used_by[ns]:
                        nodes_used_by[ns].append(nodename)
                else:
                    print('Skip unknown node type: ', node.getName())

            if len(nodes_use_list) > 0:
                nodes_use[nodename] = nodes_use_list
            else:
                if nodename not in nongraph_nodes:
                    nongraph_nodes.append(nodename)
        else:
            if nodename not in unimplemented:
                unimplemented.append(nodename)

    # Sort 
    nongraph_nodes = sorted(nongraph_nodes)
    unimplemented = sorted(unimplemented)
    nodes_use = {k: v for k, v in sorted(nodes_use.items(), key=lambda item: len(item[1]), reverse=True)}
    nodes_used_by = {k: v for k, v in sorted(nodes_used_by.items(), key=lambda item: len(item[1]), reverse=True)}

    return nodes_use, nodes_used_by, nongraph_nodes, unimplemented

def printNodeDefUsage(nodes_use, nodes_used_by, nongraph_nodes, unimplemented):
    #
    result = '| Node Definition | Uses |\n| --- | --- |'
    for nu in nodes_use:
        if (len(nodes_use[nu]) > 0):
            result += '\n| %s | %d nodes: %s |' % (nu, len(nodes_use[nu]), ', '.join(sorted(nodes_use[nu])))
    display_markdown(result, raw=True)

    result = '| Node Definition | Used by |\n| --- | --- |'
    for nu in nodes_used_by:
        if (len(nodes_used_by[nu]) > 0):
            result += '\n| %s | %d nodes: %s |' % (nu, len(nodes_used_by[nu]), ', '.join(sorted(nodes_used_by[nu])) )
    display_markdown(result, raw=True)

    if len(nongraph_nodes) > 0:
        result = '| Non-Graph Nodes: %d |\n| --- |\n' % (len(nongraph_nodes))
        result += '|' + ', '.join(nongraph_nodes) + '|'
        display_markdown(result, raw=True)

    if (len(unimplemented) > 0):
        result = '| Unimplemented Nodes %d |\n| --- |\n' % (len(unimplemented))
        #for nu in unimplemented:
        #    result += '\n| %s |' % (nu)
        result += '|' + ', '.join(unimplemented) + '|'
        display_markdown(result, raw=True)
    

# %% [markdown]
# ## Node Usages Results for "Standard Library"

# %%
nodes_use, nodes_used_by, nongraph_nodes, unimplemented = getNodeDefUsage(doc, ['stdlib', 'nprlib'])

printNodeDefUsage(nodes_use, nodes_used_by, nongraph_nodes, unimplemented)

# %% [markdown]
# ## Node Usage Results for "pbrlib, bxdf"

# %%
nodes_use, nodes_used_by, nongraph_nodes, unimplemented = getNodeDefUsage(doc, ['pbrlib', 'bxdf'])

printNodeDefUsage(nodes_use, nodes_used_by, nongraph_nodes, unimplemented)

# %% [markdown]
# ## Node Usage Results for all Standard Library Nodes

# %%
nodes_use, nodes_used_by, nongraph_nodes, unimplemented = getNodeDefUsage(doc)

printNodeDefUsage(nodes_use, nodes_used_by, nongraph_nodes, unimplemented)


