
### Interface Building / Publishing Interfaces

The act of adding or removing `nodegraph` `input`s and `output`s can be thought of as **publishing** the public interface for the graph. 

A `node` should **never** have inputs / outputs added or removed which are not part of their definition -- in fact this will be tagged a node instance which has no matching definition if a validation check is performed. 

## Compound and Functional Nodegraphs and "Flattening" and "Publishing"

If node is implemented by a nodegraph, then the nodegraph is called a **functional nodegraph**. Otherwise it is called a **compound nodegraph**.

Thus a more complete definition of a shader graph is that:
1. It is composed of a series of connected nodes and compound nodegraphs.
2. One or more of these nodes may be implemented as  **functional graphs**. 
3. If the node instance is replaced with the functional graph implementation then the node essentially "becomes" a compound graph. This operation is called **flattening** a node instance.
4. If all nodes are taken out of the scope of their parent nodegraphs then all that is left is a series of connected nodes. This operation is is called **flattening** a nodegraph.
5. The reverse operation to add nodes to nodegraphs allows users to logically group nodes and/or publisih it's public interface. 
If a new definition `<nodedef>` is created and the nodegraph becomes a **functional graph** then can be thought of as  **publishing** a new definition.

### Flattening Example
```mermaid
graph LR
  subgraph document
    subgraph nodegraph1
        nodegraph1.input1 --> nodegraph1/node1.input1
        nodegraph1.input1 --> nodegraph1/node2.input2
        nodegraph1.input2 --> nodegraph1/node2.input1
        subgraph node1;
            nodegraph1/node1.input1
            nodegraph1/node1.input2
        end
        subgraph node2;
            nodegraph1/node2.input2
            nodegraph1/node2.input1
        end
        nodegraph1/node1.input1 --> nodegraph1/operator 
        nodegraph1/node1.input1 --> nodegraph1/operator 
        nodegraph1/operator --> nodegraph1.output2
        nodegraph1/node1.input2 --> nodegraph1/operator2
        nodegraph1/operator2 --> nodegraph1.output3
        nodegraph1/node2.input2 --> nodegraph1/operator2 
        nodegraph1/node2.input1 --> nodegraph1/operator2
        nodegraph1/node2.input1 -.-> nodegraph1/dot((dot)) -.-> nodegraph1.output1

        style nodegraph1.input1 fill:#1b1,color:#fff 
        style nodegraph1.input2 fill:#1b1,color:#fff 
        style nodegraph1.output1 fill:#0bb,color:#fff
        style nodegraph1.output2 fill:#0bb,color:#fff
        style nodegraph1.output3 fill:#0bb,color:#fff
    end
  end
```
if flattened would look something like this if the parent of the nodegraph was a document. The interface `<input>` and `<output>` elements are not present as this is disallowed within the document scope.
```mermaid
graph 
  subgraph document
    node1.input1 --> operator
    node1.input1 --> operator 
    node1.input2 --> operator2
    node2.input2 --> operator2 
    node2.input1 --> operator2
    node2.input1 -.-> dot((dot))
  end
```
The reverse process could create a nodegraph, with inputs and outputs added to create the public interface for the nodegraph.

## Shader Generation Graphs
When dealing with shader generation shader graphs are simplified to having only nodes with inputs and outputs **"ports"**. 

The key components are:
* Shader Node: Basically corresponds to a node.
* Shader Port: A connectable attribute of a Shader Node. Can either be Input or Output Ports.
* Public Ports: Are bindable as shader code inputs or exposed as the root for evaluation as an output.
* Private Ports: Inputs and Outputs which are not exposed.

All original nodes are flattened to remove the notion of a graph hierarchy
and replace any nodes which are represented as functional graphs.

## Upstream Traversal

Upstream traversal is fairly simple where the root to start from should be an `<output>` on a node or nodegraph. Traversal will naturally only follow direct connections. 

This is straightforward when:

  1. There are no nodegraphs within the shader graph. 
  2. Or all of the nodes reside within a single nodegraph.

In this case only node inputs connect to upstream outputs.

# Examples

Interior of nodegraph to upstream nodegraphs and nodes
```mermaid
graph TD;
  subgraph Document;
  subgraph surf_graph_graph; 
    surf_graph_graph_default_shader[surf_graph_graph/default_shader] --> surf_graph_graph_surf_graph_graph_out[surf_graph_graph/surf_graph_graph_out]
    style surf_graph_graph_surf_graph_graph_out fill:#1b1,color:#fff
    surf_graph_graph_input([surf_graph_graph/input]) ==.base_color==> surf_graph_graph_default_shader[surf_graph_graph/default_shader]
    style surf_graph_graph_input fill:#0bb,color:#fff
    graph_graph_multiply[graph_graph/multiply] --.base_color--> surf_graph_graph_default_shader[surf_graph_graph/default_shader]
    graph_graph_input([graph_graph/input]) ==.in1==> graph_graph_multiply[graph_graph/multiply]
    style graph_graph_input fill:#0bb,color:#fff
    upstream_graph_image[upstream_graph/image] --.in1--> graph_graph_multiply[graph_graph/multiply]
    upstream_graph_file([upstream_graph/file]) ==.file==> upstream_graph_image[upstream_graph/image]
    style upstream_graph_file fill:#0bb,color:#fff
  subgraph graph_graph;
    graph_graph_multiply
    graph_graph_input
  end
  subgraph upstream_graph;
    upstream_graph_image
    upstream_graph_file
  end
  end
  end
```
Cascading nodegraph to nodegraph
```mermaid
graph TD;
  subgraph DocumentRoot; 
    standard_surface[standard_surface] --.surfaceshader--> surfacematerial[surfacematerial]
    upstream1_make_yellow[upstream1/make_yellow] --.base_color--> standard_surface[standard_surface]
    upstream1_upstream1_in1([upstream1/upstream1_in1]) ==.in1==> upstream1_make_yellow[upstream1/make_yellow]
    style upstream1_upstream1_in1 fill:#0bb,color:#111
    upstream2_multiply_by_image[upstream2/multiply_by_image] --.in1--> upstream1_make_yellow[upstream1/make_yellow]
    upstream2_upstream2_in1([upstream2/upstream2_in1]) ==.in1==> upstream2_multiply_by_image[upstream2/multiply_by_image]
    style upstream2_upstream2_in1 fill:#0bb,color:#111
    upstream3_upstream_image[upstream3/upstream_image] --.in1--> upstream2_multiply_by_image[upstream2/multiply_by_image]
    upstream3_file([upstream3/file]) ==.file==> upstream3_upstream_image[upstream3/upstream_image]
    style upstream3_file fill:#0bb,color:#111
    upstream2_image[upstream2/image] --.in2--> upstream2_multiply_by_image[upstream2/multiply_by_image]
  end
```
Sample AMD material
```mermaid
graph BT;
  subgraph DocumentRoot; 
    SR_MaterialX_Graph[SR_MaterialX_Graph] --.surfaceshader--> MaterialX_Graph[MaterialX_Graph]
    NG_MaterialX_Graph_node_image_color3_2[NG_MaterialX_Graph/node_image_color3_2] --.base_color--> SR_MaterialX_Graph[SR_MaterialX_Graph]
    NG_MaterialX_Graph_node_multiply_9[NG_MaterialX_Graph/node_multiply_9] --.texcoord--> NG_MaterialX_Graph_node_image_color3_2[NG_MaterialX_Graph/node_image_color3_2]
    NG_MaterialX_Graph_node_texcoord_vector2_8[NG_MaterialX_Graph/node_texcoord_vector2_8] --.in1--> NG_MaterialX_Graph_node_multiply_9[NG_MaterialX_Graph/node_multiply_9]
    NG_MaterialX_Graph_node_float_1[NG_MaterialX_Graph/node_float_1] --.in2--> NG_MaterialX_Graph_node_multiply_9[NG_MaterialX_Graph/node_multiply_9]
    NG_MaterialX_Graph_node_mix_3[NG_MaterialX_Graph/node_mix_3] --.specular_roughness--> SR_MaterialX_Graph[SR_MaterialX_Graph]
    NG_MaterialX_Graph_node_float_7[NG_MaterialX_Graph/node_float_7] --.fg--> NG_MaterialX_Graph_node_mix_3[NG_MaterialX_Graph/node_mix_3]
    NG_MaterialX_Graph_node_float_0[NG_MaterialX_Graph/node_float_0] --.bg--> NG_MaterialX_Graph_node_mix_3[NG_MaterialX_Graph/node_mix_3]
    NG_MaterialX_Graph_node_extract_11[NG_MaterialX_Graph/node_extract_11] --.mix--> NG_MaterialX_Graph_node_mix_3[NG_MaterialX_Graph/node_mix_3]
    NG_MaterialX_Graph_node_image_vector3_12[NG_MaterialX_Graph/node_image_vector3_12] --.in--> NG_MaterialX_Graph_node_extract_11[NG_MaterialX_Graph/node_extract_11]
    NG_MaterialX_Graph_node_multiply_9[NG_MaterialX_Graph/node_multiply_9] --.texcoord--> NG_MaterialX_Graph_node_image_vector3_12[NG_MaterialX_Graph/node_image_vector3_12]
    NG_MaterialX_Graph_onthefly_4[NG_MaterialX_Graph/onthefly_4] --.coat_normal--> SR_MaterialX_Graph[SR_MaterialX_Graph]
    NG_MaterialX_Graph_node_normalmap[NG_MaterialX_Graph/node_normalmap] --.normal--> SR_MaterialX_Graph[SR_MaterialX_Graph]
    NG_MaterialX_Graph_node_image_vector3_10[NG_MaterialX_Graph/node_image_vector3_10] --.in--> NG_MaterialX_Graph_node_normalmap[NG_MaterialX_Graph/node_normalmap]
    NG_MaterialX_Graph_node_multiply_9[NG_MaterialX_Graph/node_multiply_9] --.texcoord--> NG_MaterialX_Graph_node_image_vector3_10[NG_MaterialX_Graph/node_image_vector3_10]
    NG_MaterialX_Graph_onthefly_6[NG_MaterialX_Graph/onthefly_6] --.tangent--> SR_MaterialX_Graph[SR_MaterialX_Graph]
  end
```
------

## Workflows

* Logically a both a Document and a NodeGraph are considered to be containers of nodes or a "node graph".
* However a Node which may have an implementation as a graph is not considered to be a container. This means
traversal up and downstream from a given node requires special casing.
* Another issue is that in order to keep a minimal size, only those inputs and which are explicit connected to or
assigned non-default values will exist on the instance of a Node or Nodegraph, even though they are part of the
interface definition.
* Any connections which within Nodegraphs which connect interior Node inputs to Nodegraph inputs also currently have
special syntax.
* All connections are specified on a downstream input instead of as a structure which provides both the input and output. This makes downstream traversal much less straightforward to perform than upstream.
* Materials as of 1.38 are nodes and traversal can find upstream shaders to allow a  full material graph to be traversed.

## Recommendations
* In order to create a "complete" graph, when instances are created all inputs and outputs should be instantiated. This can be done via utilities which scan the associated NodeDef (definition) and add inputs and outputs with default values.
* An NodeGraph itself should have all of it's inputs specified even if it's a functional graph for the same reason.
* 