# %% [markdown]
#  ## Node Deletion
# 
#  There is one option for removing nodes, and that is by name. It is not recommended to use low level
#  APIs such as `removeChild()` as they can remove non-nodes.
# 
#  In this example `getNodes()` is used to get the nodes and delete them one at a time.# Deleting Nodes
# 

# %% [markdown]
# ## Setup

# %%
import MaterialX as mx

libraryPath = mx.FilePath('libraries')
stdlib = mx.createDocument()
searchPath = mx.FileSearchPath()
libFiles = mx.loadLibraries([ libraryPath ], searchPath, stdlib)

doc = mx.createDocument()
doc.importLibrary(stdlib)

# Write predicate
def skipLibraryElement(elem):
    return not elem.hasSourceUri()

# %% [markdown]
# 

# %%
# There is no way to remove all nodes at the same time, so we remove them
# one at a timme
print('Clear library:')
for elem in doc.getChildren():
    if elem.hasSourceUri():
        doc.removeChild(elem.getName())

print('- Result:')
print('  ', mx.prettyPrint(doc))


