# %% [markdown]
# ## Targets and Implementations
# 
# This notebook will go over some of the details about adding implementations for custom "targets". 
# 
# We will cover:
# 
# 1. Creating a new target definition
# 2. Inheriting from an existing target
# 3. Setting the target for an implementation
# 4. Associating a target with a node definition
# 4. Implementations without targets versus ones with targets.

# %% [markdown]
# ### Setup
# 
# For this setup all is the core package

# %%
import MaterialX as mx

# %% [markdown]
# ### Target Definitions
# 
# A target is defined by the <a href="https://materialx.org/docs/api/class_target_def.html" target="_blank">TargetDef</a> interface.
# 
# Any string can be used but for code generation it is advised to follow the
# existing naming conventions if contributing back to the MaterialX repo. The provided target definitions can be found by loading in the standard libraries.
# 

# %%
doc = mx.createDocument()
searchPath = mx.getDefaultDataSearchPath()
libFiles = mx.loadLibraries(mx.getDefaultDataLibraryFolders(), searchPath, doc)

print('Standard library target definitions:')
for targetDef in doc.getTargetDefs():
    print('-', targetDef.getName()) 

# %% [markdown]
# ### Creating a New Target
# 
# A new target can be created using the Document API addTargetDef.
# Any valid logical name can be used.

# %%
doc = mx.createDocument()
mytargetDef = doc.addTargetDef("mytarget")
print('%s' % mx.prettyPrint(doc) + '</materialx>')

# %% [markdown]
# If the implementations for this target are meant to override an existing target's implementation then it should "inherit" from that target by setting the inheritance attribute. In this example, the parent target is for OSL (`genosl`).

# %%
mytargetDef.setInheritString('genosl')
print('%s' % mx.prettyPrint(doc) + '</materialx>')

# %% [markdown]
# This target can then be used by new implementations by setting the `target` property on the implementation using the <a href="https://materialx.org/docs/api/class_interface_element.htm" target="_blank">setTarget()</a> interface which
# is defined on the `InterfaceElement` class. 
# 
# Assuming the function to implement is called `function`, we follow the recommended convention of prefixing the function name with `IM_` (for implementation, and appending the target name to come up with the identifier `IM_function_mytarget`

# %%
myimpl = doc.addImplementation('IM_functon_mytarget')
myimpl.setTarget('mytarget')
print('%s' % mx.prettyPrint(doc) + '</materialx>')

# %% [markdown]
# To be useful an implementation needs to associated with a node definition.
# This can be done by additionally specifying the `nodedef` property.
# 
# We will add in a sample definition which outputs a color to reference in the example. 
# Again we follow recommended conventions by prefixing the definition name with `ND_` (for `nodedef`). As definitions define function interfaces they *do not* have a target specifier. 
# 

# %%
mynodeDef = doc.addNodeDef("ND_myfunction", "color3", "myfunction")
myimpl.setNodeDefString("ND_myfunction")
print('%s' % mx.prettyPrint(doc) + '</materialx>')

# %% [markdown]
# Any number of implementations can be defined for different node definitions. It is not valid to have two implementations with the same target for a given definition. The first one found will be used and any others ignored so can be unpredictable as to which one is associated.

# %% [markdown]
# ### Inheritance Example
# 
# The following example show creating a base and derived target and adding a different implementation for each target.

# %%
doc = mx.createDocument()

# Create a base and derived targetdef
base_targetDef = doc.addTargetDef("base")
derived_targetDef = doc.addTargetDef("derived")
derived_targetDef.setInheritString('base')

# Create an implementation for the base targetdef
base_impl = doc.addImplementation("IM_function_base")
base_impl.setTarget("base")
base_impl.setNodeDefString("ND_function")

# Create an implementation for the derived targetdef
derived_impl = doc.addImplementation("IM_functon_derived")
derived_impl.setTarget("derived")
derived_impl.setNodeDefString("ND_function")

# Create a nodedef
nodeDef = doc.addNodeDef("ND_function", "color3", "function")

print('%s' % mx.prettyPrint(doc) + '</materialx>')


# %% [markdown]
# We can then query for the implementation based on target.

# %%
impl = nodeDef.getImplementation('derived')
print('Got derived target: "%s". Implementation name: "%s"' % (impl.getTarget(), impl.getName()))

impl = nodeDef.getImplementation('base')
print('Got base target: "%s". Implementation name: "%s"' % (impl.getTarget(), impl.getName()))


# %% [markdown]
# ### Functional Node Graphs: Implementations Without Targets
# 
# Node graphs which are used as implementations (`functional graph`) do not have a shader `target`.
# 
# Many of the standard library implementations are node graphs composed of instances of other node definitions. The implementations of these definitions can in turn be composed of other node instances. Basically, more complex functionality can be made up of lower level functionality.
# 
# At some point the implementation is made up of actual shader code which is explicitly specified or generated via a shader generator and hence a `target`` must be specified.
# 
# Node graph implementations can either be associated with node definitions by adding a reference from the graph itself or via an `implementation` declaration (added after 1.38). Below is one such case used for "Autodesk Standard Surface".
# 
# ```xml
#  <implementation name="IMPL_standard_surface_surfaceshader_101" nodedef="ND_standard_surface_surfaceshader" nodegraph="NG_standard_surface_surfaceshader_100" />
# 
#   <implementation name="IMPL_standard_surface_surfaceshader_100" nodedef="ND_standard_surface_surfaceshader_100" nodegraph="NG_standard_surface_surfaceshader_100" />
# ```

# %% [markdown]
# ## Implementation Association Caveats
# 
# ### Finding Implementation Given a Node Definition
# 
# There are currently issues in the search for implementations if any of the implementations in the target hierarchy have no target. The result is that
# the implementation which has no target is always returned.
# 
# In the following example we have a base implementation without a target.
# Even though we ask for the implementation by name (`derived`) the implementation
# returned in the one without a target.
# 
# This should hopefully be addressed in an upcoming release.

# %%
base_impl.setTarget('')

impl = nodeDef.getImplementation('derived')
print('Want derived, but got this target: "%s". Implementation name: "%s"' % (impl.getTarget(), impl.getName()))

impl = nodeDef.getImplementation()
print('Asked for no target implementation and got it: "%s". Implementation name:" %s"' % (impl.getTarget(), impl.getName()))

# %% [markdown]
# ### Finding Implementations Given a Node Instance
# 
# In the example below we reuse some code from the "Basics" book to create a node
# based on the definition previously specified.

# %%
definitionName = 'ND_function'
nodeName = 'test_function'
childName = doc.createValidChildName(nodeName)
shaderNode = doc.addNodeInstance(nodeDef, childName)
if shaderNode:
    shaderName = shaderNode.getName()
    print('Created node via nodedef "%s"' % definitionName)

definition = shaderNode.getNodeDef()
impl = shaderNode.getImplementation()
if impl:
    print('Get implementation:', impl.getTarget())
impl = shaderNode.getImplementation('derived')
if impl:
    print('Get implementation:', impl.getTarget())    

# %% [markdown]
# With an empty base implementation, the `getImplementation()` call from the instance actually fails to return an implementation. 
# 
# Only after restoring the `base` target does it work again:

# %%
base_impl.setTarget('base')
impl = shaderNode.getImplementation()
if impl:
    print('Get implementation:', impl.getTarget())

impl = shaderNode.getImplementation('derived')
if impl:
    print('Get implementation:', impl.getTarget())    

# %% [markdown]
# ### Node Definition Targets
# 
# It is possible for a node definition to also specify a target. This is less common and adds some additional checking when trying to find an implementation for a given node
# as the definition needs to be queried with a `target`.
# 
# We will not cover this in detail as such as there appears to be outstanding issues with support in this area.
# 
# The basic setup would be similar to the example below where we associate implementations for separate definitions with differing targets.

# %%
doc = mx.createDocument()

base_impl = doc.addImplementation("IM_function_base")
base_impl.setTarget("base")
base_impl.setNodeDefString("ND_function_base")

# Create an implementation for the derived targetdef
derived_impl = doc.addImplementation("IM_functon_derived")
derived_impl.setTarget("derived")
derived_impl.setNodeDefString("ND_function_derived")

base_nodeDef = doc.addNodeDef("ND_function_base", "color3", "function")
base_nodeDef.setTarget("base")

derived_nodeDef = doc.addNodeDef("ND_function_derived", "color3", "function")
derived_nodeDef.setTarget("derived")

print('%s' % mx.prettyPrint(doc) + '</materialx>\n')

mpl = base_nodeDef.getImplementation('derived')
print('- Incorrectly find derived on base?: "%s". Implementation name: "%s"' % (impl.getTarget(), impl.getName()))

impl = base_nodeDef.getImplementation()
print('- Find base on base: "%s". Implementation name:" %s"' % (impl.getTarget(), impl.getName()))

mpl = derived_nodeDef.getImplementation('derived')
print('- Incorrectly find base on derived?: "%s". Implementation name: "%s"' % (impl.getTarget(), impl.getName()))

impl = derived_nodeDef.getImplementation()
print('- Find derived on derived: "%s". Implementation name:" %s"' % (impl.getTarget(), impl.getName()))


