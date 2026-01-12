## 1. Module: MaterialX.PyMaterialXCore

### Classes

<hr><h4>1. <a id='materialx-pymaterialxcore-attributedef'>AttributeDef</a></h4>

An attribute definition element within a Document.

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setAttrName`: setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s attrname string.

- `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -&gt; bool<br>        <br>        Return true if this element has an attrname string.

- `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -&gt; str<br>        <br>        Return the element&#39;s attrname string.

- `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -&gt; None<br>        <br>        Set the value string of an element.

- `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -&gt; bool<br>        <br>        Return true if the given element has a value string.

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -&gt; str<br>        <br>        Get the value string of a element.

- `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -&gt; None<br>        <br>        Set the exportable boolean for the element.

- `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -&gt; bool<br>        <br>        Return the exportable boolean for the element.<br>        <br>        Defaults to false if exportable is not set.

##### Attributes

- `CATEGORY` = 'attributedef'
<hr><h4>2. <a id='materialx-pymaterialxcore-backdrop'>Backdrop</a></h4>

A layout element used to contain, group and document nodes within a graph.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -&gt; None<br>        <br>        Set the contains string for this backdrop.

- `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; bool<br>        <br>        Return true if this backdrop has a contains string.

- `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; str<br>        <br>        Return the contains string for this backdrop.

- `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: typing.SupportsFloat) -&gt; None<br>        <br>        Set the width attribute of the backdrop.

- `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; bool<br>        <br>        Return true if this backdrop has a width attribute.

- `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; float<br>        <br>        Return the width attribute of the backdrop.

- `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: typing.SupportsFloat) -&gt; None<br>        <br>        Set the height attribute of the backdrop.

- `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; bool<br>        <br>        Return true if this backdrop has a height attribute.

- `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; float<br>        <br>        Return the height attribute of the backdrop.

- `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.TypedElement]) -&gt; None<br>        <br>        Set the vector of elements that this backdrop contains.

- `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -&gt; list[MaterialX.PyMaterialXCore.TypedElement]<br>        <br>        Return the vector of elements that this backdrop contains.

##### Attributes

- `CATEGORY` = 'backdrop'
- `CONTAINS_ATTRIBUTE` = 'contains'
- `WIDTH_ATTRIBUTE` = 'width'
- `HEIGHT_ATTRIBUTE` = 'height'
<hr><h4>3. <a id='materialx-pymaterialxcore-collection'>Collection</a></h4>

A collection element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -&gt; None<br>        <br>        Set the include geometry string of this element.

- `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -&gt; bool<br>        <br>        Return true if this element has an include geometry string.

- `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -&gt; str<br>        <br>        Return the include geometry string of this element.

- `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -&gt; None<br>        <br>        Set the exclude geometry string of this element.

- `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -&gt; bool<br>        <br>        Return true if this element has an exclude geometry string.

- `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -&gt; str<br>        <br>        Return the exclude geometry string of this element.

- `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -&gt; None<br>        <br>        Set the include collection string of this element.

- `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -&gt; bool<br>        <br>        Return true if this element has an include collection string.

- `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -&gt; str<br>        <br>        Return the include collection string of this element.

- `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -&gt; None<br>        <br>        Set the collection that is directly included by this element.

- `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Collection]) -&gt; None<br>        <br>        Set the vector of collections that are directly included by this element.

- `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -&gt; list[MaterialX.PyMaterialXCore.Collection]<br>        <br>        Return the vector of collections that are directly included by this element.

- `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -&gt; bool<br>        <br>        Return true if the include chain for this element contains a cycle.

- `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -&gt; bool<br>        <br>        Return true if this collection and the given geometry string have any geometries in common.

##### Attributes

- `CATEGORY` = 'collection'
<hr><h4>4. <a id='materialx-pymaterialxcore-color3'>Color3</a></h4>

A three-component color value.

##### Inheritance
- [VectorBase](#materialx-pymaterialxcore-vectorbase)
##### Methods

- `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -&gt; float

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -&gt; MaterialX.PyMaterialXCore.Color3

- `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -&gt; float

- `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -&gt; MaterialX.PyMaterialXCore.Color3

- `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -&gt; MaterialX.PyMaterialXCore.Color3<br>        <br>        Transform the given color from linear RGB to the sRGB encoding, returning the result as a new value.

- `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -&gt; MaterialX.PyMaterialXCore.Color3<br>        <br>        Transform the given color from the sRGB encoding to linear RGB, returning the result as a new value.

- `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -&gt; tuple[float, float, float]

<hr><h4>5. <a id='materialx-pymaterialxcore-color4'>Color4</a></h4>

A four-component color value.

##### Inheritance
- [VectorBase](#materialx-pymaterialxcore-vectorbase)
##### Methods

- `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -&gt; float

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -&gt; MaterialX.PyMaterialXCore.Color4

- `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -&gt; float

- `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -&gt; MaterialX.PyMaterialXCore.Color4

- `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -&gt; tuple[float, float, float, float]

<hr><h4>6. <a id='materialx-pymaterialxcore-commentelement'>CommentElement</a></h4>

An element representing a block of descriptive text within a document, which will be stored a comment when the document is written out.

The comment text may be accessed with the methods Element::setDocString and Element::getDocString.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'comment'
<hr><h4>7. <a id='materialx-pymaterialxcore-document'>Document</a></h4>

A MaterialX document, which represents the top-level element in the MaterialX ownership hierarchy.

Use the factory function createDocument() to create a Document instance.

##### Inheritance
- [GraphElement](#materialx-pymaterialxcore-graphelement)
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Initialize the document, removing any existing content.

- `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -&gt; MaterialX.PyMaterialXCore.Document<br>        <br>        Create a deep copy of the document.

- `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Store a reference to a data library in this document.

- `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -&gt; MaterialX.PyMaterialXCore.Document<br>        <br>        Return the data library, if any, referenced by this document.

- `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -&gt; bool<br>        <br>        Return true if this document has a data library.

- `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Import the given data library into this document.<br>        <br>        Args:<br>            library: The data library to be imported.

- `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -&gt; set[str]<br>        <br>        Get a list of source URIs referenced by the document.

- `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.NodeGraph<br>        <br>        Add a NodeGraph to the document.<br>        <br>        Args:<br>            name: The name of the new NodeGraph. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new NodeGraph.

- `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.NodeGraph<br>        <br>        Return the NodeGraph, if any, with the given name.

- `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.NodeGraph]<br>        <br>        Return a vector of all NodeGraph elements in the document.

- `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the NodeGraph, if any, with the given name.

- `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; list[MaterialX.PyMaterialXCore.PortElement]<br>        <br>        Return a vector of all port elements that match the given node name.<br>        <br>        Port elements support spatially-varying upstream connections to nodes, and include both Input and Output elements.

- `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;, geom: str = &#39;/&#39;) -&gt; MaterialX.PyMaterialXCore.GeomInfo<br>        <br>        Add a GeomInfo to the document.<br>        <br>        Args:<br>            name: The name of the new GeomInfo. If no name is specified, then a unique name will automatically be generated.<br>            geom: An optional geometry string for the GeomInfo.<br>        <br>        Returns:<br>            A shared pointer to the new GeomInfo.

- `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.GeomInfo<br>        <br>        Return the GeomInfo, if any, with the given name.

- `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.GeomInfo]<br>        <br>        Return a vector of all GeomInfo elements in the document.

- `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the GeomInfo, if any, with the given name.

- `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = &#39;/&#39;) -&gt; MaterialX.PyMaterialXCore.Value<br>        <br>        Return the value of a geometric property for the given geometry string.

- `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -&gt; MaterialX.PyMaterialXCore.GeomPropDef<br>        <br>        Add a GeomPropDef to the document.<br>        <br>        Args:<br>            name: The name of the new GeomPropDef.<br>            geomprop: The geometric property to use for the GeomPropDef.<br>        <br>        Returns:<br>            A shared pointer to the new GeomPropDef.

- `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.GeomPropDef<br>        <br>        Return the GeomPropDef, if any, with the given name.

- `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.GeomPropDef]<br>        <br>        Return a vector of all GeomPropDef elements in the document.

- `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the GeomPropDef, if any, with the given name.

- `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.Output]<br>        <br>        Return material-type outputs for all nodegraphs in the document.

- `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Look<br>        <br>        Add a Look to the document.<br>        <br>        Args:<br>            name: The name of the new Look. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Look.

- `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.Look<br>        <br>        Return the Look, if any, with the given name.

- `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.Look]<br>        <br>        Return a vector of all Look elements in the document.

- `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the Look, if any, with the given name.

- `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.LookGroup<br>        <br>        Add a LookGroup to the document.<br>        <br>        Args:<br>            name: The name of the new LookGroup. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new LookGroup.

- `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.LookGroup<br>        <br>        Return the LookGroup, if any, with the given name.

- `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.LookGroup]<br>        <br>        Return a vector of all LookGroup elements in the document.

- `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the LookGroup, if any, with the given name.

- `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Collection<br>        <br>        Add a Collection to the document.<br>        <br>        Args:<br>            name: The name of the new Collection. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Collection.

- `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.Collection<br>        <br>        Return the Collection, if any, with the given name.

- `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.Collection]<br>        <br>        Return a vector of all Collection elements in the document.

- `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the Collection, if any, with the given name.

- `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.TypeDef<br>        <br>        Add a TypeDef to the document.<br>        <br>        Args:<br>            name: The name of the new TypeDef. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new TypeDef.

- `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.TypeDef<br>        <br>        Return the TypeDef, if any, with the given name.

- `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.TypeDef]<br>        <br>        Return a vector of all TypeDef elements in the document.

- `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the TypeDef, if any, with the given name.

- `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;, type: str = &#39;color3&#39;, node: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        Add a NodeDef to the document.<br>        <br>        Args:<br>            name: The name of the new NodeDef. If no name is specified, then a unique name will automatically be generated.<br>            type: An optional type string. If specified, then the new NodeDef will be assigned an Output of the given type.<br>            node: An optional node string.<br>        <br>        Returns:<br>            A shared pointer to the new NodeDef.

- `addNodeDefFromGraph`: addNodeDefFromGraph(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -&gt; MaterialX.PyMaterialXCore.NodeDef

- `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        Return the NodeDef, if any, with the given name.

- `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.NodeDef]<br>        <br>        Return a vector of all NodeDef elements in the document.

- `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the NodeDef, if any, with the given name.

- `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; list[MaterialX.PyMaterialXCore.NodeDef]<br>        <br>        Return a vector of all NodeDef elements that match the given node name.

- `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.AttributeDef<br>        <br>        Add an AttributeDef to the document.<br>        <br>        Args:<br>            name: The name of the new AttributeDef. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new AttributeDef.

- `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.AttributeDef<br>        <br>        Return the AttributeDef, if any, with the given name.

- `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.AttributeDef]<br>        <br>        Return a vector of all AttributeDef elements in the document.

- `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the AttributeDef, if any, with the given name.

- `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.TargetDef<br>        <br>        Add an TargetDef to the document.<br>        <br>        Args:<br>            name: The name of the new TargetDef. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new TargetDef.

- `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.TargetDef<br>        <br>        Return the AttributeDef, if any, with the given name.

- `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.TargetDef]<br>        <br>        Return a vector of all TargetDef elements in the document.

- `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the TargetDef, if any, with the given name.

- `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.PropertySet<br>        <br>        Add a PropertySet to the document.<br>        <br>        Args:<br>            name: The name of the new PropertySet. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new PropertySet.

- `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.PropertySet<br>        <br>        Return the PropertySet, if any, with the given name.

- `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.PropertySet]<br>        <br>        Return a vector of all PropertySet elements in the document.

- `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the PropertySet, if any, with the given name.

- `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.VariantSet<br>        <br>        Add a VariantSet to the document.<br>        <br>        Args:<br>            name: The name of the new VariantSet. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new VariantSet.

- `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.VariantSet<br>        <br>        Return the VariantSet, if any, with the given name.

- `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.VariantSet]<br>        <br>        Return a vector of all VariantSet elements in the document.

- `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the VariantSet, if any, with the given name.

- `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Implementation<br>        <br>        Add an Implementation to the document.<br>        <br>        Args:<br>            name: The name of the new Implementation. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Implementation.

- `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.Implementation<br>        <br>        Return the Implementation, if any, with the given name.

- `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.Implementation]<br>        <br>        Return a vector of all Implementation elements in the document.

- `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the Implementation, if any, with the given name.

- `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; list[MaterialX.PyMaterialXCore.InterfaceElement]<br>        <br>        Return a vector of all node implementations that match the given NodeDef string.<br>        <br>        Note that a node implementation may be either an Implementation element or NodeGraph element.

- `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.UnitDef

- `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.UnitDef<br>        <br>        Return the UnitDef, if any, with the given name.

- `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.UnitDef]<br>        <br>        Return a vector of all Member elements in the TypeDef.

- `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the UnitDef, if any, with the given name.

- `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.UnitTypeDef

- `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; MaterialX.PyMaterialXCore.UnitTypeDef<br>        <br>        Return the UnitTypeDef, if any, with the given name.

- `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXCore.UnitTypeDef]<br>        <br>        Return a vector of all UnitTypeDef elements in the document.

- `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Remove the UnitTypeDef, if any, with the given name.

- `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Upgrade the content of this document from earlier supported versions to the library version.

- `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Set the color management system string.

- `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -&gt; bool<br>        <br>        Return true if a color management system string has been set.

- `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -&gt; str<br>        <br>        Return the color management system string.

- `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -&gt; None<br>        <br>        Set the color management config string.

- `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -&gt; bool<br>        <br>        Return true if a color management config string has been set.

- `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -&gt; str<br>        <br>        Return the color management config string.

- `addMaterial`: (Deprecated) Add a material element to the document.

- `getMaterials`: (Deprecated) Return a vector of all materials in the document.

<hr><h4>8. <a id='materialx-pymaterialxcore-edge'>Edge</a></h4>

An edge between two connected Elements, returned during graph traversal.

##### Methods

- `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the downstream element of the edge.

- `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the connecting element of the edge, if any.

- `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the upstream element of the edge.

- `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -&gt; str<br>        <br>        Return the name of this edge, if any.

<hr><h4>9. <a id='materialx-pymaterialxcore-element'>Element</a></h4>

The base class for MaterialX elements.

An Element is a named object within a Document, which may possess any number of child elements and attributes.

##### Methods

- `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -&gt; tuple[bool, str]<br>        <br>        Return true if the given element tree, including all descendents, is considered to be equivalent to this one based on the equivalence criteria provided.<br>        <br>        Args:<br>            rhs: Element to compare against<br>            options: Equivalence criteria<br>            message: Optional text description of differences<br>        <br>        Returns:<br>            True if the elements are equivalent. False otherwise.

- `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s category string.

- `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s category string.<br>        <br>        The category of a MaterialX element represents its role within the document, with common examples being &quot;material&quot;, &quot;nodegraph&quot;, and &quot;image&quot;.

- `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s name string.

- `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s name string.

- `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -&gt; str<br>        <br>        Return the element&#39;s hierarchical name path, relative to the root document.<br>        <br>        Args:<br>            relativeTo: If a valid ancestor element is specified, then the returned path will be relative to this ancestor.

- `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the element specified by the given hierarchical name path, relative to the current element.<br>        <br>        Args:<br>            namePath: The relative name path of the specified element.

- `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s file prefix string.

- `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if the given element has a file prefix string.

- `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s file prefix string.

- `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the file prefix string that is active at the scope of this element, taking all ancestor elements into account.

- `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s geom prefix string.

- `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if the given element has a geom prefix string.

- `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s geom prefix string.

- `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the geom prefix string that is active at the scope of this element, taking all ancestor elements into account.

- `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s color space string.

- `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if the given element has a color space string.

- `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s color space string.

- `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the color space string that is active at the scope of this element, taking all ancestor elements into account.

- `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the inherit string of this element.

- `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if this element has an inherit string.

- `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the inherit string of this element.

- `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -&gt; None<br>        <br>        Set the element that this one directly inherits from.

- `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the element, if any, that this one directly inherits from.

- `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if this element has the given element as an inherited base, taking the full inheritance chain into account.

- `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if the inheritance chain for this element contains a cycle.

- `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the namespace string of this element.

- `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if this element has a namespace string.

- `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the namespace string of this element.

- `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; str<br>        <br>        Return a qualified version of the given name, taking the namespace at the scope of this element into account.

- `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the documentation string of this element.

- `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the documentation string of this element.

- `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Add a child element of the given category and name.<br>        <br>        Args:<br>            category: The category string of the new child element. If the category string is recognized, then the corresponding Element subclass is generated; otherwise, a GenericElement is generated.<br>            name: The name of the new child element. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new child element.

- `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Change the category of the given child element.<br>        <br>        Args:<br>            child: The child element that will be modified.<br>            category: The new category string for the child element.<br>        <br>        Returns:<br>            A shared pointer to a new child element, containing the contents of the original child but with a new category and subclass.

- `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -&gt; list[MaterialX.PyMaterialXCore.Element]<br>        <br>        Return a constant vector of all child elements.<br>        <br>        The returned vector maintains the order in which children were added.

- `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: typing.SupportsInt) -&gt; None<br>        <br>        Set the index of the child, if any, with the given name.<br>        <br>        If the given index is out of bounds, then an exception is thrown.

- `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; int<br>        <br>        Return the index of the child, if any, with the given name.<br>        <br>        If no child with the given name is found, then -1 is returned.

- `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Remove the child element, if any, with the given name.

- `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -&gt; None<br>        <br>        Set the value string of the given attribute.

- `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; bool<br>        <br>        Return true if the given attribute is present.

- `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; str<br>        <br>        Return the value string of the given attribute.<br>        <br>        If the given attribute is not present, then an empty string is returned.

- `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -&gt; list[str]<br>        <br>        Return a vector of stored attribute names, in the order they were set.

- `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Remove the given attribute, if present.

- `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX.PyMaterialXCore.Element

- `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX.PyMaterialXCore.Element

- `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX.PyMaterialXCore.Element

- `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX_v1_39_5::Document

- `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX_v1_39_5::TreeIterator<br>        <br>        Traverse the tree from the given element to each of its descendants in depth-first order, using pre-order visitation.<br>        <br>        Returns:<br>            A TreeIterator object.

- `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX_v1_39_5::GraphIterator<br>        <br>        Traverse the dataflow graph from the given element to each of its upstream sources in depth-first order, using pre-order visitation.<br>        <br>        Returns:<br>            A GraphIterator object.

- `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: typing.SupportsInt = 0) -&gt; MaterialX_v1_39_5::Edge<br>        <br>        Return the Edge with the given index that lies directly upstream from this element in the dataflow graph.<br>        <br>        Args:<br>            index: An optional index of the edge to be returned, where the valid index range may be determined with getUpstreamEdgeCount.<br>        <br>        Returns:<br>            The upstream Edge, if valid, or an empty Edge object.

- `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -&gt; int<br>        <br>        Return the number of queryable upstream edges for this element.

- `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: typing.SupportsInt = 0) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the Element with the given index that lies directly upstream from this one in the dataflow graph.<br>        <br>        Args:<br>            index: An optional index of the element to be returned, where the valid index range may be determined with getUpstreamEdgeCount.<br>        <br>        Returns:<br>            The upstream Element, if valid, or an empty ElementPtr.

- `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -&gt; MaterialX_v1_39_5::InheritanceIterator<br>        <br>        Traverse the inheritance chain from the given element to each element from which it inherits.<br>        <br>        Returns:<br>            An InheritanceIterator object.

- `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s source URI.<br>        <br>        Args:<br>            sourceUri: A URI string representing the resource from which this element originates. This string may be used by serialization and deserialization routines to maintain hierarchies of include references.

- `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -&gt; bool<br>        <br>        Return true if this element has a source URI.

- `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the element&#39;s source URI.

- `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return the source URI that is active at the scope of this element, taking all ancestor elements into account.

- `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -&gt; tuple[bool, str]<br>        <br>        Validate that the given document is consistent with the MaterialX specification.<br>        <br>        Args:<br>            message: An optional output string, to which a description of each error will be appended.<br>        <br>        Returns:<br>            True if the document passes all tests, false otherwise.

- `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -&gt; None<br>        <br>        Copy all attributes and descendants from the given element to this one.<br>        <br>        Args:<br>            source: The element from which content is copied.

- `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -&gt; None<br>        <br>        Clear all attributes and descendants from this element.

- `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -&gt; str<br>        <br>        Using the input name as a starting point, modify it to create a valid, unique name for a child element.

- `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::StringResolver<br>        <br>        Construct a StringResolver at the scope of this element.<br>        <br>        Args:<br>            geom: An optional geometry name, which will be used to select the applicable set of geometry token substitutions. By default, no geometry token substitutions are applied. If the universal geometry name &quot;/&quot; is given, then all geometry token substitutions are applied,<br>        <br>        Returns:<br>            A shared pointer to a StringResolver.

- `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -&gt; str<br>        <br>        Return a single-line description of this element, including its category, name, and attributes.

- `isA`: Return True if this element is an instance of the given subclass.<br>               If a category string is specified, then both subclass and category<br>               matches are required.

- `addChild`: Add a child element of the given subclass, name, and optional type string.

- `getChild`: Return the child element, if any, with the given name.

- `getChildOfType`: Return the child element, if any, with the given name and subclass.

- `getChildrenOfType`: Return a list of all child elements that are instances of the given type.<br>               The returned list maintains the order in which children were added.

- `removeChildOfType`: Remove the typed child element, if any, with the given name.

##### Attributes

- `NAME_ATTRIBUTE` = 'name'
- `FILE_PREFIX_ATTRIBUTE` = 'fileprefix'
- `GEOM_PREFIX_ATTRIBUTE` = 'geomprefix'
- `COLOR_SPACE_ATTRIBUTE` = 'colorspace'
- `INHERIT_ATTRIBUTE` = 'inherit'
- `NAMESPACE_ATTRIBUTE` = 'namespace'
- `DOC_ATTRIBUTE` = 'doc'
- `XPOS_ATTRIBUTE` = 'xpos'
- `YPOS_ATTRIBUTE` = 'ypos'
<hr><h4>10. <a id='materialx-pymaterialxcore-elementequivalenceoptions'>ElementEquivalenceOptions</a></h4>

A set of options for comparing the functional equivalence of elements.

##### Attributes

- `performValueComparisons` = (property)
- `floatFormat` = (property)
- `floatPrecision` = (property)
- `attributeExclusionList` = (property)
<hr><h4>11. <a id='materialx-pymaterialxcore-elementpredicate'>ElementPredicate</a></h4>



<hr><h4>12. <a id='materialx-pymaterialxcore-exception'>Exception</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxcore-exception)
- [BaseException](#materialx-pymaterialxcore-baseexception)
<hr><h4>13. <a id='materialx-pymaterialxcore-exceptionfoundcycle'>ExceptionFoundCycle</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxcore-exception)
- [BaseException](#materialx-pymaterialxcore-baseexception)
<hr><h4>14. <a id='materialx-pymaterialxcore-exceptionorphanedelement'>ExceptionOrphanedElement</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxcore-exception)
- [BaseException](#materialx-pymaterialxcore-baseexception)
<hr><h4>15. <a id='materialx-pymaterialxcore-genericelement'>GenericElement</a></h4>

A generic element subclass, for instantiating elements with unrecognized categories.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'generic'
<hr><h4>16. <a id='materialx-pymaterialxcore-geomelement'>GeomElement</a></h4>

The base class for geometric elements, which support bindings to geometries and geometric collections.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -&gt; None<br>        <br>        Set the geometry string of this element.

- `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -&gt; bool<br>        <br>        Return true if this element has a geometry string.

- `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -&gt; str<br>        <br>        Return the geometry string of this element.

- `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -&gt; None<br>        <br>        Set the collection string of this element.

- `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -&gt; bool<br>        <br>        Return true if this element has a collection string.

- `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -&gt; str<br>        <br>        Return the collection string of this element.

- `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -&gt; None<br>        <br>        Assign a Collection to this element.

- `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -&gt; MaterialX_v1_39_5::Collection<br>        <br>        Return the Collection that is assigned to this element.

<hr><h4>17. <a id='materialx-pymaterialxcore-geominfo'>GeomInfo</a></h4>

A geometry info element within a Document.

##### Inheritance
- [GeomElement](#materialx-pymaterialxcore-geomelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -&gt; MaterialX_v1_39_5::GeomProp<br>        <br>        Add a GeomProp to this element.<br>        <br>        Args:<br>            name: The name of the new GeomProp. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new GeomProp.

- `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -&gt; MaterialX_v1_39_5::GeomProp<br>        <br>        Return the GeomProp, if any, with the given name.

- `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -&gt; list[MaterialX_v1_39_5::GeomProp]<br>        <br>        Return a vector of all GeomProp elements.

- `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -&gt; None<br>        <br>        Remove the GeomProp, if any, with the given name.

- `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = &#39;color3&#39;) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Add a Token to this element.<br>        <br>        Args:<br>            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Token.

- `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Return the Token, if any, with the given name.

- `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -&gt; list[MaterialX.PyMaterialXCore.Token]<br>        <br>        Return a vector of all Token elements.

- `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -&gt; None<br>        <br>        Remove the Token, if any, with the given name.

- `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Set the string value of a Token by its name, creating a child element to hold the Token if needed.

- `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element<br>               to hold the geomprop if needed.

- `addGeomAttr`: (Deprecated) Add a geomprop to this element.

- `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.

##### Attributes

- `CATEGORY` = 'geominfo'
<hr><h4>18. <a id='materialx-pymaterialxcore-geomprop'>GeomProp</a></h4>

A geometric property element within a GeomInfo.

##### Inheritance
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'geomprop'
<hr><h4>19. <a id='materialx-pymaterialxcore-geompropdef'>GeomPropDef</a></h4>

An element representing a declaration of geometric property data.

A GeomPropDef element contains a reference to a geometric node and a set of modifiers for that node. For example, a world-space normal can be declared as a reference to the "normal" geometric node with a space setting of "world", or a specific set of texture coordinates can be declared as a reference to the "texcoord" geometric node with an index setting of "1".

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setGeomProp`: setGeomProp(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -&gt; None<br>        <br>        Set the geometric property string of this element.<br>        <br>        2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -&gt; None<br>        <br>        Set the geometric property string of this element.

- `hasGeomProp`: hasGeomProp(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; bool<br>        <br>        Return true if this element has a geometric property string.<br>        <br>        2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; bool<br>        <br>        Return true if this element has a geometric property string.

- `getGeomProp`: getGeomProp(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; str<br>        <br>        Return the geometric property string of this element.<br>        <br>        2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; str<br>        <br>        Return the geometric property string of this element.

- `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -&gt; None<br>        <br>        Set the geometric space string of this element.

- `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; bool<br>        <br>        Return true if this element has a geometric space string.

- `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; str<br>        <br>        Return the geometric space string of this element.

- `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -&gt; None<br>        <br>        Set the index string of this element.

- `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; bool<br>        <br>        Return true if this element has an index string.

- `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -&gt; str<br>        <br>        Return the index string of this element.

##### Attributes

- `CATEGORY` = 'geompropdef'
<hr><h4>20. <a id='materialx-pymaterialxcore-graphelement'>GraphElement</a></h4>

The base class for graph elements such as NodeGraph and Document.

##### Inheritance
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = &#39;&#39;, type: str = &#39;color3&#39;) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Add a Node to the graph.<br>        <br>        Args:<br>            category: The category of the new Node.<br>            name: The name of the new Node. If no name is specified, then a unique name will automatically be generated.<br>            type: An optional type string.<br>        <br>        Returns:<br>            A shared pointer to the new Node.

- `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Add a Node that is an instance of the given NodeDef.

- `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Return the Node, if any, with the given name.

- `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = &#39;&#39;) -&gt; list[MaterialX.PyMaterialXCore.Node]<br>        <br>        Return a vector of all Nodes in the graph, optionally filtered by the given category string.

- `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -&gt; None<br>        <br>        Remove the Node, if any, with the given name.

- `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = &#39;&#39;, shaderNode: MaterialX.PyMaterialXCore.Node = None) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Add a material node to the graph, optionally connecting it to the given shader node.

- `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -&gt; list[MaterialX.PyMaterialXCore.Node]<br>        <br>        Return a vector of all material nodes.

- `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::Backdrop<br>        <br>        Add a Backdrop to the graph.

- `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -&gt; MaterialX_v1_39_5::Backdrop<br>        <br>        Return the Backdrop, if any, with the given name.

- `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -&gt; list[MaterialX_v1_39_5::Backdrop]<br>        <br>        Return a vector of all Backdrop elements in the graph.

- `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -&gt; None<br>        <br>        Remove the Backdrop, if any, with the given name.

- `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = &#39;&#39;, filter: collections.abc.Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -&gt; None<br>        <br>        Flatten all subgraphs at the root scope of this graph element, recursively replacing each graph-defined node with its equivalent node network.<br>        <br>        Args:<br>            target: An optional target string to be used in specifying which node definitions are used in this process.<br>            filter: An optional node predicate specifying which nodes should be included and excluded from this process.

- `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -&gt; list[MaterialX.PyMaterialXCore.Element]<br>        <br>        Return a vector of all children (nodes and outputs) sorted in topological order.

- `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        If not yet present, add a geometry node to this graph matching the given property definition and name prefix.

- `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -&gt; str<br>        <br>        Convert this graph to a string in the DOT language syntax.<br>        <br>        This can be used to visualise the graph using GraphViz (http://www.graphviz.org).<br>        <br>        If declarations for the contained nodes are provided as nodedefs in the owning document, then they will be used to provide additional formatting details.

<hr><h4>21. <a id='materialx-pymaterialxcore-graphiterator'>GraphIterator</a></h4>

An iterator object representing the state of an upstream graph traversal.

##### Methods

- `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the downstream element of the current edge.

- `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the connecting element, if any, of the current edge.

- `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the upstream element of the current edge.

- `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; int<br>        <br>        Return the index of the current edge within the range of upstream edges available to the downstream element.

- `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; int<br>        <br>        Return the element depth of the current traversal, where a single edge between two elements represents a depth of one.

- `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; int<br>        <br>        Return the node depth of the current traversal, where a single edge between two nodes represents a depth of one.

- `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -&gt; None<br>        <br>        Set the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.<br>        <br>        Args:<br>            prune: If set to true, then the current subgraph will be pruned.

- `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -&gt; bool<br>        <br>        Return the prune subgraph flag, which controls whether the current subgraph is pruned from traversal.

<hr><h4>22. <a id='materialx-pymaterialxcore-implementation'>Implementation</a></h4>

An implementation element within a Document.

An Implementation is used to associate external source code with a specific NodeDef, providing a definition for the node that may either be universal or restricted to a specific target.

##### Inheritance
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -&gt; None<br>        <br>        Set the file string for the Implementation.

- `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -&gt; bool<br>        <br>        Return true if the given Implementation has a file string.

- `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -&gt; str<br>        <br>        Return the file string for the Implementation.

- `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -&gt; None<br>        <br>        Set the function string for the Implementation.

- `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -&gt; bool<br>        <br>        Return true if the given Implementation has a function string.

- `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -&gt; str<br>        <br>        Return the function string for the Implementation.

- `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -&gt; None<br>        <br>        Set the NodeDef element referenced by the Implementation.

- `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        Return the NodeDef element referenced by the Implementation.

- `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -&gt; None<br>        <br>        Set the nodegraph string for the Implementation.

- `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -&gt; bool<br>        <br>        Return true if the given Implementation has a nodegraph string.

- `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -&gt; str<br>        <br>        Return the nodegraph string for the Implementation.

##### Attributes

- `CATEGORY` = 'implementation'
- `FILE_ATTRIBUTE` = 'file'
- `FUNCTION_ATTRIBUTE` = 'function'
<hr><h4>23. <a id='materialx-pymaterialxcore-inheritanceiterator'>InheritanceIterator</a></h4>

An iterator object representing the current state of an inheritance traversal.

<hr><h4>24. <a id='materialx-pymaterialxcore-input'>Input</a></h4>

An input element within a Node or NodeDef.

An Input holds either a uniform value or a connection to a spatially-varying Output, either of which may be modified within the scope of a Material.

##### Inheritance
- [PortElement](#materialx-pymaterialxcore-portelement)
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -&gt; None<br>        <br>        Set the defaultgeomprop string for the input.

- `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -&gt; bool<br>        <br>        Return true if the given input has a defaultgeomprop string.

- `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -&gt; str<br>        <br>        Return the defaultgeomprop string for the input.

- `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -&gt; MaterialX_v1_39_5::GeomPropDef<br>        <br>        Return the GeomPropDef element to use, if defined for this input.

- `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -&gt; MaterialX_v1_39_5::Node<br>        <br>        Return the node, if any, to which this input is connected.

- `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -&gt; None<br>        <br>        Connects this input to a corresponding interface with the given name.<br>        <br>        If the interface name specified is an empty string then any existing connection is removed.

- `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Return the input on the parent graph corresponding to the interface name for this input.

##### Attributes

- `CATEGORY` = 'input'
<hr><h4>25. <a id='materialx-pymaterialxcore-interfaceelement'>InterfaceElement</a></h4>

The base class for interface elements such as Node, NodeDef, and NodeGraph.

An InterfaceElement supports a set of Input and Output elements, with an API for setting their values.

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Set the NodeDef string for the interface.

- `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; bool<br>        <br>        Return true if the given interface has a NodeDef string.

- `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; str<br>        <br>        Return the NodeDef string for the interface.

- `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = &#39;&#39;, type: str = &#39;color3&#39;) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Add an Input to this interface.<br>        <br>        Args:<br>            name: The name of the new Input. If no name is specified, then a unique name will automatically be generated.<br>            type: An optional type string.<br>        <br>        Returns:<br>            A shared pointer to the new Input.

- `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Return the Input, if any, with the given name.

- `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Input]<br>        <br>        Return a vector of all Input elements.

- `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; int<br>        <br>        Return the number of Input elements.

- `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Remove the Input, if any, with the given name.

- `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Return the first Input with the given name that belongs to this interface, taking interface inheritance into account.

- `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Input]<br>        <br>        Return a vector of all Input elements that belong to this interface, taking inheritance into account.

- `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = &#39;&#39;, type: str = &#39;color3&#39;) -&gt; MaterialX.PyMaterialXCore.Output<br>        <br>        Add an Output to this interface.<br>        <br>        Args:<br>            name: The name of the new Output. If no name is specified, then a unique name will automatically be generated.<br>            type: An optional type string.<br>        <br>        Returns:<br>            A shared pointer to the new Output.

- `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Output<br>        <br>        Return the Output, if any, with the given name.

- `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Output]<br>        <br>        Return a vector of all Output elements.

- `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; int<br>        <br>        Return the number of Output elements.

- `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Remove the Output, if any, with the given name.

- `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Output<br>        <br>        Return the first Output with the given name that belongs to this interface, taking interface inheritance into account.

- `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Output]<br>        <br>        Return a vector of all Output elements that belong to this interface, taking inheritance into account.

- `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -&gt; None<br>        <br>        Set the output to which the given input is connected, creating a child input if needed.<br>        <br>        If the node argument is null, then any existing output connection on the input will be cleared.

- `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Output<br>        <br>        Return the output connected to the given input.<br>        <br>        If the given input is not present, then an empty OutputPtr is returned.

- `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = &#39;color3&#39;) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Add a Token to this interface.<br>        <br>        Args:<br>            name: The name of the new Token. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Token.

- `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Return the Token, if any, with the given name.

- `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Token]<br>        <br>        Return a vector of all Token elements.

- `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Remove the Token, if any, with the given name.

- `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Return the first Token with the given name that belongs to this interface, taking interface inheritance into account.

- `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.Token]<br>        <br>        Return a vector of all Token elements that belong to this interface, taking inheritance into account.

- `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; MaterialX.PyMaterialXCore.ValueElement<br>        <br>        Return the first value element with the given name that belongs to this interface, taking interface inheritance into account.<br>        <br>        Examples of value elements are Input, Output, and Token.

- `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; list[MaterialX.PyMaterialXCore.ValueElement]<br>        <br>        Return a vector of all value elements that belong to this interface, taking inheritance into account.<br>        <br>        Examples of value elements are Input, Output, and Token.

- `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -&gt; MaterialX.PyMaterialXCore.Token<br>        <br>        Set the string value of a Token by its name, creating a child element to hold the Token if needed.

- `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; str<br>        <br>        Return the string value of a Token by its name, or an empty string if the given Token is not present.

- `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Set the target string of this interface.

- `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; bool<br>        <br>        Return true if the given interface has a target string.

- `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; str<br>        <br>        Return the target string of this interface.

- `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -&gt; None<br>        <br>        Set the version string of this interface.

- `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; bool<br>        <br>        Return true if this interface has a version string.

- `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; str<br>        <br>        Return the version string of this interface.

- `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -&gt; None<br>        <br>        Set the major and minor versions as an integer pair.

- `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; tuple[int, int]<br>        <br>        Return the major and minor versions as an integer pair.

- `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -&gt; None<br>        <br>        Set the default version flag of this element.

- `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; bool<br>        <br>        Return the default version flag of this element.

- `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.InterfaceElement<br>        <br>        Return the first declaration of this interface, optionally filtered by the given target name.<br>        <br>        Args:<br>            target: An optional target name, which will be used to filter the declarations that are considered.<br>        <br>        Returns:<br>            A shared pointer to declaration, or an empty shared pointer if no declaration was found.

- `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -&gt; None<br>        <br>        Clear all attributes and descendants from this element.

- `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -&gt; bool<br>        <br>        Return true if this instance has an exact input match with the given declaration, where each input of this the instance corresponds to a declaration input of the same name and type.<br>        <br>        If an exact input match is not found, and the optional message argument is provided, then an error message will be appended to the given string.

- `setInputValue`: Set the typed value of an input by its name, creating a child element<br>               to hold the input if needed.

- `getInputValue`: Return the typed value of an input by its name, taking both the<br>               calling element and its declaration into account.  If the given<br>               input is not found, then None is returned.

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

##### Attributes

- `NODE_DEF_ATTRIBUTE` = 'nodedef'
<hr><h4>26. <a id='materialx-pymaterialxcore-linearunitconverter'>LinearUnitConverter</a></h4>

A converter class for linear units that require only a scalar multiplication.

##### Inheritance
- [UnitConverter](#materialx-pymaterialxcore-unitconverter)
##### Methods

- `create`: create(arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -&gt; MaterialX.PyMaterialXCore.LinearUnitConverter<br>        <br>        Creator.

- `getUnitScale`: getUnitScale(self: MaterialX.PyMaterialXCore.LinearUnitConverter) -&gt; dict[str, float]<br>        <br>        Return the mappings from unit names to the scale value defined by a linear converter.

- `convert`: convert(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: typing.SupportsFloat, arg1: str, arg2: str) -&gt; float<br>        <br>        2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector2<br>        <br>        3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector4

- `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -&gt; int<br>        <br>        Given a unit name return a value that it can map to as an integer.<br>        <br>        Returns -1 value if not found

- `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: typing.SupportsInt) -&gt; str<br>        <br>        Given an integer index return the unit name in the map used by the converter.<br>        <br>        Returns Empty string if not found

<hr><h4>27. <a id='materialx-pymaterialxcore-look'>Look</a></h4>

A look element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = &#39;&#39;, material: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::MaterialAssign<br>        <br>        Add a MaterialAssign to the look.<br>        <br>        Args:<br>            name: The name of the new MaterialAssign. If no name is specified, then a unique name will automatically be generated.<br>            material: An optional material string, which should match the name of the material node to be assigned.<br>        <br>        Returns:<br>            A shared pointer to the new MaterialAssign.

- `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; MaterialX_v1_39_5::MaterialAssign<br>        <br>        Return the MaterialAssign, if any, with the given name.

- `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::MaterialAssign]<br>        <br>        Return a vector of all MaterialAssign elements in the look.

- `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::MaterialAssign]<br>        <br>        Return a vector of all MaterialAssign elements that belong to this look, taking look inheritance into account.

- `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; None<br>        <br>        Remove the MaterialAssign, if any, with the given name.

- `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.PropertyAssign<br>        <br>        Add a PropertyAssign to the look.<br>        <br>        Args:<br>            name: The name of the new PropertyAssign. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new PropertyAssign.

- `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; MaterialX.PyMaterialXCore.PropertyAssign<br>        <br>        Return the PropertyAssign, if any, with the given name.

- `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX.PyMaterialXCore.PropertyAssign]<br>        <br>        Return a vector of all PropertyAssign elements in the look.

- `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX.PyMaterialXCore.PropertyAssign]<br>        <br>        Return a vector of all PropertyAssign elements that belong to this look, taking look inheritance into account.

- `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; None<br>        <br>        Remove the PropertyAssign, if any, with the given name.

- `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.PropertySetAssign<br>        <br>        Add a PropertySetAssign to the look.<br>        <br>        Args:<br>            name: The name of the new PropertySetAssign. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new PropertySetAssign.

- `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; MaterialX.PyMaterialXCore.PropertySetAssign<br>        <br>        Return the PropertySetAssign, if any, with the given name.

- `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX.PyMaterialXCore.PropertySetAssign]<br>        <br>        Return a vector of all PropertySetAssign elements in the look.

- `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX.PyMaterialXCore.PropertySetAssign]<br>        <br>        Return a vector of all PropertySetAssign elements that belong to this look, taking look inheritance into account.

- `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; None<br>        <br>        Remove the PropertySetAssign, if any, with the given name.

- `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::VariantAssign<br>        <br>        Add a VariantAssign to the look.<br>        <br>        Args:<br>            name: The name of the new VariantAssign. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new VariantAssign.

- `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; MaterialX_v1_39_5::VariantAssign<br>        <br>        Return the VariantAssign, if any, with the given name.

- `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::VariantAssign]<br>        <br>        Return a vector of all VariantAssign elements in the look.

- `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::VariantAssign]<br>        <br>        Return a vector of all VariantAssign elements that belong to this look, taking look inheritance into account.

- `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; None<br>        <br>        Remove the VariantAssign, if any, with the given name.

- `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::Visibility<br>        <br>        Add a Visibility to the look.<br>        <br>        Args:<br>            name: The name of the new Visibility. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Visibility.

- `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; MaterialX_v1_39_5::Visibility<br>        <br>        Return the Visibility, if any, with the given name.

- `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::Visibility]<br>        <br>        Return a vector of all Visibility elements in the look.

- `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -&gt; list[MaterialX_v1_39_5::Visibility]<br>        <br>        Return a vector of all Visibility elements that belong to this look, taking look inheritance into account.

- `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -&gt; None<br>        <br>        Remove the Visibility, if any, with the given name.

##### Attributes

- `CATEGORY` = 'look'
<hr><h4>28. <a id='materialx-pymaterialxcore-lookgroup'>LookGroup</a></h4>

A look group element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -&gt; str<br>        <br>        Get comma-separated list of looks.

- `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -&gt; None<br>        <br>        Set comma-separated list of looks.

- `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -&gt; str<br>        <br>        Return the active look, if any.

- `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -&gt; None<br>        <br>        Set the active look.

##### Attributes

- `CATEGORY` = 'lookgroup'
- `LOOKS_ATTRIBUTE` = 'looks'
- `ACTIVE_ATTRIBUTE` = 'active'
<hr><h4>29. <a id='materialx-pymaterialxcore-materialassign'>MaterialAssign</a></h4>

A material assignment element within a Look.

##### Inheritance
- [GeomElement](#materialx-pymaterialxcore-geomelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -&gt; None<br>        <br>        Set the material string for the MaterialAssign.

- `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -&gt; bool<br>        <br>        Return true if the given MaterialAssign has a material string.

- `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -&gt; str<br>        <br>        Return the material string for the MaterialAssign.

- `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -&gt; list[MaterialX.PyMaterialXCore.Output]<br>        <br>        Return the outputs on any referenced material.

- `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -&gt; None<br>        <br>        Set the exclusive boolean for the MaterialAssign.

- `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -&gt; bool<br>        <br>        Return the exclusive boolean for the MaterialAssign.

- `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -&gt; MaterialX_v1_39_5::Node<br>        <br>        Return the material node, if any, referenced by the MaterialAssign.

##### Attributes

- `CATEGORY` = 'materialassign'
<hr><h4>30. <a id='materialx-pymaterialxcore-matrix33'>Matrix33</a></h4>

A 3x3 matrix of floating-point values.

Vector transformation methods follow the row-vector convention, with matrix-vector multiplication computed as v' = vM.

##### Inheritance
- [MatrixBase](#materialx-pymaterialxcore-matrixbase)
##### Methods

- `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: typing.SupportsFloat) -&gt; bool

- `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -&gt; float

- `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Matrix33

- `numRows`: numRows() -&gt; int

- `numColumns`: numColumns() -&gt; int

- `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the product of this matrix and a 3D vector.

- `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Vector2<br>        <br>        Transform the given 2D point.

- `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Vector2<br>        <br>        Transform the given 2D direction vector.

- `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Transform the given 3D normal vector.

- `createRotation`: createRotation(arg0: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix33<br>        <br>        Create a rotation matrix.<br>        <br>        Args:<br>            angle: Angle in radians

##### Attributes

- `IDENTITY` = (property)
<hr><h4>31. <a id='materialx-pymaterialxcore-matrix44'>Matrix44</a></h4>

A 4x4 matrix of floating-point values.

Vector transformation methods follow the row-vector convention, with matrix-vector multiplication computed as v' = vM.

##### Inheritance
- [MatrixBase](#materialx-pymaterialxcore-matrixbase)
##### Methods

- `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: typing.SupportsFloat) -&gt; bool

- `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -&gt; float

- `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Matrix44

- `numRows`: numRows() -&gt; int

- `numColumns`: numColumns() -&gt; int

- `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -&gt; MaterialX.PyMaterialXCore.Vector4<br>        <br>        Return the product of this matrix and a 4D vector.

- `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Transform the given 3D point.

- `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Transform the given 3D direction vector.

- `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Transform the given 3D normal vector.

- `createRotationX`: createRotationX(arg0: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create a rotation matrix about the X-axis.<br>        <br>        Args:<br>            angle: Angle in radians

- `createRotationY`: createRotationY(arg0: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create a rotation matrix about the Y-axis.<br>        <br>        Args:<br>            angle: Angle in radians

- `createRotationZ`: createRotationZ(arg0: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create a rotation matrix about the Z-axis.<br>        <br>        Args:<br>            angle: Angle in radians

##### Attributes

- `IDENTITY` = (property)
<hr><h4>32. <a id='materialx-pymaterialxcore-matrixbase'>MatrixBase</a></h4>

The base class for square matrices of scalar values.

<hr><h4>33. <a id='materialx-pymaterialxcore-member'>Member</a></h4>

A member element within a TypeDef.

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'typedef'
<hr><h4>34. <a id='materialx-pymaterialxcore-newlineelement'>NewlineElement</a></h4>

An element representing a newline within a document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'newline'
<hr><h4>35. <a id='materialx-pymaterialxcore-node'>Node</a></h4>

A node element within a NodeGraph or Document.

A Node represents an instance of a NodeDef within a graph, and its Input elements apply specific values and connections to that instance.

##### Inheritance
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: MaterialX.PyMaterialXCore.Node) -&gt; None<br>        <br>        Set the node to which the given input is connected, creating a child input if needed.<br>        <br>        If the node argument is null, then any existing node connection on the input will be cleared.

- `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Return the Node connected to the given input.<br>        <br>        If the given input is not present, then an empty NodePtr is returned.

- `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -&gt; None<br>        <br>        Set the name of the Node connected to the given input, creating a child element for the input if needed.

- `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -&gt; str<br>        <br>        Return the name of the Node connected to the given input.<br>        <br>        If the given input is not present, then an empty string is returned.

- `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = &#39;&#39;, allowRoughMatch: bool = False) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        Return the first NodeDef that declares this node, optionally filtered by the given target name.<br>        <br>        Args:<br>            target: An optional target name, which will be used to filter the nodedefs that are considered.<br>            allowRoughMatch: If specified, then a rough match will be allowed when an exact match is not found. An exact match requires that each node input corresponds to a nodedef input of the same name and type.<br>        <br>        Returns:<br>            A NodeDef for this node, or an empty shared pointer if none was found.

- `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.InterfaceElement<br>        <br>        Return the first implementation for this node, optionally filtered by the given target and language names.<br>        <br>        Args:<br>            target: An optional target name, which will be used to filter the implementations that are considered.<br>        <br>        Returns:<br>            An implementation for this node, or an empty shared pointer if none was found. Note that a node implementation may be either an Implementation element or a NodeGraph element.

- `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -&gt; list[MaterialX.PyMaterialXCore.PortElement]<br>        <br>        Return a vector of all downstream ports that connect to this node, ordered by the names of the port elements.

- `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Add an input based on the corresponding input for the associated node definition.<br>        <br>        If the input already exists on the node it will just be returned.

- `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -&gt; None<br>        <br>        Add inputs based on the corresponding associated node definition.

- `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.

- `addShaderRef`: (Deprecated) Add a shader reference to this material element.

- `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.

- `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.

##### Attributes

- `CATEGORY` = 'node'
<hr><h4>36. <a id='materialx-pymaterialxcore-nodedef'>NodeDef</a></h4>

A node definition element within a Document.

A NodeDef provides the declaration of a node interface, which may then be instantiated as a Node.

##### Inheritance
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -&gt; None<br>        <br>        Set the node string of the NodeDef.

- `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -&gt; bool<br>        <br>        Return true if the given NodeDef has a node string.

- `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -&gt; str<br>        <br>        Return the node string of the NodeDef.

- `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -&gt; None<br>        <br>        Set the node group of the NodeDef.

- `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -&gt; bool<br>        <br>        Return true if the given NodeDef has a node group.

- `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -&gt; str<br>        <br>        Return the node group of the NodeDef.

- `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = &#39;&#39;, resolveNodeGraph: bool = True) -&gt; MaterialX.PyMaterialXCore.InterfaceElement<br>        <br>        Return the first implementation for this nodedef, optionally filtered by the given target name.<br>        <br>        Args:<br>            target: An optional target name, which will be used to filter the implementations that are considered.<br>            resolveNodeGraph: Allow resolution of Implementation elements to their linked NodeGraph elements. Defaults to true.<br>        <br>        Returns:<br>            An implementation for this nodedef, or an empty shared pointer if none was found. Note that a node implementation may be either an Implementation element or a NodeGraph element.

- `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -&gt; bool<br>        <br>        Return true if the given version string is compatible with this NodeDef.<br>        <br>        This may be used to test, for example, whether a NodeDef and Node may be used together.

##### Attributes

- `CATEGORY` = 'nodedef'
- `NODE_ATTRIBUTE` = 'node'
- `TEXTURE_NODE_GROUP` = 'texture'
- `PROCEDURAL_NODE_GROUP` = 'procedural'
- `GEOMETRIC_NODE_GROUP` = 'geometric'
- `ADJUSTMENT_NODE_GROUP` = 'adjustment'
- `CONDITIONAL_NODE_GROUP` = 'conditional'
- `CHANNEL_NODE_GROUP` = 'channel'
- `ORGANIZATION_NODE_GROUP` = 'organization'
- `TRANSLATION_NODE_GROUP` = 'translation'
<hr><h4>37. <a id='materialx-pymaterialxcore-nodegraph'>NodeGraph</a></h4>

A node graph element within a Document.

##### Inheritance
- [GraphElement](#materialx-pymaterialxcore-graphelement)
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -&gt; list[MaterialX.PyMaterialXCore.Output]<br>        <br>        Return all material-type outputs of the nodegraph.

- `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -&gt; None<br>        <br>        Set the NodeDef element referenced by this NodeGraph.

- `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -&gt; MaterialX.PyMaterialXCore.NodeDef<br>        <br>        Return the NodeDef element referenced by this NodeGraph.

- `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -&gt; MaterialX.PyMaterialXCore.InterfaceElement<br>        <br>        Return the first declaration of this interface, optionally filtered by the given target name.

- `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -&gt; MaterialX.PyMaterialXCore.Input<br>        <br>        Add an interface name to an existing NodeDef associated with this NodeGraph.<br>        <br>        Args:<br>            inputPath: Path to an input descendant of this graph.<br>            interfaceName: The new interface name.<br>        <br>        Returns:<br>            Interface input.

- `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -&gt; None<br>        <br>        Remove an interface name from an existing NodeDef associated with this NodeGraph.<br>        <br>        Args:<br>            inputPath: Path to an input descendant of this graph.

- `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -&gt; None<br>        <br>        Modify the interface name on an existing NodeDef associated with this NodeGraph.<br>        <br>        Args:<br>            inputPath: Path to an input descendant of this graph.<br>            interfaceName: The new interface name.

- `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -&gt; list[MaterialX.PyMaterialXCore.PortElement]<br>        <br>        Return a vector of all downstream ports that connect to this graph, ordered by the names of the port elements.

##### Attributes

- `CATEGORY` = 'nodegraph'
<hr><h4>38. <a id='materialx-pymaterialxcore-nodepredicate'>NodePredicate</a></h4>



<hr><h4>39. <a id='materialx-pymaterialxcore-output'>Output</a></h4>

A spatially-varying output element within a NodeGraph or NodeDef.

##### Inheritance
- [PortElement](#materialx-pymaterialxcore-portelement)
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -&gt; bool<br>        <br>        Return true if a cycle exists in any upstream path from this element.

##### Attributes

- `CATEGORY` = 'output'
- `DEFAULT_INPUT_ATTRIBUTE` = 'defaultinput'
<hr><h4>40. <a id='materialx-pymaterialxcore-portelement'>PortElement</a></h4>

The base class for port elements such as Input and Output.

Port elements support spatially-varying upstream connections to nodes.

##### Inheritance
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -&gt; None<br>        <br>        Set the node name string of this element, creating a connection to the Node with the given name within the same NodeGraph.

- `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -&gt; str<br>        <br>        Return the node name string of this element.

- `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -&gt; None<br>        <br>        Set the node graph string of this element.

- `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -&gt; bool<br>        <br>        Return true if this element has a node graph string.

- `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -&gt; str<br>        <br>        Return the node graph string of this element.

- `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -&gt; None<br>        <br>        Set the output string of this element.

- `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -&gt; bool<br>        <br>        Return true if this element has an output string.

- `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -&gt; str<br>        <br>        Return the output string of this element.

- `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -&gt; None<br>        <br>        Set the node to which this element is connected.<br>        <br>        The given node must belong to the same node graph. If the node argument is null, then any existing node connection will be cleared.

- `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -&gt; MaterialX_v1_39_5::Node<br>        <br>        Return the node, if any, to which this element is connected.

- `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -&gt; None<br>        <br>        Set the output to which this input is connected.<br>        <br>        If the output argument is null, then any existing output connection will be cleared.

- `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -&gt; MaterialX_v1_39_5::Output<br>        <br>        Return the output, if any, to which this input is connected.

<hr><h4>41. <a id='materialx-pymaterialxcore-property'>Property</a></h4>

A property element within a PropertySet.

##### Inheritance
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'property'
<hr><h4>42. <a id='materialx-pymaterialxcore-propertyassign'>PropertyAssign</a></h4>

A property assignment element within a Look.

##### Inheritance
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -&gt; None<br>        <br>        Set the property string of this element.

- `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; bool<br>        <br>        Return true if this element has a property string.

- `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; str<br>        <br>        Return the property string of this element.

- `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -&gt; None<br>        <br>        Set the geometry string of this element.

- `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; bool<br>        <br>        Return true if this element has a geometry string.

- `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; str<br>        <br>        Return the geometry string of this element.

- `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -&gt; None<br>        <br>        Set the collection string of this element.

- `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; bool<br>        <br>        Return true if this element has a collection string.

- `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; str<br>        <br>        Return the collection string of this element.

- `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -&gt; None<br>        <br>        Assign a Collection to this element.

- `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -&gt; MaterialX.PyMaterialXCore.Collection<br>        <br>        Return the Collection that is assigned to this element.

##### Attributes

- `CATEGORY` = 'propertyassign'
<hr><h4>43. <a id='materialx-pymaterialxcore-propertyset'>PropertySet</a></h4>

A property set element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -&gt; MaterialX.PyMaterialXCore.Property<br>        <br>        Add a Property to the set.<br>        <br>        Args:<br>            name: The name of the new Property. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Property.

- `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -&gt; list[MaterialX.PyMaterialXCore.Property]<br>        <br>        Return a vector of all Property elements in the set.

- `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -&gt; None<br>        <br>        Remove the Property with the given name, if present.

- `setPropertyValue`: Set the typed value of a property by its name, creating a child element<br>               to hold the property if needed.

- `getPropertyValue`: Return the typed value of a property by its name.  If the given property<br>               is not found, then None is returned.

##### Attributes

- `CATEGORY` = 'property'
<hr><h4>44. <a id='materialx-pymaterialxcore-propertysetassign'>PropertySetAssign</a></h4>

A property set assignment element within a Look.

##### Inheritance
- [GeomElement](#materialx-pymaterialxcore-geomelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -&gt; None<br>        <br>        Set the property set string of this element.

- `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -&gt; bool<br>        <br>        Return true if this element has a property set string.

- `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -&gt; str<br>        <br>        Return the property set string of this element.

- `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -&gt; None<br>        <br>        Assign a property set to this element.

- `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -&gt; MaterialX.PyMaterialXCore.PropertySet<br>        <br>        Return the property set that is assigned to this element.

##### Attributes

- `CATEGORY` = 'propertysetassign'
<hr><h4>45. <a id='materialx-pymaterialxcore-stringresolver'>StringResolver</a></h4>

A helper object for applying string modifiers to data values in the context of a specific element and geometry.

A StringResolver may be constructed through the Element::createStringResolver method, which initializes it in the context of a specific element, geometry, and material.

Calling the StringResolver::resolve method applies all modifiers to a particular string value.

Methods such as StringResolver::setFilePrefix may be used to edit the stored string modifiers before calling StringResolver::resolve.

##### Methods

- `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -&gt; None<br>        <br>        Set the file prefix for this context.

- `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -&gt; str<br>        <br>        Return the file prefix for this context.

- `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -&gt; None<br>        <br>        Set the geom prefix for this context.

- `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -&gt; str<br>        <br>        Return the geom prefix for this context.

- `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -&gt; None<br>        <br>        Set the UDIM substring substitution for filename data values.<br>        <br>        This string will be used to replace the standard &lt;UDIM&gt; token.

- `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -&gt; None<br>        <br>        Set the UV-tile substring substitution for filename data values.<br>        <br>        This string will be used to replace the standard &lt;UVTILE&gt; token.

- `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -&gt; None<br>        <br>        Set an arbitrary substring substitution for filename data values.

- `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -&gt; dict[str, str]<br>        <br>        Return the map of filename substring substitutions.

- `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -&gt; None<br>        <br>        Set an arbitrary substring substitution for geometry name data values.

- `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -&gt; dict[str, str]<br>        <br>        Return the map of geometry name substring substitutions.

- `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -&gt; str<br>        <br>        Given an input string and type, apply all appropriate modifiers and return the resulting string.

<hr><h4>46. <a id='materialx-pymaterialxcore-targetdef'>TargetDef</a></h4>

A definition of an implementation target.

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -&gt; list[str]<br>        <br>        Return a vector of target names that is matching this targetdef either by itself of by its inheritance.<br>        <br>        The vector is ordered by priority starting with this targetdef itself and then upwards in the inheritance hierarchy.

##### Attributes

- `CATEGORY` = 'targetdef'
<hr><h4>47. <a id='materialx-pymaterialxcore-token'>Token</a></h4>

A token element representing a string value.

Token elements are used to define input and output values for string substitutions in image filenames.

##### Inheritance
- [ValueElement](#materialx-pymaterialxcore-valueelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'token'
<hr><h4>48. <a id='materialx-pymaterialxcore-treeiterator'>TreeIterator</a></h4>

An iterator object representing the state of a tree traversal.

##### Methods

- `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -&gt; MaterialX.PyMaterialXCore.Element<br>        <br>        Return the current element in the traversal.

- `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -&gt; int<br>        <br>        Return the element depth of the current traversal, where the starting element represents a depth of zero.

- `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -&gt; None<br>        <br>        Set the prune subtree flag, which controls whether the current subtree is pruned from traversal.<br>        <br>        Args:<br>            prune: If set to true, then the current subtree will be pruned.

- `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -&gt; bool<br>        <br>        Return the prune subtree flag, which controls whether the current subtree is pruned from traversal.

<hr><h4>49. <a id='materialx-pymaterialxcore-typedef'>TypeDef</a></h4>

A type definition element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -&gt; None<br>        <br>        Set the semantic string of the TypeDef.

- `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -&gt; bool<br>        <br>        Return true if the given TypeDef has a semantic string.

- `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -&gt; str<br>        <br>        Return the semantic string of the TypeDef.

- `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -&gt; None<br>        <br>        Set the context string of the TypeDef.

- `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -&gt; bool<br>        <br>        Return true if the given TypeDef has a context string.

- `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -&gt; str<br>        <br>        Return the context string of the TypeDef.

- `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = &#39;&#39;) -&gt; MaterialX_v1_39_5::Member<br>        <br>        Add a Member to the TypeDef.<br>        <br>        Args:<br>            name: The name of the new Member. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Member.

- `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -&gt; MaterialX_v1_39_5::Member<br>        <br>        Return the Member, if any, with the given name.

- `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -&gt; list[MaterialX_v1_39_5::Member]<br>        <br>        Return a vector of all Member elements in the TypeDef.

- `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -&gt; None<br>        <br>        Remove the Member, if any, with the given name.

##### Attributes

- `CATEGORY` = 'typedef'
- `SEMANTIC_ATTRIBUTE` = 'semantic'
- `CONTEXT_ATTRIBUTE` = 'context'
<hr><h4>50. <a id='materialx-pymaterialxcore-typedelement'>TypedElement</a></h4>

The base class for typed elements.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s type string.

- `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -&gt; bool<br>        <br>        Return true if the given element has a type string.

- `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -&gt; str<br>        <br>        Return the element&#39;s type string.

- `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -&gt; bool<br>        <br>        Return true if the element is of color type.

- `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -&gt; bool<br>        <br>        Return true if the element is of multi-output type.

- `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -&gt; MaterialX_v1_39_5::TypeDef<br>        <br>        Return the TypeDef declaring the type string of this element.<br>        <br>        If no matching TypeDef is found, then an empty shared pointer is returned.

##### Attributes

- `TYPE_ATTRIBUTE` = 'type'
<hr><h4>51. <a id='materialx-pymaterialxcore-typedvalue_boolean'>TypedValue_boolean</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -&gt; bool

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -&gt; str

- `createValue`: createValue(arg0: bool) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'boolean'
<hr><h4>52. <a id='materialx-pymaterialxcore-typedvalue_booleanarray'>TypedValue_booleanarray</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -&gt; list[bool]

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -&gt; str

- `createValue`: createValue(arg0: collections.abc.Sequence[bool]) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'booleanarray'
<hr><h4>53. <a id='materialx-pymaterialxcore-typedvalue_color3'>TypedValue_color3</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -&gt; MaterialX_v1_39_5::Color3

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'color3'
<hr><h4>54. <a id='materialx-pymaterialxcore-typedvalue_color4'>TypedValue_color4</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -&gt; MaterialX_v1_39_5::Color4

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'color4'
<hr><h4>55. <a id='materialx-pymaterialxcore-typedvalue_float'>TypedValue_float</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -&gt; float

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -&gt; str

- `createValue`: createValue(arg0: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'float'
<hr><h4>56. <a id='materialx-pymaterialxcore-typedvalue_floatarray'>TypedValue_floatarray</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -&gt; list[float]

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -&gt; str

- `createValue`: createValue(arg0: collections.abc.Sequence[typing.SupportsFloat]) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'floatarray'
<hr><h4>57. <a id='materialx-pymaterialxcore-typedvalue_integer'>TypedValue_integer</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -&gt; int

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -&gt; str

- `createValue`: createValue(arg0: typing.SupportsInt) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'integer'
<hr><h4>58. <a id='materialx-pymaterialxcore-typedvalue_integerarray'>TypedValue_integerarray</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -&gt; list[int]

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -&gt; str

- `createValue`: createValue(arg0: collections.abc.Sequence[typing.SupportsInt]) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'integerarray'
<hr><h4>59. <a id='materialx-pymaterialxcore-typedvalue_matrix33'>TypedValue_matrix33</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -&gt; MaterialX_v1_39_5::Matrix33

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'matrix33'
<hr><h4>60. <a id='materialx-pymaterialxcore-typedvalue_matrix44'>TypedValue_matrix44</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -&gt; MaterialX_v1_39_5::Matrix44

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'matrix44'
<hr><h4>61. <a id='materialx-pymaterialxcore-typedvalue_string'>TypedValue_string</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -&gt; str

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -&gt; str

- `createValue`: createValue(arg0: str) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'string'
<hr><h4>62. <a id='materialx-pymaterialxcore-typedvalue_stringarray'>TypedValue_stringarray</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -&gt; list[str]

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -&gt; str

- `createValue`: createValue(arg0: collections.abc.Sequence[str]) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'stringarray'
<hr><h4>63. <a id='materialx-pymaterialxcore-typedvalue_vector2'>TypedValue_vector2</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -&gt; MaterialX_v1_39_5::Vector2

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'vector2'
<hr><h4>64. <a id='materialx-pymaterialxcore-typedvalue_vector3'>TypedValue_vector3</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -&gt; MaterialX_v1_39_5::Vector3

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'vector3'
<hr><h4>65. <a id='materialx-pymaterialxcore-typedvalue_vector4'>TypedValue_vector4</a></h4>



##### Inheritance
- [Value](#materialx-pymaterialxcore-value)
##### Methods

- `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -&gt; MaterialX_v1_39_5::Vector4

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -&gt; str

- `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -&gt; MaterialX.PyMaterialXCore.Value

##### Attributes

- `TYPE` = 'vector4'
<hr><h4>66. <a id='materialx-pymaterialxcore-unit'>Unit</a></h4>

A unit declaration within a UnitDef.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'unit'
<hr><h4>67. <a id='materialx-pymaterialxcore-unitconverter'>UnitConverter</a></h4>

An abstract base class for unit converters.

Each unit converter instance is responsible for a single unit type.

##### Methods

- `convert`: convert(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: typing.SupportsFloat, arg1: str, arg2: str) -&gt; float<br>        <br>        2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector2<br>        <br>        3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -&gt; MaterialX.PyMaterialXCore.Vector4

- `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -&gt; int<br>        <br>        Given a unit name return a value that it can map to as an integer Returns -1 value if not found.

- `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: typing.SupportsInt) -&gt; str<br>        <br>        Given an integer index return the unit name in the map used by the converter Returns Empty string if not found.

<hr><h4>68. <a id='materialx-pymaterialxcore-unitconverterregistry'>UnitConverterRegistry</a></h4>

A registry for unit converters.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXCore.UnitConverterRegistry<br>        <br>        Creator.

- `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -&gt; bool<br>        <br>        Add a unit converter for a given UnitDef.<br>        <br>        Returns false if a converter has already been registered for the given UnitDef

- `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -&gt; bool<br>        <br>        Remove a unit converter for a given UnitDef.<br>        <br>        Returns false if a converter does not exist for the given UnitDef

- `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -&gt; MaterialX.PyMaterialXCore.UnitConverter<br>        <br>        Get a unit converter for a given UnitDef Returns any empty pointer if a converter does not exist for the given UnitDef.

- `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -&gt; None<br>        <br>        Clear all unit converters from the registry.

<hr><h4>69. <a id='materialx-pymaterialxcore-unitdef'>UnitDef</a></h4>

A unit definition element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s unittype string.

- `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -&gt; bool<br>        <br>        Return true if the given element has a unittype string.

- `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -&gt; str<br>        <br>        Return the element&#39;s type string.

- `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -&gt; MaterialX.PyMaterialXCore.Unit<br>        <br>        Add a Unit to the UnitDef.<br>        <br>        Args:<br>            name: The name of the new Unit. An exception is thrown if the name provided is an empty string.<br>        <br>        Returns:<br>            A shared pointer to the new Unit.

- `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -&gt; MaterialX.PyMaterialXCore.Unit<br>        <br>        Return the Unit, if any, with the given name.

- `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -&gt; list[MaterialX.PyMaterialXCore.Unit]<br>        <br>        Return a vector of all Unit elements in the UnitDef.

##### Attributes

- `CATEGORY` = 'unitdef'
- `UNITTYPE_ATTRIBUTE` = 'unittype'
<hr><h4>70. <a id='materialx-pymaterialxcore-unittypedef'>UnitTypeDef</a></h4>

A unit type definition element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -&gt; list[MaterialX.PyMaterialXCore.UnitDef]<br>        <br>        Find all UnitDefs for the UnitTypeDef.

##### Attributes

- `CATEGORY` = 'unittypedef'
<hr><h4>71. <a id='materialx-pymaterialxcore-value'>Value</a></h4>

A generic, discriminated value, whose type may be queried dynamically.

##### Methods

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -&gt; str<br>        <br>        Return the value string for this value.

- `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -&gt; str<br>        <br>        Return the type string for this value.

- `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -&gt; MaterialX.PyMaterialXCore.Value<br>        <br>        Create a new value instance from value and type strings.<br>        <br>        Returns:<br>            A shared pointer to a typed value, or an empty shared pointer if the conversion to the given data type cannot be performed.

<hr><h4>72. <a id='materialx-pymaterialxcore-valueelement'>ValueElement</a></h4>

The base class for elements that support typed values.

##### Inheritance
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -&gt; None<br>        <br>        Set the value string of an element.

- `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        Return true if the given element has a value string.

- `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Get the value string of a element.

- `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -&gt; str<br>        <br>        Return the resolved value string of an element, applying any string substitutions that are defined at the element&#39;s scope.<br>        <br>        Args:<br>            resolver: An optional string resolver, which will be used to apply string substitutions. By default, a new string resolver will be created at this scope and applied to the return value.

- `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -&gt; None<br>        <br>        Set the interface name of an element.

- `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        Return true if the given element has an interface name.

- `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Return the interface name of an element.

- `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -&gt; None<br>        <br>        Set the implementation name of an element.

- `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        Return true if the given element has an implementation name.

- `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Return the implementation name of an element.

- `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -&gt; None<br>        <br>        Set the unit string of an element.

- `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        Return true if the given element has a unit string.

- `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Return the unit string of an element.

- `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Return the unit defined by the associated NodeDef if this element is a child of a Node.

- `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -&gt; None<br>        <br>        Set the unit type of an element.

- `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        Return true if the given element has a unit type.

- `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; str<br>        <br>        Return the unit type of an element.

- `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -&gt; bool<br>        <br>        The the uniform attribute flag for this element.

- `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -&gt; None<br>        <br>        Set the uniform attribute flag on this element.

- `setValue`: Set the typed value of an element.

- `getValue`: Return the typed value of an element.

- `getDefaultValue`: Return the default value for this element.

##### Attributes

- `VALUE_ATTRIBUTE` = 'value'
- `INTERFACE_NAME_ATTRIBUTE` = 'interfacename'
- `IMPLEMENTATION_NAME_ATTRIBUTE` = 'implname'
- `IMPLEMENTATION_TYPE_ATTRIBUTE` = 'impltype'
- `ENUM_ATTRIBUTE` = 'enum'
- `ENUM_VALUES_ATTRIBUTE` = 'enumvalues'
- `UNIT_ATTRIBUTE` = 'unit'
- `UI_NAME_ATTRIBUTE` = 'uiname'
- `UI_FOLDER_ATTRIBUTE` = 'uifolder'
- `UI_MIN_ATTRIBUTE` = 'uimin'
- `UI_MAX_ATTRIBUTE` = 'uimax'
- `UI_SOFT_MIN_ATTRIBUTE` = 'uisoftmin'
- `UI_SOFT_MAX_ATTRIBUTE` = 'uisoftmax'
- `UI_STEP_ATTRIBUTE` = 'uistep'
- `UI_ADVANCED_ATTRIBUTE` = 'uiadvanced'
<hr><h4>73. <a id='materialx-pymaterialxcore-variant'>Variant</a></h4>

A variant element within a VariantSet.

##### Inheritance
- [InterfaceElement](#materialx-pymaterialxcore-interfaceelement)
- [TypedElement](#materialx-pymaterialxcore-typedelement)
- [Element](#materialx-pymaterialxcore-element)
##### Attributes

- `CATEGORY` = 'variant'
<hr><h4>74. <a id='materialx-pymaterialxcore-variantassign'>VariantAssign</a></h4>

A variant assignment element within a Look.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s variant set string.

- `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -&gt; bool<br>        <br>        Return true if the given element has a variant set string.

- `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -&gt; str<br>        <br>        Return the element&#39;s variant set string.

- `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -&gt; None<br>        <br>        Set the element&#39;s variant string.

- `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -&gt; bool<br>        <br>        Return true if the given element has a variant string.

- `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -&gt; str<br>        <br>        Return the element&#39;s variant string.

##### Attributes

- `CATEGORY` = 'variantassign'
<hr><h4>75. <a id='materialx-pymaterialxcore-variantset'>VariantSet</a></h4>

A variant set element within a Document.

##### Inheritance
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = &#39;&#39;) -&gt; MaterialX.PyMaterialXCore.Variant<br>        <br>        Add a Variant to the variant set.<br>        <br>        Args:<br>            name: The name of the new Variant. If no name is specified, then a unique name will automatically be generated.<br>        <br>        Returns:<br>            A shared pointer to the new Variant.

- `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -&gt; MaterialX.PyMaterialXCore.Variant<br>        <br>        Return the Variant, if any, with the given name.

- `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -&gt; list[MaterialX.PyMaterialXCore.Variant]<br>        <br>        Return a vector of all Variant elements in the look.

- `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -&gt; None<br>        <br>        Remove the Variant, if any, with the given name.

##### Attributes

- `CATEGORY` = 'variantset'
<hr><h4>76. <a id='materialx-pymaterialxcore-vector2'>Vector2</a></h4>

A vector of two floating-point values.

##### Inheritance
- [VectorBase](#materialx-pymaterialxcore-vectorbase)
##### Methods

- `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -&gt; float

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Vector2

- `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; float

- `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -&gt; MaterialX.PyMaterialXCore.Vector2

- `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; float<br>        <br>        Return the cross product of two vectors.

- `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -&gt; tuple[float, float]

<hr><h4>77. <a id='materialx-pymaterialxcore-vector3'>Vector3</a></h4>

A vector of three floating-point values.

##### Inheritance
- [VectorBase](#materialx-pymaterialxcore-vectorbase)
##### Methods

- `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -&gt; float

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3

- `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; float

- `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3

- `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the cross product of two vectors.

- `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -&gt; tuple[float, float, float]

<hr><h4>78. <a id='materialx-pymaterialxcore-vector4'>Vector4</a></h4>

A vector of four floating-point values.

##### Inheritance
- [VectorBase](#materialx-pymaterialxcore-vectorbase)
##### Methods

- `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -&gt; float

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -&gt; MaterialX.PyMaterialXCore.Vector4

- `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -&gt; float

- `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -&gt; MaterialX.PyMaterialXCore.Vector4

- `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -&gt; tuple[float, float, float, float]

<hr><h4>79. <a id='materialx-pymaterialxcore-vectorbase'>VectorBase</a></h4>

The base class for vectors of scalar values.

<hr><h4>80. <a id='materialx-pymaterialxcore-visibility'>Visibility</a></h4>

A visibility element within a Look.

A Visibility describes the visibility relationship between two geometries or geometric collections.

##### Inheritance
- [GeomElement](#materialx-pymaterialxcore-geomelement)
- [Element](#materialx-pymaterialxcore-element)
##### Methods

- `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -&gt; None<br>        <br>        Set the viewer geom string of the element.

- `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -&gt; bool<br>        <br>        Return true if the given element has a viewer geom string.

- `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -&gt; str<br>        <br>        Return the viewer geom string of the element.

- `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -&gt; None<br>        <br>        Set the viewer geom string of the element.

- `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -&gt; bool<br>        <br>        Return true if the given element has a viewer collection string.

- `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -&gt; str<br>        <br>        Return the viewer collection string of the element.

- `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -&gt; None<br>        <br>        Set the visibility type string of the element.

- `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -&gt; bool<br>        <br>        Return true if the given element has a visibility type string.

- `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -&gt; str<br>        <br>        Return the visibility type string of the element.

- `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -&gt; None<br>        <br>        Set the visible boolean of the element.

- `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -&gt; bool<br>        <br>        Return the visible boolean of the element.

##### Attributes

- `CATEGORY` = 'visibility'

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

- `ARRAY_PREFERRED_SEPARATOR`
 = ', '
- `ARRAY_VALID_SEPARATORS`
 = ', '
- `BSDF_TYPE_STRING`
 = 'BSDF'
- `DEFAULT_TYPE_STRING`
 = 'color3'
- `DISPLACEMENT_SHADER_TYPE_STRING`
 = 'displacementshader'
- `EDF_TYPE_STRING`
 = 'EDF'
- `FILENAME_TYPE_STRING`
 = 'filename'
- `GEOMNAME_TYPE_STRING`
 = 'geomname'
- `GEOM_PATH_SEPARATOR`
 = '/'
- `LIGHT_SHADER_TYPE_STRING`
 = 'lightshader'
- `MATERIAL_TYPE_STRING`
 = 'material'
- `MULTI_OUTPUT_TYPE_STRING`
 = 'multioutput'
- `NAME_PATH_SEPARATOR`
 = '/'
- `NAME_PREFIX_SEPARATOR`
 = ':'
- `NONE_TYPE_STRING`
 = 'none'
- `STRING_TYPE_STRING`
 = 'string'
- `SURFACE_MATERIAL_NODE_STRING`
 = 'surfacematerial'
- `SURFACE_SHADER_TYPE_STRING`
 = 'surfaceshader'
- `UDIM_SET_PROPERTY`
 = 'udimset'
- `UDIM_TOKEN`
 = '(UDIM)'
- `UNIVERSAL_GEOM_NAME`
 = '/'
- `UV_TILE_TOKEN`
 = '(UVTILE)'
- `VALUE_STRING_FALSE`
 = 'false'
- `VALUE_STRING_TRUE`
 = 'true'
- `VDF_TYPE_STRING`
 = 'VDF'
- `VOLUME_MATERIAL_NODE_STRING`
 = 'volumematerial'
- `VOLUME_SHADER_TYPE_STRING`
 = 'volumeshader'

---

## 2. Module: MaterialX.PyMaterialXFormat

### Classes

<hr><h4>1. <a id='materialx-pymaterialxformat-exceptionfilemissing'>ExceptionFileMissing</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxformat-exception)
- [BaseException](#materialx-pymaterialxformat-baseexception)
<hr><h4>2. <a id='materialx-pymaterialxformat-exceptionparseerror'>ExceptionParseError</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxformat-exception)
- [BaseException](#materialx-pymaterialxformat-baseexception)
<hr><h4>3. <a id='materialx-pymaterialxformat-filepath'>FilePath</a></h4>

A generic file path, supporting both syntactic and file system operations.

##### Methods

- `asString`: asString(self: MaterialX.PyMaterialXFormat.FilePath, format: MaterialX.PyMaterialXFormat.Format = &lt;Format.FormatPosix: 1&gt;) -&gt; str<br>        <br>        Return this path as a standard string with the given format.

- `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; bool<br>        <br>        Return true if the given path is empty.

- `isAbsolute`: isAbsolute(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; bool<br>        <br>        Return true if the given path is absolute.

- `getBaseName`: getBaseName(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; str<br>        <br>        Return the base name of the given path, with leading directory information removed.

- `getParentPath`: getParentPath(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Return the parent directory of the given path, if any.<br>        <br>        If no parent directory is present, then the empty path is returned.

- `getExtension`: getExtension(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; str<br>        <br>        Return the file extension of the given path.

- `addExtension`: addExtension(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -&gt; None<br>        <br>        Add a file extension to the given path.

- `removeExtension`: removeExtension(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Remove the file extension, if any, from the given path.

- `size`: size(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; int<br>        <br>        Return the number of strings in the path.

- `getNormalized`: getNormalized(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Return a normalized version of the given path, collapsing current path and parent path references so that &#39;a/.<br>        <br>        /b&#39; and &#39;c/../d/../a/b&#39; become &#39;a/b&#39;.

- `exists`: exists(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; bool<br>        <br>        Return true if the given path exists on the file system.

- `isDirectory`: isDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; bool<br>        <br>        Return true if the given path is a directory on the file system.

- `getFilesInDirectory`: getFilesInDirectory(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -&gt; list[MaterialX.PyMaterialXFormat.FilePath]<br>        <br>        Return a vector of all files in the given directory with the given extension.<br>        <br>        If extension is empty all files are returned.

- `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; list[MaterialX.PyMaterialXFormat.FilePath]<br>        <br>        Return a vector of all directories at or beneath the given path.

- `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Create a directory on the file system at the given path.

- `getCurrentPath`: getCurrentPath() -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Return the current working directory of the file system.

- `getModulePath`: getModulePath() -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Return the directory containing the executable module.

<hr><h4>4. <a id='materialx-pymaterialxformat-filesearchpath'>FileSearchPath</a></h4>

A sequence of file paths, which may be queried to find the first instance of a given filename on the file system.

##### Methods

- `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = &#39;:&#39;) -&gt; str<br>        <br>        Convert this sequence to a string using the given separator.

- `append`: append(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; None

- `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Prepend the given path to the sequence.

- `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; None<br>        <br>        Clear all paths from the sequence.

- `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; int<br>        <br>        Return the number of paths in the sequence.

- `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; bool<br>        <br>        Return true if the search path is empty.

- `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Given an input filename, iterate through each path in this sequence, returning the first combined path found on the file system.<br>        <br>        On success, the combined path is returned; otherwise the original filename is returned unmodified.

<hr><h4>5. <a id='materialx-pymaterialxformat-format'>Format</a></h4>

Members:

  FormatWindows

  FormatPosix

  FormatNative

##### Attributes

- `name` = (property)
- `value` = (property)
- `FormatWindows` = (property)
- `FormatPosix` = (property)
- `FormatNative` = (property)
<hr><h4>6. <a id='materialx-pymaterialxformat-type'>Type</a></h4>

Members:

  TypeRelative

  TypeAbsolute

  TypeNetwork

##### Attributes

- `name` = (property)
- `value` = (property)
- `TypeRelative` = (property)
- `TypeAbsolute` = (property)
- `TypeNetwork` = (property)
<hr><h4>7. <a id='materialx-pymaterialxformat-xmlreadoptions'>XmlReadOptions</a></h4>

A set of options for controlling the behavior of XML read functions.

##### Attributes

- `readXIncludeFunction` = (property)
- `readComments` = (property)
- `readNewlines` = (property)
- `upgradeVersion` = (property)
- `parentXIncludes` = (property)
<hr><h4>8. <a id='materialx-pymaterialxformat-xmlwriteoptions'>XmlWriteOptions</a></h4>

A set of options for controlling the behavior of XML write functions.

##### Attributes

- `writeXIncludeEnable` = (property)
- `elementPredicate` = (property)

### Functions

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x1030bfbf0>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

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

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x1030bf930>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Load a given MaterialX library into a document.

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

Read the given file and return a string containing its contents; if the read is not successful, then the empty string is returned.

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x1030befb0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Read a Document as XML from the given filename.

Args:
    doc: The Document into which data is read.
    filename: The filename from which data is read. This argument can be supplied either as a FilePath or a standard string.
    searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
    readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x1030bf130>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

Read a Document as XML from the given string.

Args:
    doc: The Document into which data is read.
    str: The string from which data is read.
    searchPath: An optional sequence of file paths that will be applied in order when searching for the given file and its includes. This argument can be supplied either as a FileSearchPath, or as a standard string with paths separated by the PATH_SEPARATOR character.
    readOptions: An optional pointer to an XmlReadOptions object. If provided, then the given options will affect the behavior of the read function. Defaults to a null pointer.

- `writeToXmlFile`: writeToXmlFile(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> None

- `writeToXmlString`: writeToXmlString(doc: MaterialX.PyMaterialXCore.Document, writeOptions: MaterialX.PyMaterialXFormat.XmlWriteOptions = None) -> str


### Globals

- `FormatNative`
 = (Format.FormatPosix: 1)
- `FormatPosix`
 = (Format.FormatPosix: 1)
- `FormatWindows`
 = (Format.FormatWindows: 0)
- `MATERIALX_SEARCH_PATH_ENV_VAR`
 = 'MATERIALX_SEARCH_PATH'
- `PATH_LIST_SEPARATOR`
 = ':'
- `TypeAbsolute`
 = (Type.TypeAbsolute: 1)
- `TypeNetwork`
 = (Type.TypeNetwork: 2)
- `TypeRelative`
 = (Type.TypeRelative: 0)

---

## 3. Module: MaterialX.PyMaterialXGenGlsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenglsl-esslshadergenerator'>EsslShaderGenerator</a></h4>

An ESSL (OpenGL ES Shading Language) shader generator.

##### Inheritance
- [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator)
- [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -&gt; str<br>        <br>        Return the version string for the ESSL version this generator is for.

<hr><h4>2. <a id='materialx-pymaterialxgenglsl-glslresourcebindingcontext'>GlslResourceBindingContext</a></h4>

Class representing a resource binding for Glsl shader resources.

##### Inheritance
- [HwResourceBindingContext](#materialx-pymaterialxgenglsl-hwresourcebindingcontext)
- [GenUserData](#materialx-pymaterialxgenglsl-genuserdata)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -&gt; MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext

- `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

- `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

<hr><h4>3. <a id='materialx-pymaterialxgenglsl-glslshadergenerator'>GlslShaderGenerator</a></h4>

Base class for GLSL (OpenGL Shading Language) code generation.

A generator for a specific GLSL target should be derived from this class.

##### Inheritance
- [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader<br>        <br>        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -&gt; str<br>        <br>        Return the version string for the GLSL version this generator is for.

<hr><h4>4. <a id='materialx-pymaterialxgenglsl-vkshadergenerator'>VkShaderGenerator</a></h4>

A Vulkan GLSL shader generator.

##### Inheritance
- [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator)
- [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -&gt; str<br>        <br>        Return the version string for the GLSL version this generator is for.

<hr><h4>5. <a id='materialx-pymaterialxgenglsl-wgslshadergenerator'>WgslShaderGenerator</a></h4>

WGSL Flavor of Vulkan GLSL shader generator.

##### Inheritance
- [GlslShaderGenerator](#materialx-pymaterialxgenglsl-glslshadergenerator)
- [HwShaderGenerator](#materialx-pymaterialxgenglsl-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenglsl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -&gt; str

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -&gt; str


---

## 4. Module: MaterialX.PyMaterialXGenMdl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenmdl-mdlshadergenerator'>MdlShaderGenerator</a></h4>

Shader generator for MDL (Material Definition Language).

##### Inheritance
- [ShaderGenerator](#materialx-pymaterialxgenmdl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMdl.MdlShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.


---

## 5. Module: MaterialX.PyMaterialXGenMsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenmsl-mslresourcebindingcontext'>MslResourceBindingContext</a></h4>



##### Inheritance
- [HwResourceBindingContext](#materialx-pymaterialxgenmsl-hwresourcebindingcontext)
- [GenUserData](#materialx-pymaterialxgenmsl-genuserdata)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt) -&gt; MaterialX.PyMaterialXGenMsl.MslResourceBindingContext

- `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

- `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenMsl.MslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

<hr><h4>2. <a id='materialx-pymaterialxgenmsl-mslshadergenerator'>MslShaderGenerator</a></h4>



##### Inheritance
- [HwShaderGenerator](#materialx-pymaterialxgenmsl-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenmsl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -&gt; str

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -&gt; str


---

## 6. Module: MaterialX.PyMaterialXGenOsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenosl-oslshadergenerator'>OslShaderGenerator</a></h4>

Base class for OSL (Open Shading Language) shader generators.

A generator for a specific OSL target should be derived from this class.

##### Inheritance
- [ShaderGenerator](#materialx-pymaterialxgenosl-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.

- `generate`: generate(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader<br>        <br>        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.


### Globals

- `OSL_INPUTS`
 = 'i'
- `OSL_OUTPUTS`
 = 'o'
- `OSL_UNIFORMS`
 = 'u'

---

## 7. Module: MaterialX.PyMaterialXGenShader

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenshader-applicationvariablehandler'>ApplicationVariableHandler</a></h4>



<hr><h4>2. <a id='materialx-pymaterialxgenshader-colormanagementsystem'>ColorManagementSystem</a></h4>

Abstract base class for color management systems.

##### Methods

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -&gt; str<br>        <br>        Return the ColorManagementSystem name.

- `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Load a library of implementations from the provided document, replacing any previously loaded content.

- `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -&gt; bool<br>        <br>        Returns whether this color management system supports a provided transform.

<hr><h4>3. <a id='materialx-pymaterialxgenshader-colorspacetransform'>ColorSpaceTransform</a></h4>

Structure that represents color space transform information.

##### Attributes

- `sourceSpace` = (property)
- `targetSpace` = (property)
- `type` = (property)
<hr><h4>4. <a id='materialx-pymaterialxgenshader-defaultcolormanagementsystem'>DefaultColorManagementSystem</a></h4>

Class for a default color management system.

##### Inheritance
- [ColorManagementSystem](#materialx-pymaterialxgenshader-colormanagementsystem)
##### Methods

- `create`: create(arg0: str) -&gt; MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem<br>        <br>        Create a new DefaultColorManagementSystem.

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -&gt; str<br>        <br>        Return the DefaultColorManagementSystem name.

<hr><h4>5. <a id='materialx-pymaterialxgenshader-gencontext'>GenContext</a></h4>

A context class for shader generation.

Used for thread local storage of data needed during shader generation.

##### Methods

- `getShaderGenerator`: getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator<br>        <br>        Return shader generatior.

- `getOptions`: getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX_v1_39_5::GenOptions

- `getTypeDesc`: getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -&gt; MaterialX_v1_39_5::TypeDesc<br>        <br>        Return a TypeDesc for the given type name.

- `registerSourceCodeSearchPath`: registerSourceCodeSearchPath(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; None

- `resolveSourceFile`: resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXFormat.FilePath<br>        <br>        Resolve a source code filename, first checking the given local path then checking any file paths registered by the user.

- `pushUserData`: pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -&gt; None<br>        <br>        Add user data to the context to make it available during shader generator.

- `setApplicationVariableHandler`: setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -&gt; None<br>        <br>        Set handler for application variables.

- `getApplicationVariableHandler`: getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -&gt; collections.abc.Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]<br>        <br>        Get handler for application variables.

<hr><h4>6. <a id='materialx-pymaterialxgenshader-genoptions'>GenOptions</a></h4>

Class holding options to configure shader generation.

##### Attributes

- `shaderInterfaceType` = (property)
- `fileTextureVerticalFlip` = (property)
- `targetColorSpaceOverride` = (property)
- `targetDistanceUnit` = (property)
- `addUpstreamDependencies` = (property)
- `libraryPrefix` = (property)
- `emitColorTransforms` = (property)
- `hwTransparency` = (property)
- `hwSpecularEnvironmentMethod` = (property)
- `hwSrgbEncodeOutput` = (property)
- `hwWriteDepthMoments` = (property)
- `hwShadowMap` = (property)
- `hwMaxActiveLightSources` = (property)
- `hwNormalizeUdimTexCoords` = (property)
- `hwAmbientOcclusion` = (property)
- `hwWriteAlbedoTable` = (property)
- `hwWriteEnvPrefilter` = (property)
- `hwImplicitBitangents` = (property)
<hr><h4>7. <a id='materialx-pymaterialxgenshader-genuserdata'>GenUserData</a></h4>

Base class for custom user data needed during shader generation.

##### Methods

- `getSelf`: getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -&gt; MaterialX.PyMaterialXGenShader.GenUserData

<hr><h4>8. <a id='materialx-pymaterialxgenshader-hwresourcebindingcontext'>HwResourceBindingContext</a></h4>



##### Inheritance
- [GenUserData](#materialx-pymaterialxgenshader-genuserdata)
##### Methods

- `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

- `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenShader.HwResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; None

<hr><h4>9. <a id='materialx-pymaterialxgenshader-hwshadergenerator'>HwShaderGenerator</a></h4>



##### Inheritance
- [ShaderGenerator](#materialx-pymaterialxgenshader-shadergenerator)
##### Methods

- `bindLightShader`: bindLightShader(self: MaterialX.PyMaterialXCore.NodeDef, arg0: typing.SupportsInt, arg1: MaterialX.PyMaterialXGenShader.GenContext) -&gt; None

- `unbindLightShader`: unbindLightShader(self: typing.SupportsInt, arg0: MaterialX.PyMaterialXGenShader.GenContext) -&gt; None

- `unbindLightShaders`: unbindLightShaders(self: MaterialX.PyMaterialXGenShader.GenContext) -&gt; None

<hr><h4>10. <a id='materialx-pymaterialxgenshader-hwspecularenvironmentmethod'>HwSpecularEnvironmentMethod</a></h4>

Members:

  SPECULAR_ENVIRONMENT_PREFILTER

  SPECULAR_ENVIRONMENT_FIS

  SPECULAR_ENVIRONMENT_NONE

##### Attributes

- `name` = (property)
- `value` = (property)
- `SPECULAR_ENVIRONMENT_PREFILTER` = (property)
- `SPECULAR_ENVIRONMENT_FIS` = (property)
- `SPECULAR_ENVIRONMENT_NONE` = (property)
<hr><h4>11. <a id='materialx-pymaterialxgenshader-shader'>Shader</a></h4>

Class containing all data needed during shader generation.

After generation is completed it will contain the resulting source code emitted by shader generators.

The class contains a default implementation using a single shader stage. Derived shaders can override this, as well as overriding all methods that add code to the shader.

##### Methods

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.Shader) -&gt; str<br>        <br>        Return the shader name.

- `hasStage`: hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; bool<br>        <br>        Return if stage exists.

- `numStages`: numStages(self: MaterialX.PyMaterialXGenShader.Shader) -&gt; int<br>        <br>        Return the number of shader stages for this shader.

- `getStage`: getStage(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: typing.SupportsInt) -&gt; MaterialX_v1_39_5::ShaderStage<br>        <br>        2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; MaterialX_v1_39_5::ShaderStage

- `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; str<br>        <br>        Return the shader source code for a given shader stage.

- `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; bool<br>        <br>        Return true if the shader has a given named attribute.

- `getAttribute`: getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; MaterialX.PyMaterialXCore.Value<br>        <br>        Return the value for a named attribute, or nullptr if no such attribute is found.

- `setAttribute`: setAttribute(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -&gt; None<br>        <br>        2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -&gt; None

<hr><h4>12. <a id='materialx-pymaterialxgenshader-shadergenerator'>ShaderGenerator</a></h4>

Base class for shader generators All third-party shader generators should derive from this class.

Derived classes should use DECLARE_SHADER_GENERATOR / DEFINE_SHADER_GENERATOR in their declaration / definition, and register with the Registry class.

##### Methods

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -&gt; str<br>        <br>        Return the name of the target this generator is for.

- `generate`: generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader<br>        <br>        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.

- `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -&gt; None<br>        <br>        Sets the color management system.

- `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -&gt; MaterialX.PyMaterialXGenShader.ColorManagementSystem<br>        <br>        Returns the color management system.

- `setUnitSystem`: setUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX_v1_39_5::UnitSystem) -&gt; None<br>        <br>        Sets the unit system.

- `getUnitSystem`: getUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -&gt; MaterialX_v1_39_5::UnitSystem<br>        <br>        Returns the unit system.

- `getTokenSubstitutions`: getTokenSubstitutions(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -&gt; dict[str, str]<br>        <br>        Return the map of token substitutions used by the generator.

- `registerTypeDefs`: registerTypeDefs(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        Register type definitions from the document.

- `registerShaderMetadata`: registerShaderMetadata(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX_v1_39_5::GenContext) -&gt; None<br>        <br>        Register metadata that should be exported to the generated shaders.<br>        <br>        Supported metadata includes standard UI attributes like &quot;uiname&quot;, &quot;uifolder&quot;, &quot;uimin&quot;, &quot;uimax&quot;, etc. But it is also extendable by defining custom attributes using AttributeDefs. Any AttributeDef in the given document with exportable=&quot;true&quot; will be exported as shader metadata when found on nodes during shader generation. Derived shader generators may override this method to change the registration. Applications must explicitly call this method before shader generation to enable export of metadata.

<hr><h4>13. <a id='materialx-pymaterialxgenshader-shaderinterfacetype'>ShaderInterfaceType</a></h4>

Members:

  SHADER_INTERFACE_COMPLETE

  SHADER_INTERFACE_REDUCED

##### Attributes

- `name` = (property)
- `value` = (property)
- `SHADER_INTERFACE_COMPLETE` = (property)
- `SHADER_INTERFACE_REDUCED` = (property)
<hr><h4>14. <a id='materialx-pymaterialxgenshader-shaderport'>ShaderPort</a></h4>

An input or output port on a ShaderNode.

##### Methods

- `setType`: setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -&gt; None<br>        <br>        Set the data type for this port.

- `getType`: getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; MaterialX_v1_39_5::TypeDesc<br>        <br>        Return the data type for this port.

- `setName`: setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set the name of this port.

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the name of this port.

- `getFullName`: getFullName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the name of this port.

- `setVariable`: setVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set the variable name of this port.

- `getVariable`: getVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the variable name of this port.

- `setSemantic`: setSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set the variable semantic of this port.

- `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the variable semantic of this port.

- `setValue`: setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value, arg1: bool) -&gt; None<br>        <br>        Set a value on this port.

- `getValue`: getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; MaterialX.PyMaterialXCore.Value<br>        <br>        Return the value set on this port.

- `getValueString`: getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the value set on this port as a string, or an empty string if there is no value.

- `setGeomProp`: setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set geomprop name if the input has a default geomprop to be assigned when it is unconnected.

- `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Get geomprop name.

- `setPath`: setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set the path to this port.

- `getPath`: getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the path to this port.

- `setUnit`: setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set a unit type for the value on this port.

- `getUnit`: getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the unit type for the value on this port.

- `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -&gt; None<br>        <br>        Set a source color space for the value on this port.

- `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; str<br>        <br>        Return the source color space for the value on this port.

- `isUniform`: isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; bool<br>        <br>        Return the uniform flag on this port.

- `isEmitted`: isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -&gt; bool<br>        <br>        Return the emitted state of this port.

<hr><h4>15. <a id='materialx-pymaterialxgenshader-shaderportpredicate'>ShaderPortPredicate</a></h4>



<hr><h4>16. <a id='materialx-pymaterialxgenshader-shaderstage'>ShaderStage</a></h4>

A shader stage, containing the state and resulting source code for the stage.

##### Methods

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; str<br>        <br>        Return the stage name.

- `getFunctionName`: getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; str<br>        <br>        Return the stage function name.

- `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; str<br>        <br>        Return the stage source code.

- `getUniformBlock`: getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -&gt; MaterialX.PyMaterialXGenShader.VariableBlock

- `getInputBlock`: getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -&gt; MaterialX.PyMaterialXGenShader.VariableBlock

- `getOutputBlock`: getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -&gt; MaterialX.PyMaterialXGenShader.VariableBlock

- `getConstantBlock`: getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; MaterialX.PyMaterialXGenShader.VariableBlock

- `getUniformBlocks`: getUniformBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]<br>        <br>        Return a map of all uniform blocks.

- `getInputBlocks`: getInputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]<br>        <br>        Return a map of all input blocks.

- `getIncludes`: getIncludes(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; set[str]<br>        <br>        Return a set of all include files.

- `getSourceDependencies`: getSourceDependencies(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; set[str]<br>        <br>        Return a set of all source dependencies.

- `getOutputBlocks`: getOutputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -&gt; dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]<br>        <br>        Return a map of all output blocks.

<hr><h4>17. <a id='materialx-pymaterialxgenshader-shadertranslator'>ShaderTranslator</a></h4>

A helper class for translating content between shading models.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderTranslator

- `translateShader`: translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -&gt; None<br>        <br>        Translate a shader node to the destination shading model.

- `translateAllMaterials`: translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -&gt; None<br>        <br>        Translate each material in the input document to the destination shading model.

<hr><h4>18. <a id='materialx-pymaterialxgenshader-typedesc'>TypeDesc</a></h4>

A type descriptor for MaterialX data types.

All types need to have a type descriptor registered in order for shader generators to know about the type. It can be used for type comparisons as well as getting more information about the type. Type descriptors for all standard library data types are defined by default and can be accessed from the Type namespace, e.g. Type::FLOAT. Custom struct types defined through typedef elements in a data library are loaded in and registered by calling the ShaderGenerator::registerTypeDefs method. The TypeSystem class, see below, is used to manage all type descriptions. It can be used to query the registered types.

##### Methods

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; str<br>        <br>        Return the name of the type.

- `getBaseType`: getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; int<br>        <br>        Return the basetype for the type.

- `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; int<br>        <br>        Return the semantic for the type.

- `getSize`: getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; int<br>        <br>        Return the number of elements the type is composed of.<br>        <br>        Will return 1 for scalar types and a size greater than 1 for aggregate type. For array types 0 is returned since the number of elements is undefined until an array is instantiated.

- `isScalar`: isScalar(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is a scalar type.

- `isAggregate`: isAggregate(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is an aggregate type.

- `isArray`: isArray(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is an array type.

- `isFloat2`: isFloat2(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is an aggregate of 2 floats.

- `isFloat3`: isFloat3(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is an aggregate of 3 floats.

- `isFloat4`: isFloat4(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type is an aggregate of 4 floats.

- `isClosure`: isClosure(self: MaterialX.PyMaterialXGenShader.TypeDesc) -&gt; bool<br>        <br>        Return true if the type represents a closure.

<hr><h4>19. <a id='materialx-pymaterialxgenshader-unitsystem'>UnitSystem</a></h4>

Base unit system support.

##### Methods

- `create`: create(arg0: str) -&gt; MaterialX.PyMaterialXGenShader.UnitSystem<br>        <br>        Create a new UnitSystem.

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -&gt; str<br>        <br>        Return the UnitSystem name.

- `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None<br>        <br>        assign document with unit implementations replacing any previously loaded content.

- `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -&gt; bool<br>        <br>        Returns whether this unit system supports a provided transform.

- `setUnitConverterRegistry`: setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -&gt; None<br>        <br>        Assign unit converter registry replacing any previous assignment.

- `getUnitConverterRegistry`: getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -&gt; MaterialX.PyMaterialXCore.UnitConverterRegistry<br>        <br>        Returns the currently assigned unit converter registry.

<hr><h4>20. <a id='materialx-pymaterialxgenshader-unittransform'>UnitTransform</a></h4>

Structure that represents unit transform information.

##### Attributes

- `sourceUnit` = (property)
- `targetUnit` = (property)
- `type` = (property)
- `unitType` = (property)
<hr><h4>21. <a id='materialx-pymaterialxgenshader-variableblock'>VariableBlock</a></h4>

A block of variables in a shader stage.

##### Methods

- `getName`: getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -&gt; str<br>        <br>        Get the name of this block.

- `getInstance`: getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -&gt; str<br>        <br>        Get the instance name of this block.

- `empty`: empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -&gt; bool<br>        <br>        Return true if the block has no variables.

- `size`: size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -&gt; int<br>        <br>        Return the number of variables in this block.

- `find`: find(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -&gt; MaterialX.PyMaterialXGenShader.ShaderPort<br>        <br>        2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: collections.abc.Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -&gt; MaterialX.PyMaterialXGenShader.ShaderPort


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

- `HW_ATTR_TRANSPARENT`
 = 'transparent'
- `HW_LIGHT_DATA`
 = 'LightData'
- `HW_PIXEL_OUTPUTS`
 = 'PixelOutputs'
- `HW_PRIVATE_UNIFORMS`
 = 'PrivateUniforms'
- `HW_PUBLIC_UNIFORMS`
 = 'PublicUniforms'
- `HW_VERTEX_DATA`
 = 'VertexData'
- `HW_VERTEX_INPUTS`
 = 'VertexInputs'
- `PIXEL_STAGE`
 = 'pixel'
- `SHADER_INTERFACE_COMPLETE`
 = (ShaderInterfaceType.SHADER_INTERFACE_COMPLETE: 0)
- `SHADER_INTERFACE_REDUCED`
 = (ShaderInterfaceType.SHADER_INTERFACE_REDUCED: 1)
- `SPECULAR_ENVIRONMENT_FIS`
 = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_FIS: 1)
- `SPECULAR_ENVIRONMENT_NONE`
 = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_NONE: 0)
- `SPECULAR_ENVIRONMENT_PREFILTER`
 = (HwSpecularEnvironmentMethod.SPECULAR_ENVIRONMENT_PREFILTER: 2)
- `VERTEX_STAGE`
 = 'vertex'

---

## 8. Module: MaterialX.PyMaterialXGenSlang

### Classes

<hr><h4>1. <a id='materialx-pymaterialxgenslang-slangshadergenerator'>SlangShaderGenerator</a></h4>

Base class for Slang code generation.

A generator for a specific Slang target should be derived from this class.

##### Inheritance
- [HwShaderGenerator](#materialx-pymaterialxgenslang-hwshadergenerator)
- [ShaderGenerator](#materialx-pymaterialxgenslang-shadergenerator)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXGenShader.ShaderGenerator

- `generate`: generate(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; MaterialX.PyMaterialXGenShader.Shader<br>        <br>        Generate a shader starting from the given element, translating the element and all dependencies upstream into shader code.

- `getTarget`: getTarget(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -&gt; str<br>        <br>        Return a unique identifier for the target this generator is for.

- `getVersion`: getVersion(self: MaterialX.PyMaterialXGenSlang.SlangShaderGenerator) -&gt; str<br>        <br>        Return the version string for the Slang version this generator is for.


---

## 9. Module: MaterialX.PyMaterialXRender

### Classes

<hr><h4>1. <a id='materialx-pymaterialxrender-basetype'>BaseType</a></h4>

Members:

  UINT8

  INT8

  UINT16

  INT16

  HALF

  FLOAT

##### Attributes

- `name` = (property)
- `value` = (property)
- `UINT8` = (property)
- `INT8` = (property)
- `UINT16` = (property)
- `INT16` = (property)
- `HALF` = (property)
- `FLOAT` = (property)
<hr><h4>2. <a id='materialx-pymaterialxrender-camera'>Camera</a></h4>

A simple camera class, supporting transform matrices and arcball functionality for object-viewing applications.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.Camera<br>        <br>        Create a new camera.

- `setWorldMatrix`: setWorldMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -&gt; None<br>        <br>        Set the world matrix.

- `getWorldMatrix`: getWorldMatrix(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Return the world matrix.

- `setViewMatrix`: setViewMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -&gt; None<br>        <br>        Set the view matrix.

- `getViewMatrix`: getViewMatrix(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Return the view matrix.

- `setProjectionMatrix`: setProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -&gt; None<br>        <br>        Set the projection matrix.

- `getProjectionMatrix`: getProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Return the projection matrix.

- `getWorldViewProjMatrix`: getWorldViewProjMatrix(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Compute our full model-view-projection matrix.

- `getViewPosition`: getViewPosition(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Derive viewer position from the view matrix.

- `getViewDirection`: getViewDirection(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Derive viewer direction from the view matrix.

- `setViewportSize`: setViewportSize(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; None<br>        <br>        Set the size of the viewport window.

- `getViewportSize`: getViewportSize(self: MaterialX.PyMaterialXRender.Camera) -&gt; MaterialX.PyMaterialXCore.Vector2<br>        <br>        Return the size of the viewport window.

- `projectToViewport`: projectToViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Project a position from object to viewport space.

- `unprojectFromViewport`: unprojectFromViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Unproject a position from viewport to object space.

- `createViewMatrix`: createViewMatrix(arg0: MaterialX.PyMaterialXCore.Vector3, arg1: MaterialX.PyMaterialXCore.Vector3, arg2: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create a view matrix given an eye position, a target position and an up vector.

- `createPerspectiveMatrix`: createPerspectiveMatrix(arg0: typing.SupportsFloat, arg1: typing.SupportsFloat, arg2: typing.SupportsFloat, arg3: typing.SupportsFloat, arg4: typing.SupportsFloat, arg5: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create a perspective projection matrix given a set of clip planes with [-1,1] projected Z.

- `createOrthographicMatrix`: createOrthographicMatrix(arg0: typing.SupportsFloat, arg1: typing.SupportsFloat, arg2: typing.SupportsFloat, arg3: typing.SupportsFloat, arg4: typing.SupportsFloat, arg5: typing.SupportsFloat) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Create an orthographic projection matrix given a set of clip planes with [-1,1] projected Z.

- `transformPointPerspective`: transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Apply a perspective transform to the given 3D point, performing a homogeneous divide on the transformed result.

<hr><h4>3. <a id='materialx-pymaterialxrender-cgltfloader'>CgltfLoader</a></h4>

Wrapper for loader to read in GLTF files using the Cgltf library.

##### Inheritance
- [GeometryLoader](#materialx-pymaterialxrender-geometryloader)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.CgltfLoader<br>        <br>        Create a new loader.

- `load`: load(self: MaterialX.PyMaterialXRender.CgltfLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -&gt; bool<br>        <br>        Load geometry from file path.

<hr><h4>4. <a id='materialx-pymaterialxrender-exceptionrendererror'>ExceptionRenderError</a></h4>



##### Inheritance
- [Exception](#materialx-pymaterialxrender-exception)
- [BaseException](#materialx-pymaterialxrender-baseexception)
<hr><h4>5. <a id='materialx-pymaterialxrender-geometryhandler'>GeometryHandler</a></h4>

Class which holds a set of geometry loaders.

Each loader is associated with a given set of file extensions.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.GeometryHandler<br>        <br>        Create a new geometry handler.

- `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.GeometryLoader) -&gt; None<br>        <br>        Add a geometry loader.<br>        <br>        Args:<br>            loader: Loader to add to list of available loaders.

- `clearGeometry`: clearGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler) -&gt; None<br>        <br>        Clear all loaded geometry.

- `hasGeometry`: hasGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: str) -&gt; bool

- `getGeometry`: getGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg1: str) -&gt; None

- `loadGeometry`: loadGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: bool) -&gt; bool<br>        <br>        Load geometry from a given location.<br>        <br>        Args:<br>            filePath: Path to geometry<br>            texcoordVerticalFlip: Flip texture coordinates in V. Default is to not flip.

- `getMeshes`: getMeshes(self: MaterialX.PyMaterialXRender.GeometryHandler) -&gt; list[MaterialX.PyMaterialXRender.Mesh]<br>        <br>        Get list of meshes.

- `findParentMesh`: findParentMesh(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.MeshPartition) -&gt; MaterialX.PyMaterialXRender.Mesh<br>        <br>        Return the first mesh in our list containing the given partition.<br>        <br>        If no matching mesh is found, then nullptr is returned.

- `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the minimum bounds for all meshes.

- `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the minimum bounds for all meshes.

<hr><h4>6. <a id='materialx-pymaterialxrender-geometryloader'>GeometryLoader</a></h4>

Base class representing a geometry loader.

A loader can be associated with one or more file extensions.

##### Methods

- `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.GeometryLoader) -&gt; set[str]<br>        <br>        Returns a list of supported extensions.<br>        <br>        Returns:<br>            List of support extensions

- `load`: load(self: MaterialX.PyMaterialXRender.GeometryLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -&gt; bool<br>        <br>        Load geometry from disk.<br>        <br>        Args:<br>            filePath: Path to file to load<br>            meshList: List of meshes to update<br>            texcoordVerticalFlip: Flip texture coordinates in V when loading<br>        <br>        Returns:<br>            True if load was successful

<hr><h4>7. <a id='materialx-pymaterialxrender-image'>Image</a></h4>

Class representing an image in system memory.

##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt, arg3: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Create an empty image with the given properties.

- `getWidth`: getWidth(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the width of the image.

- `getHeight`: getHeight(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the height of the image.

- `getChannelCount`: getChannelCount(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the channel count of the image.

- `getBaseType`: getBaseType(self: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.BaseType<br>        <br>        Return the base type of the image.

- `getBaseStride`: getBaseStride(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the stride of our base type in bytes.

- `getMaxMipCount`: getMaxMipCount(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the maximum number of mipmaps for this image.

- `setTexelColor`: setTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXCore.Color4) -&gt; None<br>        <br>        Set the texel color at the given coordinates.<br>        <br>        If the coordinates or image resource buffer are invalid, then an exception is thrown.

- `getTexelColor`: getTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -&gt; MaterialX.PyMaterialXCore.Color4<br>        <br>        Return the texel color at the given coordinates.<br>        <br>        If the coordinates or image resource buffer are invalid, then an exception is thrown.

- `isUniformColor`: isUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -&gt; bool<br>        <br>        Return true if all texels of this image are identical in color.<br>        <br>        Args:<br>            uniformColor: Return the uniform color of the image, if any.

- `setUniformColor`: setUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -&gt; None<br>        <br>        Set all texels of this image to a uniform color.

- `applyMatrixTransform`: applyMatrixTransform(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Matrix33) -&gt; None<br>        <br>        Apply the given matrix transform to all texels of this image.

- `applyGammaTransform`: applyGammaTransform(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsFloat) -&gt; None<br>        <br>        Apply the given gamma transform to all texels of this image.

- `copy`: copy(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt, arg1: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Create a copy of this image with the given channel count and base type.

- `applyBoxBlur`: applyBoxBlur(self: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Apply a 3x3 box blur to this image, returning a new blurred image.

- `applyGaussianBlur`: applyGaussianBlur(self: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Apply a 7x7 Gaussian blur to this image, returning a new blurred image.

- `applyBoxDownsample`: applyBoxDownsample(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsInt) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Downsample this image by an integer factor using a box filter, returning the new reduced image.

- `splitByLuminance`: splitByLuminance(self: MaterialX.PyMaterialXRender.Image, arg0: typing.SupportsFloat) -&gt; tuple[MaterialX.PyMaterialXRender.Image, MaterialX.PyMaterialXRender.Image]<br>        <br>        Split this image by the given luminance threshold, returning the resulting underflow and overflow images.

- `setResourceBuffer`: setResourceBuffer(self: MaterialX.PyMaterialXRender.Image, arg0: typing_extensions.CapsuleType) -&gt; None<br>        <br>        Set the resource buffer for this image.

- `getResourceBuffer`: getResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -&gt; int<br>        <br>        Return the resource buffer for this image.

- `createResourceBuffer`: createResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -&gt; None<br>        <br>        Allocate a resource buffer for this image that matches its properties.

- `releaseResourceBuffer`: releaseResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -&gt; None<br>        <br>        Release the resource buffer for this image.

- `setResourceBufferDeallocator`: setResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image, arg0: collections.abc.Callable[[typing_extensions.CapsuleType], None]) -&gt; None<br>        <br>        Set the resource buffer deallocator for this image.

- `getResourceBufferDeallocator`: getResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image) -&gt; collections.abc.Callable[[typing_extensions.CapsuleType], None]<br>        <br>        Return the resource buffer deallocator for this image.

<hr><h4>8. <a id='materialx-pymaterialxrender-imagebufferdeallocator'>ImageBufferDeallocator</a></h4>



<hr><h4>9. <a id='materialx-pymaterialxrender-imagehandler'>ImageHandler</a></h4>

Base image handler class.

Keeps track of images which are loaded from disk via supplied ImageLoader. Derived classes are responsible for determining how to perform the logic for "binding" of these resources for a given target (such as a given shading language).

##### Methods

- `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -&gt; MaterialX.PyMaterialXRender.ImageHandler

- `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.ImageLoader) -&gt; None<br>        <br>        Add another image loader to the handler, which will be invoked if existing loaders cannot load a given image.

- `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, image: MaterialX.PyMaterialXRender.Image, verticalFlip: bool = False) -&gt; bool<br>        <br>        Save image to disk.<br>        <br>        Args:<br>            filePath: File path to be written<br>            image: The image to be saved<br>            verticalFlip: Whether the image should be flipped in Y during save<br>        <br>        Returns:<br>            if save succeeded

- `acquireImage`: acquireImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = &lt;MaterialX.PyMaterialXCore.Color4 object at 0x1030849f0&gt;) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Acquire an image from the cache or file system.<br>        <br>        Args:<br>            filePath: File path of the image.<br>            defaultColor: Default color to use as a fallback for missing images.<br>        <br>        Returns:<br>            On success, a shared pointer to the acquired image.

- `bindImage`: bindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -&gt; bool<br>        <br>        Bind an image for rendering.<br>        <br>        Args:<br>            image: The image to bind.<br>            samplingProperties: Sampling properties for the image.

- `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image) -&gt; bool<br>        <br>        Unbind an image, making it no longer active for rendering.<br>        <br>        Args:<br>            image: The image to unbind.

- `unbindImages`: unbindImages(self: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None<br>        <br>        Unbind all images that are currently stored in the cache.

- `setSearchPath`: setSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; None<br>        <br>        Set the search path to be used for finding images on the file system.

- `getSearchPath`: getSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler) -&gt; MaterialX.PyMaterialXFormat.FileSearchPath<br>        <br>        Return the image search path.

- `setFilenameResolver`: setFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.StringResolver) -&gt; None<br>        <br>        Set the filename resolver for images.

- `getFilenameResolver`: getFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler) -&gt; MaterialX.PyMaterialXCore.StringResolver<br>        <br>        Return the filename resolver for images.

- `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -&gt; bool<br>        <br>        Create rendering resources for the given image.

- `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, image: MaterialX.PyMaterialXRender.Image = None) -&gt; None<br>        <br>        Release rendering resources for the given image, or for all cached images if no image pointer is specified.

- `clearImageCache`: clearImageCache(self: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None<br>        <br>        Clear the contents of the image cache, first releasing any render resources associated with cached images.

- `getZeroImage`: getZeroImage(self: MaterialX.PyMaterialXRender.ImageHandler) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Return a fallback image with zeroes in all channels.

- `getReferencedImages`: getReferencedImages(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.Document) -&gt; list[MaterialX.PyMaterialXRender.Image]<br>        <br>        Acquire all images referenced by the given document, and return the images in a vector.

<hr><h4>10. <a id='materialx-pymaterialxrender-imageloader'>ImageLoader</a></h4>

Abstract base class for file-system image loaders.

##### Methods

- `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.ImageLoader) -&gt; set[str]<br>        <br>        Returns a list of supported extensions.<br>        <br>        Returns:<br>            List of support extensions

- `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -&gt; bool<br>        <br>        Save an image to the file system.<br>        <br>        Args:<br>            filePath: File path to be written<br>            image: The image to be saved<br>            verticalFlip: Whether the image should be flipped in Y during save<br>        <br>        Returns:<br>            if save succeeded

- `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Load an image from the file system.<br>        <br>        Args:<br>            filePath: The requested image file path.<br>        <br>        Returns:<br>            On success, a shared pointer to the loaded image; otherwise an empty shared pointer.

##### Attributes

- `BMP_EXTENSION` = 'bmp'
- `EXR_EXTENSION` = 'exr'
- `GIF_EXTENSION` = 'gif'
- `HDR_EXTENSION` = 'hdr'
- `JPG_EXTENSION` = 'jpg'
- `JPEG_EXTENSION` = 'jpeg'
- `PIC_EXTENSION` = 'pic'
- `PNG_EXTENSION` = 'png'
- `PSD_EXTENSION` = 'psd'
- `TGA_EXTENSION` = 'tga'
- `TIF_EXTENSION` = 'tif'
- `TIFF_EXTENSION` = 'tiff'
- `TXT_EXTENSION` = 'txt'
<hr><h4>11. <a id='materialx-pymaterialxrender-imagesamplingproperties'>ImageSamplingProperties</a></h4>

Interface to describe sampling properties for images.

##### Attributes

- `uaddressMode` = (property)
- `vaddressMode` = (property)
- `filterType` = (property)
- `defaultColor` = (property)
<hr><h4>12. <a id='materialx-pymaterialxrender-lighthandler'>LightHandler</a></h4>

Utility light handler for creating and providing light data for shader binding.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.LightHandler<br>        <br>        Create a new light handler.

- `setLightTransform`: setLightTransform(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Matrix44) -&gt; None<br>        <br>        Set the light transform.

- `getLightTransform`: getLightTransform(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; MaterialX.PyMaterialXCore.Matrix44<br>        <br>        Return the light transform.

- `setDirectLighting`: setDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -&gt; None<br>        <br>        Set whether direct lighting is enabled.

- `getDirectLighting`: getDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; bool<br>        <br>        Return whether direct lighting is enabled.

- `setIndirectLighting`: setIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -&gt; None<br>        <br>        Set whether indirect lighting is enabled.

- `getIndirectLighting`: getIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; bool<br>        <br>        Return whether indirect lighting is enabled.

- `setEnvRadianceMap`: setEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -&gt; None<br>        <br>        Set the environment radiance map.

- `getEnvRadianceMap`: getEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; MaterialX_v1_39_5::Image<br>        <br>        Return the environment radiance map.

- `setEnvIrradianceMap`: setEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -&gt; None<br>        <br>        Set the environment irradiance map.

- `getEnvIrradianceMap`: getEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; MaterialX_v1_39_5::Image<br>        <br>        Return the environment irradiance map.

- `setAlbedoTable`: setAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -&gt; None<br>        <br>        Set the directional albedo table.

- `getAlbedoTable`: getAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; MaterialX_v1_39_5::Image<br>        <br>        Return the directional albedo table.

- `setEnvSampleCount`: setEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Set the environment lighting sample count.

- `getEnvSampleCount`: getEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; int<br>        <br>        Return the environment lighting sample count.

- `setRefractionTwoSided`: setRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -&gt; None<br>        <br>        Set the two-sided refraction property.

- `getRefractionTwoSided`: getRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; int<br>        <br>        Return the two-sided refraction property.

- `addLightSource`: addLightSource(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Node) -&gt; None<br>        <br>        Add a light source.

- `setLightSources`: setLightSources(self: MaterialX.PyMaterialXRender.LightHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -&gt; None<br>        <br>        Set the vector of light sources.

- `getLightSources`: getLightSources(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; list[MaterialX.PyMaterialXCore.Node]<br>        <br>        Return the vector of light sources.

- `getFirstLightOfCategory`: getFirstLightOfCategory(self: MaterialX.PyMaterialXRender.LightHandler, arg0: str) -&gt; MaterialX.PyMaterialXCore.Node<br>        <br>        Return the first light source, if any, of the given category.

- `getLightIdMap`: getLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler) -&gt; dict[str, int]<br>        <br>        Get a list of identifiers associated with a given light nodedef.

- `computeLightIdMap`: computeLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -&gt; dict[str, int]<br>        <br>        From a set of nodes, create a mapping of corresponding nodedef identifiers to numbers.

- `findLights`: findLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node]) -&gt; None<br>        <br>        Find lights to use based on an input document.<br>        <br>        Args:<br>            doc: Document to scan for lights<br>            lights: List of lights found in document

- `registerLights`: registerLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: collections.abc.Sequence[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -&gt; None<br>        <br>        Register light node definitions and light count with a given generation context.<br>        <br>        Args:<br>            doc: Document containing light nodes and definitions<br>            lights: Lights to register<br>            context: Context to update

<hr><h4>13. <a id='materialx-pymaterialxrender-mesh'>Mesh</a></h4>

Container for mesh data.

##### Methods

- `create`: create(arg0: str) -&gt; MaterialX.PyMaterialXRender.Mesh<br>        <br>        Create a new mesh.

- `getName`: getName(self: MaterialX.PyMaterialXRender.Mesh) -&gt; str<br>        <br>        Return the name of this mesh.

- `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -&gt; None<br>        <br>        Set the mesh&#39;s source URI.

- `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -&gt; bool<br>        <br>        Return true if this mesh has a source URI.

- `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -&gt; str<br>        <br>        Return the mesh&#39;s source URI.

- `getStream`: getStream(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: typing.SupportsInt) -&gt; MaterialX.PyMaterialXRender.MeshStream

- `addStream`: addStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -&gt; None<br>        <br>        Add a mesh stream.

- `setVertexCount`: setVertexCount(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Set vertex count.

- `getVertexCount`: getVertexCount(self: MaterialX.PyMaterialXRender.Mesh) -&gt; int<br>        <br>        Get vertex count.

- `setMinimumBounds`: setMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; None<br>        <br>        Set the minimum bounds for the geometry.

- `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the minimum bounds for the geometry.

- `setMaximumBounds`: setMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; None<br>        <br>        Set the minimum bounds for the geometry.

- `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return the minimum bounds for the geometry.

- `setSphereCenter`: setSphereCenter(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -&gt; None<br>        <br>        Set center of the bounding sphere.

- `getSphereCenter`: getSphereCenter(self: MaterialX.PyMaterialXRender.Mesh) -&gt; MaterialX.PyMaterialXCore.Vector3<br>        <br>        Return center of the bounding sphere.

- `setSphereRadius`: setSphereRadius(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsFloat) -&gt; None<br>        <br>        Set radius of the bounding sphere.

- `getSphereRadius`: getSphereRadius(self: MaterialX.PyMaterialXRender.Mesh) -&gt; float<br>        <br>        Return radius of the bounding sphere.

- `getPartitionCount`: getPartitionCount(self: MaterialX.PyMaterialXRender.Mesh) -&gt; int<br>        <br>        Return the number of mesh partitions.

- `addPartition`: addPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshPartition) -&gt; None<br>        <br>        Add a partition.

- `getPartition`: getPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: typing.SupportsInt) -&gt; MaterialX.PyMaterialXRender.MeshPartition<br>        <br>        Return a reference to a mesh partition.

- `generateTextureCoordinates`: generateTextureCoordinates(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        Create texture coordinates from the given positions.<br>        <br>        Args:<br>            positionStream: Input position stream<br>        <br>        Returns:<br>            The generated texture coordinate stream

- `generateNormals`: generateNormals(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        Generate face normals from the given positions.<br>        <br>        Args:<br>            positionStream: Input position stream<br>        <br>        Returns:<br>            The generated normal stream

- `generateTangents`: generateTangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream, arg2: MaterialX.PyMaterialXRender.MeshStream) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        Generate tangents from the given positions, normals, and texture coordinates.<br>        <br>        Args:<br>            positionStream: Input position stream<br>            normalStream: Input normal stream<br>            texcoordStream: Input texcoord stream<br>        <br>        Returns:<br>            The generated tangent stream, on success; otherwise, a null pointer.

- `generateBitangents`: generateBitangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        Generate bitangents from the given normals and tangents.<br>        <br>        Args:<br>            normalStream: Input normal stream<br>            tangentStream: Input tangent stream<br>        <br>        Returns:<br>            The generated bitangent stream, on success; otherwise, a null pointer.

- `mergePartitions`: mergePartitions(self: MaterialX.PyMaterialXRender.Mesh) -&gt; None<br>        <br>        Merge all mesh partitions into one.

- `splitByUdims`: splitByUdims(self: MaterialX.PyMaterialXRender.Mesh) -&gt; None<br>        <br>        Split the mesh into a single partition per UDIM.

<hr><h4>14. <a id='materialx-pymaterialxrender-meshpartition'>MeshPartition</a></h4>

Class that describes a sub-region of a mesh using vertex indexing.

Note that a face is considered to be a triangle.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.MeshPartition<br>        <br>        Create a new mesh partition.

- `resize`: resize(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Resize data to the given number of indices.

- `setName`: setName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -&gt; None<br>        <br>        Set the name of this partition.

- `getName`: getName(self: MaterialX.PyMaterialXRender.MeshPartition) -&gt; str<br>        <br>        Return the name of this partition.

- `addSourceName`: addSourceName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -&gt; None<br>        <br>        Add a source name, representing a partition that was processed to generate this one.

- `getSourceNames`: getSourceNames(self: MaterialX.PyMaterialXRender.MeshPartition) -&gt; set[str]<br>        <br>        Return the vector of source names, representing all partitions that were processed to generate this one.

- `getIndices`: getIndices(self: MaterialX.PyMaterialXRender.MeshPartition) -&gt; list[int]

- `getFaceCount`: getFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition) -&gt; int<br>        <br>        Return number of faces.

- `setFaceCount`: setFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Set face count.

<hr><h4>15. <a id='materialx-pymaterialxrender-meshstream'>MeshStream</a></h4>

Class to represent a mesh data stream.

##### Methods

- `create`: create(arg0: str, arg1: str, arg2: typing.SupportsInt) -&gt; MaterialX.PyMaterialXRender.MeshStream<br>        <br>        Create a new mesh stream.

- `reserve`: reserve(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Reserve memory for a given number of elements.

- `resize`: resize(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Resize data to an given number of elements.

- `getName`: getName(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; str<br>        <br>        Get stream name.

- `getType`: getType(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; str<br>        <br>        Get stream attribute name.

- `getIndex`: getIndex(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; int<br>        <br>        Get stream index.

- `getData`: getData(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; list[float]

- `getStride`: getStride(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; int<br>        <br>        Get stride between elements.

- `setStride`: setStride(self: MaterialX.PyMaterialXRender.MeshStream, arg0: typing.SupportsInt) -&gt; None<br>        <br>        Set stride between elements.

- `getSize`: getSize(self: MaterialX.PyMaterialXRender.MeshStream) -&gt; int<br>        <br>        Get the number of elements.

- `transform`: transform(self: MaterialX.PyMaterialXRender.MeshStream, arg0: MaterialX.PyMaterialXCore.Matrix44) -&gt; None<br>        <br>        Transform elements by a matrix.

##### Attributes

- `POSITION_ATTRIBUTE` = 'position'
- `NORMAL_ATTRIBUTE` = 'normal'
- `TEXCOORD_ATTRIBUTE` = 'texcoord'
- `TANGENT_ATTRIBUTE` = 'tangent'
- `BITANGENT_ATTRIBUTE` = 'bitangent'
- `COLOR_ATTRIBUTE` = 'color'
- `GEOMETRY_PROPERTY_ATTRIBUTE` = 'geomprop'
<hr><h4>16. <a id='materialx-pymaterialxrender-shaderrenderer'>ShaderRenderer</a></h4>

Base class for renderers that generate shader code to produce images.

##### Methods

- `initialize`: initialize(self: MaterialX.PyMaterialXRender.ShaderRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -&gt; None<br>        <br>        Initialize the renderer.

- `setCamera`: setCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.Camera) -&gt; None<br>        <br>        Set the camera.

- `getCamera`: getCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; MaterialX.PyMaterialXRender.Camera<br>        <br>        Return the camera.

- `setImageHandler`: setImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None<br>        <br>        Set the image handler used by this renderer for image I/O.

- `getImageHandler`: getImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; MaterialX.PyMaterialXRender.ImageHandler<br>        <br>        Return the image handler.

- `setLightHandler`: setLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.LightHandler) -&gt; None<br>        <br>        Set the light handler used by this renderer for light bindings.

- `getLightHandler`: getLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; MaterialX.PyMaterialXRender.LightHandler<br>        <br>        Return the light handler.

- `setGeometryHandler`: setGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.GeometryHandler) -&gt; None<br>        <br>        Set the geometry handler.

- `getGeometryHandler`: getGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; MaterialX.PyMaterialXRender.GeometryHandler<br>        <br>        Return the geometry handler.

- `createProgram`: createProgram(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None<br>        <br>        2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: collections.abc.Mapping[str, str]) -&gt; None

- `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; None<br>        <br>        Validate inputs for the program.

- `updateUniform`: updateUniform(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -&gt; None<br>        <br>        Update the program with value of the uniform.

- `setSize`: setSize(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -&gt; None<br>        <br>        Set the size of the rendered image.

- `render`: render(self: MaterialX.PyMaterialXRender.ShaderRenderer) -&gt; None<br>        <br>        Render the current program to produce an image.

<hr><h4>17. <a id='materialx-pymaterialxrender-stbimageloader'>StbImageLoader</a></h4>

Stb image file loader.

##### Inheritance
- [ImageLoader](#materialx-pymaterialxrender-imageloader)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.StbImageLoader<br>        <br>        Create a new stb image loader.

- `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -&gt; bool<br>        <br>        Save an image to the file system.

- `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Load an image from the file system.

<hr><h4>18. <a id='materialx-pymaterialxrender-tinyobjloader'>TinyObjLoader</a></h4>

Wrapper for geometry loader to read in OBJ files using the TinyObj library.

##### Inheritance
- [GeometryLoader](#materialx-pymaterialxrender-geometryloader)
##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRender.TinyObjLoader<br>        <br>        Create a new TinyObjLoader.

- `load`: load(self: MaterialX.PyMaterialXRender.TinyObjLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: collections.abc.Sequence[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -&gt; bool<br>        <br>        Load geometry from disk.


### Functions

- `createImageStrip`: createImageStrip(arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Image]) -> MaterialX.PyMaterialXRender.Image

Create a horizontal image strip from a vector of images with identical resolutions and formats.

- `createUniformImage`: createUniformImage(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: typing.SupportsInt, arg3: MaterialX.PyMaterialXRender.BaseType, arg4: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXRender.Image

Create a uniform-color image with the given properties.

- `getMaxDimensions`: getMaxDimensions(arg0: collections.abc.Sequence[MaterialX.PyMaterialXRender.Image]) -> tuple[int, int]

Compute the maximum width and height of all images in the given vector.


### Globals

- `FLOAT`
 = (BaseType.FLOAT: 5)
- `HALF`
 = (BaseType.HALF: 4)
- `INT16`
 = (BaseType.INT16: 3)
- `INT8`
 = (BaseType.INT8: 1)
- `UINT16`
 = (BaseType.UINT16: 2)
- `UINT8`
 = (BaseType.UINT8: 0)

---

## 10. Module: MaterialX.PyMaterialXRenderGlsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxrenderglsl-gltexturehandler'>GLTextureHandler</a></h4>

An OpenGL texture handler class.

##### Inheritance
- [ImageHandler](#materialx-pymaterialxrenderglsl-imagehandler)
##### Methods

- `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -&gt; MaterialX.PyMaterialXRender.ImageHandler

- `bindImage`: bindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -&gt; bool<br>        <br>        Bind an image.<br>        <br>        This method will bind the texture to an active texture unit as defined by the corresponding image description. The method will fail if there are not enough available image units to bind to.

- `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -&gt; bool<br>        <br>        Unbind an image.

- `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -&gt; bool<br>        <br>        Create rendering resources for the given image.

- `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -&gt; None<br>        <br>        Release rendering resources for the given image, or for all cached images if no image pointer is specified.

<hr><h4>2. <a id='materialx-pymaterialxrenderglsl-glslprogram'>GlslProgram</a></h4>

A class representing an executable GLSL program.

There are two main interfaces which can be used. One which takes in a HwShader and one which allows for explicit setting of shader stage code.

##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRenderGlsl.GlslProgram<br>        <br>        Create a GLSL program instance.

- `setStages`: setStages(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None<br>        <br>        Set up code stages to validate based on an input hardware shader.<br>        <br>        Args:<br>            shader: Hardware shader to use

- `addStage`: addStage(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: str) -&gt; None<br>        <br>        Set the code stages based on a list of stage strings.<br>        <br>        Args:<br>            stage: Name of the shader stage.<br>            sourceCode: Source code of the shader stage.

- `getStageSourceCode`: getStageSourceCode(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str) -&gt; str<br>        <br>        Get source code string for a given stage.<br>        <br>        Returns:<br>            Shader stage string. String is empty if not found.

- `getShader`: getShader(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; MaterialX.PyMaterialXGenShader.Shader<br>        <br>        Return the shader, if any, used to generate this program.

- `build`: build(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; None<br>        <br>        Build shader program data from the source code set for each shader stage.<br>        <br>        An exception is thrown if the program cannot be built. The exception will contain a list of compilation errors.

- `hasBuiltData`: hasBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; bool<br>        <br>        Return true if built shader program data is present.

- `clearBuiltData`: clearBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; None

- `getUniformsList`: getUniformsList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; dict[str, MaterialX_v1_39_5::GlslProgram::Input]<br>        <br>        Get list of program input uniforms.<br>        <br>        Returns:<br>            Program uniforms list.

- `getAttributesList`: getAttributesList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; dict[str, MaterialX_v1_39_5::GlslProgram::Input]<br>        <br>        Get list of program input attributes.<br>        <br>        Returns:<br>            Program attributes list.

- `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg2: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg3: bool) -&gt; None<br>        <br>        Find the locations in the program which starts with a given variable name.<br>        <br>        Args:<br>            variable: Variable to search for<br>            variableList: List of program inputs to search<br>            foundList: Returned list of found program inputs. Empty if none found.<br>            exactMatch: Search for exact variable name match.

- `bind`: bind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; bool<br>        <br>        Bind the program.<br>        <br>        Returns:<br>            False if failed

- `hasActiveAttributes`: hasActiveAttributes(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; bool<br>        <br>        Return true if the program has active attributes.

- `bindUniform`: bindUniform(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -&gt; None<br>        <br>        Bind a value to the uniform with the given name.

- `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: collections.abc.Mapping[str, MaterialX_v1_39_5::GlslProgram::Input], arg1: MaterialX.PyMaterialXRender.Mesh) -&gt; None<br>        <br>        Bind attribute buffers to attribute inputs.<br>        <br>        Args:<br>            inputs: Attribute inputs to bind to<br>            mesh: Mesh containing streams to bind

- `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -&gt; None<br>        <br>        Bind input geometry partition (indexing).

- `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Mesh) -&gt; None<br>        <br>        Bind input geometry streams.

- `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; None<br>        <br>        Unbind any bound geometry.

- `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None<br>        <br>        Bind any input textures.

- `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None<br>        <br>        Bind lighting.

- `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -&gt; None<br>        <br>        Bind view information.

- `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, time: typing.SupportsFloat = 0.0, frame: typing.SupportsFloat = 1.0) -&gt; None<br>        <br>        Bind time and frame.

- `unbind`: unbind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -&gt; None<br>        <br>        Unbind the program. Equivalent to binding no program.

##### Attributes

- `UNDEFINED_OPENGL_RESOURCE_ID` = 0
- `UNDEFINED_OPENGL_PROGRAM_LOCATION` = -1
<hr><h4>3. <a id='materialx-pymaterialxrenderglsl-glslrenderer'>GlslRenderer</a></h4>

Helper class for rendering generated GLSL code to produce images.

There are two main interfaces which can be used. One which takes in a HwShader and one which allows for explicit setting of shader stage code.

The main services provided are: Validation: All shader stages are compiled and atteched to a GLSL shader program. Introspection: The compiled shader program is examined for uniforms and attributes. Binding: Uniforms and attributes which match the predefined variables generated the GLSL code generator will have values assigned to this. This includes matrices, attribute streams, and textures. Rendering: The program with bound inputs will be used to drawing geometry to an offscreen buffer. An interface is provided to save this offscreen buffer to disk using an externally defined image handler.

##### Inheritance
- [ShaderRenderer](#materialx-pymaterialxrenderglsl-shaderrenderer)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRenderGlsl.GlslRenderer<br>        <br>        Create a GLSL renderer instance.

- `initialize`: initialize(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -&gt; None<br>        <br>        Internal initialization of stages and OpenGL constructs required for program validation and rendering.<br>        <br>        Args:<br>            renderContextHandle: allows initializing the GlslRenderer with a Shared OpenGL Context

- `createProgram`: createProgram(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None<br>        <br>        2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: collections.abc.Mapping[str, str]) -&gt; None

- `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -&gt; None<br>        <br>        Validate inputs for the program.

- `render`: render(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -&gt; None<br>        <br>        Render the current program to an offscreen buffer.

- `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -&gt; None<br>        <br>        Render the current program in texture space to an off-screen buffer.

- `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Capture the current contents of the off-screen hardware buffer as an image.

- `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -&gt; MaterialX.PyMaterialXRenderGlsl.GlslProgram<br>        <br>        Return the GLSL program.

<hr><h4>4. <a id='materialx-pymaterialxrenderglsl-input'>Input</a></h4>

An input element within a Node or NodeDef.

An Input holds either a uniform value or a connection to a spatially-varying Output, either of which may be modified within the scope of a Material.

##### Attributes

- `INVALID_OPENGL_TYPE` = -1
- `location` = (property)
- `gltype` = (property)
- `size` = (property)
- `typeString` = (property)
- `value` = (property)
- `isConstant` = (property)
- `path` = (property)
<hr><h4>5. <a id='materialx-pymaterialxrenderglsl-texturebaker'>TextureBaker</a></h4>

A helper class for baking procedural material content to textures.

TODO: Add support for graphs containing geometric nodes such as position and normal.

##### Inheritance
- [GlslRenderer](#materialx-pymaterialxrenderglsl-glslrenderer)
- [ShaderRenderer](#materialx-pymaterialxrenderglsl-shaderrenderer)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRenderGlsl.TextureBaker

- `setExtension`: setExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getExtension`: getExtension(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setDistanceUnit`: setDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getDistanceUnit`: getDistanceUnit(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setAverageImages`: setAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -&gt; None

- `getAverageImages`: getAverageImages(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; bool

- `setOptimizeConstants`: setOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -&gt; None

- `getOptimizeConstants`: getOptimizeConstants(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; bool

- `setOutputImagePath`: setOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None

- `getOutputImagePath`: getOutputImagePath(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; MaterialX.PyMaterialXFormat.FilePath

- `setBakedGraphName`: setBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getBakedGraphName`: getBakedGraphName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setBakedGeomInfoName`: setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getBakedGeomInfoName`: getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setTextureFilenameTemplate`: setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str) -&gt; None

- `getTextureFilenameTemplate`: getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; str

- `setFilenameTemplateVarOverride`: setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: str, arg1: str) -&gt; None

- `setHashImageNames`: setHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -&gt; None

- `getHashImageNames`: getHashImageNames(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; bool

- `setTextureSpaceMin`: setTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; None

- `getTextureSpaceMin`: getTextureSpaceMin(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; MaterialX.PyMaterialXCore.Vector2

- `setTextureSpaceMax`: setTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; None

- `getTextureSpaceMax`: getTextureSpaceMax(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker) -&gt; MaterialX.PyMaterialXCore.Vector2

- `setupUnitSystem`: setupUnitSystem(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None

- `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: collections.abc.Sequence[str], arg4: str) -&gt; MaterialX.PyMaterialXCore.Document

- `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -&gt; None

- `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -&gt; None


---

## 11. Module: MaterialX.PyMaterialXRenderMsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxrendermsl-input'>Input</a></h4>



##### Attributes

- `location` = (property)
- `size` = (property)
- `typeString` = (property)
- `value` = (property)
- `isConstant` = (property)
- `path` = (property)
<hr><h4>2. <a id='materialx-pymaterialxrendermsl-metaltexturehandler'>MetalTextureHandler</a></h4>



##### Inheritance
- [ImageHandler](#materialx-pymaterialxrendermsl-imagehandler)
##### Methods

- `create`: create(arg0: objc_object&lt;MTLDevice&gt;, arg1: MaterialX.PyMaterialXRender.ImageLoader) -&gt; MaterialX.PyMaterialXRenderMsl.MetalTextureHandler

- `bindImage`: bindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -&gt; bool

- `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -&gt; bool

- `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -&gt; bool

- `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderMsl.MetalTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -&gt; None

<hr><h4>3. <a id='materialx-pymaterialxrendermsl-mslprogram'>MslProgram</a></h4>



##### Methods

- `create`: create() -&gt; MaterialX.PyMaterialXRenderMsl.MslProgram

- `setStages`: setStages(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None

- `addStage`: addStage(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: str) -&gt; None

- `getStageSourceCode`: getStageSourceCode(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str) -&gt; str

- `getShader`: getShader(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -&gt; MaterialX.PyMaterialXGenShader.Shader

- `build`: build(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLDevice&gt;, arg1: MaterialX_v1_39_5::MetalFramebuffer) -&gt; objc_object&lt;MTLRenderPipelineState&gt;

- `prepareUsedResources`: prepareUsedResources(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLRenderCommandEncoder&gt;, arg1: MaterialX.PyMaterialXRender.Camera, arg2: MaterialX.PyMaterialXRender.GeometryHandler, arg3: MaterialX.PyMaterialXRender.ImageHandler, arg4: MaterialX.PyMaterialXRender.LightHandler) -&gt; None

- `getUniformsList`: getUniformsList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -&gt; dict[str, MaterialX_v1_39_5::MslProgram::Input]

- `getAttributesList`: getAttributesList(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -&gt; dict[str, MaterialX_v1_39_5::MslProgram::Input]

- `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg2: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg3: bool) -&gt; None

- `bind`: bind(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLRenderCommandEncoder&gt;) -&gt; bool

- `bindUniform`: bindUniform(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -&gt; None

- `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLRenderCommandEncoder&gt;, arg1: collections.abc.Mapping[str, MaterialX_v1_39_5::MslProgram::Input], arg2: MaterialX.PyMaterialXRender.Mesh) -&gt; None

- `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -&gt; None

- `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLRenderCommandEncoder&gt;, arg1: MaterialX.PyMaterialXRender.Mesh) -&gt; None

- `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderMsl.MslProgram) -&gt; None

- `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: objc_object&lt;MTLRenderCommandEncoder&gt;, arg1: MaterialX.PyMaterialXRender.LightHandler, arg2: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None

- `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -&gt; None

- `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderMsl.MslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -&gt; None

- `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderMsl.MslProgram, time: typing.SupportsFloat = 0.0, frame: typing.SupportsFloat = 1.0) -&gt; None

<hr><h4>4. <a id='materialx-pymaterialxrendermsl-mslrenderer'>MslRenderer</a></h4>



##### Inheritance
- [ShaderRenderer](#materialx-pymaterialxrendermsl-shaderrenderer)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRenderMsl.MslRenderer

- `initialize`: initialize(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -&gt; None

- `createProgram`: createProgram(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None<br>        <br>        2. createProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: collections.abc.Mapping[str, str]) -&gt; None

- `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -&gt; None

- `render`: render(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -&gt; None

- `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -&gt; None

- `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderMsl.MslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.Image

- `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderMsl.MslRenderer) -&gt; MaterialX.PyMaterialXRenderMsl.MslProgram

<hr><h4>5. <a id='materialx-pymaterialxrendermsl-texturebaker'>TextureBaker</a></h4>



##### Inheritance
- [MslRenderer](#materialx-pymaterialxrendermsl-mslrenderer)
- [ShaderRenderer](#materialx-pymaterialxrendermsl-shaderrenderer)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRenderMsl.TextureBaker

- `setExtension`: setExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getExtension`: getExtension(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setDistanceUnit`: setDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getDistanceUnit`: getDistanceUnit(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setAverageImages`: setAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -&gt; None

- `getAverageImages`: getAverageImages(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; bool

- `setOptimizeConstants`: setOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -&gt; None

- `getOptimizeConstants`: getOptimizeConstants(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; bool

- `setOutputImagePath`: setOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None

- `getOutputImagePath`: getOutputImagePath(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; MaterialX.PyMaterialXFormat.FilePath

- `setBakedGraphName`: setBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getBakedGraphName`: getBakedGraphName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setBakedGeomInfoName`: setBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getBakedGeomInfoName`: getBakedGeomInfoName(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setTextureFilenameTemplate`: setTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str) -&gt; None

- `getTextureFilenameTemplate`: getTextureFilenameTemplate(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; str

- `setFilenameTemplateVarOverride`: setFilenameTemplateVarOverride(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: str, arg1: str) -&gt; None

- `setHashImageNames`: setHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -&gt; None

- `getHashImageNames`: getHashImageNames(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; bool

- `setTextureSpaceMin`: setTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; None

- `getTextureSpaceMin`: getTextureSpaceMin(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; MaterialX.PyMaterialXCore.Vector2

- `setTextureSpaceMax`: setTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Vector2) -&gt; None

- `getTextureSpaceMax`: getTextureSpaceMax(self: MaterialX.PyMaterialXRenderMsl.TextureBaker) -&gt; MaterialX.PyMaterialXCore.Vector2

- `setupUnitSystem`: setupUnitSystem(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document) -&gt; None

- `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: collections.abc.Sequence[str], arg4: str) -&gt; MaterialX.PyMaterialXCore.Document

- `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -&gt; None

- `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderMsl.TextureBaker, arg0: bool) -&gt; None


---

## 12. Module: MaterialX.PyMaterialXRenderOsl

### Classes

<hr><h4>1. <a id='materialx-pymaterialxrenderosl-oslrenderer'>OslRenderer</a></h4>

Helper class for rendering generated OSL code to produce images.

The main services provided are: Source code validation: Use of "oslc" to compile and test output results Introspection check: None at this time. Binding: None at this time. Render validation: Use of "testrender" to output rendered images. Assumes source compilation was success as it depends on the existence of corresponding .oso files.

##### Inheritance
- [ShaderRenderer](#materialx-pymaterialxrenderosl-shaderrenderer)
##### Methods

- `create`: create(arg0: typing.SupportsInt, arg1: typing.SupportsInt, arg2: MaterialX.PyMaterialXRender.BaseType) -&gt; MaterialX.PyMaterialXRenderOsl.OslRenderer<br>        <br>        Create an OSL renderer instance.

- `initialize`: initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: typing_extensions.CapsuleType = None) -&gt; None<br>        <br>        Internal initialization required for program validation and rendering.<br>        <br>        An exception is thrown on failure. The exception will contain a list of initialization errors.

- `createProgram`: createProgram(*args, **kwargs)<br>        Overloaded function.<br>        <br>        1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -&gt; None<br>        <br>        2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Mapping[str, str]) -&gt; None

- `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -&gt; None<br>        <br>        Validate inputs for the compiled OSL program.<br>        <br>        Note: Currently no validation has been implemented.

- `render`: render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -&gt; None<br>        <br>        Render OSL program to disk.<br>        <br>        This is done by using either &quot;testshade&quot; or &quot;testrender&quot;. Currently only &quot;testshade&quot; is supported.<br>        <br>        Usage of both executables requires compiled source (.oso) files as input. A shader output must be set before running this test via the setOslOutputName() method to ensure that the appropriate .oso files can be located.

- `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -&gt; MaterialX.PyMaterialXRender.Image<br>        <br>        Capture the current rendered output as an image.

- `setOslCompilerExecutable`: setOslCompilerExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the path to the OSL executable.<br>        <br>        Args:<br>            executableFilePath: Path to OSL compiler executable

- `setOslIncludePath`: setOslIncludePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -&gt; None<br>        <br>        Set the search locations for OSL include files.<br>        <br>        Args:<br>            dirPath: Include path(s) for the OSL compiler. This should include the path to stdosl.h.

- `setOslOutputFilePath`: setOslOutputFilePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the location where compiled OSL files will reside.<br>        <br>        Args:<br>            dirPath: Path to output location

- `setShaderParameterOverrides`: setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: collections.abc.Sequence[str]) -&gt; None<br>        <br>        Set shader parameter strings to be added to the scene XML file.<br>        <br>        These strings will set parameter overrides for the shader.

- `setOslShaderOutput`: setOslShaderOutput(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str, arg1: str) -&gt; None<br>        <br>        Set the OSL shader output.<br>        <br>        Args:<br>            outputName: Name of shader output<br>            outputType: The MaterialX type of the output

- `setOslTestShadeExecutable`: setOslTestShadeExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the path to the OSL shading tester.<br>        <br>        Args:<br>            executableFilePath: Path to OSL &quot;testshade&quot; executable

- `setOslTestRenderExecutable`: setOslTestRenderExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the path to the OSL rendering tester.<br>        <br>        Args:<br>            executableFilePath: Path to OSL &quot;testrender&quot; executable

- `setOslTestRenderSceneTemplateFile`: setOslTestRenderSceneTemplateFile(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the XML scene file to use for testrender.<br>        <br>        This is a template file with the following tokens for replacement: shader% : which will be replaced with the name of the shader to use shader_output% : which will be replace with the name of the shader output to use templateFilePath Scene file name<br>        <br>        Args:<br>            templateFilePath: Scene file name

- `setOslShaderName`: setOslShaderName(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str) -&gt; None<br>        <br>        Set the name of the shader to be used for the input XML scene file.<br>        <br>        Args:<br>            shaderName: Name of shader

- `setOslUtilityOSOPath`: setOslUtilityOSOPath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Set the search path for dependent shaders (.oso files) which are used when rendering with testrender.<br>        <br>        Args:<br>            dirPath: Path to location containing .oso files.

- `useTestRender`: useTestRender(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: bool) -&gt; None<br>        <br>        Used to toggle to either use testrender or testshade during render validation By default testshade is used.<br>        <br>        Args:<br>            useTestRender: Indicate whether to use testrender.

- `compileOSL`: compileOSL(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -&gt; None<br>        <br>        Compile OSL code stored in a file.<br>        <br>        Args:<br>            oslFilePath: OSL file path.

##### Attributes

- `OSL_CLOSURE_COLOR_STRING` = 'closure color'

---

## 13. Module: MaterialX.main


### Functions

- `getDefaultDataLibraryFolders`: Return list of default data library folders

- `getDefaultDataSearchPath`: Return the default data search path.

- `stringToValue`: (Deprecated) Convert a MaterialX value string and Python type to the corresponding Python value.

- `typeToName`: (Deprecated) Return the MaterialX type string associated with the given Python type.

- `valueToString`: (Deprecated) Convert a Python value to its corresponding MaterialX value string.


---
