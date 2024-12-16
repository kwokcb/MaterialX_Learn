## MaterialX and Usd

![](images/usd_materialx_interop.png)

The [Usd / MaterialX
notebook](../pymaterialx/mtlx_definitions_libraries_notebook.html)
examines the interoperability of material / shader graphs between `Usd`
and `MaterialX`.

Observations are summarized below.

### Hierarchy

Currently Usd can support arbitrary nesting of graphs. The MaterialX
specification also denotes this support but this has not been
implemented at the time of writing.

Usd will \"flatten\" nested graphs to a single level, but this
functionally does not seem to be exposed via a public API.

For example the following graphs nodegraph \"childNG\" has to be placed
under the nodegraph \"parentNG\" to be supported in MaterialX.
![](images/nested_nodegraphs.png)

It is possible to \"flatten\" graphs within MaterialX, but no such
utility / API is provided by default.

In Usd, for encapsulation, shader graphs are children of a Usd material
with reuse via referencing. In MaterialX materials are not parents of
the graphs they reference. No child hierarchy / grouping is enforced.
(For more detailed information see the [Materials](#materials) section)

*One proposal would be to [support MaterialX node graph
hierarchies](https://github.com/AcademySoftwareFoundation/MaterialX/issues/1272)*.
Related to this is how a \"top\" or document level graphs (which is not
contained in a MaterialX nodegraph) behave. Basically MaterialX
documents are \"graph elements\" as are MaterialX nodegraphs but are
inconsistent from nodegraphs in that output ports are treated as AOVs
and input ports are not allowed.

### Paths and Connections

-   Usd specifies explicit output ports on nodes and graphs. MaterialX
    only does this for nodegraphs, requiring complex logic to discover
    and extract node output information.

-   There is no uniform nor formal connection \"API\" in MaterialX as
    with Usd. This could be added to MaterialX to mask out the
    complexities due to the next point:

-   There is no uniform syntax for specifying connections between ports
    and nodes in a MaterialX graph. Variants exists for connections
    between:

-   -   requirement to extract various meta-data attributes to compose a
        path.
    -   input and output ports for nodes versus nodegraphs
    -   nodegraph (interface) inputs / outputs vs node inputs and
        outputs.
    -   Implicit channel extraction via additional meta-data attributes
        which does not exist in Usd.

-   MaterialX has no concept of absolute vs relative path notation to
    specify port paths. (This differs from geometric dag paths used for
    material assignment)

This contrasts with Usd which simply uses absolute paths syntax for all
connections (e.g. \'/a/b/c\') which are specified on input ports. The
path references output ports which always exist.

A path API in Usd has no correspondance in MaterialX. A MaterialX
`FilePath` can be used in lieu of this, or path modification can be done
via string changes.

> Note that MaterialX uses relative paths to form connections and does
> not allow for parent path syntax (such as \"../\"). This has the
> advantage of assuring that no connections are ever formed between
> ports which do not have the same parent. This rule appears for Usd as
> well, but it could be possible with absolute path usage to connect to
> arbitrary ports within the hierarchy.

Note that there is a connection `edge` construct but this is only
available within upstream traversal within an iterator.

Downstream traversal is available in MaterialX relies on a caching
system which is always dirtied on arbitrary attribute changes and not
just connection changes.

### Materials

Usd represents a material as a node graph (container). This allows for
arbitrary inputs and outputs to exist, with connections being made to
child ports within the material.

MaterialX used to have a similar concept for materials but only as a
material \"collection\". As of version 1.38.6, material nodes were
introduced (`surfacematerial` and `volumematerial`) which more closely
matches existing DCC concepts such as \"shading engines\" in Maya.

If bidirectional interop between Usd and MaterialX is performed, the
question arises as to how handle the mapping.

The following diagram shows the class hierarchy for Usd and MaterialX.
It is mostly the discrepancy between have one as a graph and one as a
pair of atomic nodes which allows for different approaches to mapping.
![](images/usd_material_vs_mtlx_material.png)

Applications like Maya and Houdini have \"graph containers\" which more
closely match a nodegraph.

-   If the Usd material graph is mapped to a MaterialX material then
    arbitrary inputs and outputs have no place to map to and the interop
    is lossy.
-   MaterialX material nodes cannot be children of a translated Usd
    material, but perhaps could be created as additional materials
    referencing the same shader graph. This is a bit of a strange
    mapping and makes it difficult to perform the reverse mapping.
-   If the Usd material graph is mapped to a MaterialX nodegraph then it
    is no longer distinguishable as a \"material\".

Additionally, note that when if the chosen mapping is from a Usd
material graph to a MaterialX material node, that the shader ports are
**output** ports while for MaterialX they are **input** ports.

Thus in Usd, these are output-to-output connections (as would occur in a
MaterialX node-to-nodegraph) instead of input-to-output connections
occurs with MaterialX node-to-node connections. The notebook shows the
added logic complexity.

### Ports

For the most parts Usd ports correspond 1:1 with MaterialX ports. At the
time of writing MaterialX tokens do not correspond to Usd (tokens).

Some differences to note:

-   There is a superset of possible types in Usd vs MaterialX. This
    includes types which indicate precision (e.g. half-float vs float),
    signed and unsigned types, and various array types. Usage of Usd
    with MaterialX definitions should avoid any type mapping issues for
    interop.
-   Usd uses `asset` references vs MaterialX which has only file name
    references for image resources. At the current time binary resource
    references are not supported in MaterialX.
-   Usd uses `token` to represent shader ports on materials. This
    requires additional parsing of the port name to discover if the port
    maps to a surface, displacement, or volume shader type in MaterialX.
-   There is some minor string syntax difference for representing tuples
    in Usd versus MaterialX which requires some extra mapping logic.

### Supported Nodes

Usd supports nodes which are not defined in MaterialX. As such there is
no way to map these to MaterialX unless \"dummy\" nodes are added.

If MaterialX and non-MaterialX graphs are under the same parent, if they
do not reference by each other, it seems possible to extract MaterialX
subgraphs out and merge them back in. (Note that this was not attempted
in the notebook example)

### Material Assignment

Though MaterialX can support material assignments via it\'s `look` API,
this was not examined as the intent is to have Usd perform this role
with the `look` interfaces being optional going forward with the 1.39
release.

### Usd-based versus Material-based Integrations

As part of the \"Libraries / Definitions\" notebook export was examined
for Maya and Houdini. The both work within the context of integration
with Usd.

Of note is that for Maya graphs MaterialX material nodes are currently
disallowed but sub-graphs are allowed, while Houdini material nodes are
allowed but sub-graphs are both not exportable.\
![](images/houdini_disallowed_nodes.png)

This could be cause some confusion as to how these map to MaterialX. (At
time of writing Maya does not support MaterialX export so to be
determined how each integration progresses). Additionally it will be
interesting to see the approach taken by Blender for MaterialX export.

Currently **only the MaterialX Graph Editor** works without the notion
of mapping to a Usd \"container\" (material graph). That said if
MaterialX import is supported it is possible some graph configurations
are not supported or required some type of transformation such as
\"flattening\" or remapping.

![](images/graph_editor_supported.png)

These are still \"early days\" and will be interesting to see how this
all works out.


