## Module: MaterialX.PyMaterialXCore

### Classes

<a id='materialx-pymaterialxcore-attributedef'></a>

- **AttributeDef**: An attribute definition element within a Document.

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setAttrName`: setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None
        
        Set the element's attrname string.


    - `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return true if this element has an attrname string.


    - `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str
        
        Return the element's attrname string.


    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None
        
        Set the value string of an element.


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return true if the given element has a value string.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str
        
        Get the value string of a element.


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None
        
        Set the exportable boolean for the element.


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return the exportable boolean for the element.
        
        Defaults to false if exportable is not set.


  - Attributes: CATEGORY = 'attributedef'

<a id='materialx-pymaterialxcore-backdrop'></a>

- **Backdrop**: A layout element used to contain, group and document nodes within a graph.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None
        
        Set the contains string for this backdrop.


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a contains string.


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str
        
        Return the contains string for this backdrop.


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: typing.SupportsFloat) -> None
        
        Set the width attribute of the backdrop.


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a width attribute.


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the width attribute of the backdrop.


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: typing.SupportsFloat) -> None
        
        Set the height attribute of the backdrop.


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a height attribute.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the height attribute of the backdrop.


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.TypedElement]) -> None
        
        Set the vector of elements that this backdrop contains.


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]
        
        Return the vector of elements that this backdrop contains.


  - Attributes: CATEGORY = 'backdrop', CONTAINS_ATTRIBUTE = 'contains', WIDTH_ATTRIBUTE = 'width', HEIGHT_ATTRIBUTE = 'height'

<a id='materialx-pymaterialxcore-collection'></a>

- **Collection**: A collection element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None
        
        Set the include geometry string of this element.


    - `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if this element has an include geometry string.


    - `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str
        
        Return the include geometry string of this element.


    - `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None
        
        Set the exclude geometry string of this element.


    - `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if this element has an exclude geometry string.


    - `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str
        
        Return the exclude geometry string of this element.


    - `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None
        
        Set the include collection string of this element.


    - `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if this element has an include collection string.


    - `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str
        
        Return the include collection string of this element.


    - `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None
        
        Set the collection that is directly included by this element.


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Collection]) -> None
        
        Set the vector of collections that are directly included by this element.


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]
        
        Return the vector of collections that are directly included by this element.


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if the include chain for this element contains a cycle.


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool
        
        Return true if this collection and the given geometry string have any geometries in common.


  - Attributes: CATEGORY = 'collection'

<a id='materialx-pymaterialxcore-color3'></a>

- **Color3**: A three-component color value.

  - Inherits from: [VectorBase](#materialx-pymaterialxcore-vectorbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


<a id='materialx-pymaterialxcore-color4'></a>

- **Color4**: A four-component color value.

  - Inherits from: [VectorBase](#materialx-pymaterialxcore-vectorbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


<a id='materialx-pymaterialxcore-commentelement'></a>

- **CommentElement**: An element representing a block of descriptive text within a document, which will be stored a comment when the document is written out.

The comment text may be accessed with the methods Element::setDocString and Element::getDocString.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'comment'

<a id='materialx-pymaterialxcore-document'></a>

- **Document**: A MaterialX document, which represents the top-level element in the MaterialX ownership hierarchy.

Use the factory function createDocument() to create a Document instance.

  - Inherits from: [GraphElement](#materialx-pymaterialxcore-graphelement), [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None
        
        Initialize the document, removing any existing content.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document
        
        Create a deep copy of the document.


    - `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Store a reference to a data library in this document.


    - `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document
        
        Return the data library, if any, referenced by this document.


    - `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool
        
        Return true if this document has a data library.


    - `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Import the given data library into this document.
        
        Args:
            library: The data library to be imported.


    - `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]
        
        Get a list of source URIs referenced by the document.


    - `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph
        
        Add a NodeGraph to the document.
        
        Args:
            name: The name of the new NodeGraph. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new NodeGraph.


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph
        
        Return the NodeGraph, if any, with the given name.


    - `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]
        
        Return a vector of all NodeGraph elements in the document.


    - `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the NodeGraph, if any, with the given name.


    - `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]
        
        Return a vector of all port elements that match the given node name.
        
        Port elements support spatially-varying upstream connections to nodes, and include both Input and Output elements.


    - `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo
        
        Add a GeomInfo to the document.
        
        Args:
            name: The name of the new GeomInfo. If no name is specified, then a unique name will automatically be generated.
            geom: An optional geometry string for the GeomInfo.
        
        Returns:
            A shared pointer to the new GeomInfo.


    - `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo
        
        Return the GeomInfo, if any, with the given name.


    - `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]
        
        Return a vector of all GeomInfo elements in the document.


    - `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the GeomInfo, if any, with the given name.


    - `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value
        
        Return the value of a geometric property for the given geometry string.


    - `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef
        
        Add a GeomPropDef to the document.
        
        Args:
            name: The name of the new GeomPropDef.
            geomprop: The geometric property to use for the GeomPropDef.
        
        Returns:
            A shared pointer to the new GeomPropDef.


    - `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef
        
        Return the GeomPropDef, if any, with the given name.


    - `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]
        
        Return a vector of all GeomPropDef elements in the document.


    - `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the GeomPropDef, if any, with the given name.


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look
        
        Add a Look to the document.
        
        Args:
            name: The name of the new Look. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Look.


    - `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look
        
        Return the Look, if any, with the given name.


    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]
        
        Return a vector of all Look elements in the document.


    - `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the Look, if any, with the given name.


    - `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup
        
        Add a LookGroup to the document.
        
        Args:
            name: The name of the new LookGroup. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new LookGroup.


    - `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup
        
        Return the LookGroup, if any, with the given name.


    - `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]
        
        Return a vector of all LookGroup elements in the document.


    - `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the LookGroup, if any, with the given name.


    - `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection
        
        Add a Collection to the document.
        
        Args:
            name: The name of the new Collection. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Collection.


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection
        
        Return the Collection, if any, with the given name.


    - `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]
        
        Return a vector of all Collection elements in the document.


    - `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the Collection, if any, with the given name.


    - `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef
        
        Add a TypeDef to the document.
        
        Args:
            name: The name of the new TypeDef. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new TypeDef.


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef
        
        Return the TypeDef, if any, with the given name.


    - `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]
        
        Return a vector of all TypeDef elements in the document.


    - `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the TypeDef, if any, with the given name.


    - `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef
        
        Add a NodeDef to the document.
        
        Args:
            name: The name of the new NodeDef. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string. If specified, then the new NodeDef will be assigned an Output of the given type.
            node: An optional node string.
        
        Returns:
            A shared pointer to the new NodeDef.


    - `addNodeDefFromGraph`: addNodeDefFromGraph(*args, **kwargs)
        Overloaded function.
        
        1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef
        
        2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef
        
        Return the NodeDef, if any, with the given name.


    - `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]
        
        Return a vector of all NodeDef elements in the document.


    - `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the NodeDef, if any, with the given name.


    - `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]
        
        Return a vector of all NodeDef elements that match the given node name.


    - `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef
        
        Add an AttributeDef to the document.
        
        Args:
            name: The name of the new AttributeDef. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new AttributeDef.


    - `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef
        
        Return the AttributeDef, if any, with the given name.


    - `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]
        
        Return a vector of all AttributeDef elements in the document.


    - `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the AttributeDef, if any, with the given name.


    - `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef
        
        Add an TargetDef to the document.
        
        Args:
            name: The name of the new TargetDef. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new TargetDef.


    - `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef
        
        Return the AttributeDef, if any, with the given name.


    - `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]
        
        Return a vector of all TargetDef elements in the document.


    - `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the TargetDef, if any, with the given name.


    - `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet
        
        Add a PropertySet to the document.
        
        Args:
            name: The name of the new PropertySet. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new PropertySet.


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet
        
        Return the PropertySet, if any, with the given name.


    - `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]
        
        Return a vector of all PropertySet elements in the document.


    - `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the PropertySet, if any, with the given name.


    - `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet
        
        Add a VariantSet to the document.
        
        Args:
            name: The name of the new VariantSet. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new VariantSet.


    - `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet
        
        Return the VariantSet, if any, with the given name.


    - `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]
        
        Return a vector of all VariantSet elements in the document.


    - `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the VariantSet, if any, with the given name.


    - `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation
        
        Add an Implementation to the document.
        
        Args:
            name: The name of the new Implementation. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Implementation.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation
        
        Return the Implementation, if any, with the given name.


    - `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]
        
        Return a vector of all Implementation elements in the document.


    - `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the Implementation, if any, with the given name.


    - `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]
        
        Return a vector of all node implementations that match the given NodeDef string.
        
        Note that a node implementation may be either an Implementation element or NodeGraph element.


    - `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef
        
        Return the UnitDef, if any, with the given name.


    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]
        
        Return a vector of all Member elements in the TypeDef.


    - `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the UnitDef, if any, with the given name.


    - `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef
        
        Return the UnitTypeDef, if any, with the given name.


    - `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]
        
        Return a vector of all UnitTypeDef elements in the document.


    - `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Remove the UnitTypeDef, if any, with the given name.


    - `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None
        
        Upgrade the content of this document from earlier supported versions to the library version.


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Set the color management system string.


    - `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool
        
        Return true if a color management system string has been set.


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str
        
        Return the color management system string.


    - `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None
        
        Set the color management config string.


    - `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool
        
        Return true if a color management config string has been set.


    - `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str
        
        Return the color management config string.


    - `addMaterial`: (Deprecated) Add a material element to the document.


    - `getMaterials`: (Deprecated) Return a vector of all materials in the document.


<a id='materialx-pymaterialxcore-edge'></a>

- **Edge**: An edge between two connected Elements, returned during graph traversal.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str
        
        Return the name of this edge, if any.


<a id='materialx-pymaterialxcore-element'></a>

- **Element**: The base class for MaterialX elements.

An Element is a named object within a Document, which may possess any number of child elements and attributes.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's category string.


    - `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's category string.
        
        The category of a MaterialX element represents its role within the document, with common examples being "material", "nodegraph", and "image".


    - `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's name string.


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's name string.


    - `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str
        
        Return the element's hierarchical name path, relative to the root document.
        
        Args:
            relativeTo: If a valid ancestor element is specified, then the returned path will be relative to this ancestor.


    - `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element
        
        Return the element specified by the given hierarchical name path, relative to the current element.
        
        Args:
            namePath: The relative name path of the specified element.


    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's file prefix string.


    - `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if the given element has a file prefix string.


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's file prefix string.


    - `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the file prefix string that is active at the scope of this element, taking all ancestor elements into account.


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's geom prefix string.


    - `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if the given element has a geom prefix string.


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's geom prefix string.


    - `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the geom prefix string that is active at the scope of this element, taking all ancestor elements into account.


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's color space string.


    - `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if the given element has a color space string.


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's color space string.


    - `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the color space string that is active at the scope of this element, taking all ancestor elements into account.


    - `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the inherit string of this element.


    - `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if this element has an inherit string.


    - `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the inherit string of this element.


    - `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None
        
        Set the element that this one directly inherits from.


    - `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return the element, if any, that this one directly inherits from.


    - `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if this element has the given element as an inherited base, taking the full inheritance chain into account.


    - `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if the inheritance chain for this element contains a cycle.


    - `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the namespace string of this element.


    - `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if this element has a namespace string.


    - `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the namespace string of this element.


    - `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str
        
        Return a qualified version of the given name, taking the namespace at the scope of this element into account.


    - `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the documentation string of this element.


    - `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the documentation string of this element.


    - `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element
        
        Add a child element of the given category and name.
        
        Args:
            category: The category string of the new child element. If the category string is recognized, then the corresponding Element subclass is generated; otherwise, a GenericElement is generated.
            name: The name of the new child element. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new child element.


    - `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element
        
        Change the category of the given child element.
        
        Args:
            child: The child element that will be modified.
            category: The new category string for the child element.
        
        Returns:
            A shared pointer to a new child element, containing the contents of the original child but with a new category and subclass.


    - `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]
        
        Return a constant vector of all child elements.
        
        The returned vector maintains the order in which children were added.


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: typing.SupportsInt) -> None
        
        Set the index of the child, if any, with the given name.
        
        If the given index is out of bounds, then an exception is thrown.


    - `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int
        
        Return the index of the child, if any, with the given name.
        
        If no child with the given name is found, then -1 is returned.


    - `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Remove the child element, if any, with the given name.


    - `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None
        
        Set the value string of the given attribute.


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool
        
        Return true if the given attribute is present.


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str
        
        Return the value string of the given attribute.
        
        If the given attribute is not present, then an empty string is returned.


    - `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]
        
        Return a vector of stored attribute names, in the order they were set.


    - `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Remove the given attribute, if present.


    - `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator
        
        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.
        
        Returns:
            A TreeIterator object.


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator
        
        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.
        
        Returns:
            A GraphIterator object.


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: typing.SupportsInt = 0) -> MaterialX_v1_39_5::Edge
        
        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.
        
        Args:
            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.
        
        Returns:
            The upstream Edge, if valid, or an empty Edge object.


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int
        
        Return the number of queryable upstream edges for this element.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: typing.SupportsInt = 0) -> MaterialX.PyMaterialXCore.Element
        
        Return the Element with the given index that lies directly upstream from this one in the dataflow graph.
        
        Args:
            index: An optional index of the element to be returned, where the valid index range may be determined with getUpstreamEdgeCount.
        
        Returns:
            The upstream Element, if valid, or an empty ElementPtr.


    - `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator
        
        Traverse the inheritance chain from the given element to each element from which it inherits.
        
        Returns:
            An InheritanceIterator object.


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None
        
        Set the element's source URI.
        
        Args:
            sourceUri: A URI string representing the resource from which this element originates. This string may be used by serialization and deserialization routines to maintain hierarchies of include references.


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool
        
        Return true if this element has a source URI.


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the element's source URI.


    - `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return the source URI that is active at the scope of this element, taking all ancestor elements into account.


    - `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]
        
        Validate that the given document is consistent with the MaterialX specification.
        
        Args:
            message: An optional output string, to which a description of each error will be appended.
        
        Returns:
            True if the document passes all tests, false otherwise.


    - `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None
        
        Copy all attributes and descendants from the given element to this one.
        
        Args:
            source: The element from which content is copied.


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -> None
        
        Clear all attributes and descendants from this element.


    - `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str
        
        Using the input name as a starting point, modify it to create a valid, unique name for a child element.


    - `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_5::StringResolver
        
        Construct a StringResolver at the scope of this element.
        
        Args:
            geom: An optional geometry name, which will be used to select the applicable set of geometry token substitutions. By default, no geometry token substitutions are applied. If the universal geometry name "/" is given, then all geometry token substitutions are applied,
        
        Returns:
            A shared pointer to a StringResolver.


    - `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -> str
        
        Return a single-line description of this element, including its category, name, and attributes.


    - `isA`: Return True if this element is an instance of the given subclass.
               If a category string is specified, then both subclass and category
               matches are required.


    - `addChild`: Add a child element of the given subclass, name, and optional type string.


    - `getChild`: Return the child element, if any, with the given name.


    - `getChildOfType`: Return the child element, if any, with the given name and subclass.


    - `getChildrenOfType`: Return a list of all child elements that are instances of the given type.
               The returned list maintains the order in which children were added.


    - `removeChildOfType`: Remove the typed child element, if any, with the given name.


  - Attributes: NAME_ATTRIBUTE = 'name', FILE_PREFIX_ATTRIBUTE = 'fileprefix', GEOM_PREFIX_ATTRIBUTE = 'geomprefix', COLOR_SPACE_ATTRIBUTE = 'colorspace', INHERIT_ATTRIBUTE = 'inherit', NAMESPACE_ATTRIBUTE = 'namespace', DOC_ATTRIBUTE = 'doc', XPOS_ATTRIBUTE = 'xpos', YPOS_ATTRIBUTE = 'ypos'

<a id='materialx-pymaterialxcore-elementequivalenceoptions'></a>

- **ElementEquivalenceOptions**: A set of options for comparing the functional equivalence of elements.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: performValueComparisons = (property), floatFormat = (property), floatPrecision = (property), attributeExclusionList = (property)

<a id='materialx-pymaterialxcore-elementpredicate'></a>

- **ElementPredicate**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

<a id='materialx-pymaterialxcore-exception'></a>

- **Exception**: 

  - Inherits from: [Exception](#materialx-pymaterialxcore-exception), [BaseException](#materialx-pymaterialxcore-baseexception)

<a id='materialx-pymaterialxcore-exceptionfoundcycle'></a>

- **ExceptionFoundCycle**: 

  - Inherits from: [Exception](#materialx-pymaterialxcore-exception), [BaseException](#materialx-pymaterialxcore-baseexception)

<a id='materialx-pymaterialxcore-exceptionorphanedelement'></a>

- **ExceptionOrphanedElement**: 

  - Inherits from: [Exception](#materialx-pymaterialxcore-exception), [BaseException](#materialx-pymaterialxcore-baseexception)

<a id='materialx-pymaterialxcore-genericelement'></a>

- **GenericElement**: A generic element subclass, for instantiating elements with unrecognized categories.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'generic'

<a id='materialx-pymaterialxcore-geomelement'></a>

- **GeomElement**: The base class for geometric elements, which support bindings to geometries and geometric collections.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None
        
        Set the geometry string of this element.


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool
        
        Return true if this element has a geometry string.


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str
        
        Return the geometry string of this element.


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None
        
        Set the collection string of this element.


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool
        
        Return true if this element has a collection string.


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str
        
        Return the collection string of this element.


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None
        
        Assign a Collection to this element.


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection
        
        Return the Collection that is assigned to this element.


<a id='materialx-pymaterialxcore-geominfo'></a>

- **GeomInfo**: A geometry info element within a Document.

  - Inherits from: [GeomElement](#materialx-pymaterialxcore-geomelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp
        
        Add a GeomProp to this element.
        
        Args:
            name: The name of the new GeomProp. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new GeomProp.


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp
        
        Return the GeomProp, if any, with the given name.


    - `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]
        
        Return a vector of all GeomProp elements.


    - `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None
        
        Remove the GeomProp, if any, with the given name.


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token
        
        Add a Token to this element.
        
        Args:
            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Token.


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token
        
        Return the Token, if any, with the given name.


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]
        
        Return a vector of all Token elements.


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None
        
        Remove the Token, if any, with the given name.


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token
        
        Set the string value of a Token by its name, creating a child element to hold the Token if needed.


    - `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element
               to hold the geomprop if needed.


    - `addGeomAttr`: (Deprecated) Add a geomprop to this element.


    - `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.


  - Attributes: CATEGORY = 'geominfo'

<a id='materialx-pymaterialxcore-geomprop'></a>

- **GeomProp**: A geometric property element within a GeomInfo.

  - Inherits from: [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'geomprop'

<a id='materialx-pymaterialxcore-geompropdef'></a>

- **GeomPropDef**: An element representing a declaration of geometric property data.

A GeomPropDef element contains a reference to a geometric node and a set of modifiers for that node. For example, a world-space normal can be declared as a reference to the "normal" geometric node with a space setting of "world", or a specific set of texture coordinates can be declared as a reference to the "texcoord" geometric node with an index setting of "1".

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setGeomProp`: setGeomProp(*args, **kwargs)
        Overloaded function.
        
        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        
        Set the geometric property string of this element.
        
        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        
        Set the geometric property string of this element.


    - `hasGeomProp`: hasGeomProp(*args, **kwargs)
        Overloaded function.
        
        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        
        Return true if this element has a geometric property string.
        
        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        
        Return true if this element has a geometric property string.


    - `getGeomProp`: getGeomProp(*args, **kwargs)
        Overloaded function.
        
        1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the geometric property string of this element.
        
        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the geometric property string of this element.


    - `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        
        Set the geometric space string of this element.


    - `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        
        Return true if this element has a geometric space string.


    - `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the geometric space string of this element.


    - `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None
        
        Set the index string of this element.


    - `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool
        
        Return true if this element has an index string.


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the index string of this element.


  - Attributes: CATEGORY = 'geompropdef'

<a id='materialx-pymaterialxcore-graphelement'></a>

- **GraphElement**: The base class for graph elements such as NodeGraph and Document.

  - Inherits from: [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node
        
        Add a Node to the graph.
        
        Args:
            category: The category of the new Node.
            name: The name of the new Node. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.
        
        Returns:
            A shared pointer to the new Node.


    - `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node
        
        Add a Node that is an instance of the given NodeDef.


    - `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the Node, if any, with the given name.


    - `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]
        
        Return a vector of all Nodes in the graph, optionally filtered by the given category string.


    - `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None
        
        Remove the Node, if any, with the given name.


    - `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node
        
        Add a material node to the graph, optionally connecting it to the given shader node.


    - `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]
        
        Return a vector of all material nodes.


    - `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop
        
        Add a Backdrop to the graph.


    - `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop
        
        Return the Backdrop, if any, with the given name.


    - `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]
        
        Return a vector of all Backdrop elements in the graph.


    - `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None
        
        Remove the Backdrop, if any, with the given name.


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: collections.abc.Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None
        
        Flatten all subgraphs at the root scope of this graph element, recursively replacing each graph-defined node with its equivalent node network.
        
        Args:
            target: An optional target string to be used in specifying which node definitions are used in this process.
            filter: An optional node predicate specifying which nodes should be included and excluded from this process.


    - `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]
        
        Return a vector of all children (nodes and outputs) sorted in topological order.


    - `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node
        
        If not yet present, add a geometry node to this graph matching the given property definition and name prefix.


    - `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str
        
        Convert this graph to a string in the DOT language syntax.
        
        This can be used to visualise the graph using GraphViz (http://www.graphviz.org).
        
        If declarations for the contained nodes are provided as nodedefs in the owning document, then they will be used to provide additional formatting details.


<a id='materialx-pymaterialxcore-graphiterator'></a>

- **GraphIterator**: An iterator object representing the state of an upstream graph traversal.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the current edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element, if any, of the current edge.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the current edge.


    - `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int
        
        Return the index of the current edge within the range of upstream edges available to the downstream element.


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int
        
        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.


    - `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int
        
        Return the node depth of the current traversal, where a single edge between two nodes represents a depth of one.


    - `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None
        
        Set the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.
        
        Args:
            prune: If set to true, then the current subgraph will be pruned.


    - `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool
        
        Return the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.


<a id='materialx-pymaterialxcore-implementation'></a>

- **Implementation**: An implementation element within a Document.

An Implementation is used to associate external source code with a specific NodeDef, providing a definition for the node that may either be universal or restricted to a specific target.

  - Inherits from: [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the file string for the Implementation.


    - `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a file string.


    - `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the file string for the Implementation.


    - `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the function string for the Implementation.


    - `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a function string.


    - `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the function string for the Implementation.


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None
        
        Set the NodeDef element referenced by the Implementation.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef
        
        Return the NodeDef element referenced by the Implementation.


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the nodegraph string for the Implementation.


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a nodegraph string.


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the nodegraph string for the Implementation.


  - Attributes: CATEGORY = 'implementation', FILE_ATTRIBUTE = 'file', FUNCTION_ATTRIBUTE = 'function'

<a id='materialx-pymaterialxcore-inheritanceiterator'></a>

- **InheritanceIterator**: An iterator object representing the current state of an inheritance traversal.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

<a id='materialx-pymaterialxcore-input'></a>

- **Input**: An input element within a Node or NodeDef.

An Input holds either a uniform value or a connection to a spatially-varying Output, either of which may be modified within the scope of a Material.

  - Inherits from: [PortElement](#materialx-pymaterialxcore-portelement), [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None
        
        Set the defaultgeomprop string for the input.


    - `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool
        
        Return true if the given input has a defaultgeomprop string.


    - `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str
        
        Return the defaultgeomprop string for the input.


    - `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef
        
        Return the GeomPropDef element to use, if defined for this input.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None
        
        Connects this input to a corresponding interface with the given name.
        
        If the interface name specified is an empty string then any existing connection is removed.


    - `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input
        
        Return the input on the parent graph corresponding to the interface name for this input.


  - Attributes: CATEGORY = 'input'

<a id='materialx-pymaterialxcore-interfaceelement'></a>

- **InterfaceElement**: The base class for interface elements such as Node, NodeDef, and NodeGraph.

An InterfaceElement supports a set of Input and Output elements, with an API for setting their values.

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the NodeDef string for the interface.


    - `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if the given interface has a NodeDef string.


    - `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the NodeDef string for the interface.


    - `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input
        
        Add an Input to this interface.
        
        Args:
            name: The name of the new Input. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.
        
        Returns:
            A shared pointer to the new Input.


    - `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input
        
        Return the Input, if any, with the given name.


    - `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]
        
        Return a vector of all Input elements.


    - `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int
        
        Return the number of Input elements.


    - `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Remove the Input, if any, with the given name.


    - `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input
        
        Return the first Input with the given name that belongs to this interface, taking interface inheritance into account.


    - `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]
        
        Return a vector of all Input elements that belong to this interface, taking inheritance into account.


    - `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output
        
        Add an Output to this interface.
        
        Args:
            name: The name of the new Output. If no name is specified, then a unique name will automatically be generated.
            type: An optional type string.
        
        Returns:
            A shared pointer to the new Output.


    - `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output
        
        Return the Output, if any, with the given name.


    - `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return a vector of all Output elements.


    - `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int
        
        Return the number of Output elements.


    - `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Remove the Output, if any, with the given name.


    - `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output
        
        Return the first Output with the given name that belongs to this interface, taking interface inheritance into account.


    - `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return a vector of all Output elements that belong to this interface, taking inheritance into account.


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None
        
        Set the output to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing output connection on the input will be cleared.


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output
        
        Return the output connected to the given input.
        
        If the given input is not present, then an empty OutputPtr is returned.


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token
        
        Add a Token to this interface.
        
        Args:
            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Token.


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token
        
        Return the Token, if any, with the given name.


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]
        
        Return a vector of all Token elements.


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Remove the Token, if any, with the given name.


    - `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token
        
        Return the first Token with the given name that belongs to this interface, taking interface inheritance into account.


    - `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]
        
        Return a vector of all Token elements that belong to this interface, taking inheritance into account.


    - `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement
        
        Return the first value element with the given name that belongs to this interface, taking interface inheritance into account.
        
        Examples of value elements are Input, Output, and Token.


    - `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]
        
        Return a vector of all value elements that belong to this interface, taking inheritance into account.
        
        Examples of value elements are Input, Output, and Token.


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token
        
        Set the string value of a Token by its name, creating a child element to hold the Token if needed.


    - `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str
        
        Return the string value of a Token by its name, or an empty string if the given Token is not present.


    - `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the target string of this interface.


    - `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if the given interface has a target string.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the target string of this interface.


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the version string of this interface.


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if this interface has a version string.


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the version string of this interface.


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> None
        
        Set the major and minor versions as an integer pair.


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]
        
        Return the major and minor versions as an integer pair.


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None
        
        Set the default version flag of this element.


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return the default version flag of this element.


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first declaration of this interface, optionally filtered by the given target name.
        
        Args:
            target: An optional target name, which will be used to filter the declarations that are considered.
        
        Returns:
            A shared pointer to declaration, or an empty shared pointer if no declaration was found.


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None
        
        Clear all attributes and descendants from this element.


    - `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool
        
        Return true if this instance has an exact input match with the given declaration, where each input of this the instance corresponds to a declaration input of the same name and type.
        
        If an exact input match is not found, and the optional message argument is provided, then an error message will be appended to the given string.


    - `setInputValue`: Set the typed value of an input by its name, creating a child element
               to hold the input if needed.


    - `getInputValue`: Return the typed value of an input by its name, taking both the
               calling element and its declaration into account.  If the given
               input is not found, then None is returned.


    - `addParameter`: (Deprecated) Add a Parameter to this interface.


    - `getParameters`: (Deprecated) Return a vector of all Parameter elements.


    - `getActiveParameters`: (Deprecated) Return a vector of all parameters belonging to this interface, taking inheritance into account.


    - `setParameterValue`: (Deprecated) Set the typed value of a parameter by its name.


    - `getParameterValue`: (Deprecated) Return the typed value of a parameter by its name.


    - `getParameterValueString`: (Deprecated) Return the value string of a parameter by its name.


    - `addBindInput`: (Deprecated) Add a BindInput to this shader reference.


    - `getBindInputs`: (Deprecated) Return a vector of all BindInput elements in this shader reference.


    - `addBindParam`: (Deprecated) Add a BindParam to this shader reference.


    - `getBindParams`: (Deprecated) Return a vector of all BindParam elements in this shader reference.


    - `getBindTokens`: (Deprecated) Return a vector of all BindToken elements in this shader reference.


  - Attributes: NODE_DEF_ATTRIBUTE = 'nodedef'

<a id='materialx-pymaterialxcore-linearunitconverter'></a>

- **LinearUnitConverter**: A converter class for linear units that require only a scalar multiplication.

  - Inherits from: [UnitConverter](#materialx-pymaterialxcore-unitconverter), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter
        
        Creator.


    - `getUnitScale`: getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]
        
        Return the mappings from unit names to the scale value defined by a linear converter.


    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: typing.SupportsFloat, arg1: str, arg2: str) -> float
        
        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: typing.SupportsInt) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


<a id='materialx-pymaterialxcore-look'></a>

- **Look**: A look element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign
        
        Add a MaterialAssign to the look.
        
        Args:
            name: The name of the new MaterialAssign. If no name is specified, then a unique name will automatically be generated.
            material: An optional material string, which should match the name of the material node to be assigned.
        
        Returns:
            A shared pointer to the new MaterialAssign.


    - `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign
        
        Return the MaterialAssign, if any, with the given name.


    - `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]
        
        Return a vector of all MaterialAssign elements in the look.


    - `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]
        
        Return a vector of all MaterialAssign elements that belong to this look, taking look inheritance into account.


    - `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None
        
        Remove the MaterialAssign, if any, with the given name.


    - `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign
        
        Add a PropertyAssign to the look.
        
        Args:
            name: The name of the new PropertyAssign. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new PropertyAssign.


    - `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign
        
        Return the PropertyAssign, if any, with the given name.


    - `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]
        
        Return a vector of all PropertyAssign elements in the look.


    - `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]
        
        Return a vector of all PropertyAssign elements that belong to this look, taking look inheritance into account.


    - `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None
        
        Remove the PropertyAssign, if any, with the given name.


    - `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign
        
        Add a PropertySetAssign to the look.
        
        Args:
            name: The name of the new PropertySetAssign. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new PropertySetAssign.


    - `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign
        
        Return the PropertySetAssign, if any, with the given name.


    - `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]
        
        Return a vector of all PropertySetAssign elements in the look.


    - `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]
        
        Return a vector of all PropertySetAssign elements that belong to this look, taking look inheritance into account.


    - `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None
        
        Remove the PropertySetAssign, if any, with the given name.


    - `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign
        
        Add a VariantAssign to the look.
        
        Args:
            name: The name of the new VariantAssign. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new VariantAssign.


    - `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign
        
        Return the VariantAssign, if any, with the given name.


    - `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]
        
        Return a vector of all VariantAssign elements in the look.


    - `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]
        
        Return a vector of all VariantAssign elements that belong to this look, taking look inheritance into account.


    - `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None
        
        Remove the VariantAssign, if any, with the given name.


    - `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility
        
        Add a Visibility to the look.
        
        Args:
            name: The name of the new Visibility. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Visibility.


    - `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility
        
        Return the Visibility, if any, with the given name.


    - `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]
        
        Return a vector of all Visibility elements in the look.


    - `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]
        
        Return a vector of all Visibility elements that belong to this look, taking look inheritance into account.


    - `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None
        
        Remove the Visibility, if any, with the given name.


  - Attributes: CATEGORY = 'look'

<a id='materialx-pymaterialxcore-lookgroup'></a>

- **LookGroup**: A look group element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Get comma-separated list of looks.


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set comma-separated list of looks.


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return the active look, if any.


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set the active look.


  - Attributes: CATEGORY = 'lookgroup', LOOKS_ATTRIBUTE = 'looks', ACTIVE_ATTRIBUTE = 'active'

<a id='materialx-pymaterialxcore-materialassign'></a>

- **MaterialAssign**: A material assignment element within a Look.

  - Inherits from: [GeomElement](#materialx-pymaterialxcore-geomelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None
        
        Set the material string for the MaterialAssign.


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return true if the given MaterialAssign has a material string.


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str
        
        Return the material string for the MaterialAssign.


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return the outputs on any referenced material.


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None
        
        Set the exclusive boolean for the MaterialAssign.


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return the exclusive boolean for the MaterialAssign.


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node
        
        Return the material node, if any, referenced by the MaterialAssign.


  - Attributes: CATEGORY = 'materialassign'

<a id='materialx-pymaterialxcore-matrix33'></a>

- **Matrix33**: A 3x3 matrix of floating-point values.

Vector transformation methods follow the row-vector convention, with matrix-vector multiplication computed as v' = vM.

  - Inherits from: [MatrixBase](#materialx-pymaterialxcore-matrixbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: typing.SupportsFloat) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the product of this matrix and a 3D vector.


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Transform the given 2D point.


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Transform the given 2D direction vector.


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D normal vector.


    - `createRotation`: createRotation(arg0: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix33
        
        Create a rotation matrix.
        
        Args:
            angle: Angle in radians


  - Attributes: IDENTITY = (property)

<a id='materialx-pymaterialxcore-matrix44'></a>

- **Matrix44**: A 4x4 matrix of floating-point values.

Vector transformation methods follow the row-vector convention, with matrix-vector multiplication computed as v' = vM.

  - Inherits from: [MatrixBase](#materialx-pymaterialxcore-matrixbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: typing.SupportsFloat) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return the product of this matrix and a 4D vector.


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D point.


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D direction vector.


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D normal vector.


    - `createRotationX`: createRotationX(arg0: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a rotation matrix about the X-axis.
        
        Args:
            angle: Angle in radians


    - `createRotationY`: createRotationY(arg0: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a rotation matrix about the Y-axis.
        
        Args:
            angle: Angle in radians


    - `createRotationZ`: createRotationZ(arg0: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a rotation matrix about the Z-axis.
        
        Args:
            angle: Angle in radians


  - Attributes: IDENTITY = (property)

<a id='materialx-pymaterialxcore-matrixbase'></a>

- **MatrixBase**: The base class for square matrices of scalar values.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

<a id='materialx-pymaterialxcore-member'></a>

- **Member**: A member element within a TypeDef.

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'typedef'

<a id='materialx-pymaterialxcore-newlineelement'></a>

- **NewlineElement**: An element representing a newline within a document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'newline'

<a id='materialx-pymaterialxcore-node'></a>

- **Node**: A node element within a NodeGraph or Document.

A Node represents an instance of a NodeDef within a graph, and its Input elements apply specific values and connections to that instance.

  - Inherits from: [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the Node connected to the given input.
        
        If the given input is not present, then an empty NodePtr is returned.


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None
        
        Set the name of the Node connected to the given input, creating a child element for the input if needed.


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str
        
        Return the name of the Node connected to the given input.
        
        If the given input is not present, then an empty string is returned.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef
        
        Return the first NodeDef that declares this node, optionally filtered by the given target name.
        
        Args:
            target: An optional target name, which will be used to filter the nodedefs that are considered.
            allowRoughMatch: If specified, then a rough match will be allowed when an exact match is not found. An exact match requires that each node input corresponds to a nodedef input of the same name and type.
        
        Returns:
            A NodeDef for this node, or an empty shared pointer if none was found.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first implementation for this node, optionally filtered by the given target and language names.
        
        Args:
            target: An optional target name, which will be used to filter the implementations that are considered.
        
        Returns:
            An implementation for this node, or an empty shared pointer if none was found. Note that a node implementation may be either an Implementation element or a NodeGraph element.


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]
        
        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.


    - `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input
        
        Add an input based on the corresponding input for the associated node definition.
        
        If the input already exists on the node it will just be returned.


    - `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None
        
        Add inputs based on the corresponding associated node definition.


    - `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.


    - `addShaderRef`: (Deprecated) Add a shader reference to this material element.


    - `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.


    - `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.


  - Attributes: CATEGORY = 'node'

<a id='materialx-pymaterialxcore-nodedef'></a>

- **NodeDef**: A node definition element within a Document.

A NodeDef provides the declaration of a node interface, which may then be instantiated as a Node.

  - Inherits from: [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None
        
        Set the node string of the NodeDef.


    - `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool
        
        Return true if the given NodeDef has a node string.


    - `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str
        
        Return the node string of the NodeDef.


    - `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None
        
        Set the node group of the NodeDef.


    - `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool
        
        Return true if the given NodeDef has a node group.


    - `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str
        
        Return the node group of the NodeDef.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '', resolveNodeGraph: bool = True) -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first implementation for this nodedef, optionally filtered by the given target name.
        
        Args:
            target: An optional target name, which will be used to filter the implementations that are considered.
            resolveNodeGraph: Allow resolution of Implementation elements to their linked NodeGraph elements. Defaults to true.
        
        Returns:
            An implementation for this nodedef, or an empty shared pointer if none was found. Note that a node implementation may be either an Implementation element or a NodeGraph element.


    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool
        
        Return true if the given version string is compatible with this NodeDef.
        
        This may be used to test, for example, whether a NodeDef and Node may be used together.


  - Attributes: CATEGORY = 'nodedef', NODE_ATTRIBUTE = 'node', TEXTURE_NODE_GROUP = 'texture', PROCEDURAL_NODE_GROUP = 'procedural', GEOMETRIC_NODE_GROUP = 'geometric', ADJUSTMENT_NODE_GROUP = 'adjustment', CONDITIONAL_NODE_GROUP = 'conditional', CHANNEL_NODE_GROUP = 'channel', ORGANIZATION_NODE_GROUP = 'organization', TRANSLATION_NODE_GROUP = 'translation'

<a id='materialx-pymaterialxcore-nodegraph'></a>

- **NodeGraph**: A node graph element within a Document.

  - Inherits from: [GraphElement](#materialx-pymaterialxcore-graphelement), [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return all material-type outputs of the nodegraph.


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None
        
        Set the NodeDef element referenced by this NodeGraph.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef
        
        Return the NodeDef element referenced by this NodeGraph.


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first declaration of this interface, optionally filtered by the given target name.


    - `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input
        
        Add an interface name to an existing NodeDef associated with this NodeGraph.
        
        Args:
            inputPath: Path to an input descendant of this graph.
            interfaceName: The new interface name.
        
        Returns:
            Interface input.


    - `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None
        
        Remove an interface name from an existing NodeDef associated with this NodeGraph.
        
        Args:
            inputPath: Path to an input descendant of this graph.


    - `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None
        
        Modify the interface name on an existing NodeDef associated with this NodeGraph.
        
        Args:
            inputPath: Path to an input descendant of this graph.
            interfaceName: The new interface name.


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]
        
        Return a vector of all downstream ports that connect to this graph, ordered by the names of the port elements.


  - Attributes: CATEGORY = 'nodegraph'

<a id='materialx-pymaterialxcore-nodepredicate'></a>

- **NodePredicate**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

<a id='materialx-pymaterialxcore-output'></a>

- **Output**: A spatially-varying output element within a NodeGraph or NodeDef.

  - Inherits from: [PortElement](#materialx-pymaterialxcore-portelement), [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool
        
        Return true if a cycle exists in any upstream path from this element.


  - Attributes: CATEGORY = 'output', DEFAULT_INPUT_ATTRIBUTE = 'defaultinput'

<a id='materialx-pymaterialxcore-portelement'></a>

- **PortElement**: The base class for port elements such as Input and Output.

Port elements support spatially-varying upstream connections to nodes.

  - Inherits from: [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None
        
        Set the node name string of this element, creating a connection to the Node with the given name within the same NodeGraph.


    - `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str
        
        Return the node name string of this element.


    - `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None
        
        Set the node graph string of this element.


    - `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool
        
        Return true if this element has a node graph string.


    - `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str
        
        Return the node graph string of this element.


    - `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None
        
        Set the output string of this element.


    - `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool
        
        Return true if this element has an output string.


    - `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str
        
        Return the output string of this element.


    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None
        
        Set the node to which this element is connected.
        
        The given node must belong to the same node graph. If the node argument is null, then any existing node connection will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node
        
        Return the node, if any, to which this element is connected.


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None
        
        Set the output to which this input is connected.
        
        If the output argument is null, then any existing output connection will be cleared.


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output
        
        Return the output, if any, to which this input is connected.


<a id='materialx-pymaterialxcore-property'></a>

- **Property**: A property element within a PropertySet.

  - Inherits from: [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'property'

<a id='materialx-pymaterialxcore-propertyassign'></a>

- **PropertyAssign**: A property assignment element within a Look.

  - Inherits from: [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None
        
        Set the property string of this element.


    - `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool
        
        Return true if this element has a property string.


    - `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str
        
        Return the property string of this element.


    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None
        
        Set the geometry string of this element.


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool
        
        Return true if this element has a geometry string.


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str
        
        Return the geometry string of this element.


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None
        
        Set the collection string of this element.


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool
        
        Return true if this element has a collection string.


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str
        
        Return the collection string of this element.


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None
        
        Assign a Collection to this element.


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection
        
        Return the Collection that is assigned to this element.


  - Attributes: CATEGORY = 'propertyassign'

<a id='materialx-pymaterialxcore-propertyset'></a>

- **PropertySet**: A property set element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property
        
        Add a Property to the set.
        
        Args:
            name: The name of the new Property. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Property.


    - `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]
        
        Return a vector of all Property elements in the set.


    - `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None
        
        Remove the Property with the given name, if present.


    - `setPropertyValue`: Set the typed value of a property by its name, creating a child element
               to hold the property if needed.


    - `getPropertyValue`: Return the typed value of a property by its name.  If the given property
               is not found, then None is returned.


  - Attributes: CATEGORY = 'property'

<a id='materialx-pymaterialxcore-propertysetassign'></a>

- **PropertySetAssign**: A property set assignment element within a Look.

  - Inherits from: [GeomElement](#materialx-pymaterialxcore-geomelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None
        
        Set the property set string of this element.


    - `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool
        
        Return true if this element has a property set string.


    - `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str
        
        Return the property set string of this element.


    - `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None
        
        Assign a property set to this element.


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet
        
        Return the property set that is assigned to this element.


  - Attributes: CATEGORY = 'propertysetassign'

<a id='materialx-pymaterialxcore-stringresolver'></a>

- **StringResolver**: A helper object for applying string modifiers to data values in the context of a specific element and geometry.

A StringResolver may be constructed through the Element::createStringResolver method, which initializes it in the context of a specific element, geometry, and material.

Calling the StringResolver::resolve method applies all modifiers to a particular string value.

Methods such as StringResolver::setFilePrefix may be used to edit the stored string modifiers before calling StringResolver::resolve.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the file prefix for this context.


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the file prefix for this context.


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the geom prefix for this context.


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the geom prefix for this context.


    - `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the UDIM substring substitution for filename data values.
        
        This string will be used to replace the standard <UDIM> token.


    - `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the UV-tile substring substitution for filename data values.
        
        This string will be used to replace the standard <UVTILE> token.


    - `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None
        
        Set an arbitrary substring substitution for filename data values.


    - `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]
        
        Return the map of filename substring substitutions.


    - `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None
        
        Set an arbitrary substring substitution for geometry name data values.


    - `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]
        
        Return the map of geometry name substring substitutions.


    - `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str
        
        Given an input string and type, apply all appropriate modifiers and return the resulting string.


<a id='materialx-pymaterialxcore-targetdef'></a>

- **TargetDef**: A definition of an implementation target.

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]
        
        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.
        
        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.


  - Attributes: CATEGORY = 'targetdef'

<a id='materialx-pymaterialxcore-token'></a>

- **Token**: A token element representing a string value.

Token elements are used to define input and output values for string substitutions in image filenames.

  - Inherits from: [ValueElement](#materialx-pymaterialxcore-valueelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'token'

<a id='materialx-pymaterialxcore-treeiterator'></a>

- **TreeIterator**: An iterator object representing the state of a tree traversal.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the current element in the traversal.


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int
        
        Return the element depth of the current traversal, where the starting element represents a depth of zero.


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None
        
        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.
        
        Args:
            prune: If set to true, then the current subtree will be pruned.


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool
        
        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.


<a id='materialx-pymaterialxcore-typedef'></a>

- **TypeDef**: A type definition element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Set the semantic string of the TypeDef.


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool
        
        Return true if the given TypeDef has a semantic string.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str
        
        Return the semantic string of the TypeDef.


    - `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Set the context string of the TypeDef.


    - `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool
        
        Return true if the given TypeDef has a context string.


    - `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str
        
        Return the context string of the TypeDef.


    - `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member
        
        Add a Member to the TypeDef.
        
        Args:
            name: The name of the new Member. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Member.


    - `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member
        
        Return the Member, if any, with the given name.


    - `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]
        
        Return a vector of all Member elements in the TypeDef.


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Remove the Member, if any, with the given name.


  - Attributes: CATEGORY = 'typedef', SEMANTIC_ATTRIBUTE = 'semantic', CONTEXT_ATTRIBUTE = 'context'

<a id='materialx-pymaterialxcore-typedelement'></a>

- **TypedElement**: The base class for typed elements.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None
        
        Set the element's type string.


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the given element has a type string.


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str
        
        Return the element's type string.


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of color type.


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of multi-output type.


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef
        
        Return the TypeDef declaring the type string of this element.
        
        If no matching TypeDef is found, then an empty shared pointer is returned.


  - Attributes: TYPE_ATTRIBUTE = 'type'

<a id='materialx-pymaterialxcore-typedvalue_boolean'></a>

- **TypedValue_boolean**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'boolean'

<a id='materialx-pymaterialxcore-typedvalue_booleanarray'></a>

- **TypedValue_booleanarray**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str


    - `createValue`: createValue(arg0: collections.abc.Sequence[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'booleanarray'

<a id='materialx-pymaterialxcore-typedvalue_color3'></a>

- **TypedValue_color3**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'color3'

<a id='materialx-pymaterialxcore-typedvalue_color4'></a>

- **TypedValue_color4**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'color4'

<a id='materialx-pymaterialxcore-typedvalue_float'></a>

- **TypedValue_float**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str


    - `createValue`: createValue(arg0: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'float'

<a id='materialx-pymaterialxcore-typedvalue_floatarray'></a>

- **TypedValue_floatarray**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str


    - `createValue`: createValue(arg0: collections.abc.Sequence[typing.SupportsFloat]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'floatarray'

<a id='materialx-pymaterialxcore-typedvalue_integer'></a>

- **TypedValue_integer**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str


    - `createValue`: createValue(arg0: typing.SupportsInt) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'integer'

<a id='materialx-pymaterialxcore-typedvalue_integerarray'></a>

- **TypedValue_integerarray**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str


    - `createValue`: createValue(arg0: collections.abc.Sequence[typing.SupportsInt]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'integerarray'

<a id='materialx-pymaterialxcore-typedvalue_matrix33'></a>

- **TypedValue_matrix33**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'matrix33'

<a id='materialx-pymaterialxcore-typedvalue_matrix44'></a>

- **TypedValue_matrix44**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'matrix44'

<a id='materialx-pymaterialxcore-typedvalue_string'></a>

- **TypedValue_string**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'string'

<a id='materialx-pymaterialxcore-typedvalue_stringarray'></a>

- **TypedValue_stringarray**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str


    - `createValue`: createValue(arg0: collections.abc.Sequence[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'stringarray'

<a id='materialx-pymaterialxcore-typedvalue_vector2'></a>

- **TypedValue_vector2**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'vector2'

<a id='materialx-pymaterialxcore-typedvalue_vector3'></a>

- **TypedValue_vector3**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'vector3'

<a id='materialx-pymaterialxcore-typedvalue_vector4'></a>

- **TypedValue_vector4**: 

  - Inherits from: [Value](#materialx-pymaterialxcore-value), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE = 'vector4'

<a id='materialx-pymaterialxcore-unit'></a>

- **Unit**: A unit declaration within a UnitDef.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'unit'

<a id='materialx-pymaterialxcore-unitconverter'></a>

- **UnitConverter**: An abstract base class for unit converters.

Each unit converter instance is responsible for a single unit type.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: typing.SupportsFloat, arg1: str, arg2: str) -> float
        
        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer Returns -1 value if not found.


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: typing.SupportsInt) -> str
        
        Given an integer index return the unit name in the map used by the converter Returns Empty string if not found.


<a id='materialx-pymaterialxcore-unitconverterregistry'></a>

- **UnitConverterRegistry**: A registry for unit converters.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry
        
        Creator.


    - `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool
        
        Add a unit converter for a given UnitDef.
        
        Returns false if a converter has already been registered for the given UnitDef


    - `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool
        
        Remove a unit converter for a given UnitDef.
        
        Returns false if a converter does not exist for the given UnitDef


    - `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter
        
        Get a unit converter for a given UnitDef Returns any empty pointer if a converter does not exist for the given UnitDef.


    - `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None
        
        Clear all unit converters from the registry.


<a id='materialx-pymaterialxcore-unitdef'></a>

- **UnitDef**: A unit definition element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str
        
        Return the element's type string.


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Add a Unit to the UnitDef.
        
        Args:
            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.
        
        Returns:
            A shared pointer to the new Unit.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Return the Unit, if any, with the given name.


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]
        
        Return a vector of all Unit elements in the UnitDef.


  - Attributes: CATEGORY = 'unitdef', UNITTYPE_ATTRIBUTE = 'unittype'

<a id='materialx-pymaterialxcore-unittypedef'></a>

- **UnitTypeDef**: A unit type definition element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]
        
        Find all UnitDefs for the UnitTypeDef.


  - Attributes: CATEGORY = 'unittypedef'

<a id='materialx-pymaterialxcore-value'></a>

- **Value**: A generic, discriminated value, whose type may be queried dynamically.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return the value string for this value.


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return the type string for this value.


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value
        
        Create a new value instance from value and type strings.
        
        Returns:
            A shared pointer to a typed value, or an empty shared pointer if the conversion to the given data type cannot be performed.


<a id='materialx-pymaterialxcore-valueelement'></a>

- **ValueElement**: The base class for elements that support typed values.

  - Inherits from: [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the value string of an element.


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a value string.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Get the value string of a element.


    - `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str
        
        Return the resolved value string of an element, applying any string substitutions that are defined at the element's scope.
        
        Args:
            resolver: An optional string resolver, which will be used to apply string substitutions. By default, a new string resolver will be created at this scope and applied to the return value.


    - `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the interface name of an element.


    - `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has an interface name.


    - `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the interface name of an element.


    - `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the implementation name of an element.


    - `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has an implementation name.


    - `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the implementation name of an element.


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the unit string of an element.


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unit string.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit string of an element.


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit defined by the associated NodeDef if this element is a child of a Node.


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the unit type of an element.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unit type.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type of an element.


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        The the uniform attribute flag for this element.


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None
        
        Set the uniform attribute flag on this element.


    - `setValue`: Set the typed value of an element.


    - `getValue`: Return the typed value of an element.


    - `getDefaultValue`: Return the default value for this element.


  - Attributes: VALUE_ATTRIBUTE = 'value', INTERFACE_NAME_ATTRIBUTE = 'interfacename', IMPLEMENTATION_NAME_ATTRIBUTE = 'implname', IMPLEMENTATION_TYPE_ATTRIBUTE = 'impltype', ENUM_ATTRIBUTE = 'enum', ENUM_VALUES_ATTRIBUTE = 'enumvalues', UNIT_ATTRIBUTE = 'unit', UI_NAME_ATTRIBUTE = 'uiname', UI_FOLDER_ATTRIBUTE = 'uifolder', UI_MIN_ATTRIBUTE = 'uimin', UI_MAX_ATTRIBUTE = 'uimax', UI_SOFT_MIN_ATTRIBUTE = 'uisoftmin', UI_SOFT_MAX_ATTRIBUTE = 'uisoftmax', UI_STEP_ATTRIBUTE = 'uistep', UI_ADVANCED_ATTRIBUTE = 'uiadvanced'

<a id='materialx-pymaterialxcore-variant'></a>

- **Variant**: A variant element within a VariantSet.

  - Inherits from: [InterfaceElement](#materialx-pymaterialxcore-interfaceelement), [TypedElement](#materialx-pymaterialxcore-typedelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Attributes: CATEGORY = 'variant'

<a id='materialx-pymaterialxcore-variantassign'></a>

- **VariantAssign**: A variant assignment element within a Look.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None
        
        Set the element's variant set string.


    - `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool
        
        Return true if the given element has a variant set string.


    - `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str
        
        Return the element's variant set string.


    - `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None
        
        Set the element's variant string.


    - `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool
        
        Return true if the given element has a variant string.


    - `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str
        
        Return the element's variant string.


  - Attributes: CATEGORY = 'variantassign'

<a id='materialx-pymaterialxcore-variantset'></a>

- **VariantSet**: A variant set element within a Document.

  - Inherits from: [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant
        
        Add a Variant to the variant set.
        
        Args:
            name: The name of the new Variant. If no name is specified, then a unique name will automatically be generated.
        
        Returns:
            A shared pointer to the new Variant.


    - `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant
        
        Return the Variant, if any, with the given name.


    - `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]
        
        Return a vector of all Variant elements in the look.


    - `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None
        
        Remove the Variant, if any, with the given name.


  - Attributes: CATEGORY = 'variantset'

<a id='materialx-pymaterialxcore-vector2'></a>

- **Vector2**: A vector of two floating-point values.

  - Inherits from: [VectorBase](#materialx-pymaterialxcore-vectorbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


<a id='materialx-pymaterialxcore-vector3'></a>

- **Vector3**: A vector of three floating-point values.

  - Inherits from: [VectorBase](#materialx-pymaterialxcore-vectorbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


<a id='materialx-pymaterialxcore-vector4'></a>

- **Vector4**: A vector of four floating-point values.

  - Inherits from: [VectorBase](#materialx-pymaterialxcore-vectorbase), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


<a id='materialx-pymaterialxcore-vectorbase'></a>

- **VectorBase**: The base class for vectors of scalar values.

  - Inherits from: [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

<a id='materialx-pymaterialxcore-visibility'></a>

- **Visibility**: A visibility element within a Look.

A Visibility describes the visibility relationship between two geometries or geometric collections.

  - Inherits from: [GeomElement](#materialx-pymaterialxcore-geomelement), [Element](#materialx-pymaterialxcore-element), [pybind11_object](#materialx-pymaterialxcore-pybind11_object)

  - Methods:

    - `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None
        
        Set the viewer geom string of the element.


    - `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool
        
        Return true if the given element has a viewer geom string.


    - `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str
        
        Return the viewer geom string of the element.


    - `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None
        
        Set the viewer geom string of the element.


    - `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool
        
        Return true if the given element has a viewer collection string.


    - `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str
        
        Return the viewer collection string of the element.


    - `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None
        
        Set the visibility type string of the element.


    - `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool
        
        Return true if the given element has a visibility type string.


    - `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str
        
        Return the visibility type string of the element.


    - `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None
        
        Set the visible boolean of the element.


    - `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool
        
        Return the visible boolean of the element.


  - Attributes: CATEGORY = 'visibility'


### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

- `createNamePath`: createNamePath(arg0: collections.abc.Sequence[str]) -> str

Create a name path from a string vector.

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

Create a valid MaterialX name from the given string.

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

Given two geometry strings, each containing an array of geom names, return true if they have any geometries in common.

An empty geometry string matches no geometries, while the universal geometry string "/" matches all non-empty geometries.

If the contains argument is set to true, then we require that a geom path in the first string completely contains a geom path in the second string.

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

Return a vector of all outputs connected to the given node's inputs.

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

Return a vector of all MaterialAssign elements that bind this material node to the given geometry string.

Args:
    materialNode: Node to examine
    geom: The geometry for which material bindings should be returned. By default, this argument is the universal geometry string "/", and all material bindings are returned.

Returns:
    Vector of MaterialAssign elements

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

Return a vector of all shader nodes connected to the given material node's inputs, filtered by the given shader type and target.

Args:
    materialNode: The node to examine.
    nodeType: THe shader node type to return. Defaults to the surface shader type.
    target: An optional target name, which will be used to filter the returned nodes.

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

Return the major, minor, and build versions of the MaterialX library as an integer tuple.

- `getVersionString`: getVersionString() -> str

Return the version of the MaterialX library as a string.

- `incrementName`: incrementName(arg0: str) -> str

Increment the numeric suffix of a name.

- `isValidName`: isValidName(arg0: str) -> bool

Return true if the given string is a valid MaterialX name.

- `joinStrings`: joinStrings(arg0: collections.abc.Sequence[str], arg1: str) -> str

Join a vector of substrings into a single string, placing the given separator between each substring.

- `parentNamePath`: parentNamePath(arg0: str) -> str

Given a name path, return the parent name path.

- `prettyPrint`: prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str

Pretty print the given element tree, calling asString recursively on each element in depth-first order.

- `replaceSubstrings`: replaceSubstrings(arg0: str, arg1: collections.abc.Mapping[str, str]) -> str

Apply the given substring substitutions to the input string.

- `splitNamePath`: splitNamePath(arg0: str) -> list[str]

Split a name path into string vector.

- `splitString`: splitString(arg0: str, arg1: str) -> list[str]

Split a string into a vector of substrings using the given set of separator characters.

- `stringEndsWith`: stringEndsWith(arg0: str, arg1: str) -> bool

Return true if the given string ends with the given suffix.

- `stringStartsWith`: stringStartsWith(arg0: str, arg1: str) -> bool

Return true if the given string starts with the given prefix.

- `targetStringsMatch`: targetStringsMatch(arg0: str, arg1: str) -> bool

Given two target strings, each containing a string array of target names, return true if they have any targets in common.

An empty target string matches all targets.


### Globals

- ARRAY_PREFERRED_SEPARATOR = ', '
- ARRAY_VALID_SEPARATORS = ', '
- BSDF_TYPE_STRING = 'BSDF'
- DEFAULT_TYPE_STRING = 'color3'
- DISPLACEMENT_SHADER_TYPE_STRING = 'displacementshader'
- EDF_TYPE_STRING = 'EDF'
- FILENAME_TYPE_STRING = 'filename'
- GEOMNAME_TYPE_STRING = 'geomname'
- GEOM_PATH_SEPARATOR = '/'
- LIGHT_SHADER_TYPE_STRING = 'lightshader'
- MATERIAL_TYPE_STRING = 'material'
- MULTI_OUTPUT_TYPE_STRING = 'multioutput'
- NAME_PATH_SEPARATOR = '/'
- NAME_PREFIX_SEPARATOR = ':'
- NONE_TYPE_STRING = 'none'
- STRING_TYPE_STRING = 'string'
- SURFACE_MATERIAL_NODE_STRING = 'surfacematerial'
- SURFACE_SHADER_TYPE_STRING = 'surfaceshader'
- UDIM_SET_PROPERTY = 'udimset'
- UDIM_TOKEN = '(UDIM)'
- UNIVERSAL_GEOM_NAME = '/'
- UV_TILE_TOKEN = '(UVTILE)'
- VALUE_STRING_FALSE = 'false'
- VALUE_STRING_TRUE = 'true'
- VDF_TYPE_STRING = 'VDF'
- VOLUME_MATERIAL_NODE_STRING = 'volumematerial'
- VOLUME_SHADER_TYPE_STRING = 'volumeshader'

---

## Module: MaterialX.PyMaterialXFormat

### Classes

<a id='materialx-pymaterialxformat-exceptionfilemissing'></a>

- **ExceptionFileMissing**: 

  - Inherits from: [Exception](#materialx-pymaterialxformat-exception), [BaseException](#materialx-pymaterialxformat-baseexception)

<a id='materialx-pymaterialxformat-exceptionparseerror'></a>

- **ExceptionParseError**: 

  - Inherits from: [Exception](#materialx-pymaterialxformat-exception), [BaseException](#materialx-pymaterialxformat-baseexception)

<a id='materialx-pymaterialxformat-filepath'></a>

- **FilePath**: A generic file path, supporting both syntactic and file system operations.

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FilePath, format: MaterialX.PyMaterialXFormat.Format = <Format.FormatPosix: 1>) -> str
        
        Return this path as a standard string with the given format.


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FilePath) -> bool
        
        Return true if the given path is empty.


    - `isAbsolute`: isAbsolute(self: MaterialX.PyMaterialXFormat.FilePath) -> bool
        
        Return true if the given path is absolute.


    - `getBaseName`: getBaseName(self: MaterialX.PyMaterialXFormat.FilePath) -> str
        
        Return the base name of the given path, with leading directory information removed.


    - `getParentPath`: getParentPath(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Return the parent directory of the given path, if any.
        
        If no parent directory is present, then the empty path is returned.


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> str
        
        Return the file extension of the given path.


    - `addExtension`: addExtension(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None
        
        Add a file extension to the given path.


    - `removeExtension`: removeExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Remove the file extension, if any, from the given path.


    - `size`: size(self: MaterialX.PyMaterialXFormat.FilePath) -> int
        
        Return the number of strings in the path.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `exists`: exists(self: MaterialX.PyMaterialXFormat.FilePath) -> bool
        
        Return true if the given path exists on the file system.


    - `isDirectory`: isDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> bool
        
        Return true if the given path is a directory on the file system.


    - `getFilesInDirectory`: getFilesInDirectory(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> list[MaterialX.PyMaterialXFormat.FilePath]
        
        Return a vector of all files in the given directory with the given extension.
        
        If extension is empty all files are returned.


    - `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]
        
        Return a vector of all directories at or beneath the given path.


    - `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Create a directory on the file system at the given path.


    - `getCurrentPath`: getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath
        
        Return the current working directory of the file system.


    - `getModulePath`: getModulePath() -> MaterialX.PyMaterialXFormat.FilePath
        
        Return the directory containing the executable module.


<a id='materialx-pymaterialxformat-filesearchpath'></a>

- **FileSearchPath**: A sequence of file paths, which may be queried to find the first instance of a given filename on the file system.

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ':') -> str
        
        Convert this sequence to a string using the given separator.


    - `append`: append(*args, **kwargs)
        Overloaded function.
        
        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Prepend the given path to the sequence.


    - `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Clear all paths from the sequence.


    - `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int
        
        Return the number of paths in the sequence.


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool
        
        Return true if the search path is empty.


    - `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.
        
        On success, the combined path is returned; otherwise the original filename is returned unmodified.


<a id='materialx-pymaterialxformat-format'></a>

- **Format**: Members:

  FormatWindows

  FormatPosix

  FormatNative

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Attributes: name = (property), value = (property), FormatWindows = (property), FormatPosix = (property), FormatNative = (property)

<a id='materialx-pymaterialxformat-type'></a>

- **Type**: Members:

  TypeRelative

  TypeAbsolute

  TypeNetwork

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Attributes: name = (property), value = (property), TypeRelative = (property), TypeAbsolute = (property), TypeNetwork = (property)

<a id='materialx-pymaterialxformat-xmlreadoptions'></a>

- **XmlReadOptions**: A set of options for controlling the behavior of XML read functions.

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Attributes: readXIncludeFunction = (property), readComments = (property), readNewlines = (property), upgradeVersion = (property), parentXIncludes = (property)

<a id='materialx-pymaterialxformat-xmlwriteoptions'></a>

- **XmlWriteOptions**: A set of options for controlling the behavior of XML write functions.

  - Inherits from: [pybind11_object](#materialx-pymaterialxformat-pybind11_object)

  - Attributes: writeXIncludeEnable = (property), elementPredicate = (property)


### Functions

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x100a5ecf0>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

Flatten all filenames in the given document, applying string resolvers at the scope of each element and removing all fileprefix attributes.

Args:
    doc: The document to modify.
    searchPath: An optional search path for relative to absolute path conversion.
    customResolver: An optional custom resolver to apply.

- `getEnvironmentPath`: getEnvironmentPath(sep: str = ':') -> MaterialX.PyMaterialXFormat.FileSearchPath

Return a FileSearchPath object from search path environment variable.

- `getSourceSearchPath`: getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXFormat.FileSearchPath

Return a file search path containing the parent folder of each source URI in the given document.

- `getSubdirectories`: getSubdirectories(arg0: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath], arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath]) -> None

Get all subdirectories for a given set of directories and search paths.

- `loadDocuments`: loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: collections.abc.Set[str], includeFiles: collections.abc.Set[str], documents: collections.abc.Sequence[MaterialX.PyMaterialXCore.Document], documentsPaths: collections.abc.Sequence[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: collections.abc.Sequence[str] = None) -> None

Scans for all documents under a root path and returns documents which can be loaded.

- `loadLibraries`: loadLibraries(libraryFolders: collections.abc.Sequence[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: collections.abc.Set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

Load all MaterialX files within the given library folders into a document, using the given search path to locate the folders on the file system.

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x100a5eaf0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Load a given MaterialX library into a document.

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

Read the given file and return a string containing its contents; if the read is not successful, then the empty string is returned.

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x100a06430>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Read a Document as XML from the given filename.

Args:
    doc: The Document into which data is read.
    filename: The filename from which data is read. This argument can be supplied either as a FilePath or a standard string.
    searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
    readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x100a364f0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Read a Document as XML from the given string.

Args:
    doc: The Document into which data is read.
    str: The string from which data is read.
    searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
    readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.

- `writeToXmlFile`: writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> None

- `writeToXmlString`: writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> str


### Globals

- FormatNative = (Format.FormatPosix: 1)
- FormatPosix = (Format.FormatPosix: 1)
- FormatWindows = (Format.FormatWindows: 0)
- MATERIALX_SEARCH_PATH_ENV_VAR = 'MATERIALX_SEARCH_PATH'
- PATH_LIST_SEPARATOR = ':'
- TypeAbsolute = (Type.TypeAbsolute: 1)
- TypeNetwork = (Type.TypeNetwork: 2)
- TypeRelative = (Type.TypeRelative: 0)

---

## Module: MaterialX.PyMaterialXGenGlsl

### Classes

<a id='materialx-pymaterialxgenglsl-esslshadergenerator'></a>

- **EsslShaderGenerator**: An ESSL (OpenGL ES Shading Language) shader generator.

  - Inherits from: [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator), [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenglsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.


<a id='materialx-pymaterialxgenglsl-glslresourcebindingcontext'></a>

- **GlslResourceBindingContext**: Class representing a resource binding for Glsl shader resources.

  - Inherits from: [HwResourceBindingContext](#materialx-pymaterialxgenglsl-hwresourcebindingcontext), [GenUserData](#materialx-pymaterialxgenglsl-genuserdata), [pybind11_object](#materialx-pymaterialxgenglsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext


    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


<a id='materialx-pymaterialxgenglsl-glslshadergenerator'></a>

- **GlslShaderGenerator**: Base class for GLSL (OpenGL Shading Language) code generation.

A generator for a specific GLSL target should be derived from this class.

  - Inherits from: [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenglsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str
        
        Return the version string for the GLSL version this generator is for.


<a id='materialx-pymaterialxgenglsl-vkshadergenerator'></a>

- **VkShaderGenerator**: A Vulkan GLSL shader generator.

  - Inherits from: [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator), [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenglsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str
        
        Return the version string for the GLSL version this generator is for.


<a id='materialx-pymaterialxgenglsl-wgslshadergenerator'></a>

- **WgslShaderGenerator**: WGSL Flavor of Vulkan GLSL shader generator.

  - Inherits from: [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator), [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenglsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str



---

## Module: MaterialX.PyMaterialXGenMdl

### Classes

<a id='materialx-pymaterialxgenmdl-mdlshadergenerator'></a>

- **MdlShaderGenerator**: Shader generator for MDL (Material Definition Language).

  - Inherits from: [ShaderGenerator](#materialx-pymaterialxgenmdl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenmdl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMdl.MdlShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.



---

## Module: MaterialX.PyMaterialXGenMsl

### Classes

<a id='materialx-pymaterialxgenmsl-mslresourcebindingcontext'></a>

- **MslResourceBindingContext**: 

  - Inherits from: [HwResourceBindingContext](#materialx-pymaterialxgenmsl-hwresourcebindingcontext), [GenUserData](#materialx-pymaterialxgenmsl-genuserdata), [pybind11_object](#materialx-pymaterialxgenmsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> MaterialX.PyMaterialXGenMsl.MslResourceBindingContext


    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


<a id='materialx-pymaterialxgenmsl-mslshadergenerator'></a>

- **MslShaderGenerator**: 

  - Inherits from: [HwShaderGenerator](#materialx-pymaterialxgenmsl-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenmsl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenmsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str



---

## Module: MaterialX.PyMaterialXGenOsl

### Classes

<a id='materialx-pymaterialxgenosl-oslshadergenerator'></a>

- **OslShaderGenerator**: Base class for OSL (Open Shading Language) shader generators.

A generator for a specific OSL target should be derived from this class.

  - Inherits from: [ShaderGenerator](#materialx-pymaterialxgenosl-shadergenerator), [pybind11_object](#materialx-pymaterialxgenosl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `generate`: generate(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.



### Globals

- OSL_INPUTS = 'i'
- OSL_OUTPUTS = 'o'
- OSL_UNIFORMS = 'u'

---

## Module: MaterialX.PyMaterialXGenShader

### Classes

<a id='materialx-pymaterialxgenshader-applicationvariablehandler'></a>

- **ApplicationVariableHandler**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

<a id='materialx-pymaterialxgenshader-colormanagementsystem'></a>

- **ColorManagementSystem**: Abstract base class for color management systems.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> str
        
        Return the ColorManagementSystem name.


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Load a library of implementations from the provided document, replacing any previously loaded content.


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -> bool
        
        Returns whether this color management system supports a provided transform.


<a id='materialx-pymaterialxgenshader-colorspacetransform'></a>

- **ColorSpaceTransform**: Structure that represents color space transform information.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Attributes: sourceSpace = (property), targetSpace = (property), type = (property)

<a id='materialx-pymaterialxgenshader-defaultcolormanagementsystem'></a>

- **DefaultColorManagementSystem**: Class for a default color management system.

  - Inherits from: [ColorManagementSystem](#materialx-pymaterialxgenshader-colormanagementsystem), [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem
        
        Create a new DefaultColorManagementSystem.


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -> str
        
        Return the DefaultColorManagementSystem name.


<a id='materialx-pymaterialxgenshader-gencontext'></a>

- **GenContext**: A context class for shader generation.

Used for thread local storage of data needed during shader generation.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getShaderGenerator`: getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.ShaderGenerator
        
        Return shader generatior.


    - `getOptions`: getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX_v1_39_5::GenOptions


    - `getTypeDesc`: getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -> MaterialX_v1_39_5::TypeDesc
        
        Return a TypeDesc for the given type name.


    - `registerSourceCodeSearchPath`: registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.
        
        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `resolveSourceFile`: resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Resolve a source code filename, first checking the given local path then checking any file paths registered by the user.


    - `pushUserData`: pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -> None
        
        Add user data to the context to make it available during shader generator.


    - `setApplicationVariableHandler`: setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -> None
        
        Set handler for application variables.


    - `getApplicationVariableHandler`: getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -> collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]
        
        Get handler for application variables.


<a id='materialx-pymaterialxgenshader-genoptions'></a>

- **GenOptions**: Class holding options to configure shader generation.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Attributes: shaderInterfaceType = (property), fileTextureVerticalFlip = (property), targetColorSpaceOverride = (property), targetDistanceUnit = (property), addUpstreamDependencies = (property), libraryPrefix = (property), emitColorTransforms = (property), hwTransparency = (property), hwSpecularEnvironmentMethod = (property), hwSrgbEncodeOutput = (property), hwWriteDepthMoments = (property), hwShadowMap = (property), hwMaxActiveLightSources = (property), hwNormalizeUdimTexCoords = (property), hwAmbientOcclusion = (property), hwWriteAlbedoTable = (property), hwWriteEnvPrefilter = (property), hwImplicitBitangents = (property)

<a id='materialx-pymaterialxgenshader-genuserdata'></a>

- **GenUserData**: Base class for custom user data needed during shader generation.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getSelf`: getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -> MaterialX.PyMaterialXGenShader.GenUserData


<a id='materialx-pymaterialxgenshader-hwresourcebindingcontext'></a>

- **HwResourceBindingContext**: 

  - Inherits from: [GenUserData](#materialx-pymaterialxgenshader-genuserdata), [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


<a id='materialx-pymaterialxgenshader-hwshadergenerator'></a>

- **HwShaderGenerator**: 

  - Inherits from: [ShaderGenerator](#materialx-pymaterialxgenshader-shadergenerator), [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `bindLightShader`: bindLightShader(self: MaterialX.PyMaterialXCore.NodeDef, arg0: typing.SupportsInt, arg1: MaterialX.PyMaterialXGenShader.GenContext) -> None


    - `unbindLightShader`: unbindLightShader(self: typing.SupportsInt, arg0: MaterialX.PyMaterialXGenShader.GenContext) -> None


    - `unbindLightShaders`: unbindLightShaders(self: MaterialX.PyMaterialXGenShader.GenContext) -> None


<a id='materialx-pymaterialxgenshader-hwspecularenvironmentmethod'></a>

- **HwSpecularEnvironmentMethod**: Members:

  SPECULAR_ENVIRONMENT_PREFILTER

  SPECULAR_ENVIRONMENT_FIS

  SPECULAR_ENVIRONMENT_NONE

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Attributes: name = (property), value = (property), SPECULAR_ENVIRONMENT_PREFILTER = (property), SPECULAR_ENVIRONMENT_FIS = (property), SPECULAR_ENVIRONMENT_NONE = (property)

<a id='materialx-pymaterialxgenshader-shader'></a>

- **Shader**: Class containing all data needed during shader generation.

After generation is completed it will contain the resulting source code emitted by shader generators.

The class contains a default implementation using a single shader stage. Derived shaders can override this, as well as overriding all methods that add code to the shader.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.Shader) -> str
        
        Return the shader name.


    - `hasStage`: hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool
        
        Return if stage exists.


    - `numStages`: numStages(self: MaterialX.PyMaterialXGenShader.Shader) -> int
        
        Return the number of shader stages for this shader.


    - `getStage`: getStage(*args, **kwargs)
        Overloaded function.
        
        1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: typing.SupportsInt) -> MaterialX_v1_39_5::ShaderStage
        
        2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX_v1_39_5::ShaderStage


    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> str
        
        Return the shader source code for a given shader stage.


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool
        
        Return true if the shader has a given named attribute.


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX.PyMaterialXCore.Value
        
        Return the value for a named attribute, or nullptr if no such attribute is found.


    - `setAttribute`: setAttribute(*args, **kwargs)
        Overloaded function.
        
        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None
        
        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None


<a id='materialx-pymaterialxgenshader-shadergenerator'></a>

- **ShaderGenerator**: Base class for shader generators All third-party shader generators should derive from this class.

Derived classes should use DECLARE_SHADER_GENERATOR / DEFINE_SHADER_GENERATOR in their declaration / definition, and register with the Registry class.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> str
        
        Return the name of the target this generator is for.


    - `generate`: generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None
        
        Sets the color management system.


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX.PyMaterialXGenShader.ColorManagementSystem
        
        Returns the color management system.


    - `setUnitSystem`: setUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX_v1_39_5::UnitSystem) -> None
        
        Sets the unit system.


    - `getUnitSystem`: getUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX_v1_39_5::UnitSystem
        
        Returns the unit system.


    - `getTokenSubstitutions`: getTokenSubstitutions(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> dict[str, str]
        
        Return the map of token substitutions used by the generator.


    - `registerTypeDefs`: registerTypeDefs(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Register type definitions from the document.


    - `registerShaderMetadata`: registerShaderMetadata(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX_v1_39_5::GenContext) -> None
        
        Register metadata that should be exported to the generated shaders.
        
        Supported metadata includes standard UI attributes like "uiname", "uifolder", "uimin", "uimax", etc. But it is also extendable by defining custom attributes using AttributeDefs. Any AttributeDef in the given document with exportable="true" will be exported as shader metadata when found on nodes during shader generation. Derived shader generators may override this method to change the registration. Applications must explicitly call this method before shader generation to enable export of metadata.


<a id='materialx-pymaterialxgenshader-shaderinterfacetype'></a>

- **ShaderInterfaceType**: Members:

  SHADER_INTERFACE_COMPLETE

  SHADER_INTERFACE_REDUCED

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Attributes: name = (property), value = (property), SHADER_INTERFACE_COMPLETE = (property), SHADER_INTERFACE_REDUCED = (property)

<a id='materialx-pymaterialxgenshader-shaderport'></a>

- **ShaderPort**: An input or output port on a ShaderNode.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -> None
        
        Set the data type for this port.


    - `getType`: getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX_v1_39_5::TypeDesc
        
        Return the data type for this port.


    - `setName`: setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the name of this port.


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the name of this port.


    - `getFullName`: getFullName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the name of this port.


    - `setVariable`: setVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the variable name of this port.


    - `getVariable`: getVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the variable name of this port.


    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the variable semantic of this port.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the variable semantic of this port.


    - `setValue`: setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -> None
        
        Set a value on this port.


    - `getValue`: getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX.PyMaterialXCore.Value
        
        Return the value set on this port.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the value set on this port as a string, or an empty string if there is no value.


    - `setGeomProp`: setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set geomprop name if the input has a default geomprop to be assigned when it is unconnected.


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Get geomprop name.


    - `setPath`: setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the path to this port.


    - `getPath`: getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the path to this port.


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set a unit type for the value on this port.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the unit type for the value on this port.


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set a source color space for the value on this port.


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the source color space for the value on this port.


    - `isUniform`: isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool
        
        Return the uniform flag on this port.


    - `isEmitted`: isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool
        
        Return the emitted state of this port.


<a id='materialx-pymaterialxgenshader-shaderportpredicate'></a>

- **ShaderPortPredicate**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

<a id='materialx-pymaterialxgenshader-shaderstage'></a>

- **ShaderStage**: A shader stage, containing the state and resulting source code for the stage.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the stage name.


    - `getFunctionName`: getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the stage function name.


    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the stage source code.


    - `getUniformBlock`: getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getInputBlock`: getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getOutputBlock`: getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getConstantBlock`: getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getUniformBlocks`: getUniformBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]
        
        Return a map of all uniform blocks.


    - `getInputBlocks`: getInputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]
        
        Return a map of all input blocks.


    - `getIncludes`: getIncludes(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]
        
        Return a set of all include files.


    - `getSourceDependencies`: getSourceDependencies(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]
        
        Return a set of all source dependencies.


    - `getOutputBlocks`: getOutputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]
        
        Return a map of all output blocks.


<a id='materialx-pymaterialxgenshader-shadertranslator'></a>

- **ShaderTranslator**: A helper class for translating content between shading models.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderTranslator


    - `translateShader`: translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None
        
        Translate a shader node to the destination shading model.


    - `translateAllMaterials`: translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None
        
        Translate each material in the input document to the destination shading model.


<a id='materialx-pymaterialxgenshader-typedesc'></a>

- **TypeDesc**: A type descriptor for MaterialX data types.

All types need to have a type descriptor registered in order for shader generators to know about the type. It can be used for type comparisons as well as getting more information about the type. Type descriptors for all standard library data types are defined by default and can be accessed from the Type namespace, e.g. Type::FLOAT. Custom struct types defined through typedef elements in a data library are loaded in and registered by calling the ShaderGenerator::registerTypeDefs method. The TypeSystem class, see below, is used to manage all type descriptions. It can be used to query the registered types.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> str
        
        Return the name of the type.


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Return the basetype for the type.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Return the semantic for the type.


    - `getSize`: getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Return the number of elements the type is composed of.
        
        Will return 1 for scalar types and a size greater than 1 for aggregate type. For array types 0 is returned since the number of elements is undefined until an array is instantiated.


    - `isScalar`: isScalar(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is a scalar type.


    - `isAggregate`: isAggregate(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is an aggregate type.


    - `isArray`: isArray(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is an array type.


    - `isFloat2`: isFloat2(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is an aggregate of 2 floats.


    - `isFloat3`: isFloat3(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is an aggregate of 3 floats.


    - `isFloat4`: isFloat4(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type is an aggregate of 4 floats.


    - `isClosure`: isClosure(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool
        
        Return true if the type represents a closure.


<a id='materialx-pymaterialxgenshader-unitsystem'></a>

- **UnitSystem**: Base unit system support.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.UnitSystem
        
        Create a new UnitSystem.


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> str
        
        Return the UnitSystem name.


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        assign document with unit implementations replacing any previously loaded content.


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -> bool
        
        Returns whether this unit system supports a provided transform.


    - `setUnitConverterRegistry`: setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None
        
        Assign unit converter registry replacing any previous assignment.


    - `getUnitConverterRegistry`: getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> MaterialX.PyMaterialXCore.UnitConverterRegistry
        
        Returns the currently assigned unit converter registry.


<a id='materialx-pymaterialxgenshader-unittransform'></a>

- **UnitTransform**: Structure that represents unit transform information.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Attributes: sourceUnit = (property), targetUnit = (property), type = (property), unitType = (property)

<a id='materialx-pymaterialxgenshader-variableblock'></a>

- **VariableBlock**: A block of variables in a shader stage.

  - Inherits from: [pybind11_object](#materialx-pymaterialxgenshader-pybind11_object)

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str
        
        Get the name of this block.


    - `getInstance`: getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str
        
        Get the instance name of this block.


    - `empty`: empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> bool
        
        Return true if the block has no variables.


    - `size`: size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int
        
        Return the number of variables in this block.


    - `find`: find(*args, **kwargs)
        Overloaded function.
        
        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort
        
        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: collections.abc.Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort



### Functions

- `connectsToWorldSpaceNode`: connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node

Determine whether the given output is directly connected to a node that generates world-space coordinates (e.g.

Args:
    output: Output to check

Returns:
    Return the node if found.

- `elementRequiresShading`: elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool

Determine if a given element requires shading / lighting for rendering.

- `findRenderableElements`: findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = False) -> list[MaterialX.PyMaterialXCore.TypedElement]

- `findRenderableMaterialNodes`: findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]

- `getNodeDefInput`: getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input

Given a node input, return the corresponding input within its matching nodedef.

The optional target string can be used to guide the selection of nodedef declarations.

- `getUdimCoordinates`: getUdimCoordinates(arg0: collections.abc.Sequence[str]) -> list[MaterialX.PyMaterialXCore.Vector2]

Compute the UDIM coordinates for a set of UDIM identifiers.

Returns:
    List of UDIM coordinates

- `getUdimScaleAndOffset`: getUdimScaleAndOffset(arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None

Get the UV scale and offset to transform uv coordinates from UDIM uv space to 0..1 space.

- `hasElementAttributes`: hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: collections.abc.Sequence[str]) -> bool

Returns true if there is are any value elements with a given set of attributes either on the starting node or any graph upsstream of that node.

Args:
    output: Starting node
    attributes: Attributes to test for

- `isTransparentSurface`: isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool

Returns true if the given element is a surface shader with the potential of being transparent.

This can be used by HW shader generators to determine if a shader will require transparency handling.

Note: This function will check some common cases for how a surface shader can be transparent. It is not covering all possible cases for how transparency can be done and target applications might need to do additional checks to track transparency correctly. For example, custom surface shader nodes implemented in source code will not be tracked by this function and transparency for such nodes must be tracked separately by the target application.

- `mapValueToColor`: mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None

Maps a value to a four channel color if it is of the appropriate type.

Supported types include float, Vector2, Vector3, Vector4, and Color4. If not mapping is possible the color value is set to opaque black.

- `requiresImplementation`: requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool

Return whether a nodedef requires an implementation.

- `tokenSubstitution`: tokenSubstitution(arg0: collections.abc.Mapping[str, str], arg1: str) -> None

Perform token substitutions on the given source string, using the given substitution map.

Tokens are required to start with '$' and can only consist of alphanumeric characters. The full token name, including '$' and all following alphanumeric character, will be replaced by the corresponding string in the substitution map, if the token exists in the map.


### Globals

- HW_ATTR_TRANSPARENT = 'transparent'
- HW_LIGHT_DATA = 'LightData'
- HW_PIXEL_OUTPUTS = 'PixelOutputs'
- HW_PRIVATE_UNIFORMS = 'PrivateUniforms'
- HW_PUBLIC_UNIFORMS = 'PublicUniforms'
- HW_VERTEX_DATA = 'VertexData'
- HW_VERTEX_INPUTS = 'VertexInputs'
- PIXEL_STAGE = 'pixel'
- SHADER_INTERFACE_COMPLETE = (ShaderInterfaceType.SHADER_INTERFACE_COMPLETE: 0)
- SHADER_INTERFACE_REDUCED = (ShaderInterfaceType.SHADER_INTERFACE_REDUCED: 1)
- SPECULAR_ENVIRONMENT_FIS = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_FIS: 1)
- SPECULAR_ENVIRONMENT_NONE = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_NONE: 0)
- SPECULAR_ENVIRONMENT_PREFILTER = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_PREFILTER: 2)
- VERTEX_STAGE = 'vertex'

---

## Module: MaterialX.PyMaterialXGenSlang

### Classes

<a id='materialx-pymaterialxgenslang-slangshadergenerator'></a>

- **SlangShaderGenerator**: Base class for Slang code generation.

A generator for a specific Slang target should be derived from this class.

  - Inherits from: [HwShaderGenerator](#materialx-pymaterialxgenslang-hwshadergenerator), [ShaderGenerator](#materialx-pymaterialxgenslang-shadergenerator), [pybind11_object](#materialx-pymaterialxgenslang-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -> str
        
        Return the version string for the Slang version this generator is for.



---

## Module: MaterialX.PyMaterialXRender

### Classes

<a id='materialx-pymaterialxrender-basetype'></a>

- **BaseType**: Members:

  UINT8

  INT8

  UINT16

  INT16

  HALF

  FLOAT

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Attributes: name = (property), value = (property), UINT8 = (property), INT8 = (property), UINT16 = (property), INT16 = (property), HALF = (property), FLOAT = (property)

<a id='materialx-pymaterialxrender-camera'></a>

- **Camera**: A simple camera class, supporting transform matrices and arcball functionality for object-viewing applications.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.Camera
        
        Create a new camera.


    - `setWorldMatrix`: setWorldMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Set the world matrix.


    - `getWorldMatrix`: getWorldMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the world matrix.


    - `setViewMatrix`: setViewMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Set the view matrix.


    - `getViewMatrix`: getViewMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the view matrix.


    - `setProjectionMatrix`: setProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Set the projection matrix.


    - `getProjectionMatrix`: getProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the projection matrix.


    - `getWorldViewProjMatrix`: getWorldViewProjMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44
        
        Compute our full model-view-projection matrix.


    - `getViewPosition`: getViewPosition(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3
        
        Derive viewer position from the view matrix.


    - `getViewDirection`: getViewDirection(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3
        
        Derive viewer direction from the view matrix.


    - `setViewportSize`: setViewportSize(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector2) -> None
        
        Set the size of the viewport window.


    - `getViewportSize`: getViewportSize(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector2
        
        Return the size of the viewport window.


    - `projectToViewport`: projectToViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Project a position from object to viewport space.


    - `unprojectFromViewport`: unprojectFromViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Unproject a position from viewport to object space.


    - `createViewMatrix`: createViewMatrix(arg0: MaterialX.PyMaterialXCore.Vector3, arg1: MaterialX.PyMaterialXCore.Vector3, arg2: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a view matrix given an eye position, a target position and an up vector.


    - `createPerspectiveMatrix`: createPerspectiveMatrix(arg0: typing.SupportsFloat, arg1: typing.SupportsFloat, arg2: typing.SupportsFloat, arg3: typing.SupportsFloat, arg4: typing.SupportsFloat, arg5: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a perspective projection matrix given a set of clip planes with [-1,1] projected Z.


    - `createOrthographicMatrix`: createOrthographicMatrix(arg0: typing.SupportsFloat, arg1: typing.SupportsFloat, arg2: typing.SupportsFloat, arg3: typing.SupportsFloat, arg4: typing.SupportsFloat, arg5: typing.SupportsFloat) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create an orthographic projection matrix given a set of clip planes with [-1,1] projected Z.


    - `transformPointPerspective`: transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Apply a perspective transform to the given 3D point, performing a homogeneous divide on the transformed result.


<a id='materialx-pymaterialxrender-cgltfloader'></a>

- **CgltfLoader**: Wrapper for loader to read in GLTF files using the Cgltf library.

  - Inherits from: [GeometryLoader](#materialx-pymaterialxrender-geometryloader), [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.CgltfLoader
        
        Create a new loader.


    - `load`: load(self: MaterialX.PyMaterialXRender.CgltfLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from file path.


<a id='materialx-pymaterialxrender-exceptionrendererror'></a>

- **ExceptionRenderError**: 

  - Inherits from: [Exception](#materialx-pymaterialxrender-exception), [BaseException](#materialx-pymaterialxrender-baseexception)

<a id='materialx-pymaterialxrender-geometryhandler'></a>

- **GeometryHandler**: Class which holds a set of geometry loaders.

Each loader is associated with a given set of file extensions.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.GeometryHandler
        
        Create a new geometry handler.


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.GeometryLoader) -> None
        
        Add a geometry loader.
        
        Args:
            loader: Loader to add to list of available loaders.


    - `clearGeometry`: clearGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler) -> None
        
        Clear all loaded geometry.


    - `hasGeometry`: hasGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: str) -> bool


    - `getGeometry`: getGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg1: str) -> None


    - `loadGeometry`: loadGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: bool) -> bool
        
        Load geometry from a given location.
        
        Args:
            filePath: Path to geometry
            texcoordVerticalFlip: Flip texture coordinates in V. Default is to not flip.


    - `getMeshes`: getMeshes(self: MaterialX.PyMaterialXRender.GeometryHandler) -> list[MaterialX.PyMaterialXRender.Mesh]
        
        Get list of meshes.


    - `findParentMesh`: findParentMesh(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> MaterialX.PyMaterialXRender.Mesh
        
        Return the first mesh in our list containing the given partition.
        
        If no matching mesh is found, then nullptr is returned.


    - `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for all meshes.


    - `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for all meshes.


<a id='materialx-pymaterialxrender-geometryloader'></a>

- **GeometryLoader**: Base class representing a geometry loader.

A loader can be associated with one or more file extensions.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.GeometryLoader) -> set[str]
        
        Returns a list of supported extensions.
        
        Returns:
            List of support extensions


    - `load`: load(self: MaterialX.PyMaterialXRender.GeometryLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from disk.
        
        Args:
            filePath: Path to file to load
            meshList: List of meshes to update
            texcoordVerticalFlip: Flip texture coordinates in V when loading
        
        Returns:
            True if load was successful


<a id='materialx-pymaterialxrender-image'></a>

- **Image**: Class representing an image in system memory.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt, arg3: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image
        
        Create an empty image with the given properties.


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the width of the image.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the height of the image.


    - `getChannelCount`: getChannelCount(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the channel count of the image.


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.BaseType
        
        Return the base type of the image.


    - `getBaseStride`: getBaseStride(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the stride of our base type in bytes.


    - `getMaxMipCount`: getMaxMipCount(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the maximum number of mipmaps for this image.


    - `setTexelColor`: setTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXCore.Color4) -> None
        
        Set the texel color at the given coordinates.
        
        If the coordinates or image resource buffer are invalid, then an exception is thrown.


    - `getTexelColor`: getTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> MaterialX.PyMaterialXCore.Color4
        
        Return the texel color at the given coordinates.
        
        If the coordinates or image resource buffer are invalid, then an exception is thrown.


    - `isUniformColor`: isUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> bool
        
        Return true if all texels of this image are identical in color.
        
        Args:
            uniformColor: Return the uniform color of the image, if any.


    - `setUniformColor`: setUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> None
        
        Set all texels of this image to a uniform color.


    - `applyMatrixTransform`: applyMatrixTransform(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Matrix33) -> None
        
        Apply the given matrix transform to all texels of this image.


    - `applyGammaTransform`: applyGammaTransform(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsFloat) -> None
        
        Apply the given gamma transform to all texels of this image.


    - `copy`: copy(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image
        
        Create a copy of this image with the given channel count and base type.


    - `applyBoxBlur`: applyBoxBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Apply a 3x3 box blur to this image, returning a new blurred image.


    - `applyGaussianBlur`: applyGaussianBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Apply a 7x7 Gaussian blur to this image, returning a new blurred image.


    - `applyBoxDownsample`: applyBoxDownsample(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt) -> MaterialX.PyMaterialXRender.Image
        
        Downsample this image by an integer factor using a box filter, returning the new reduced image.


    - `splitByLuminance`: splitByLuminance(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsFloat) -> tuple[MaterialX.PyMaterialXRender.Image, MaterialX.PyMaterialXRender.Image]
        
        Split this image by the given luminance threshold, returning the resulting underflow and overflow images.


    - `setResourceBuffer`: setResourceBuffer(self: MaterialX.PyMaterialXRender.Image, arg0: typing_extensions.CapsuleType) -> None
        
        Set the resource buffer for this image.


    - `getResourceBuffer`: getResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the resource buffer for this image.


    - `createResourceBuffer`: createResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None
        
        Allocate a resource buffer for this image that matches its properties.


    - `releaseResourceBuffer`: releaseResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None
        
        Release the resource buffer for this image.


    - `setResourceBufferDeallocator`: setResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image, arg0: collections.abc.Callable[[typing_extensions.CapsuleType], None]) -> None
        
        Set the resource buffer deallocator for this image.


    - `getResourceBufferDeallocator`: getResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image) -> collections.abc.Callable[[typing_extensions.CapsuleType], None]
        
        Return the resource buffer deallocator for this image.


<a id='materialx-pymaterialxrender-imagebufferdeallocator'></a>

- **ImageBufferDeallocator**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

<a id='materialx-pymaterialxrender-imagehandler'></a>

- **ImageHandler**: Base image handler class.

Keeps track of images which are loaded from disk via supplied ImageLoader. Derived classes are responsible for determining how to perform the logic for "binding" of these resources for a given target (such as a given shading language).

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.ImageLoader) -> None
        
        Add another image loader to the handler, which will be invoked if existing loaders cannot load a given image.


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, image: MaterialX.PyMaterialXRender.Image, verticalFlip: bool = False) -> bool
        
        Save image to disk.
        
        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save
        
        Returns:
            if save succeeded


    - `acquireImage`: acquireImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = <MaterialX.PyMaterialXCore.Color4 object at 0x10106c3b0>) -> MaterialX.PyMaterialXRender.Image
        
        Acquire an image from the cache or file system.
        
        Args:
            filePath: File path of the image.
            defaultColor: Default color to use as a fallback for missing images.
        
        Returns:
            On success, a shared pointer to the acquired image.


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool
        
        Bind an image for rendering.
        
        Args:
            image: The image to bind.
            samplingProperties: Sampling properties for the image.


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool
        
        Unbind an image, making it no longer active for rendering.
        
        Args:
            image: The image to unbind.


    - `unbindImages`: unbindImages(self: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Unbind all images that are currently stored in the cache.


    - `setSearchPath`: setSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Set the search path to be used for finding images on the file system.


    - `getSearchPath`: getSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXFormat.FileSearchPath
        
        Return the image search path.


    - `setFilenameResolver`: setFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.StringResolver) -> None
        
        Set the filename resolver for images.


    - `getFilenameResolver`: getFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXCore.StringResolver
        
        Return the filename resolver for images.


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool
        
        Create rendering resources for the given image.


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None
        
        Release rendering resources for the given image, or for all cached images if no image pointer is specified.


    - `clearImageCache`: clearImageCache(self: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Clear the contents of the image cache, first releasing any render resources associated with cached images.


    - `getZeroImage`: getZeroImage(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXRender.Image
        
        Return a fallback image with zeroes in all channels.


    - `getReferencedImages`: getReferencedImages(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXRender.Image]
        
        Acquire all images referenced by the given document, and return the images in a vector.


<a id='materialx-pymaterialxrender-imageloader'></a>

- **ImageLoader**: Abstract base class for file-system image loaders.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.ImageLoader) -> set[str]
        
        Returns a list of supported extensions.
        
        Returns:
            List of support extensions


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool
        
        Save an image to the file system.
        
        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save
        
        Returns:
            if save succeeded


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image
        
        Load an image from the file system.
        
        Args:
            filePath: The requested image file path.
        
        Returns:
            On success, a shared pointer to the loaded image; otherwise an empty shared pointer.


  - Attributes: BMP_EXTENSION = 'bmp', EXR_EXTENSION = 'exr', GIF_EXTENSION = 'gif', HDR_EXTENSION = 'hdr', JPG_EXTENSION = 'jpg', JPEG_EXTENSION = 'jpeg', PIC_EXTENSION = 'pic', PNG_EXTENSION = 'png', PSD_EXTENSION = 'psd', TGA_EXTENSION = 'tga', TIF_EXTENSION = 'tif', TIFF_EXTENSION = 'tiff', TXT_EXTENSION = 'txt'

<a id='materialx-pymaterialxrender-imagesamplingproperties'></a>

- **ImageSamplingProperties**: Interface to describe sampling properties for images.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Attributes: uaddressMode = (property), vaddressMode = (property), filterType = (property), defaultColor = (property)

<a id='materialx-pymaterialxrender-lighthandler'></a>

- **LightHandler**: Utility light handler for creating and providing light data for shader binding.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.LightHandler
        
        Create a new light handler.


    - `setLightTransform`: setLightTransform(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Set the light transform.


    - `getLightTransform`: getLightTransform(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the light transform.


    - `setDirectLighting`: setDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None
        
        Set whether direct lighting is enabled.


    - `getDirectLighting`: getDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool
        
        Return whether direct lighting is enabled.


    - `setIndirectLighting`: setIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None
        
        Set whether indirect lighting is enabled.


    - `getIndirectLighting`: getIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool
        
        Return whether indirect lighting is enabled.


    - `setEnvRadianceMap`: setEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None
        
        Set the environment radiance map.


    - `getEnvRadianceMap`: getEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image
        
        Return the environment radiance map.


    - `setEnvIrradianceMap`: setEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None
        
        Set the environment irradiance map.


    - `getEnvIrradianceMap`: getEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image
        
        Return the environment irradiance map.


    - `setAlbedoTable`: setAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None
        
        Set the directional albedo table.


    - `getAlbedoTable`: getAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image
        
        Return the directional albedo table.


    - `setEnvSampleCount`: setEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler, arg0: typing.SupportsInt) -> None
        
        Set the environment lighting sample count.


    - `getEnvSampleCount`: getEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler) -> int
        
        Return the environment lighting sample count.


    - `setRefractionTwoSided`: setRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None
        
        Set the two-sided refraction property.


    - `getRefractionTwoSided`: getRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler) -> int
        
        Return the two-sided refraction property.


    - `addLightSource`: addLightSource(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Node) -> None
        
        Add a light source.


    - `setLightSources`: setLightSources(self: MaterialX.PyMaterialXRender.LightHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -> None
        
        Set the vector of light sources.


    - `getLightSources`: getLightSources(self: MaterialX.PyMaterialXRender.LightHandler) -> list[MaterialX.PyMaterialXCore.Node]
        
        Return the vector of light sources.


    - `getFirstLightOfCategory`: getFirstLightOfCategory(self: MaterialX.PyMaterialXRender.LightHandler, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the first light source, if any, of the given category.


    - `getLightIdMap`: getLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler) -> dict[str, int]
        
        Get a list of identifiers associated with a given light nodedef.


    - `computeLightIdMap`: computeLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -> dict[str, int]
        
        From a set of nodes, create a mapping of corresponding nodedef identifiers to numbers.


    - `findLights`: findLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -> None
        
        Find lights to use based on an input document.
        
        Args:
            doc: Document to scan for lights
            lights: List of lights found in document


    - `registerLights`: registerLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -> None
        
        Register light node definitions and light count with a given generation context.
        
        Args:
            doc: Document containing light nodes and definitions
            lights: Lights to register
            context: Context to update


<a id='materialx-pymaterialxrender-mesh'></a>

- **Mesh**: Container for mesh data.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXRender.Mesh
        
        Create a new mesh.


    - `getName`: getName(self: MaterialX.PyMaterialXRender.Mesh) -> str
        
        Return the name of this mesh.


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> None
        
        Set the mesh's source URI.


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> bool
        
        Return true if this mesh has a source URI.


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> str
        
        Return the mesh's source URI.


    - `getStream`: getStream(*args, **kwargs)
        Overloaded function.
        
        1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> MaterialX.PyMaterialXRender.MeshStream
        
        2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: typing.SupportsInt) -> MaterialX.PyMaterialXRender.MeshStream


    - `addStream`: addStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> None
        
        Add a mesh stream.


    - `setVertexCount`: setVertexCount(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsInt) -> None
        
        Set vertex count.


    - `getVertexCount`: getVertexCount(self: MaterialX.PyMaterialXRender.Mesh) -> int
        
        Get vertex count.


    - `setMinimumBounds`: setMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set the minimum bounds for the geometry.


    - `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for the geometry.


    - `setMaximumBounds`: setMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set the minimum bounds for the geometry.


    - `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for the geometry.


    - `setSphereCenter`: setSphereCenter(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set center of the bounding sphere.


    - `getSphereCenter`: getSphereCenter(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return center of the bounding sphere.


    - `setSphereRadius`: setSphereRadius(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsFloat) -> None
        
        Set radius of the bounding sphere.


    - `getSphereRadius`: getSphereRadius(self: MaterialX.PyMaterialXRender.Mesh) -> float
        
        Return radius of the bounding sphere.


    - `getPartitionCount`: getPartitionCount(self: MaterialX.PyMaterialXRender.Mesh) -> int
        
        Return the number of mesh partitions.


    - `addPartition`: addPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None
        
        Add a partition.


    - `getPartition`: getPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsInt) -> MaterialX.PyMaterialXRender.MeshPartition
        
        Return a reference to a mesh partition.


    - `generateTextureCoordinates`: generateTextureCoordinates(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream
        
        Create texture coordinates from the given positions.
        
        Args:
            positionStream: Input position stream
        
        Returns:
            The generated texture coordinate stream


    - `generateNormals`: generateNormals(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream
        
        Generate face normals from the given positions.
        
        Args:
            positionStream: Input position stream
        
        Returns:
            The generated normal stream


    - `generateTangents`: generateTangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream, arg2: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream
        
        Generate tangents from the given positions, normals, and texture coordinates.
        
        Args:
            positionStream: Input position stream
            normalStream: Input normal stream
            texcoordStream: Input texcoord stream
        
        Returns:
            The generated tangent stream, on success; otherwise, a null pointer.


    - `generateBitangents`: generateBitangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream
        
        Generate bitangents from the given normals and tangents.
        
        Args:
            normalStream: Input normal stream
            tangentStream: Input tangent stream
        
        Returns:
            The generated bitangent stream, on success; otherwise, a null pointer.


    - `mergePartitions`: mergePartitions(self: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Merge all mesh partitions into one.


    - `splitByUdims`: splitByUdims(self: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Split the mesh into a single partition per UDIM.


<a id='materialx-pymaterialxrender-meshpartition'></a>

- **MeshPartition**: Class that describes a sub-region of a mesh using vertex indexing.

Note that a face is considered to be a triangle.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.MeshPartition
        
        Create a new mesh partition.


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: typing.SupportsInt) -> None
        
        Resize data to the given number of indices.


    - `setName`: setName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None
        
        Set the name of this partition.


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshPartition) -> str
        
        Return the name of this partition.


    - `addSourceName`: addSourceName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None
        
        Add a source name, representing a partition that was processed to generate this one.


    - `getSourceNames`: getSourceNames(self: MaterialX.PyMaterialXRender.MeshPartition) -> set[str]
        
        Return the vector of source names, representing all partitions that were processed to generate this one.


    - `getIndices`: getIndices(self: MaterialX.PyMaterialXRender.MeshPartition) -> list[int]


    - `getFaceCount`: getFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition) -> int
        
        Return number of faces.


    - `setFaceCount`: setFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: typing.SupportsInt) -> None
        
        Set face count.


<a id='materialx-pymaterialxrender-meshstream'></a>

- **MeshStream**: Class to represent a mesh data stream.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create(arg0: str, arg1: str, arg2: typing.SupportsInt) -> MaterialX.PyMaterialXRender.MeshStream
        
        Create a new mesh stream.


    - `reserve`: reserve(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -> None
        
        Reserve memory for a given number of elements.


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -> None
        
        Resize data to an given number of elements.


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshStream) -> str
        
        Get stream name.


    - `getType`: getType(self: MaterialX.PyMaterialXRender.MeshStream) -> str
        
        Get stream attribute name.


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Get stream index.


    - `getData`: getData(self: MaterialX.PyMaterialXRender.MeshStream) -> list[float]


    - `getStride`: getStride(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Get stride between elements.


    - `setStride`: setStride(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -> None
        
        Set stride between elements.


    - `getSize`: getSize(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Get the number of elements.


    - `transform`: transform(self: MaterialX.PyMaterialXRender.MeshStream, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Transform elements by a matrix.


  - Attributes: POSITION_ATTRIBUTE = 'position', NORMAL_ATTRIBUTE = 'normal', TEXCOORD_ATTRIBUTE = 'texcoord', TANGENT_ATTRIBUTE = 'tangent', BITANGENT_ATTRIBUTE = 'bitangent', COLOR_ATTRIBUTE = 'color', GEOMETRY_PROPERTY_ATTRIBUTE = 'geomprop'

<a id='materialx-pymaterialxrender-shaderrenderer'></a>

- **ShaderRenderer**: Base class for renderers that generate shader code to produce images.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXRender.ShaderRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -> None
        
        Initialize the renderer.


    - `setCamera`: setCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.Camera) -> None
        
        Set the camera.


    - `getCamera`: getCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.Camera
        
        Return the camera.


    - `setImageHandler`: setImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Set the image handler used by this renderer for image I/O.


    - `getImageHandler`: getImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.ImageHandler
        
        Return the image handler.


    - `setLightHandler`: setLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.LightHandler) -> None
        
        Set the light handler used by this renderer for light bindings.


    - `getLightHandler`: getLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.LightHandler
        
        Return the light handler.


    - `setGeometryHandler`: setGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.GeometryHandler) -> None
        
        Set the geometry handler.


    - `getGeometryHandler`: getGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.GeometryHandler
        
        Return the geometry handler.


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: collections.abc.Mapping[str, str]) -> None


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None
        
        Validate inputs for the program.


    - `updateUniform`: updateUniform(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None
        
        Update the program with value of the uniform.


    - `setSize`: setSize(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> None
        
        Set the size of the rendered image.


    - `render`: render(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None
        
        Render the current program to produce an image.


<a id='materialx-pymaterialxrender-stbimageloader'></a>

- **StbImageLoader**: Stb image file loader.

  - Inherits from: [ImageLoader](#materialx-pymaterialxrender-imageloader), [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.StbImageLoader
        
        Create a new stb image loader.


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool
        
        Save an image to the file system.


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image
        
        Load an image from the file system.


<a id='materialx-pymaterialxrender-tinyobjloader'></a>

- **TinyObjLoader**: Wrapper for geometry loader to read in OBJ files using the TinyObj library.

  - Inherits from: [GeometryLoader](#materialx-pymaterialxrender-geometryloader), [pybind11_object](#materialx-pymaterialxrender-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.TinyObjLoader
        
        Create a new TinyObjLoader.


    - `load`: load(self: MaterialX.PyMaterialXRender.TinyObjLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from disk.



### Functions

- `createImageStrip`: createImageStrip(arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Image]) -> MaterialX.PyMaterialXRender.Image

Create a horizontal image strip from a vector of images with identical resolutions and formats.

- `createUniformImage`: createUniformImage(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt, arg3: MaterialX.PyMaterialXRender.BaseType, arg4: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXRender.Image

Create a uniform-color image with the given properties.

- `getMaxDimensions`: getMaxDimensions(arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Image]) -> tuple[int, int]

Compute the maximum width and height of all images in the given vector.


### Globals

- FLOAT = (BaseType.FLOAT: 5)
- HALF = (BaseType.HALF: 4)
- INT16 = (BaseType.INT16: 3)
- INT8 = (BaseType.INT8: 1)
- UINT16 = (BaseType.UINT16: 2)
- UINT8 = (BaseType.UINT8: 0)

---

## Module: MaterialX.PyMaterialXRenderGlsl

### Classes

<a id='materialx-pymaterialxrenderglsl-gltexturehandler'></a>

- **GLTextureHandler**: An OpenGL texture handler class.

  - Inherits from: [ImageHandler](#materialx-pymaterialxrenderglsl-imagehandler), [pybind11_object](#materialx-pymaterialxrenderglsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool
        
        Bind an image.
        
        This method will bind the texture to an active texture unit as defined by the corresponding image description. The method will fail if there are not enough available image units to bind to.


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool
        
        Unbind an image.


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool
        
        Create rendering resources for the given image.


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None
        
        Release rendering resources for the given image, or for all cached images if no image pointer is specified.


<a id='materialx-pymaterialxrenderglsl-glslprogram'></a>

- **GlslProgram**: A class representing an executable GLSL program.

There are two main interfaces which can be used. One which takes in a HwShader and one which allows for explicit setting of shader stage code.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrenderglsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRenderGlsl.GlslProgram
        
        Create a GLSL program instance.


    - `setStages`: setStages(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        Set up code stages to validate based on an input hardware shader.
        
        Args:
            shader: Hardware shader to use


    - `addStage`: addStage(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: str) -> None
        
        Set the code stages based on a list of stage strings.
        
        Args:
            stage: Name of the shader stage.
            sourceCode: Source code of the shader stage.


    - `getStageSourceCode`: getStageSourceCode(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str) -> str
        
        Get source code string for a given stage.
        
        Returns:
            Shader stage string. String is empty if not found.


    - `getShader`: getShader(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> MaterialX.PyMaterialXGenShader.Shader
        
        Return the shader, if any, used to generate this program.


    - `build`: build(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None
        
        Build shader program data from the source code set for each shader stage.
        
        An exception is thrown if the program cannot be built. The exception will contain a list of compilation errors.


    - `hasBuiltData`: hasBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool
        
        Return true if built shader program data is present.


    - `clearBuiltData`: clearBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None


    - `getUniformsList`: getUniformsList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]
        
        Get list of program input uniforms.
        
        Returns:
            Program uniforms list.


    - `getAttributesList`: getAttributesList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]
        
        Get list of program input attributes.
        
        Returns:
            Program attributes list.


    - `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg2: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg3: bool) -> None
        
        Find the locations in the program which starts with a given variable name.
        
        Args:
            variable: Variable to search for
            variableList: List of program inputs to search
            foundList: Returned list of found program inputs. Empty if none found.
            exactMatch: Search for exact variable name match.


    - `bind`: bind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool
        
        Bind the program.
        
        Returns:
            False if failed


    - `hasActiveAttributes`: hasActiveAttributes(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool
        
        Return true if the program has active attributes.


    - `bindUniform`: bindUniform(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None
        
        Bind a value to the uniform with the given name.


    - `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg1: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Bind attribute buffers to attribute inputs.
        
        Args:
            inputs: Attribute inputs to bind to
            mesh: Mesh containing streams to bind


    - `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None
        
        Bind input geometry partition (indexing).


    - `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Bind input geometry streams.


    - `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None
        
        Unbind any bound geometry.


    - `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Bind any input textures.


    - `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Bind lighting.


    - `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None
        
        Bind view information.


    - `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, time: typing.SupportsFloat = 0.0, frame: typing.SupportsFloat = 1.0) -> None
        
        Bind time and frame.


    - `unbind`: unbind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None
        
        Unbind the program. Equivalent to binding no program.


  - Attributes: UNDEFINED_OPENGL_RESOURCE_ID = 0, UNDEFINED_OPENGL_PROGRAM_LOCATION = -1

<a id='materialx-pymaterialxrenderglsl-glslrenderer'></a>

- **GlslRenderer**: Helper class for rendering generated GLSL code to produce images.

There are two main interfaces which can be used. One which takes in a HwShader and one which allows for explicit setting of shader stage code.

The main services provided are: Validation: All shader stages are compiled and atteched to a GLSL shader program. Introspection: The compiled shader program is examined for uniforms and attributes. Binding: Uniforms and attributes which match the predefined variables generated the GLSL code generator will have values assigned to this. This includes matrices, attribute streams, and textures. Rendering: The program with bound inputs will be used to drawing geometry to an offscreen buffer. An interface is provided to save this offscreen buffer to disk using an externally defined image handler.

  - Inherits from: [ShaderRenderer](#materialx-pymaterialxrenderglsl-shaderrenderer), [pybind11_object](#materialx-pymaterialxrenderglsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.GlslRenderer
        
        Create a GLSL renderer instance.


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -> None
        
        Internal initialization of stages and OpenGL constructs required for program validation and rendering.
        
        Args:
            renderContextHandle: allows initializing the GlslRenderer with a Shared OpenGL Context


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: collections.abc.Mapping[str, str]) -> None


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None
        
        Validate inputs for the program.


    - `render`: render(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None
        
        Render the current program to an offscreen buffer.


    - `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None
        
        Render the current program in texture space to an off-screen buffer.


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Capture the current contents of the off-screen hardware buffer as an image.


    - `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> MaterialX.PyMaterialXRenderGlsl.GlslProgram
        
        Return the GLSL program.


<a id='materialx-pymaterialxrenderglsl-input'></a>

- **Input**: An input element within a Node or NodeDef.

An Input holds either a uniform value or a connection to a spatially-varying Output, either of which may be modified within the scope of a Material.

  - Inherits from: [pybind11_object](#materialx-pymaterialxrenderglsl-pybind11_object)

  - Attributes: INVALID_OPENGL_TYPE = -1, location = (property), gltype = (property), size = (property), typeString = (property), value = (property), isConstant = (property), path = (property)

<a id='materialx-pymaterialxrenderglsl-texturebaker'></a>

- **TextureBaker**: A helper class for baking procedural material content to textures.

TODO: Add support for graphs containing geometric nodes such as position and normal.

  - Inherits from: [GlslRenderer](#materialx-pymaterialxrenderglsl-glslrenderer), [ShaderRenderer](#materialx-pymaterialxrenderglsl-shaderrenderer), [pybind11_object](#materialx-pymaterialxrenderglsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.TextureBaker


    - `setExtension`: setExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setDistanceUnit`: setDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getDistanceUnit`: getDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setAverageImages`: setAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None


    - `getAverageImages`: getAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool


    - `setOptimizeConstants`: setOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None


    - `getOptimizeConstants`: getOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool


    - `setOutputImagePath`: setOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `getOutputImagePath`: getOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXFormat.FilePath


    - `setBakedGraphName`: setBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getBakedGraphName`: getBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setBakedGeomInfoName`: setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getBakedGeomInfoName`: getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setTextureFilenameTemplate`: setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None


    - `getTextureFilenameTemplate`: getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str


    - `setFilenameTemplateVarOverride`: setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str, arg1: str) -> None


    - `setHashImageNames`: setHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None


    - `getHashImageNames`: getHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool


    - `setTextureSpaceMin`: setTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None


    - `getTextureSpaceMin`: getTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2


    - `setTextureSpaceMax`: setTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None


    - `getTextureSpaceMax`: getTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2


    - `setupUnitSystem`: setupUnitSystem(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: collections.abc.Sequence[str], arg4: str) -> MaterialX.PyMaterialXCore.Document


    - `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None



---

## Module: MaterialX.PyMaterialXRenderMsl

### Classes

<a id='materialx-pymaterialxrendermsl-input'></a>

- **Input**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxrendermsl-pybind11_object)

  - Attributes: location = (property), size = (property), typeString = (property), value = (property), isConstant = (property), path = (property)

<a id='materialx-pymaterialxrendermsl-metaltexturehandler'></a>

- **MetalTextureHandler**: 

  - Inherits from: [ImageHandler](#materialx-pymaterialxrendermsl-imagehandler), [pybind11_object](#materialx-pymaterialxrendermsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: objc_object<MTLDevice>, arg1: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRenderMsl.MetalTextureHandler


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None


<a id='materialx-pymaterialxrendermsl-mslprogram'></a>

- **MslProgram**: 

  - Inherits from: [pybind11_object](#materialx-pymaterialxrendermsl-pybind11_object)

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRenderMsl.MslProgram


    - `setStages`: setStages(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None


    - `addStage`: addStage(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: str) -> None


    - `getStageSourceCode`: getStageSourceCode(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str) -> str


    - `getShader`: getShader(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> MaterialX.PyMaterialXGenShader.Shader


    - `build`: build(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLDevice>, arg1: MaterialX_v1_39_5::MetalFramebuffer) -> objc_object<MTLRenderPipelineState>


    - `prepareUsedResources`: prepareUsedResources(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.Camera, arg2: MaterialX.PyMaterialXRender.GeometryHandler, arg3: MaterialX.PyMaterialXRender.ImageHandler, arg4: MaterialX.PyMaterialXRender.LightHandler) -> None


    - `getUniformsList`: getUniformsList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> dict[str, MaterialX_v1_39_5::MslProgram::Input]


    - `getAttributesList`: getAttributesList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> dict[str, MaterialX_v1_39_5::MslProgram::Input]


    - `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg2: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg3: bool) -> None


    - `bind`: bind(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>) -> bool


    - `bindUniform`: bindUniform(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None


    - `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg2: MaterialX.PyMaterialXRender.Mesh) -> None


    - `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None


    - `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.Mesh) -> None


    - `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -> None


    - `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object<MTLRenderCommandEncoder>, arg1: MaterialX.PyMaterialXRender.LightHandler, arg2: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None


    - `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderMsl.MslProgram, time: typing.SupportsFloat = 0.0, frame: typing.SupportsFloat = 1.0) -> None


<a id='materialx-pymaterialxrendermsl-mslrenderer'></a>

- **MslRenderer**: 

  - Inherits from: [ShaderRenderer](#materialx-pymaterialxrendermsl-shaderrenderer), [pybind11_object](#materialx-pymaterialxrendermsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderMsl.MslRenderer


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -> None


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        2. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: collections.abc.Mapping[str, str]) -> None


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> None


    - `render`: render(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> None


    - `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image


    - `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -> MaterialX.PyMaterialXRenderMsl.MslProgram


<a id='materialx-pymaterialxrendermsl-texturebaker'></a>

- **TextureBaker**: 

  - Inherits from: [MslRenderer](#materialx-pymaterialxrendermsl-mslrenderer), [ShaderRenderer](#materialx-pymaterialxrendermsl-shaderrenderer), [pybind11_object](#materialx-pymaterialxrendermsl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderMsl.TextureBaker


    - `setExtension`: setExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setDistanceUnit`: setDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getDistanceUnit`: getDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setAverageImages`: setAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None


    - `getAverageImages`: getAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool


    - `setOptimizeConstants`: setOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None


    - `getOptimizeConstants`: getOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool


    - `setOutputImagePath`: setOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `getOutputImagePath`: getOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXFormat.FilePath


    - `setBakedGraphName`: setBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getBakedGraphName`: getBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setBakedGeomInfoName`: setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getBakedGeomInfoName`: getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setTextureFilenameTemplate`: setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -> None


    - `getTextureFilenameTemplate`: getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> str


    - `setFilenameTemplateVarOverride`: setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str, arg1: str) -> None


    - `setHashImageNames`: setHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None


    - `getHashImageNames`: getHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> bool


    - `setTextureSpaceMin`: setTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None


    - `getTextureSpaceMin`: getTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2


    - `setTextureSpaceMax`: setTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None


    - `getTextureSpaceMax`: getTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2


    - `setupUnitSystem`: setupUnitSystem(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: collections.abc.Sequence[str], arg4: str) -> MaterialX.PyMaterialXCore.Document


    - `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -> None



---

## Module: MaterialX.PyMaterialXRenderOsl

### Classes

<a id='materialx-pymaterialxrenderosl-oslrenderer'></a>

- **OslRenderer**: Helper class for rendering generated OSL code to produce images.

The main services provided are: Source code validation: Use of "oslc" to compile and test output results Introspection check: None at this time. Binding: None at this time. Render validation: Use of "testrender" to output rendered images. Assumes source compilation was success as it depends on the existence of corresponding .oso files.

  - Inherits from: [ShaderRenderer](#materialx-pymaterialxrenderosl-shaderrenderer), [pybind11_object](#materialx-pymaterialxrenderosl-pybind11_object)

  - Methods:

    - `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderOsl.OslRenderer
        
        Create an OSL renderer instance.


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -> None
        
        Internal initialization required for program validation and rendering.
        
        An exception is thrown on failure. The exception will contain a list of initialization errors.


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Mapping[str, str]) -> None


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None
        
        Validate inputs for the compiled OSL program.
        
        Note: Currently no validation has been implemented.


    - `render`: render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None
        
        Render OSL program to disk.
        
        This is done by using either "testshade" or "testrender". Currently only "testshade" is supported.
        
        Usage of both executables requires compiled source (.oso) files as input. A shader output must be set before running this test via the setOslOutputName() method to ensure that the appropriate .oso files can be located.


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Capture the current rendered output as an image.


    - `setOslCompilerExecutable`: setOslCompilerExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the path to the OSL executable.
        
        Args:
            executableFilePath: Path to OSL compiler executable


    - `setOslIncludePath`: setOslIncludePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Set the search locations for OSL include files.
        
        Args:
            dirPath: Include path(s) for the OSL compiler. This should include the path to stdosl.h.


    - `setOslOutputFilePath`: setOslOutputFilePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the location where compiled OSL files will reside.
        
        Args:
            dirPath: Path to output location


    - `setShaderParameterOverrides`: setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Sequence[str]) -> None
        
        Set shader parameter strings to be added to the scene XML file.
        
        These strings will set parameter overrides for the shader.


    - `setOslShaderOutput`: setOslShaderOutput(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str, arg1: str) -> None
        
        Set the OSL shader output.
        
        Args:
            outputName: Name of shader output
            outputType: The MaterialX type of the output


    - `setOslTestShadeExecutable`: setOslTestShadeExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the path to the OSL shading tester.
        
        Args:
            executableFilePath: Path to OSL "testshade" executable


    - `setOslTestRenderExecutable`: setOslTestRenderExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the path to the OSL rendering tester.
        
        Args:
            executableFilePath: Path to OSL "testrender" executable


    - `setOslTestRenderSceneTemplateFile`: setOslTestRenderSceneTemplateFile(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the XML scene file to use for testrender.
        
        This is a template file with the following tokens for replacement: shader% : which will be replaced with the name of the shader to use shader_output% : which will be replace with the name of the shader output to use templateFilePath Scene file name
        
        Args:
            templateFilePath: Scene file name


    - `setOslShaderName`: setOslShaderName(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str) -> None
        
        Set the name of the shader to be used for the input XML scene file.
        
        Args:
            shaderName: Name of shader


    - `setOslUtilityOSOPath`: setOslUtilityOSOPath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the search path for dependent shaders (.oso files) which are used when rendering with testrender.
        
        Args:
            dirPath: Path to location containing .oso files.


    - `useTestRender`: useTestRender(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: bool) -> None
        
        Used to toggle to either use testrender or testshade during render validation By default testshade is used.
        
        Args:
            useTestRender: Indicate whether to use testrender.


    - `compileOSL`: compileOSL(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Compile OSL code stored in a file.
        
        Args:
            oslFilePath: OSL file path.


  - Attributes: OSL_CLOSURE_COLOR_STRING = 'closure color'


---

## Module: MaterialX.main


### Functions

- `getDefaultDataLibraryFolders`: Return list of default data library folders

- `getDefaultDataSearchPath`: Return the default data search path.

- `stringToValue`: (Deprecated) Convert a MaterialX value string and Python type to the corresponding Python value.

- `typeToName`: (Deprecated) Return the MaterialX type string associated with the given Python type.

- `valueToString`: (Deprecated) Convert a Python value to its corresponding MaterialX value string.


---
