# MaterialX Workflows

## MaterialX and Usd

The Usd / MaterialX notebook examines the 
interoperability of material / shader graphs between `Usd` and `MaterialX`.

The following is summary of observations.

### Hierarchy

Currently Usd can support arbitrary nesting of graphs. The MaterialX specification also denotes this support but this has not been implemented at the time of writing.

Usd will "flatten" nested graphs to a single level, but this
functionally does not seem to be exposed via a public API.

It is possible to "flatten" graphs within MaterialX, but no such
utility / API is provided by default.

In Use, for encapsulation, shader graphs are children of a Usd material with reuse via referencing. In MaterialX materials are not parents of the graphs they reference. Basically no child hierarchy / grouping is enforced. (See more on the [Materials](#materials) section) 

*One proposal would be to support MaterialX node graph hierarchies*. Related to this is how a "top" or document level
graphs (which is not contained in a MaterialX nodegraph) behave.
Basically MaterialX documents are "graph elements" as 
are MaterialX nodegraphs but are inconsistent from nodegraphs in that output ports are treated as AOVs and input ports are not allowed.

### Paths and Connections

* Usd specifies explicit output ports on nodes and graph. MaterialX only does this for nodegraphs, requiring complex logic
to discover and extract node output information.
* There is no uniform nor formal connection "API" in MaterialX as with Usd. This could be added to MaterialX to mask out the
complexities due to the next point:
* There is no uniform syntax for specifying connections between
ports and nodes in a MaterialX graph. Variants exists for connections between:
  * requirement to extract various meta-data attributes to compose a path.
  * input and output ports for nodes versus nodegraphs  
  * nodegraph (interface) inputs / outputs vs node inputs and outputs. 
  * Implicit channel extraction via additional meta-data attributes which does not exist in Usd. 

* MaterialX has no concept of absolute vs relative path notation to specify port paths. (This differs from geometric dag paths used for material assignment)

This contrasts with Usd which simply uses absolute paths syntax for all connections (e.g. '/a/b/c') which are specified on
input ports. The path references output ports which always exist.

A path API in Usd has no correspondance in MaterialX. A MaterialX `FilePath` can be used in lieu of this, or 
path modification can be done via string changes.

> Note that MaterialX uses relative paths to form connections and does not allow for parent path syntax (such as "../"). This has the advantage of assuring that no connections are ever formed between ports which do not have the same parent. This rule appears for Usd as well, but it could be possible with 
absoluate path usage to connect to arbitrary ports within the hierarchy.

Note that there is a connection `edge` construct but this is only available within upstream traversal within an iterator.

Downstream traversal is available in MaterialX relies on a caching system which is always dirtied on arbitrary attribute changes and not just connection changes.

### Materials

Usd represents a material as a node graph (container). This allows for arbitrary inputs and outputs to exist, with connections being made to child ports within the material.

MaterialX used to have a similar concept for materials but only
as a material "collection". As of version 1.38.6, material nodes were introduced (`surfacematerial` and `volumematerial`)
which more closely matches existing DCC concepts such as "shading engines" in Maya.

If bidirectional interop between Usd and MaterialX is performed, the question arises as to how handle the mapping.

Applications like Maya and Houdini have "graph containers"
which more closely match a nodegraph. 
* If the graph is mapped to a MaterialX material then 
  * Arbitrary inputs and outputs have no place to map to and the interop is lossy.
  * MaterialX material nodes cannot be children of a translated
  material, but could be additional ones. 
* If the graph is mapped to a MaterialX nodegraph then it is no longer distinguishable as a "material". Additionally 

> Note that when if the chosen mapping is from a Usd material graph to a MaterialX material node, that the shader ports are **output** ports while for MaterialX they are **input** ports.
So in Usd, these are output-to-output connections as with a MaterialX node-to-nodegraph connection instead of input-to-output connections as with MaterialX node-to-node connection. The notebook shows the added complexity.

### Ports

* There is a superset of possible types in Usd vs MaterialX. This includes types which indicate precision (e.g. half-float vs float), signed and unsigned types, and various array types.
* Usd uses "asset" references vs MaterialX which has only file name references for image resources. At the current time binary resource references are not supported in MaterialX.
* Usd uses 'token' to represent shader ports on materials.
This requires additional parsing of the port name to discover if the port maps to a surface, displacement, or volume shader type in MaterialX.  

### Supported Nodes

Naturally Usd supports nodes which are not defined in MaterialX.
As such there is no way to map these to MaterialX unless "dummy" nodes are added. 

If MaterialX and non-MaterialX graphs are under the same parent, if they do not reference by each other, it seems possible to  extract MaterialX subgraphs out and merge them back in. (Note that this was not attempted in the notebook example)

### Material Assignment

Though MaterialX can support material assignments via it's `look` API, this was not examined as the intent is to have Usd perform this role with the `look` interfaces being optional going forward with the 1.39 release.

### Usd-based vs Material-based Integrations

As part of the "Libraries / Definitions" notebook export was examined for Maya and Houdini. The both work within the 
context of integration with Usd.

Of note is that for Maya graphs that MaterialX material nodes are currently disallowed but sub-graphs are allowed, while for Houdini material nodes are allowed but sub-graphs are not.

This could be a cause for some confusion without clarification on how these map to MaterialX. (At time of writing Maya does not support MaterialX export so to be determined how each integration progresses). Additionally it will be interesting to see the approach taken by Blender for MaterialX export.

Currently only the MaterialX Graph Editor works without the notion of mapping to a Usd "container" (material graph). That said if MaterialX import is supported it is possible some
graph configurations are not supported or required some type of
transformation such as "flattening" or remapping.

These are still "early days" and will be interesting to see how
this all works out.

## MaterialX and glTF

<img src="https://raw.githubusercontent.com/kwokcb/glTF_MaterialX/main/docs/bidirectional_workflow.png" width="80%">

Bi-directional conversion between MaterialX and glTF is available via the library and utilities found in 
<a href="https://github.com/kwokcb/glTF_MaterialX" target="_blank">this repo.</a>

As MaterialX supports the glTF PBR surface shading model directly
as of version 1.38.6, the mapping from a glTF surface shader
to MaterialX is fairly straight forward. Supplementary nodes which match the glTF image mapping logic are provided as
part of the MaterialX standard library and are used during translation.

The reverse process which is the more natural one requires "distilling" a MaterialX shading graph down to a glTF one.

If users an use only the  MaterialX nodes supported which correspond to glTF then this mapping is more straight-forward.
If not then a "baking" step is required to convert all upstream connected graphs into a single image, and if a non-glTF shading model is used then "shader translation" is required.

Fortunately, translation and baking are provided as part of the code API. What is not currently handled however is merging of multiple images into single images such as for `ORM` images used by glTF shaders. This would be a useful utility, and could actually be done as a MaterialX shader graph.

## MaterialX Libraries

The creation of custom definitions is being done by a few integrations such as for Maya, Houdini, and appears to be the direction for Blender.

Agreement on semantics and syntax is under discussion. The
`Libraries and Definitions` notebook contains some current workflow investigations.
