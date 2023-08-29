# %% [markdown]
# # MaterialX XML / JSON Notebook
# 
# In this notebook we will look how JSON can be used in the context of MaterialX interop.
# Items to examine include:
# 
# * [Extracting out "interfaces" for `nodegraph`s](#nodegraph-interface-extraction)
# * [Converting XML to JSON.](#conversion-of-graphs-to-json)
# * [Determining a JSON schema.](#obtaining-a-json-schema-for-materialx)
# * [Validating JSON data against such as schema](#validating-materialx-json-with-schema)
# 
# <table>
# <tr>
# <td style="background:#000000"><img src="./images/jsoncrack_snap.png">
# <td style="background:#000000"><img src="./images/jsoncrack_snap2.png">
# </tr>
# </table>
# <sub>Snaphots of graphs generated using the JSONCrack add-on.</sub>
# 
# ## Setup for JSON support
# 
# We will use the `xmltodict` Python package to convert from MaterialX represented in XML to JSON.
# The JSON package `json` will then be used to manipulate data.

# %%
import MaterialX as mx
import mtlxutils.mxfile as mxf

import xmltodict
import json

from IPython.display import display_markdown

# Print xmltodict version
print('xmltodict version: ', xmltodict.__version__)
print('json version: ', json.__version__)
print('materialx version: ', mx.__version__)

# %% [markdown]
# ## Nodegraph Interface Extraction 
# 
# We are interested in just the "pattern graphs" which are connected to any surface shader connected to a material.
# We define two utility functions:
# * `getShaderNodes()` : To get all the surface shader nodes either connected to a material or not.
# * `getRenderableGraphs` : To find any upstream graphs connected to a surface shader.

# %%
def getShaderNodes(graphElement):
    '''
    Find all surface shaders in a GraphElement.
    '''
    shaderNodes = set()
    for material in graphElement.getMaterialNodes():
        for shader in mx.getShaderNodes(material):
            shaderNodes.add(shader.getNamePath())
    for shader in graphElement.getNodes():
        if shader.getType() == 'surfaceshader':
            shaderNodes.add(shader.getNamePath())
    return shaderNodes


def getRenderableGraphs(graphElement):
    '''
    Find all renderable graphs in a GraphElement.
    '''
    ngnamepaths = set()
    graphs = []
    shaderNodes = getShaderNodes(graphElement)
    for shaderPath in shaderNodes:
        shader = doc.getDescendant(shaderPath)
        for input in shader.getInputs():
            ngString = input.getNodeGraphString()
            if ngString and ngString not in ngnamepaths:
                graphs.append(graphElement.getNodeGraph(ngString))
                ngnamepaths.add(ngString)
    return graphs

# %% [markdown]
# 
# For each graph, we only wish to include the interface and include any connections on inputs or outputs. 
# This provides a clean encapsulation of such a graph.
# 
# All graphs are assumed to be parented directly under the root Document.
# 
# Currently the process to just copy and extract this nodegraphs is overtly complex if we just want the interace. 
# The `copyContentsFrom()` interface for nodegraphs copies over too much information requiring the removal of unneeded children.
# The alternative is to manually copy over nodegraph attributes, and child inputs and outputs.
# 
# It would be useful to have the logic encapsulated in a single API call.  
# 
# We add in a `copyGraphInterfaces()` function which will copy only the interface of a `nodegraph` to a new `nodegraph` under a given document element. 

# %%
def copyGraphInterfaces(dest, ng):
    '''
    Copy the interface of a nodegraph to a new nodegraph under a specified parent `dest`.
    '''
    copyMethod = 'add_remove'
    ng1 = dest.addNodeGraph(ng.getName())
    if copyMethod == 'add_remove':
        ng1.copyContentFrom(ng)
        for child in ng1.getChildren():
            if child.isA(mx.Input) or child.isA(mx.Output):
                for attr in ['nodegraph', 'nodename', 'defaultinput']:
                    child.removeAttribute(attr)
                continue
            ng1.removeChild(child.getName())
    else:
        for attrName in ng.getAttributeNames():
            attr = ng.getAttribute(attrName)
            newattr = ng1.addAttribute(attr.getName(), attr.getType(), attr.getValue())
            newattr.copyContentFrom(attr)
        for port in ng.getInputs():
            newport = ng1.addInput(port.getName(), port.getType())
            newport.copyContentFrom(port)
        for port in ng.getOutputs():
            newport = ng1.addOutput(port.getName(), port.getType())
            newport.copyContentFrom(port)
            for attr in ['nodegraph', 'nodename', 'defaultinput']:
                newport.removeAttribute(attr)    

# %% [markdown]
# The top level logic, loads in the "Brick" graph which can be found in the Examples folder of a MaterialX distribution.
# These are extracted out to a new document from which we get the representation as an XML string. 
# The results are printed out.  

# %%
# Load in sample MaterialX file
doc, libFiles, status = mxf.MtlxFile.createWorkingDocument()
mx.readFromXmlFile(doc, './data/standard_surface_brick_procedural.mtlx')

# Create destination document and copy nodegraph interfaces over
xmldoc = mx.createDocument()
graphs = getRenderableGraphs(doc)
for ng in graphs:
    copyGraphInterfaces(xmldoc, ng)

# Get interfaces as an XML string
xml_string = mxf.MtlxFile.writeDocumentToString(xmldoc)

text = '<details><summary>Extracted MaterialX Nodegraphs in XML</summary>\n\n' + '```xml\n' + xml_string + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# %% [markdown]
# ## Test : XML text to JSON
# 
# As a first test we will first just convert the XML string to JSON.
# 
# After this extraction process we parse the `XML` string to produce the equivalent data as a `Python` dictionary using the `xmltodict.parse()` interfaces.
# 
# This is then converted into a string to get the required `JSON` data using e `json.dumps`. 
# ( For the sake of display formatting some additional indentation is specified when dumping out a string. )

# %%
# Build JSON from XML
options = {
    'attr_prefix': '',          # Set prefix for attributes
}
python_dict = xmltodict.parse(xml_string, **options)
json_string = json.dumps(python_dict)
json_string_fmt = json.dumps(python_dict, indent=2)

text = '<details><summary>MaterialX in JSON</summary>\n\n' + '```json\n' + json_string_fmt + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

with open('mtlx_brick.json', 'w') as jsonfile:
    jsonfile.write(json_string_fmt)

# %% [markdown]
# ## Explicit Conversion
# 
# The desire is to introduce a standardized JSON representation for MaterialX. For this a match for what is supported for XML is required.
# 
# XML is supported via the `MaterialXFormat` library. This this JSON can be added.
# 
# For this book, we will create a bidirectional conversion between XML and JSON. Thus instead of 
# a non-standard conversion using a generic converter like `xmltodict` we will the logic in these scripts (and eventually 
# the `MaterialXFormat` library) for JSON conversion.
# 
# Some key factors to consider include:
# 1. The JSON representation should be a direct match to the XML representation.
# 2. The JSON representation should match the XML size as closely as possible.
# 3. Export and import options for XML should be supported for JSON.
# 4. There is no concept of "includes" in JSON. This is a concept specific to XML.

# %% [markdown]
# ### JSON Serialization
# 
# To perform a proper serialization, the MaterialX document itself should be examined with direct conversion to JSON.   
# 
# #### Serialization to JSON
# 
# For conversion to JSON we introduce two functions:
# 
# 1. `documentToJSON()` : Converts a MaterialX document to a JSON string.
# 2. `elementToJSON()` : Converts a MaterialX element to a JSON string, and continues to recursively convert any children.

# %%
# We use a colon to separate the category and name of an element in the JSON hierarchy
JSON_CATEGORY_NAME_SEPARATOR = ':'
# The root of the JSON hierarchy
MATERIALX_DOCUMENT_ROOT = 'materialx'

# Convert MaterialX element to JSON
def elementToJSON(elem, jsonParent):
    '''
    Convert an MaterialX XML element to JSON.
    Will recursively traverse the parent/child Element hierarchy.
    '''
    if (elem.getSourceUri() != ""):
        return
    
    # Create a new JSON element for the MaterialX element
    jsonElem = {}

    # Add attributes
    for attrName in elem.getAttributeNames():
        jsonElem[attrName] = elem.getAttribute(attrName)

    # Add children
    for child in elem.getChildren():
        jsonElem = elementToJSON(child, jsonElem)
    
    # Add element to parent
    jsonParent[elem.getCategory() + JSON_CATEGORY_NAME_SEPARATOR + elem.getName()] = jsonElem
    return jsonParent

# Convert MaterialX document to JSON
def documentToJSON(doc):
    '''Convert an MaterialX XML document to JSON'''
    root = {}
    root["materialx"] = {}

    for attrName in doc.getAttributeNames():
        root[attrName] =  doc.getAttribute(attrName)

    for elem in doc.getChildren():
        elementToJSON(elem, root[MATERIALX_DOCUMENT_ROOT])

    result = json.dumps(root, indent=2)
    return result

# %% [markdown]
# We call `documentToJSON()` to convert both the entire document as well as just the NodeGraph interface document below:

# %%
# Convert entire document
doc_result = documentToJSON(doc)

text = '<details><summary>Entire document to JSON</summary>\n\n' + '```json\n' + doc_result  + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# Convert just the graph
graph_result = documentToJSON(xmldoc)

text = '<details><summary>Node Graph Interface to JSON</summary>\n\n' + '```json\n' + graph_result  + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# %% [markdown]
# The JSON is visualized as a graph for the entire document below, as well as another sample conversion of the glTF "Boombox" and "Olvies" examples from the <a href="https://github.com/KhronosGroup/glTF-Sample-Models" target="_blank">sample models library</a>
# 

# %% [markdown]
# <details><summary>Graph of Marble Material</summary>
# <img src="./images/sample_marble_json.svg">
# </details>

# %% [markdown]
# <details><summary>Graph of "Boombox" Example</summary>
# <img src="./images/gltf_pbr_boombox.svg">
# </details>

# %% [markdown]
# <details><summary>Graph of "Olives" Example</summary>
# <img src="./images/sample_olives.svg">
# </details>

# %% [markdown]
# #### Deserialization from JSON
# 
# For conversion from JSON we introduce two functions:
# 
# 1. `documentFromJSON()` : Converts a JSON string to a MaterialX document.
# 2. `elementFromJSON()` : Converts a JSON string to a MaterialX element, and continues to recursively convert any children.
# 
# Note that to perform deserialization we need to split the `category` and `name` out for non-attribute elements.

# %%
# Separator between category and name in JSON element
JSON_CATEGORY_NAME_SEPARATOR = ":"

# Convert JSON element to MaterialX
def elementFromJSON(node, elem):
    '''
    Convert an JSON element to MaterialX
    '''
    for key in node:
        value = node[key]

        # Set attributes            
        if isinstance(value, str):
            elem.setAttribute(key, str(value))

        # Traverse chilren
        else:
            # Traverse down from root
            if key == MATERIALX_DOCUMENT_ROOT:
                elementFromJSON(value, elem)
                continue

            # Split key name by ":" to get category and name
            category, name = key.split(JSON_CATEGORY_NAME_SEPARATOR, 1)
            if category and not elem.getChild(name):
                child = elem.addChildOfCategory(category, name)
                elementFromJSON(value, child)

# Convert JSON to MaterialX document
def documentFromJSON(jsonDoc, doc):
    '''
    Convert a JSON document to MaterialX
    '''
    elementFromJSON(jsonDoc, doc)


# %% [markdown]
# Using these functions we can convert the JSON document and NodeGraph results back to a MaterialX documents.
# 
# We also add in validation and an <a href="https://materialx.org/docs/api/class_xml_read_options.html" target="_blank">"upgrade" call</a> to roughly match what is performed for XML serialization.

# %%
# Convert entire document back from JSON
newDoc = mx.createDocument() 
jsonObject = json.loads(doc_result)
documentFromJSON(jsonObject, newDoc)

# Validate and upgrade element version
valid, errors = newDoc.validate()
if not valid:
    print('Validation errors:')
    for err in errors:
        print('  {}'.format(err))
newDoc.upgradeVersion()

newDocString = mx.writeToXmlString(newDoc)    
text = '<details><summary>JSON Deserialization of Document</summary>\n\n' + '```xml\n' + newDocString  + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# %%
# Convert nodegraph interface back from JSON
newDoc = mx.createDocument() 
jsonObject = json.loads(graph_result)
documentFromJSON(jsonObject, newDoc)

# Validate and upgrade element version
valid, errors = newDoc.validate()
if not valid:
    print('Validation errors:')
    for err in errors:
        print('  {}'.format(err))
newDoc.upgradeVersion()

newDocString = mx.writeToXmlString(newDoc)    
text = '<details><summary>JSON Deserialization of NodeGraph</summary>\n\n' + '```xml\n' + newDocString  + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# %% [markdown]
# ## Obtaining a JSON Schema for MaterialX 
# 
# For this example we will use the first test results just the `NodeGraph`` for simplicity. It is possible to create a schema for all elements of MaterialX which would include all the definitions which are part of the standard library.
# 
# The schema is created using the [OpenAI](https://platform.openai.com/docs/api-reference) Python package. Various MaterialX documents (saved out in JSON) were used as input data.
# 
# A graph of the schema is shown below, with the textual description below:
# <img src="./images/materialx_json_schema.svg">
# 
# Some examples and test suite documents are suitable to obtain most of the schema. Small edits we're made for anything amiss such setting "required" attributes.
# 
# Note that this is just a sample schema. It is not complete. It is also not the only possible schema.

# %%
# Define the JSON schema.  
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "definitions": {
    "port": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "enum": ["float", "vector2", "vector3", "vector4", "color3", "color4", "bool", "integer", "filename"]
        },
        "nodename": {
          "type": "string"
        }
      },
      "required": ["name", "type"]
    },
    "inputPort": {
      "allOf": [
        {
          "$ref": "#/definitions/port"
        },
        {
          "properties": {
            "value": {
               "type" : "string"
            },
            "uiname": {
              "type": "string"
            },
            "uifolder": {
              "type": "string"
            },
            "uimin": {
              "type": "string"
            },
            "uimax": {
              "type": "string"
            },
            "uisoftmin": {
              "type": "string"
            },
            "uisoftmax": {
              "type": "string"
            }
          },
          "required": ["value"]
        }
      ]
    },
    "outputPort": {
      "allOf": [
        {
          "$ref": "#/definitions/port"
        }
      ]
    },
    "nodegraph": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "input": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/inputPort"
          }
        },
        "output": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/outputPort"
          }
        }
      },
      "required": ["name", "input", "output"]
    },
    "materialx": {
      "type": "object",
      "properties": {
        "@version": {
          "type": "string"
        },
        "nodegraph": {
          "$ref": "#/definitions/nodegraph"
        }
      },
      "required": ["version", "nodegraph"]
    }
  },
  "type": "object",
  "properties": {
    "materialx": {
      "$ref": "#/definitions/materialx"
    }
  },
  "required": ["materialx"]
}

# Write the schema to a file
jsonSchemaFilePath = 'data/mtlx_sample_schema.json'
with open(jsonSchemaFilePath, 'w') as f:
    json.dump(schema, f)

# Read the schema from a file
loaded_schema = {}
with open(jsonSchemaFilePath, 'r') as schema_file:
    loaded_schema = json.loads(schema_file.read())

text = '<details><summary>MaterialX JSON Schema</summary>\n\n' + '```json\n' + json.dumps(schema, indent=2) + '\n```\n' + '</details>\n' 
display_markdown(text, raw=True)

# %% [markdown]
# ## Validating MaterialX JSON with Schema 
# 
# To perform validation we will use the `validate` interface from the [`jsconschema`](https://pypi.org/project/jsonschema/) package.

# %%
# Validate JSON formatted MaterialX document.
from jsonschema import validate as jsvalidate

# Validate the JSON string against the schema
def validateJson(json_string, schema):
    try:
        data = json.loads(json_string)
        jsvalidate(data, schema)
    except Exception as e:
        return e
    return ''


error = validateJson(json_string, loaded_schema)
if not error:
  print("JSON string is valid against the schema")
else:
  print('JSON string is not valid:\n')
  print(error)


