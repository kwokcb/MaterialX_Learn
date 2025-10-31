## Module: MaterialX.PyMaterialXCore

### Classes

- **AttributeDef**: 

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
        
        Return value string.


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None
        
        Set the exportable boolean for the element.


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return the exportable boolean for the element.
        
        Defaults to false if exportable is not set.


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None
        
        Set the contains string for this backdrop.


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a contains string.


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str
        
        Return the contains string for this backdrop.


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the width attribute of the backdrop.


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a width attribute.


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the width attribute of the backdrop.


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the height attribute of the backdrop.


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a height attribute.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the height attribute of the backdrop.


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None
        
        Set the vector of elements that this backdrop contains.


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]
        
        Return the vector of elements that this backdrop contains.


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

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


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None
        
        Set the vector of collections that are directly included by this element.


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]
        
        Return the vector of collections that are directly included by this element.


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if the include chain for this element contains a cycle.


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool
        
        Return true if this collection and the given geometry string have any geometries in common.


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Create a deep copy of the value.


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document
        
        Create a deep copy of the value.


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
        
        Returns a nodedef for a given transform.


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


- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str
        
        Return the ColorManagementSystem name.


- **Element**: 

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
        
        Return the ColorManagementSystem name.


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


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None
        
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
        
        Return our self pointer.


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return our parent element.


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return the root element of our tree.


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document
        
        Return the root document of our tree.


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator
        
        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.
        
        Returns:
            A TreeIterator object.


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator
        
        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.
        
        Returns:
            A GraphIterator object.


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge
        
        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.
        
        Args:
            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.
        
        Returns:
            The upstream Edge, if valid, or an empty Edge object.


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int
        
        Return the number of queryable upstream edges for this element.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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
        
        Validate that the given element tree, including all descendants, is consistent with the MaterialX specification.


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


  - Attributes: NAME_ATTRIBUTE, FILE_PREFIX_ATTRIBUTE, GEOM_PREFIX_ATTRIBUTE, COLOR_SPACE_ATTRIBUTE, INHERIT_ATTRIBUTE, NAMESPACE_ATTRIBUTE, DOC_ATTRIBUTE, XPOS_ATTRIBUTE, YPOS_ATTRIBUTE

- **ElementEquivalenceOptions**: 

  - Attributes: performValueComparisons, floatFormat, floatPrecision, attributeExclusionList

- **ElementPredicate**: 

- **Exception**: 

- **ExceptionFoundCycle**: 

- **ExceptionOrphanedElement**: 

- **GenericElement**: 

  - Attributes: CATEGORY

- **GeomElement**: 

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
        
        Return the Collection, if any, with the given name.


- **GeomInfo**: 

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


  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

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
        
        Return the GeomProp, if any, with the given name.
        
        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the GeomProp, if any, with the given name.


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


  - Attributes: CATEGORY

- **GraphElement**: 

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


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None
        
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


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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


- **Implementation**: 

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
        
        Returns a nodedef for a given transform.


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the nodegraph string for the Implementation.


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a nodegraph string.


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the NodeGraph, if any, with the given name.


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

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


  - Attributes: CATEGORY

- **InterfaceElement**: 

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
        
        Add a Token to this element.
        
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
        
        Return a unique identifier for the target this generator is for.


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the version string of this interface.


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if this interface has a version string.


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the version string of this interface.


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None
        
        Set the major and minor versions as an integer pair.


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]
        
        Return the major and minor versions as an integer pair.


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None
        
        Set the default version flag of this element.


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return the default version flag of this element.


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first declaration of this interface, optionally filtered by the given target name.


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


  - Attributes: NODE_DEF_ATTRIBUTE

- **LinearUnitConverter**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter


    - `getUnitScale`: getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]
        
        Return the mappings from unit names to the scale value defined by a linear converter.


    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **Look**: 

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


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return a vector of all Look elements in the document.


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set comma-separated list of looks.


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return the active look, if any.


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set the active look.


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None
        
        Set the material string for the MaterialAssign.


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return true if the given MaterialAssign has a material string.


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str
        
        Return the material string for the MaterialAssign.


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None
        
        Set the exclusive boolean for the MaterialAssign.


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return the exclusive boolean for the MaterialAssign.


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node
        
        Return the material node, if any, referenced by the MaterialAssign.


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the inverse of the matrix.


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


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the inverse of the matrix.


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return the product of this matrix and a 3D vector.


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D point.


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D direction vector.


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D normal vector.


    - `createRotationX`: createRotationX(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationY`: createRotationY(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationZ`: createRotationZ(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


  - Attributes: IDENTITY

- **MatrixBase**: 

- **Member**: 

  - Attributes: CATEGORY

- **NewlineElement**: 

  - Attributes: CATEGORY

- **Node**: 

  - Methods:

    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None
        
        Set the name of the Node connected to the given input, creating a child element for the input if needed.


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str
        
        Return the name of the Node connected to the given input.
        
        If the given input is not present, then an empty string is returned.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


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


  - Attributes: CATEGORY

- **NodeDef**: 

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


    - `getImplementation`: getImplementation(*args, **kwargs)
        Overloaded function.
        
        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.
        
        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool
        
        Return true if the given version string is compatible with this NodeDef.
        
        This may be used to test, for example, whether a NodeDef and Node may be used together.


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None
        
        Set the NodeDef element referenced by the Implementation.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


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
        
        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool
        
        Return true if a cycle exists in any upstream path from this element.


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

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
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None
        
        Set the output to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing output connection on the input will be cleared.


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output
        
        Return the output connected to the given input.
        
        If the given input is not present, then an empty OutputPtr is returned.


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

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
        
        Return the Collection, if any, with the given name.


  - Attributes: CATEGORY

- **PropertySet**: 

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


  - Attributes: CATEGORY

- **PropertySetAssign**: 

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
        
        Return the PropertySet, if any, with the given name.


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's file prefix string.


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's file prefix string.


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's geom prefix string.


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's geom prefix string.


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


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]
        
        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.
        
        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int
        
        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None
        
        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.
        
        Args:
            prune: If set to true, then the current subtree will be pruned.


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool
        
        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.


- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Set the variable semantic of this port.


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool
        
        Return true if the given TypeDef has a semantic string.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str
        
        Return the variable semantic of this port.


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


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Remove the Member, if any, with the given name.


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None
        
        Set the data type for this port.


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the given element has a type string.


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str
        
        Get stream attribute name.


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of color type.


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of multi-output type.


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef
        
        Return the TypeDef, if any, with the given name.


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


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


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str
        
        Return the unit type string.


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Add a Unit to the UnitDef.
        
        Args:
            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.
        
        Returns:
            A shared pointer to the new Unit.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Return the unit type for the value on this port.


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]
        
        Return a vector of all Unit elements in the UnitDef.


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]
        
        Return a vector of all Member elements in the TypeDef.


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return value string.


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return type string.


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the value string of an element.


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a value string.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return value string.


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
        
        Set a unit type for the value on this port.


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unit string.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type for the value on this port.


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit defined by the associated NodeDef if this element is a child of a Node.


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type string.


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        The the uniform attribute flag for this element.


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None
        
        Set the uniform attribute flag on this element.


    - `setValue`: Set the typed value of an element.


    - `getValue`: Return the typed value of an element.


    - `getDefaultValue`: Return the default value for this element.


  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

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


  - Attributes: CATEGORY

- **VariantSet**: 

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


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

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


  - Attributes: CATEGORY


### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

Create a new document of the given subclass.

Create a new Document.

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

Return the major and minor versions as an integer pair.

- `getVersionString`: getVersionString() -> str

Return the version string of this interface.

- `incrementName`: incrementName(arg0: str) -> str

- `isValidName`: isValidName(arg0: str) -> bool

- `joinStrings`: joinStrings(arg0: list[str], arg1: str) -> str

- `parentNamePath`: parentNamePath(arg0: str) -> str

- `prettyPrint`: prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str

- `replaceSubstrings`: replaceSubstrings(arg0: str, arg1: dict[str, str]) -> str

- `splitNamePath`: splitNamePath(arg0: str) -> list[str]

- `splitString`: splitString(arg0: str, arg1: str) -> list[str]

- `stringEndsWith`: stringEndsWith(arg0: str, arg1: str) -> bool

- `stringStartsWith`: stringStartsWith(arg0: str, arg1: str) -> bool

- `targetStringsMatch`: targetStringsMatch(arg0: str, arg1: str) -> bool


### Globals

ARRAY_PREFERRED_SEPARATOR, ARRAY_VALID_SEPARATORS, BSDF_TYPE_STRING, DEFAULT_TYPE_STRING, DISPLACEMENT_SHADER_TYPE_STRING, EDF_TYPE_STRING, FILENAME_TYPE_STRING, GEOMNAME_TYPE_STRING, GEOM_PATH_SEPARATOR, LIGHT_SHADER_TYPE_STRING, MATERIAL_TYPE_STRING, MULTI_OUTPUT_TYPE_STRING, NAME_PATH_SEPARATOR, NAME_PREFIX_SEPARATOR, NONE_TYPE_STRING, STRING_TYPE_STRING, SURFACE_MATERIAL_NODE_STRING, SURFACE_SHADER_TYPE_STRING, UDIM_SET_PROPERTY, UDIM_TOKEN, UNIVERSAL_GEOM_NAME, UV_TILE_TOKEN, VALUE_STRING_FALSE, VALUE_STRING_TRUE, VDF_TYPE_STRING, VOLUME_MATERIAL_NODE_STRING, VOLUME_SHADER_TYPE_STRING



---

## Module: MaterialX.PyMaterialXFormat

### Classes

- **ExceptionFileMissing**: 

- **ExceptionParseError**: 

- **FilePath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FilePath, format: MaterialX.PyMaterialXFormat.Format = <Format.FormatWindows: 0>) -> str
        
        Return a single-line description of this element, including its category, name, and attributes.


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


    - `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]
        
        Return a vector of all directories at or beneath the given path.


    - `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Create a directory on the file system at the given path.


    - `getCurrentPath`: getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath


    - `getModulePath`: getModulePath() -> MaterialX.PyMaterialXFormat.FilePath


- **FileSearchPath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ';') -> str
        
        Return a single-line description of this element, including its category, name, and attributes.


    - `append`: append(*args, **kwargs)
        Overloaded function.
        
        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Append the given search path to the sequence.
        
        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Append the given search path to the sequence.


    - `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Prepend the given path to the sequence.


    - `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Clear all paths from the sequence.


    - `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int
        
        Return the number of strings in the path.


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool
        
        Return true if the given path is empty.


    - `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.
        
        On success, the combined path is returned; otherwise the original filename is returned unmodified.


- **Format**: Members:

  FormatWindows

  FormatPosix

  FormatNative

  - Attributes: name, value, FormatWindows, FormatPosix, FormatNative

- **Type**: Members:

  TypeRelative

  TypeAbsolute

  TypeNetwork

  - Attributes: name, value, TypeRelative, TypeAbsolute, TypeNetwork

- **XmlReadOptions**: 

  - Attributes: readXIncludeFunction, readComments, readNewlines, upgradeVersion, parentXIncludes

- **XmlWriteOptions**: 

  - Attributes: writeXIncludeEnable, elementPredicate


### Functions

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A36D1230>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

- `getEnvironmentPath`: getEnvironmentPath(sep: str = ';') -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getSourceSearchPath`: getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getSubdirectories`: getSubdirectories(arg0: list[MaterialX.PyMaterialXFormat.FilePath], arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: list[MaterialX.PyMaterialXFormat.FilePath]) -> None

- `loadDocuments`: loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: set[str], includeFiles: set[str], documents: list[MaterialX.PyMaterialXCore.Document], documentsPaths: list[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: list[str] = None) -> None

- `loadLibraries`: loadLibraries(libraryFolders: list[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A3730A30>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Load a library of implementations from the provided document, replacing any previously loaded content.

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A36D18F0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A32B0FF0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `writeToXmlFile`: writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> None

- `writeToXmlString`: writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> str


### Globals

FormatNative, FormatPosix, FormatWindows, MATERIALX_SEARCH_PATH_ENV_VAR, PATH_LIST_SEPARATOR, TypeAbsolute, TypeNetwork, TypeRelative



---

## Module: MaterialX.PyMaterialXGenGlsl

### Classes

- **EsslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.


- **GlslResourceBindingContext**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int) -> MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext


    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


- **GlslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.


- **VkShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.


- **WgslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.



---

## Module: MaterialX.PyMaterialXGenMdl

### Classes

- **MdlShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMdl.MdlShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.



---

## Module: MaterialX.PyMaterialXGenMsl

### Classes

- **MslResourceBindingContext**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int) -> MaterialX.PyMaterialXGenMsl.MslResourceBindingContext


    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


- **MslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str
        
        Return the version string for the ESSL version this generator is for.



---

## Module: MaterialX.PyMaterialXGenOsl

### Classes

- **OslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `generate`: generate(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.



### Globals

OSL_INPUTS, OSL_OUTPUTS, OSL_UNIFORMS



---

## Module: MaterialX.PyMaterialXGenShader

### Classes

- **ApplicationVariableHandler**: 

- **ColorManagementSystem**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> str
        
        Return the ColorManagementSystem name.


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Load a library of implementations from the provided document, replacing any previously loaded content.


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -> bool
        
        Returns whether this color management system supports a provided transform.


- **ColorSpaceTransform**: 

  - Attributes: sourceSpace, targetSpace, type

- **DefaultColorManagementSystem**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -> str
        
        Return the ColorManagementSystem name.


- **GenContext**: 

  - Methods:

    - `getShaderGenerator`: getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.ShaderGenerator
        
        Return shader generatior.


    - `getOptions`: getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX_v1_39_5::GenOptions
        
        Return shader generation options.


    - `getTypeDesc`: getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -> MaterialX_v1_39_5::TypeDesc
        
        Return a TypeDesc for the given type name.


    - `registerSourceCodeSearchPath`: registerSourceCodeSearchPath(*args, **kwargs)
        Overloaded function.
        
        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Register a user search path for finding source code during code generation.
        
        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Register a user search path for finding source code during code generation.


    - `resolveSourceFile`: resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Resolve a source code filename, first checking the given local path then checking any file paths registered by the user.


    - `pushUserData`: pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -> None
        
        Add user data to the context to make it available during shader generator.


    - `setApplicationVariableHandler`: setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -> None
        
        Set handler for application variables.


    - `getApplicationVariableHandler`: getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -> Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]
        
        Get handler for application variables.


- **GenOptions**: 

  - Attributes: shaderInterfaceType, fileTextureVerticalFlip, targetColorSpaceOverride, targetDistanceUnit, addUpstreamDependencies, libraryPrefix, emitColorTransforms, hwTransparency, hwSpecularEnvironmentMethod, hwSrgbEncodeOutput, hwWriteDepthMoments, hwShadowMap, hwMaxActiveLightSources, hwNormalizeUdimTexCoords, hwAmbientOcclusion, hwWriteAlbedoTable, hwWriteEnvPrefilter, hwImplicitBitangents

- **GenUserData**: 

  - Methods:

    - `getSelf`: getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -> MaterialX.PyMaterialXGenShader.GenUserData
        
        Return our self pointer.


- **HwResourceBindingContext**: 

  - Methods:

    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


- **HwShaderGenerator**: 

  - Methods:

    - `bindLightShader`: bindLightShader(self: MaterialX.PyMaterialXCore.NodeDef, arg0: int, arg1: MaterialX.PyMaterialXGenShader.GenContext) -> None


    - `unbindLightShader`: unbindLightShader(self: int, arg0: MaterialX.PyMaterialXGenShader.GenContext) -> None


    - `unbindLightShaders`: unbindLightShaders(self: MaterialX.PyMaterialXGenShader.GenContext) -> None


- **HwSpecularEnvironmentMethod**: Members:

  SPECULAR_ENVIRONMENT_PREFILTER

  SPECULAR_ENVIRONMENT_FIS

  SPECULAR_ENVIRONMENT_NONE

  - Attributes: name, value, SPECULAR_ENVIRONMENT_PREFILTER, SPECULAR_ENVIRONMENT_FIS, SPECULAR_ENVIRONMENT_NONE

- **Shader**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.Shader) -> str
        
        Return the ColorManagementSystem name.


    - `hasStage`: hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool
        
        Return if stage exists.


    - `numStages`: numStages(self: MaterialX.PyMaterialXGenShader.Shader) -> int
        
        Return the number of shader stages for this shader.


    - `getStage`: getStage(*args, **kwargs)
        Overloaded function.
        
        1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: int) -> MaterialX_v1_39_5::ShaderStage
        
        Return a stage by name.
        
        2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX_v1_39_5::ShaderStage
        
        Return a stage by name.


    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> str
        
        Return the shader source code for a given shader stage.


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool
        
        Return true if the given attribute is present.


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX.PyMaterialXCore.Value
        
        Return the value string of the given attribute.
        
        If the given attribute is not present, then an empty string is returned.


    - `setAttribute`: setAttribute(*args, **kwargs)
        Overloaded function.
        
        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None
        
        Set the value string of the given attribute.
        
        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None
        
        Set the value string of the given attribute.


- **ShaderGenerator**: 

  - Methods:

    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> str
        
        Return a unique identifier for the target this generator is for.


    - `generate`: generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -> MaterialX.PyMaterialXGenShader.Shader
        
        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None
        
        Set the color management system string.


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX.PyMaterialXGenShader.ColorManagementSystem
        
        Return the color management system string.


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


- **ShaderInterfaceType**: Members:

  SHADER_INTERFACE_COMPLETE

  SHADER_INTERFACE_REDUCED

  - Attributes: name, value, SHADER_INTERFACE_COMPLETE, SHADER_INTERFACE_REDUCED

- **ShaderPort**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -> None
        
        Set the data type for this port.


    - `getType`: getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX_v1_39_5::TypeDesc
        
        Get stream attribute name.


    - `setName`: setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the element's name string.


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the ColorManagementSystem name.


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


    - `setValue`: setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value) -> None
        
        Set the typed value of an element from a C-style string.


    - `getValue`: getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX.PyMaterialXCore.Value
        
        Returns a value formatted according to this type syntax.
        
        The value is constructed from the given value object.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return value string.


    - `setGeomProp`: setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the geometric property string of this element.


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the GeomProp, if any, with the given name.


    - `setPath`: setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the path to this port.


    - `getPath`: getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the path to this port.


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set a unit type for the value on this port.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the unit type for the value on this port.


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None
        
        Set the element's color space string.


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str
        
        Return the element's color space string.


    - `isUniform`: isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool
        
        Return the uniform flag on this port.


    - `isEmitted`: isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool
        
        Return the emitted state of this port.


- **ShaderPortPredicate**: 

- **ShaderStage**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the ColorManagementSystem name.


    - `getFunctionName`: getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the stage function name.


    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str
        
        Return the shader source code for a given shader stage.


    - `getUniformBlock`: getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock
        
        Return the uniform variable block with given name.


    - `getInputBlock`: getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock
        
        Return the input variable block with given name.


    - `getOutputBlock`: getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock
        
        Return the output variable block with given name.


    - `getConstantBlock`: getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> MaterialX.PyMaterialXGenShader.VariableBlock
        
        Return the constant variable block.


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


- **ShaderTranslator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderTranslator


    - `translateShader`: translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None
        
        Translate a shader node to the destination shading model.


    - `translateAllMaterials`: translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None
        
        Translate each material in the input document to the destination shading model.


- **TypeDesc**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> str
        
        Return the ColorManagementSystem name.


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Return the base type of the image.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Return the variable semantic of this port.


    - `getSize`: getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int
        
        Get the number of elements.


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


- **UnitSystem**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.UnitSystem


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> str
        
        Return the ColorManagementSystem name.


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Load a library of implementations from the provided document, replacing any previously loaded content.


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -> bool
        
        Returns whether this color management system supports a provided transform.


    - `setUnitConverterRegistry`: setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None
        
        Assign unit converter registry replacing any previous assignment.


    - `getUnitConverterRegistry`: getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> MaterialX.PyMaterialXCore.UnitConverterRegistry
        
        Returns the currently assigned unit converter registry.


- **UnitTransform**: 

  - Attributes: sourceUnit, targetUnit, type, unitType

- **VariableBlock**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str
        
        Return the ColorManagementSystem name.


    - `getInstance`: getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str
        
        Get the instance name of this block.


    - `empty`: empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> bool
        
        Return true if the block has no variables.


    - `size`: size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int
        
        Return the number of strings in the path.


    - `find`: find(*args, **kwargs)
        Overloaded function.
        
        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort
        
        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.
        
        On success, the combined path is returned; otherwise the original filename is returned unmodified.
        
        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort
        
        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.
        
        On success, the combined path is returned; otherwise the original filename is returned unmodified.



### Functions

- `connectsToWorldSpaceNode`: connectsToWorldSpaceNode(arg0: MaterialX.PyMaterialXCore.Output) -> MaterialX.PyMaterialXCore.Node

- `elementRequiresShading`: elementRequiresShading(arg0: MaterialX.PyMaterialXCore.TypedElement) -> bool

- `findRenderableElements`: findRenderableElements(doc: MaterialX.PyMaterialXCore.Document, includeReferencedGraphs: bool = False) -> list[MaterialX.PyMaterialXCore.TypedElement]

- `findRenderableMaterialNodes`: findRenderableMaterialNodes(arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypedElement]

- `getNodeDefInput`: getNodeDefInput(arg0: MaterialX.PyMaterialXCore.Input, arg1: str) -> MaterialX.PyMaterialXCore.Input

- `getUdimCoordinates`: getUdimCoordinates(arg0: list[str]) -> list[MaterialX.PyMaterialXCore.Vector2]

- `getUdimScaleAndOffset`: getUdimScaleAndOffset(arg0: list[MaterialX.PyMaterialXCore.Vector2], arg1: MaterialX.PyMaterialXCore.Vector2, arg2: MaterialX.PyMaterialXCore.Vector2) -> None

- `hasElementAttributes`: hasElementAttributes(arg0: MaterialX.PyMaterialXCore.Output, arg1: list[str]) -> bool

- `isTransparentSurface`: isTransparentSurface(arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> bool

- `mapValueToColor`: mapValueToColor(arg0: MaterialX.PyMaterialXCore.Value, arg1: MaterialX.PyMaterialXCore.Color4) -> None

- `requiresImplementation`: requiresImplementation(arg0: MaterialX.PyMaterialXCore.NodeDef) -> bool

- `tokenSubstitution`: tokenSubstitution(arg0: dict[str, str], arg1: str) -> None


### Globals

HW_ATTR_TRANSPARENT, HW_LIGHT_DATA, HW_PIXEL_OUTPUTS, HW_PRIVATE_UNIFORMS, HW_PUBLIC_UNIFORMS, HW_VERTEX_DATA, HW_VERTEX_INPUTS, PIXEL_STAGE, SHADER_INTERFACE_COMPLETE, SHADER_INTERFACE_REDUCED, SPECULAR_ENVIRONMENT_FIS, SPECULAR_ENVIRONMENT_NONE, SPECULAR_ENVIRONMENT_PREFILTER, VERTEX_STAGE



---

## Module: MaterialX.PyMaterialXRender

### Classes

- **BaseType**: Members:

  UINT8

  UINT16

  HALF

  FLOAT

  - Attributes: name, value, UINT8, UINT16, HALF, FLOAT

- **Camera**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.Camera


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


    - `createPerspectiveMatrix`: createPerspectiveMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createOrthographicMatrix`: createOrthographicMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `transformPointPerspective`: transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


- **CgltfLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.CgltfLoader


    - `load`: load(self: MaterialX.PyMaterialXRender.CgltfLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from file path.


- **ExceptionRenderError**: 

- **GeometryHandler**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.GeometryHandler


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.GeometryLoader) -> None
        
        Add a geometry loader.
        
        Args:
            loader: Loader to add to list of available loaders.


    - `clearGeometry`: clearGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler) -> None
        
        Clear all loaded geometry.


    - `hasGeometry`: hasGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: str) -> bool


    - `getGeometry`: getGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: list[MaterialX.PyMaterialXRender.Mesh], arg1: str) -> None


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


- **GeometryLoader**: 

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.GeometryLoader) -> set[str]
        
        Get a list of extensions supported by the handler.


    - `load`: load(self: MaterialX.PyMaterialXRender.GeometryLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from file path.


- **Image**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: int, arg3: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the width attribute of the backdrop.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the height attribute of the backdrop.


    - `getChannelCount`: getChannelCount(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the channel count of the image.


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.BaseType
        
        Return the base type of the image.


    - `getBaseStride`: getBaseStride(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the stride of our base type in bytes.


    - `getMaxMipCount`: getMaxMipCount(self: MaterialX.PyMaterialXRender.Image) -> int
        
        Return the maximum number of mipmaps for this image.


    - `setTexelColor`: setTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int, arg2: MaterialX.PyMaterialXCore.Color4) -> None
        
        Set the texel color at the given coordinates.
        
        If the coordinates or image resource buffer are invalid, then an exception is thrown.


    - `getTexelColor`: getTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int) -> MaterialX.PyMaterialXCore.Color4
        
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


    - `applyGammaTransform`: applyGammaTransform(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> None
        
        Apply the given gamma transform to all texels of this image.


    - `copy`: copy(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image
        
        Create a deep copy of the value.


    - `applyBoxBlur`: applyBoxBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Apply a 3x3 box blur to this image, returning a new blurred image.


    - `applyGaussianBlur`: applyGaussianBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Apply a 7x7 Gaussian blur to this image, returning a new blurred image.


    - `applyBoxDownsample`: applyBoxDownsample(self: MaterialX.PyMaterialXRender.Image, arg0: int) -> MaterialX.PyMaterialXRender.Image
        
        Downsample this image by an integer factor using a box filter, returning the new reduced image.


    - `splitByLuminance`: splitByLuminance(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> tuple[MaterialX.PyMaterialXRender.Image, MaterialX.PyMaterialXRender.Image]
        
        Split this image by the given luminance threshold, returning the resulting underflow and overflow images.


    - `setResourceBuffer`: setResourceBuffer(self: MaterialX.PyMaterialXRender.Image, arg0: capsule) -> None
        
        Set the resource buffer for this image.


    - `getResourceBuffer`: getResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> capsule
        
        Return the resource buffer for this image.


    - `createResourceBuffer`: createResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None
        
        Allocate a resource buffer for this image that matches its properties.


    - `releaseResourceBuffer`: releaseResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None
        
        Release the resource buffer for this image.


    - `setResourceBufferDeallocator`: setResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image, arg0: Callable[[capsule], None]) -> None
        
        Set the resource buffer deallocator for this image.


    - `getResourceBufferDeallocator`: getResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image) -> Callable[[capsule], None]
        
        Return the resource buffer deallocator for this image.


- **ImageBufferDeallocator**: 

- **ImageHandler**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.ImageLoader) -> None
        
        Add a geometry loader.
        
        Args:
            loader: Loader to add to list of available loaders.


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, image: MaterialX.PyMaterialXRender.Image, verticalFlip: bool = False) -> bool
        
        Save image to disk.
        
        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save
        
        Returns:
            if save succeeded


    - `acquireImage`: acquireImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = <MaterialX.PyMaterialXCore.Color4 object at 0x00000235A370C8F0>) -> MaterialX.PyMaterialXRender.Image
        
        Acquire an image from the cache or file system.
        
        Args:
            filePath: File path of the image.
            defaultColor: Default color to use as a fallback for missing images.
        
        Returns:
            On success, a shared pointer to the acquired image.


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool
        
        Bind a single image.


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool
        
        Unbind an image.


    - `unbindImages`: unbindImages(self: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Unbbind all images for this material.


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


- **ImageLoader**: 

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.ImageLoader) -> set[str]
        
        Get a list of extensions supported by the handler.


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool
        
        Save image to disk.
        
        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save
        
        Returns:
            if save succeeded


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image


  - Attributes: BMP_EXTENSION, EXR_EXTENSION, GIF_EXTENSION, HDR_EXTENSION, JPG_EXTENSION, JPEG_EXTENSION, PIC_EXTENSION, PNG_EXTENSION, PSD_EXTENSION, TGA_EXTENSION, TIF_EXTENSION, TIFF_EXTENSION, TXT_EXTENSION

- **ImageSamplingProperties**: 

  - Attributes: uaddressMode, vaddressMode, filterType, defaultColor

- **LightHandler**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.LightHandler


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


    - `setEnvSampleCount`: setEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler, arg0: int) -> None
        
        Set the environment lighting sample count.


    - `getEnvSampleCount`: getEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler) -> int
        
        Return the environment lighting sample count.


    - `setRefractionTwoSided`: setRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None
        
        Set the two-sided refraction property.


    - `getRefractionTwoSided`: getRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler) -> int
        
        Return the two-sided refraction property.


    - `addLightSource`: addLightSource(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Node) -> None
        
        Add a light source.


    - `setLightSources`: setLightSources(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> None
        
        Set the vector of light sources.


    - `getLightSources`: getLightSources(self: MaterialX.PyMaterialXRender.LightHandler) -> list[MaterialX.PyMaterialXCore.Node]
        
        Return the vector of light sources.


    - `getFirstLightOfCategory`: getFirstLightOfCategory(self: MaterialX.PyMaterialXRender.LightHandler, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the first light source, if any, of the given category.


    - `getLightIdMap`: getLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler) -> dict[str, int]
        
        Get a list of identifiers associated with a given light nodedef.


    - `computeLightIdMap`: computeLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> dict[str, int]
        
        From a set of nodes, create a mapping of corresponding nodedef identifiers to numbers.


    - `findLights`: findLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node]) -> None
        
        Find lights to use based on an input document.
        
        Args:
            doc: Document to scan for lights
            lights: List of lights found in document


    - `registerLights`: registerLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -> None
        
        Register light node definitions and light count with a given generation context.
        
        Args:
            doc: Document containing light nodes and definitions
            lights: Lights to register
            context: Context to update


- **Mesh**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXRender.Mesh


    - `getName`: getName(self: MaterialX.PyMaterialXRender.Mesh) -> str
        
        Return the ColorManagementSystem name.


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> None
        
        Set the element's source URI.
        
        Args:
            sourceUri: A URI string representing the resource from which this element originates. This string may be used by serialization and deserialization routines to maintain hierarchies of include references.


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> bool
        
        Return true if this element has a source URI.


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> str
        
        Return the element's source URI.


    - `getStream`: getStream(*args, **kwargs)
        Overloaded function.
        
        1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> MaterialX.PyMaterialXRender.MeshStream
        
        Get a mesh stream by type and index.
        
        Args:
            type: Type of stream
            index: Index of stream
        
        Returns:
            Reference to a mesh stream if found
        
        2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: int) -> MaterialX.PyMaterialXRender.MeshStream
        
        Get a mesh stream by type and index.
        
        Args:
            type: Type of stream
            index: Index of stream
        
        Returns:
            Reference to a mesh stream if found


    - `addStream`: addStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> None
        
        Add a mesh stream.


    - `setVertexCount`: setVertexCount(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> None
        
        Set vertex count.


    - `getVertexCount`: getVertexCount(self: MaterialX.PyMaterialXRender.Mesh) -> int
        
        Get vertex count.


    - `setMinimumBounds`: setMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set the minimum bounds for the geometry.


    - `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for all meshes.


    - `setMaximumBounds`: setMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set the minimum bounds for the geometry.


    - `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the minimum bounds for all meshes.


    - `setSphereCenter`: setSphereCenter(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None
        
        Set center of the bounding sphere.


    - `getSphereCenter`: getSphereCenter(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3
        
        Return center of the bounding sphere.


    - `setSphereRadius`: setSphereRadius(self: MaterialX.PyMaterialXRender.Mesh, arg0: float) -> None
        
        Set radius of the bounding sphere.


    - `getSphereRadius`: getSphereRadius(self: MaterialX.PyMaterialXRender.Mesh) -> float
        
        Return radius of the bounding sphere.


    - `getPartitionCount`: getPartitionCount(self: MaterialX.PyMaterialXRender.Mesh) -> int
        
        Return the number of mesh partitions.


    - `addPartition`: addPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None
        
        Add a partition.


    - `getPartition`: getPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> MaterialX.PyMaterialXRender.MeshPartition
        
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


- **MeshPartition**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.MeshPartition


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None
        
        Resize data to the given number of indices.


    - `setName`: setName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None
        
        Set the element's name string.


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshPartition) -> str
        
        Return the ColorManagementSystem name.


    - `addSourceName`: addSourceName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None
        
        Add a source name, representing a partition that was processed to generate this one.


    - `getSourceNames`: getSourceNames(self: MaterialX.PyMaterialXRender.MeshPartition) -> set[str]
        
        Return the vector of source names, representing all partitions that were processed to generate this one.


    - `getIndices`: getIndices(self: MaterialX.PyMaterialXRender.MeshPartition) -> list[int]
        
        Return indexing.


    - `getFaceCount`: getFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition) -> int
        
        Return number of faces.


    - `setFaceCount`: setFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None
        
        Set face count.


- **MeshStream**: 

  - Methods:

    - `create`: create(arg0: str, arg1: str, arg2: int) -> MaterialX.PyMaterialXRender.MeshStream


    - `reserve`: reserve(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None
        
        Reserve memory for a given number of elements.


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None
        
        Resize data to the given number of indices.


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshStream) -> str
        
        Return the ColorManagementSystem name.


    - `getType`: getType(self: MaterialX.PyMaterialXRender.MeshStream) -> str
        
        Get stream attribute name.


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Return the index string of this element.


    - `getData`: getData(self: MaterialX.PyMaterialXRender.MeshStream) -> list[float]
        
        Return the raw float vector.


    - `getStride`: getStride(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Get stride between elements.


    - `setStride`: setStride(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None
        
        Set stride between elements.


    - `getSize`: getSize(self: MaterialX.PyMaterialXRender.MeshStream) -> int
        
        Get the number of elements.


    - `transform`: transform(self: MaterialX.PyMaterialXRender.MeshStream, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None
        
        Transform elements by a matrix.


  - Attributes: POSITION_ATTRIBUTE, NORMAL_ATTRIBUTE, TEXCOORD_ATTRIBUTE, TANGENT_ATTRIBUTE, BITANGENT_ATTRIBUTE, COLOR_ATTRIBUTE, GEOMETRY_PROPERTY_ATTRIBUTE

- **ShaderRenderer**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXRender.ShaderRenderer, renderContextHandle: capsule = None) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


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
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.
        
        2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: dict[str, str]) -> None
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None
        
        Validate inputs for the program.


    - `updateUniform`: updateUniform(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None
        
        Update the program with value of the uniform.


    - `setSize`: setSize(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: int, arg1: int) -> None
        
        Set the size of the rendered image.


    - `render`: render(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None
        
        Render the current program to an offscreen buffer.


- **StbImageLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.StbImageLoader


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool
        
        Save image to disk.
        
        Args:
            filePath: File path to be written
            image: The image to be saved
            verticalFlip: Whether the image should be flipped in Y during save
        
        Returns:
            if save succeeded


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image


- **TinyObjLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.TinyObjLoader


    - `load`: load(self: MaterialX.PyMaterialXRender.TinyObjLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool
        
        Load geometry from file path.



### Functions

- `createImageStrip`: createImageStrip(arg0: list[MaterialX.PyMaterialXRender.Image]) -> MaterialX.PyMaterialXRender.Image

- `createUniformImage`: createUniformImage(arg0: int, arg1: int, arg2: int, arg3: MaterialX.PyMaterialXRender.BaseType, arg4: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXRender.Image

- `getMaxDimensions`: getMaxDimensions(arg0: list[MaterialX.PyMaterialXRender.Image]) -> tuple[int, int]


### Globals

FLOAT, HALF, UINT16, UINT8



---

## Module: MaterialX.PyMaterialXRenderGlsl

### Classes

- **GLTextureHandler**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool
        
        Bind a single image.


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool
        
        Unbind an image.


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool
        
        Create rendering resources for the given image.


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None
        
        Release rendering resources for the given image, or for all cached images if no image pointer is specified.


- **GlslProgram**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRenderGlsl.GlslProgram


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


    - `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg2: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg3: bool) -> None
        
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


    - `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg1: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Bind attribute buffers to attribute inputs.
        
        Args:
            inputs: Attribute inputs to bind to
            mesh: Mesh containing streams to bind


    - `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None
        
        Bind a mesh partition to this material.


    - `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Mesh) -> None
        
        Bind the given mesh to this material.


    - `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None
        
        Unbind all geometry from this material.


    - `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Bind any input textures.


    - `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None
        
        Bind lights to shader.


    - `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None
        
        Bind viewing information for this material.


    - `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, time: float = 0.0, frame: float = 1.0) -> None
        
        Bind time and frame.


    - `unbind`: unbind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None
        
        Unbind the program. Equivalent to binding no program.


  - Attributes: UNDEFINED_OPENGL_RESOURCE_ID, UNDEFINED_OPENGL_PROGRAM_LOCATION

- **GlslRenderer**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.GlslRenderer


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, renderContextHandle: capsule = None) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.
        
        2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: dict[str, str]) -> None
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None
        
        Validate inputs for the program.


    - `render`: render(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None
        
        Render the current program to an offscreen buffer.


    - `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None
        
        Render the current program in texture space to an off-screen buffer.


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Capture the current contents of the off-screen hardware buffer as an image.


    - `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> MaterialX.PyMaterialXRenderGlsl.GlslProgram
        
        Return the underlying GLSL program.


- **Input**: 

  - Attributes: INVALID_OPENGL_TYPE, location, gltype, size, typeString, value, isConstant, path

- **TextureBaker**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.TextureBaker


    - `setExtension`: setExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the file extension for baked textures.


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Return the file extension of the given path.


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the element's color space string.


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Return the element's color space string.


    - `setDistanceUnit`: setDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the distance unit to which textures are baked. Defaults to meters.


    - `getDistanceUnit`: getDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Return the distance unit to which textures are baked.


    - `setAverageImages`: setAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None
        
        Set whether images should be averaged to generate constants. Defaults to false.


    - `getAverageImages`: getAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool
        
        Return whether images should be averaged to generate constants.


    - `setOptimizeConstants`: setOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None
        
        Set whether uniform textures should be stored as constants. Defaults to true.


    - `getOptimizeConstants`: getOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool
        
        Return whether uniform textures should be stored as constants.


    - `setOutputImagePath`: setOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Set the output location for baked texture images.
        
        Defaults to the root folder of the destination material.


    - `getOutputImagePath`: getOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXFormat.FilePath
        
        Get the current output location for baked texture images.


    - `setBakedGraphName`: setBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the name of the baked graph element.


    - `getBakedGraphName`: getBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Return the name of the baked graph element.


    - `setBakedGeomInfoName`: setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the name of the baked geometry info element.


    - `getBakedGeomInfoName`: getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Return the name of the baked geometry info element.


    - `setTextureFilenameTemplate`: setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -> None
        
        Set the texture filename template.


    - `getTextureFilenameTemplate`: getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> str
        
        Get the texture filename template.


    - `setFilenameTemplateVarOverride`: setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str, arg1: str) -> None
        
        Set texFilenameOverrides if template variable exists.


    - `setHashImageNames`: setHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None
        
        Set whether to create a short name for baked images by hashing the baked image filenames This is useful for file systems which may have a maximum limit on filename size.
        
        By default names are not hashed.


    - `getHashImageNames`: getHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> bool
        
        Return whether automatic baked texture resolution is set.


    - `setTextureSpaceMin`: setTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None
        
        Set the minimum texcoords used in texture baking. Defaults to 0, 0.


    - `getTextureSpaceMin`: getTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2
        
        Return the minimum texcoords used in texture baking.


    - `setTextureSpaceMax`: setTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -> None
        
        Set the maximum texcoords used in texture baking. Defaults to 1, 1.


    - `getTextureSpaceMax`: getTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -> MaterialX.PyMaterialXCore.Vector2
        
        Return the maximum texcoords used in texture baking.


    - `setupUnitSystem`: setupUnitSystem(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -> None
        
        Set up the unit definitions to be used in baking.


    - `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document
        
        Bake material to document in memory and write baked textures to disk.


    - `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Bake materials in the given document and write them to disk.
        
        If multiple documents are written, then the given output filename will be used as a template.


    - `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None
        
        Set whether to write a separate document per material when calling bakeAllMaterials.
        
        By default separate documents are written.



---

## Module: MaterialX.PyMaterialXRenderOsl

### Classes

- **OslRenderer**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderOsl.OslRenderer


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: capsule = None) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


    - `createProgram`: createProgram(*args, **kwargs)
        Overloaded function.
        
        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.
        
        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: dict[str, str]) -> None
        
        Create GLSL program based on shader stage source code.
        
        Args:
            stages: Map of name and source code for the shader stages.


    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None
        
        Validate inputs for the program.


    - `render`: render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None
        
        Render the current program to an offscreen buffer.


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image
        
        Capture the current contents of the off-screen hardware buffer as an image.


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


    - `setShaderParameterOverrides`: setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: list[str]) -> None
        
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


  - Attributes: OSL_CLOSURE_COLOR_STRING


---

## Module: MaterialX.datatype

### Classes

- **AttributeDef**: 

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
        
        Return value string.


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None
        
        Set the exportable boolean for the element.


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return the exportable boolean for the element.
        
        Defaults to false if exportable is not set.


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None
        
        Set the contains string for this backdrop.


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a contains string.


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str
        
        Return the contains string for this backdrop.


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the width attribute of the backdrop.


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a width attribute.


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the width attribute of the backdrop.


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the height attribute of the backdrop.


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a height attribute.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the height attribute of the backdrop.


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None
        
        Set the vector of elements that this backdrop contains.


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]
        
        Return the vector of elements that this backdrop contains.


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

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


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None
        
        Set the vector of collections that are directly included by this element.


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]
        
        Return the vector of collections that are directly included by this element.


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if the include chain for this element contains a cycle.


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool
        
        Return true if this collection and the given geometry string have any geometries in common.


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Create a deep copy of the value.


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document
        
        Create a deep copy of the value.


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
        
        Returns a nodedef for a given transform.


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


- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str
        
        Return the ColorManagementSystem name.


- **Element**: 

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
        
        Return the ColorManagementSystem name.


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


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None
        
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
        
        Return our self pointer.


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return our parent element.


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return the root element of our tree.


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document
        
        Return the root document of our tree.


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator
        
        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.
        
        Returns:
            A TreeIterator object.


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator
        
        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.
        
        Returns:
            A GraphIterator object.


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge
        
        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.
        
        Args:
            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.
        
        Returns:
            The upstream Edge, if valid, or an empty Edge object.


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int
        
        Return the number of queryable upstream edges for this element.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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
        
        Validate that the given element tree, including all descendants, is consistent with the MaterialX specification.


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


  - Attributes: NAME_ATTRIBUTE, FILE_PREFIX_ATTRIBUTE, GEOM_PREFIX_ATTRIBUTE, COLOR_SPACE_ATTRIBUTE, INHERIT_ATTRIBUTE, NAMESPACE_ATTRIBUTE, DOC_ATTRIBUTE, XPOS_ATTRIBUTE, YPOS_ATTRIBUTE

- **ElementEquivalenceOptions**: 

  - Attributes: performValueComparisons, floatFormat, floatPrecision, attributeExclusionList

- **ElementPredicate**: 

- **Exception**: 

- **ExceptionFoundCycle**: 

- **ExceptionOrphanedElement**: 

- **GenericElement**: 

  - Attributes: CATEGORY

- **GeomElement**: 

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
        
        Return the Collection, if any, with the given name.


- **GeomInfo**: 

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


  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

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
        
        Return the GeomProp, if any, with the given name.
        
        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the GeomProp, if any, with the given name.


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


  - Attributes: CATEGORY

- **GraphElement**: 

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


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None
        
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


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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


- **Implementation**: 

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
        
        Returns a nodedef for a given transform.


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the nodegraph string for the Implementation.


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a nodegraph string.


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the NodeGraph, if any, with the given name.


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

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


  - Attributes: CATEGORY

- **InterfaceElement**: 

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
        
        Add a Token to this element.
        
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
        
        Return a unique identifier for the target this generator is for.


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the version string of this interface.


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if this interface has a version string.


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the version string of this interface.


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None
        
        Set the major and minor versions as an integer pair.


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]
        
        Return the major and minor versions as an integer pair.


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None
        
        Set the default version flag of this element.


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return the default version flag of this element.


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first declaration of this interface, optionally filtered by the given target name.


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


  - Attributes: NODE_DEF_ATTRIBUTE

- **LinearUnitConverter**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter


    - `getUnitScale`: getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]
        
        Return the mappings from unit names to the scale value defined by a linear converter.


    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **Look**: 

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


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return a vector of all Look elements in the document.


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set comma-separated list of looks.


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return the active look, if any.


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set the active look.


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None
        
        Set the material string for the MaterialAssign.


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return true if the given MaterialAssign has a material string.


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str
        
        Return the material string for the MaterialAssign.


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None
        
        Set the exclusive boolean for the MaterialAssign.


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return the exclusive boolean for the MaterialAssign.


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node
        
        Return the material node, if any, referenced by the MaterialAssign.


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the inverse of the matrix.


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


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the inverse of the matrix.


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return the product of this matrix and a 3D vector.


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D point.


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D direction vector.


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D normal vector.


    - `createRotationX`: createRotationX(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationY`: createRotationY(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationZ`: createRotationZ(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


  - Attributes: IDENTITY

- **MatrixBase**: 

- **Member**: 

  - Attributes: CATEGORY

- **NewlineElement**: 

  - Attributes: CATEGORY

- **Node**: 

  - Methods:

    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None
        
        Set the name of the Node connected to the given input, creating a child element for the input if needed.


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str
        
        Return the name of the Node connected to the given input.
        
        If the given input is not present, then an empty string is returned.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


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


  - Attributes: CATEGORY

- **NodeDef**: 

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


    - `getImplementation`: getImplementation(*args, **kwargs)
        Overloaded function.
        
        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.
        
        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool
        
        Return true if the given version string is compatible with this NodeDef.
        
        This may be used to test, for example, whether a NodeDef and Node may be used together.


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None
        
        Set the NodeDef element referenced by the Implementation.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


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
        
        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool
        
        Return true if a cycle exists in any upstream path from this element.


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

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
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None
        
        Set the output to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing output connection on the input will be cleared.


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output
        
        Return the output connected to the given input.
        
        If the given input is not present, then an empty OutputPtr is returned.


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

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
        
        Return the Collection, if any, with the given name.


  - Attributes: CATEGORY

- **PropertySet**: 

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


  - Attributes: CATEGORY

- **PropertySetAssign**: 

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
        
        Return the PropertySet, if any, with the given name.


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's file prefix string.


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's file prefix string.


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's geom prefix string.


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's geom prefix string.


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


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]
        
        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.
        
        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int
        
        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None
        
        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.
        
        Args:
            prune: If set to true, then the current subtree will be pruned.


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool
        
        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.


- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Set the variable semantic of this port.


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool
        
        Return true if the given TypeDef has a semantic string.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str
        
        Return the variable semantic of this port.


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


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Remove the Member, if any, with the given name.


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None
        
        Set the data type for this port.


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the given element has a type string.


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str
        
        Get stream attribute name.


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of color type.


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of multi-output type.


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef
        
        Return the TypeDef, if any, with the given name.


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


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


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str
        
        Return the unit type string.


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Add a Unit to the UnitDef.
        
        Args:
            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.
        
        Returns:
            A shared pointer to the new Unit.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Return the unit type for the value on this port.


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]
        
        Return a vector of all Unit elements in the UnitDef.


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]
        
        Return a vector of all Member elements in the TypeDef.


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return value string.


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return type string.


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the value string of an element.


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a value string.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return value string.


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
        
        Set a unit type for the value on this port.


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unit string.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type for the value on this port.


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit defined by the associated NodeDef if this element is a child of a Node.


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type string.


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        The the uniform attribute flag for this element.


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None
        
        Set the uniform attribute flag on this element.


    - `setValue`: Set the typed value of an element.


    - `getValue`: Return the typed value of an element.


    - `getDefaultValue`: Return the default value for this element.


  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

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


  - Attributes: CATEGORY

- **VariantSet**: 

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


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

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


  - Attributes: CATEGORY


### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

Create a new document of the given subclass.

Create a new Document.

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `createValueFromStrings`: Convert a MaterialX value and type strings to the corresponding
       Python value.  If the given conversion cannot be performed, then None
       is returned.

       Examples:
           createValueFromStrings('0.1', 'float') -> 0.1
           createValueFromStrings('0.1, 0.2, 0.3', 'color3') -> mx.Color3(0.1, 0.2, 0.3)

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

- `getTypeString`: Return the MaterialX type string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned.

       Examples:
           getTypeString(1.0) -> 'float'
           getTypeString(mx.Color3(1)) -> 'color3'

- `getValueString`: Return the MaterialX value string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned

       Examples:
           getValueString(0.1) -> '0.1'
           getValueString(mx.Color3(0.1, 0.2, 0.3)) -> '0.1, 0.2, 0.3'

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

Return the major and minor versions as an integer pair.

- `getVersionString`: getVersionString() -> str

Return the version string of this interface.

- `incrementName`: incrementName(arg0: str) -> str

- `isColorType`: Return True if the given type is a MaterialX color.

- `isColorValue`: Return True if the given value is a MaterialX color.

- `isValidName`: isValidName(arg0: str) -> bool

- `joinStrings`: joinStrings(arg0: list[str], arg1: str) -> str

- `parentNamePath`: parentNamePath(arg0: str) -> str

- `prettyPrint`: prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str

- `replaceSubstrings`: replaceSubstrings(arg0: str, arg1: dict[str, str]) -> str

- `splitNamePath`: splitNamePath(arg0: str) -> list[str]

- `splitString`: splitString(arg0: str, arg1: str) -> list[str]

- `stringEndsWith`: stringEndsWith(arg0: str, arg1: str) -> bool

- `stringStartsWith`: stringStartsWith(arg0: str, arg1: str) -> bool

- `stringToBoolean`: Return boolean value found in a string. Throws and exception if a boolean value could not be parsed

- `targetStringsMatch`: targetStringsMatch(arg0: str, arg1: str) -> bool


### Globals

ARRAY_PREFERRED_SEPARATOR, ARRAY_VALID_SEPARATORS, BSDF_TYPE_STRING, DEFAULT_TYPE_STRING, DISPLACEMENT_SHADER_TYPE_STRING, EDF_TYPE_STRING, FILENAME_TYPE_STRING, GEOMNAME_TYPE_STRING, GEOM_PATH_SEPARATOR, LIGHT_SHADER_TYPE_STRING, MATERIAL_TYPE_STRING, MULTI_OUTPUT_TYPE_STRING, NAME_PATH_SEPARATOR, NAME_PREFIX_SEPARATOR, NONE_TYPE_STRING, STRING_TYPE_STRING, SURFACE_MATERIAL_NODE_STRING, SURFACE_SHADER_TYPE_STRING, UDIM_SET_PROPERTY, UDIM_TOKEN, UNIVERSAL_GEOM_NAME, UV_TILE_TOKEN, VALUE_STRING_FALSE, VALUE_STRING_TRUE, VDF_TYPE_STRING, VOLUME_MATERIAL_NODE_STRING, VOLUME_SHADER_TYPE_STRING



---

## Module: MaterialX.main

### Classes

- **AttributeDef**: 

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
        
        Return value string.


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None
        
        Set the exportable boolean for the element.


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool
        
        Return the exportable boolean for the element.
        
        Defaults to false if exportable is not set.


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None
        
        Set the contains string for this backdrop.


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a contains string.


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str
        
        Return the contains string for this backdrop.


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the width attribute of the backdrop.


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a width attribute.


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the width attribute of the backdrop.


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None
        
        Set the height attribute of the backdrop.


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool
        
        Return true if this backdrop has a height attribute.


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float
        
        Return the height attribute of the backdrop.


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None
        
        Set the vector of elements that this backdrop contains.


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]
        
        Return the vector of elements that this backdrop contains.


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

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


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None
        
        Set the vector of collections that are directly included by this element.


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]
        
        Return the vector of collections that are directly included by this element.


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool
        
        Return true if the include chain for this element contains a cycle.


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool
        
        Return true if this collection and the given geometry string have any geometries in common.


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Create a deep copy of the value.


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3
        
        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None
        
        Initialize with the given implementation element.
        
        Initialization must set the name and hash for the implementation, as well as any other data needed to emit code for the node.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document
        
        Create a deep copy of the value.


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
        
        Returns a nodedef for a given transform.


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


- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str
        
        Return the ColorManagementSystem name.


- **Element**: 

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
        
        Return the ColorManagementSystem name.


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


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None
        
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
        
        Return our self pointer.


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return our parent element.


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element
        
        Return the root element of our tree.


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document
        
        Return the root document of our tree.


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator
        
        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.
        
        Returns:
            A TreeIterator object.


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator
        
        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.
        
        Returns:
            A GraphIterator object.


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge
        
        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.
        
        Args:
            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.
        
        Returns:
            The upstream Edge, if valid, or an empty Edge object.


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int
        
        Return the number of queryable upstream edges for this element.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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
        
        Validate that the given element tree, including all descendants, is consistent with the MaterialX specification.


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


  - Attributes: NAME_ATTRIBUTE, FILE_PREFIX_ATTRIBUTE, GEOM_PREFIX_ATTRIBUTE, COLOR_SPACE_ATTRIBUTE, INHERIT_ATTRIBUTE, NAMESPACE_ATTRIBUTE, DOC_ATTRIBUTE, XPOS_ATTRIBUTE, YPOS_ATTRIBUTE

- **ElementEquivalenceOptions**: 

  - Attributes: performValueComparisons, floatFormat, floatPrecision, attributeExclusionList

- **ElementPredicate**: 

- **Exception**: 

- **ExceptionFileMissing**: 

- **ExceptionFoundCycle**: 

- **ExceptionOrphanedElement**: 

- **ExceptionParseError**: 

- **FilePath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FilePath, format: MaterialX.PyMaterialXFormat.Format = <Format.FormatWindows: 0>) -> str
        
        Return a single-line description of this element, including its category, name, and attributes.


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


    - `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]
        
        Return a vector of all directories at or beneath the given path.


    - `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Create a directory on the file system at the given path.


    - `getCurrentPath`: getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath


    - `getModulePath`: getModulePath() -> MaterialX.PyMaterialXFormat.FilePath


- **FileSearchPath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ';') -> str
        
        Return a single-line description of this element, including its category, name, and attributes.


    - `append`: append(*args, **kwargs)
        Overloaded function.
        
        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Append the given search path to the sequence.
        
        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Append the given search path to the sequence.


    - `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None
        
        Prepend the given path to the sequence.


    - `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None
        
        Clear all paths from the sequence.


    - `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int
        
        Return the number of strings in the path.


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool
        
        Return true if the given path is empty.


    - `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath
        
        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.
        
        On success, the combined path is returned; otherwise the original filename is returned unmodified.


- **Format**: Members:

  FormatWindows

  FormatPosix

  FormatNative

  - Attributes: name, value, FormatWindows, FormatPosix, FormatNative

- **GenericElement**: 

  - Attributes: CATEGORY

- **GeomElement**: 

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
        
        Return the Collection, if any, with the given name.


- **GeomInfo**: 

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


  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

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
        
        Return the GeomProp, if any, with the given name.
        
        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str
        
        Return the GeomProp, if any, with the given name.


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


  - Attributes: CATEGORY

- **GraphElement**: 

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


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None
        
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


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the downstream element of the edge.


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the connecting element of the edge, if any.


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element
        
        Return the upstream element of the edge.


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


- **Implementation**: 

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
        
        Returns a nodedef for a given transform.


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None
        
        Set the nodegraph string for the Implementation.


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool
        
        Return true if the given Implementation has a nodegraph string.


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str
        
        Return the NodeGraph, if any, with the given name.


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

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


  - Attributes: CATEGORY

- **InterfaceElement**: 

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
        
        Add a Token to this element.
        
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
        
        Return a unique identifier for the target this generator is for.


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None
        
        Set the version string of this interface.


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return true if this interface has a version string.


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str
        
        Return the version string of this interface.


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None
        
        Set the major and minor versions as an integer pair.


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]
        
        Return the major and minor versions as an integer pair.


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None
        
        Set the default version flag of this element.


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool
        
        Return the default version flag of this element.


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the first declaration of this interface, optionally filtered by the given target name.


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


  - Attributes: NODE_DEF_ATTRIBUTE

- **LinearUnitConverter**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.LinearUnitConverter


    - `getUnitScale`: getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -> dict[str, float]
        
        Return the mappings from unit names to the scale value defined by a linear converter.


    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **Look**: 

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


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return a vector of all Look elements in the document.


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set comma-separated list of looks.


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str
        
        Return the active look, if any.


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None
        
        Set the active look.


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None
        
        Set the material string for the MaterialAssign.


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return true if the given MaterialAssign has a material string.


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str
        
        Return the material string for the MaterialAssign.


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None
        
        Set the exclusive boolean for the MaterialAssign.


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool
        
        Return the exclusive boolean for the MaterialAssign.


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node
        
        Return the material node, if any, referenced by the MaterialAssign.


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33
        
        Return the inverse of the matrix.


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


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Create a deep copy of the value.


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool
        
        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.
        
        Args:
            rhs: Element to compare against
            options: Equivalence criteria
            message: Optional text description of differences
        
        Returns:
            True if the elements are equivalent. False otherwise.


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the transpose of the matrix.


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float
        
        Return the determinant of the matrix.


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the adjugate of the matrix.


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44
        
        Return the inverse of the matrix.


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return the product of this matrix and a 3D vector.


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D point.


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 2D direction vector.


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Transform the given 3D normal vector.


    - `createRotationX`: createRotationX(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationY`: createRotationY(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createRotationZ`: createRotationZ(arg0: float) -> MaterialX.PyMaterialXCore.Matrix44


  - Attributes: IDENTITY

- **MatrixBase**: 

- **Member**: 

  - Attributes: CATEGORY

- **NewlineElement**: 

  - Attributes: CATEGORY

- **Node**: 

  - Methods:

    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -> None
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None
        
        Set the name of the Node connected to the given input, creating a child element for the input if needed.


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str
        
        Return the name of the Node connected to the given input.
        
        If the given input is not present, then an empty string is returned.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


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


  - Attributes: CATEGORY

- **NodeDef**: 

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


    - `getImplementation`: getImplementation(*args, **kwargs)
        Overloaded function.
        
        1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.
        
        2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement
        
        Return the Implementation, if any, with the given name.


    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool
        
        Return true if the given version string is compatible with this NodeDef.
        
        This may be used to test, for example, whether a NodeDef and Node may be used together.


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]
        
        Return material-type outputs for all nodegraphs in the document.


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None
        
        Set the NodeDef element referenced by the Implementation.


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef
        
        Returns a nodedef for a given transform.


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
        
        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool
        
        Return true if a cycle exists in any upstream path from this element.


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

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
        
        Set the node to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing node connection on the input will be cleared.


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node
        
        Return the node, if any, to which this input is connected.


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None
        
        Set the output to which the given input is connected, creating a child input if needed.
        
        If the node argument is null, then any existing output connection on the input will be cleared.


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output
        
        Return the output connected to the given input.
        
        If the given input is not present, then an empty OutputPtr is returned.


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

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
        
        Return the Collection, if any, with the given name.


  - Attributes: CATEGORY

- **PropertySet**: 

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


  - Attributes: CATEGORY

- **PropertySetAssign**: 

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
        
        Return the PropertySet, if any, with the given name.


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's file prefix string.


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's file prefix string.


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None
        
        Set the element's geom prefix string.


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str
        
        Return the element's geom prefix string.


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


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]
        
        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.
        
        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int
        
        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None
        
        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.
        
        Args:
            prune: If set to true, then the current subtree will be pruned.


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool
        
        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.


- **Type**: Members:

  TypeRelative

  TypeAbsolute

  TypeNetwork

  - Attributes: name, value, TypeRelative, TypeAbsolute, TypeNetwork

- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Set the variable semantic of this port.


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool
        
        Return true if the given TypeDef has a semantic string.


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str
        
        Return the variable semantic of this port.


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


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None
        
        Remove the Member, if any, with the given name.


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None
        
        Set the data type for this port.


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the given element has a type string.


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str
        
        Get stream attribute name.


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of color type.


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool
        
        Return true if the element is of multi-output type.


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef
        
        Return the TypeDef, if any, with the given name.


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4
        
        Return the raw float vector.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str
        
        Return value string.


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: convert(*args, **kwargs)
        Overloaded function.
        
        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value
        
        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4
        
        Convert a given value in a given unit to a desired unit.
        
        Args:
            input: Input value to convert
            inputUnit: Unit of input value
            outputUnit: Unit for output value


    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int
        
        Given a unit name return a value that it can map to as an integer.
        
        Returns -1 value if not found


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str
        
        Given an integer index return the unit name in the map used by the converter.
        
        Returns Empty string if not found


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


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


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str
        
        Return the unit type string.


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Add a Unit to the UnitDef.
        
        Args:
            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.
        
        Returns:
            A shared pointer to the new Unit.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit
        
        Return the unit type for the value on this port.


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]
        
        Return a vector of all Unit elements in the UnitDef.


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]
        
        Return a vector of all Member elements in the TypeDef.


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return value string.


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str
        
        Return type string.


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the value string of an element.


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a value string.


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return value string.


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
        
        Set a unit type for the value on this port.


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unit string.


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type for the value on this port.


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit defined by the associated NodeDef if this element is a child of a Node.


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None
        
        Set the element's unittype string.


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        Return true if the given element has a unittype string.


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str
        
        Return the unit type string.


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool
        
        The the uniform attribute flag for this element.


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None
        
        Set the uniform attribute flag on this element.


    - `setValue`: Set the typed value of an element.


    - `getValue`: Return the typed value of an element.


    - `getDefaultValue`: Return the default value for this element.


  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

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


  - Attributes: CATEGORY

- **VariantSet**: 

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


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Create a deep copy of the value.


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3
        
        Return the cross product of two vectors.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the magnitude of the vector.


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Return a normalized version of the given path, collapsing current path and parent path references so that 'a/.
        
        /b' and 'c/../d/../a/b' become 'a/b'.


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float
        
        Return the dot product of two vectors.


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4
        
        Create a deep copy of the value.


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

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


  - Attributes: CATEGORY

- **XmlReadOptions**: 

  - Attributes: readXIncludeFunction, readComments, readNewlines, upgradeVersion, parentXIncludes

- **XmlWriteOptions**: 

  - Attributes: writeXIncludeEnable, elementPredicate


### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

Create a new document of the given subclass.

Create a new Document.

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `createValueFromStrings`: Convert a MaterialX value and type strings to the corresponding
       Python value.  If the given conversion cannot be performed, then None
       is returned.

       Examples:
           createValueFromStrings('0.1', 'float') -> 0.1
           createValueFromStrings('0.1, 0.2, 0.3', 'color3') -> mx.Color3(0.1, 0.2, 0.3)

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A36D1230>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

- `getDefaultDataLibraryFolders`: Return list of default data library folders

- `getDefaultDataSearchPath`: Return the default data search path.

- `getEnvironmentPath`: getEnvironmentPath(sep: str = ';') -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

- `getSourceSearchPath`: getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getSubdirectories`: getSubdirectories(arg0: list[MaterialX.PyMaterialXFormat.FilePath], arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: list[MaterialX.PyMaterialXFormat.FilePath]) -> None

- `getTypeString`: Return the MaterialX type string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned.

       Examples:
           getTypeString(1.0) -> 'float'
           getTypeString(mx.Color3(1)) -> 'color3'

- `getValueString`: Return the MaterialX value string associated with the given Python value
       If the type of the given Python value is not recognized by MaterialX,
       then None is returned

       Examples:
           getValueString(0.1) -> '0.1'
           getValueString(mx.Color3(0.1, 0.2, 0.3)) -> '0.1, 0.2, 0.3'

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

Return the major and minor versions as an integer pair.

- `getVersionString`: getVersionString() -> str

Return the version string of this interface.

- `incrementName`: incrementName(arg0: str) -> str

- `isColorType`: Return True if the given type is a MaterialX color.

- `isColorValue`: Return True if the given value is a MaterialX color.

- `isValidName`: isValidName(arg0: str) -> bool

- `joinStrings`: joinStrings(arg0: list[str], arg1: str) -> str

- `loadDocuments`: loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: set[str], includeFiles: set[str], documents: list[MaterialX.PyMaterialXCore.Document], documentsPaths: list[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: list[str] = None) -> None

- `loadLibraries`: loadLibraries(libraryFolders: list[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A3730A30>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Load a library of implementations from the provided document, replacing any previously loaded content.

- `parentNamePath`: parentNamePath(arg0: str) -> str

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `prettyPrint`: prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

- `readFromXmlFile`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A36D18F0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A36D18F0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x00000235A32B0FF0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `replaceSubstrings`: replaceSubstrings(arg0: str, arg1: dict[str, str]) -> str

- `splitNamePath`: splitNamePath(arg0: str) -> list[str]

- `splitString`: splitString(arg0: str, arg1: str) -> list[str]

- `stringEndsWith`: stringEndsWith(arg0: str, arg1: str) -> bool

- `stringStartsWith`: stringStartsWith(arg0: str, arg1: str) -> bool

- `stringToBoolean`: Return boolean value found in a string. Throws and exception if a boolean value could not be parsed

- `stringToValue`: (Deprecated) Convert a MaterialX value string and Python type to the corresponding Python value.

- `targetStringsMatch`: targetStringsMatch(arg0: str, arg1: str) -> bool

- `typeToName`: (Deprecated) Return the MaterialX type string associated with the given Python type.

- `valueToString`: (Deprecated) Convert a Python value to its corresponding MaterialX value string.

- `writeToXmlFile`: writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> None

- `writeToXmlString`: writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> str


### Globals

ARRAY_PREFERRED_SEPARATOR, ARRAY_VALID_SEPARATORS, BSDF_TYPE_STRING, DEFAULT_TYPE_STRING, DISPLACEMENT_SHADER_TYPE_STRING, EDF_TYPE_STRING, FILENAME_TYPE_STRING, GEOMNAME_TYPE_STRING, GEOM_PATH_SEPARATOR, LIGHT_SHADER_TYPE_STRING, MATERIALX_SEARCH_PATH_ENV_VAR, MATERIAL_TYPE_STRING, MULTI_OUTPUT_TYPE_STRING, NAME_PATH_SEPARATOR, NAME_PREFIX_SEPARATOR, NONE_TYPE_STRING, PATH_LIST_SEPARATOR, STRING_TYPE_STRING, SURFACE_MATERIAL_NODE_STRING, SURFACE_SHADER_TYPE_STRING, UDIM_SET_PROPERTY, UDIM_TOKEN, UNIVERSAL_GEOM_NAME, UV_TILE_TOKEN, VALUE_STRING_FALSE, VALUE_STRING_TRUE, VDF_TYPE_STRING, VOLUME_MATERIAL_NODE_STRING, VOLUME_SHADER_TYPE_STRING



---
