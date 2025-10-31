## Module: MaterialX.PyMaterialXCore

### Classes

- **AttributeDef**: 

  - Methods:

    - `setAttrName`: setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

  - Methods:

    - `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]


    - `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]


    - `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]


    - `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value


    - `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]


    - `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]


    - `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look


    - `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look


    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]


    - `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]


    - `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection


    - `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]


    - `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]


    - `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef


    - `addNodeDefFromGraph`: Overloaded function.

<br>1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

<br>2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef

    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef


    - `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]


    - `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]


    - `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]


    - `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]


    - `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]


    - `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]


    - `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]


    - `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]


    - `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str


    - `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str


    - `addMaterial`: (Deprecated) Add a material element to the document.

    - `getMaterials`: (Deprecated) Return a vector of all materials in the document.

- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str


- **Element**: 

  - Methods:

    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]


    - `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str


    - `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element


    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool


    - `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element


    - `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element


    - `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None


    - `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int


    - `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]


    - `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element


    - `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]


    - `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -> None


    - `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_5::StringResolver


    - `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -> str


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


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection


- **GeomInfo**: 

  - Methods:

    - `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]


    - `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element
       to hold the geomprop if needed.

    - `addGeomAttr`: (Deprecated) Add a geomprop to this element.

    - `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.

  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

  - Methods:

    - `setGeomProp`: Overloaded function.

<br>1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

<br>2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

    - `hasGeomProp`: Overloaded function.

<br>1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

<br>2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

    - `getGeomProp`: Overloaded function.

<br>1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

<br>2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

    - `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


    - `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


  - Attributes: CATEGORY

- **GraphElement**: 

  - Methods:

    - `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node


    - `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node


    - `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]


    - `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node


    - `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]


    - `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop


    - `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop


    - `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]


    - `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None


    - `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]


    - `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node


    - `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None


    - `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool


- **Implementation**: 

  - Methods:

    - `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

  - Methods:

    - `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool


    - `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str


    - `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node


    - `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input


  - Attributes: CATEGORY

- **InterfaceElement**: 

  - Methods:

    - `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input


    - `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output


    - `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement


    - `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str


    - `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None


    - `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool


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


    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str


- **Look**: 

  - Methods:

    - `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility


    - `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility


    - `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


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


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None


    - `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.

    - `addShaderRef`: (Deprecated) Add a shader reference to this material element.

    - `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.

    - `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.

  - Attributes: CATEGORY

- **NodeDef**: 

  - Methods:

    - `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `getImplementation`: Overloaded function.

<br>1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

<br>2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement


    - `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input


    - `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None


    - `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

  - Methods:

    - `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

  - Methods:

    - `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection


  - Attributes: CATEGORY

- **PropertySet**: 

  - Methods:

    - `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property


    - `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]


    - `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None


    - `setPropertyValue`: Set the typed value of a property by its name, creating a child element
       to hold the property if needed.

    - `getPropertyValue`: Return the typed value of a property by its name.  If the given property
       is not found, then None is returned.

  - Attributes: CATEGORY

- **PropertySetAssign**: 

  - Methods:

    - `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None


    - `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool


    - `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str


    - `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool


- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member


    - `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member


    - `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


    - `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool


    - `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool


    - `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter


    - `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str


    - `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None


    - `setValue`: Set the typed value of an element.

    - `getValue`: Return the typed value of an element.

    - `getDefaultValue`: Return the default value for this element.

  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

  - Methods:

    - `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


    - `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


  - Attributes: CATEGORY

- **VariantSet**: 

  - Methods:

    - `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant


    - `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant


    - `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]


    - `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

  - Methods:

    - `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None


    - `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool


  - Attributes: CATEGORY

### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

- `getVersionString`: getVersionString() -> str

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


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `isAbsolute`: isAbsolute(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `getBaseName`: getBaseName(self: MaterialX.PyMaterialXFormat.FilePath) -> str


    - `getParentPath`: getParentPath(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> str


    - `addExtension`: addExtension(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None


    - `removeExtension`: removeExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `size`: size(self: MaterialX.PyMaterialXFormat.FilePath) -> int


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


    - `exists`: exists(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `isDirectory`: isDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `getFilesInDirectory`: getFilesInDirectory(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> list[MaterialX.PyMaterialXFormat.FilePath]


    - `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]


    - `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `getCurrentPath`: getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath


    - `getModulePath`: getModulePath() -> MaterialX.PyMaterialXFormat.FilePath


- **FileSearchPath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ';') -> str


    - `append`: Overloaded function.

<br>1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

<br>2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

    - `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool


    - `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


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

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A3068A6F0>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

- `getEnvironmentPath`: getEnvironmentPath(sep: str = ';') -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getSourceSearchPath`: getSourceSearchPath(arg0: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXFormat.FileSearchPath

- `getSubdirectories`: getSubdirectories(arg0: list[MaterialX.PyMaterialXFormat.FilePath], arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: list[MaterialX.PyMaterialXFormat.FilePath]) -> None

- `loadDocuments`: loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: set[str], includeFiles: set[str], documents: list[MaterialX.PyMaterialXCore.Document], documentsPaths: list[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: list[str] = None) -> None

- `loadLibraries`: loadLibraries(libraryFolders: list[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A30688BF0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A30658930>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A3064BB30>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

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


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.EsslShaderGenerator) -> str


- **GlslResourceBindingContext**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int) -> MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext


    - `emitDirectives`: emitDirectives(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


    - `emitResourceBindings`: emitResourceBindings(self: MaterialX.PyMaterialXGenGlsl.GlslResourceBindingContext, arg0: MaterialX.PyMaterialXGenShader.GenContext, arg1: MaterialX.PyMaterialXGenShader.VariableBlock, arg2: MaterialX.PyMaterialXGenShader.ShaderStage) -> None


- **GlslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.GlslShaderGenerator) -> str


- **VkShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.VkShaderGenerator) -> str


- **WgslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `generate`: generate(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenGlsl.WgslShaderGenerator) -> str



---

## Module: MaterialX.PyMaterialXGenMdl

### Classes

- **MdlShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMdl.MdlShaderGenerator) -> str



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


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str


    - `getVersion`: getVersion(self: MaterialX.PyMaterialXGenMsl.MslShaderGenerator) -> str



---

## Module: MaterialX.PyMaterialXGenOsl

### Classes

- **OslShaderGenerator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator) -> str


    - `generate`: generate(self: MaterialX.PyMaterialXGenOsl.OslShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.Shader


### Globals

OSL_INPUTS, OSL_OUTPUTS, OSL_UNIFORMS



---

## Module: MaterialX.PyMaterialXGenShader

### Classes

- **ApplicationVariableHandler**: 

- **ColorManagementSystem**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> str


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.ColorManagementSystem, arg0: MaterialX.PyMaterialXGenShader.ColorSpaceTransform) -> bool


- **ColorSpaceTransform**: 

  - Attributes: sourceSpace, targetSpace, type

- **DefaultColorManagementSystem**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.DefaultColorManagementSystem) -> str


- **GenContext**: 

  - Methods:

    - `getShaderGenerator`: getShaderGenerator(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX.PyMaterialXGenShader.ShaderGenerator


    - `getOptions`: getOptions(self: MaterialX.PyMaterialXGenShader.GenContext) -> MaterialX_v1_39_5::GenOptions


    - `getTypeDesc`: getTypeDesc(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str) -> MaterialX_v1_39_5::TypeDesc


    - `registerSourceCodeSearchPath`: Overloaded function.

<br>1. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

<br>2. registerSourceCodeSearchPath(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

    - `resolveSourceFile`: resolveSourceFile(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


    - `pushUserData`: pushUserData(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: str, arg1: MaterialX_v1_39_5::GenUserData) -> None


    - `setApplicationVariableHandler`: setApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext, arg0: Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]) -> None


    - `getApplicationVariableHandler`: getApplicationVariableHandler(self: MaterialX.PyMaterialXGenShader.GenContext) -> Callable[[MaterialX_v1_39_5::ShaderNode, MaterialX.PyMaterialXGenShader.GenContext], None]


- **GenOptions**: 

  - Attributes: shaderInterfaceType, fileTextureVerticalFlip, targetColorSpaceOverride, targetDistanceUnit, addUpstreamDependencies, libraryPrefix, emitColorTransforms, hwTransparency, hwSpecularEnvironmentMethod, hwSrgbEncodeOutput, hwWriteDepthMoments, hwShadowMap, hwMaxActiveLightSources, hwNormalizeUdimTexCoords, hwAmbientOcclusion, hwWriteAlbedoTable, hwWriteEnvPrefilter, hwImplicitBitangents

- **GenUserData**: 

  - Methods:

    - `getSelf`: getSelf(self: MaterialX.PyMaterialXGenShader.GenUserData) -> MaterialX.PyMaterialXGenShader.GenUserData


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


    - `hasStage`: hasStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool


    - `numStages`: numStages(self: MaterialX.PyMaterialXGenShader.Shader) -> int


    - `getStage`: Overloaded function.

<br>1. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: int) -> MaterialX_v1_39_5::ShaderStage

<br>2. getStage(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX_v1_39_5::ShaderStage

    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> str


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> bool


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> MaterialX.PyMaterialXCore.Value


    - `setAttribute`: Overloaded function.

<br>1. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str) -> None

<br>2. setAttribute(self: MaterialX.PyMaterialXGenShader.Shader, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None

- **ShaderGenerator**: 

  - Methods:

    - `getTarget`: getTarget(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> str


    - `generate`: generate(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: str, arg1: MaterialX.PyMaterialXCore.Element, arg2: MaterialX_v1_39_5::GenContext) -> MaterialX.PyMaterialXGenShader.Shader


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXGenShader.ColorManagementSystem) -> None


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX.PyMaterialXGenShader.ColorManagementSystem


    - `setUnitSystem`: setUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX_v1_39_5::UnitSystem) -> None


    - `getUnitSystem`: getUnitSystem(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> MaterialX_v1_39_5::UnitSystem


    - `getTokenSubstitutions`: getTokenSubstitutions(self: MaterialX.PyMaterialXGenShader.ShaderGenerator) -> dict[str, str]


    - `registerTypeDefs`: registerTypeDefs(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `registerShaderMetadata`: registerShaderMetadata(self: MaterialX.PyMaterialXGenShader.ShaderGenerator, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX_v1_39_5::GenContext) -> None


- **ShaderInterfaceType**: Members:

  SHADER_INTERFACE_COMPLETE

  SHADER_INTERFACE_REDUCED

  - Attributes: name, value, SHADER_INTERFACE_COMPLETE, SHADER_INTERFACE_REDUCED

- **ShaderPort**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX_v1_39_5::TypeDesc) -> None


    - `getType`: getType(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX_v1_39_5::TypeDesc


    - `setName`: setName(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `getFullName`: getFullName(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setVariable`: setVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getVariable`: getVariable(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setValue`: setValue(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: MaterialX.PyMaterialXCore.Value) -> None


    - `getValue`: getValue(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> MaterialX.PyMaterialXCore.Value


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setGeomProp`: setGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setPath`: setPath(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getPath`: getPath(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort, arg0: str) -> None


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> str


    - `isUniform`: isUniform(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool


    - `isEmitted`: isEmitted(self: MaterialX.PyMaterialXGenShader.ShaderPort) -> bool


- **ShaderPortPredicate**: 

- **ShaderStage**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str


    - `getFunctionName`: getFunctionName(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str


    - `getSourceCode`: getSourceCode(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> str


    - `getUniformBlock`: getUniformBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getInputBlock`: getInputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getOutputBlock`: getOutputBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage, arg0: str) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getConstantBlock`: getConstantBlock(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> MaterialX.PyMaterialXGenShader.VariableBlock


    - `getUniformBlocks`: getUniformBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]


    - `getInputBlocks`: getInputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]


    - `getIncludes`: getIncludes(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]


    - `getSourceDependencies`: getSourceDependencies(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> set[str]


    - `getOutputBlocks`: getOutputBlocks(self: MaterialX.PyMaterialXGenShader.ShaderStage) -> dict[str, MaterialX.PyMaterialXGenShader.VariableBlock]


- **ShaderTranslator**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXGenShader.ShaderTranslator


    - `translateShader`: translateShader(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Node, arg1: str) -> None


    - `translateAllMaterials`: translateAllMaterials(self: MaterialX.PyMaterialXGenShader.ShaderTranslator, arg0: MaterialX.PyMaterialXCore.Document, arg1: str) -> None


- **TypeDesc**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> str


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int


    - `getSize`: getSize(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> int


    - `isScalar`: isScalar(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isAggregate`: isAggregate(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isArray`: isArray(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isFloat2`: isFloat2(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isFloat3`: isFloat3(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isFloat4`: isFloat4(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


    - `isClosure`: isClosure(self: MaterialX.PyMaterialXGenShader.TypeDesc) -> bool


- **UnitSystem**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXGenShader.UnitSystem


    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> str


    - `loadLibrary`: loadLibrary(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `supportsTransform`: supportsTransform(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXGenShader.UnitTransform) -> bool


    - `setUnitConverterRegistry`: setUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem, arg0: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None


    - `getUnitConverterRegistry`: getUnitConverterRegistry(self: MaterialX.PyMaterialXGenShader.UnitSystem) -> MaterialX.PyMaterialXCore.UnitConverterRegistry


- **UnitTransform**: 

  - Attributes: sourceUnit, targetUnit, type, unitType

- **VariableBlock**: 

  - Methods:

    - `getName`: getName(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str


    - `getInstance`: getInstance(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> str


    - `empty`: empty(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> bool


    - `size`: size(self: MaterialX.PyMaterialXGenShader.VariableBlock) -> int


    - `find`: Overloaded function.

<br>1. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: str) -> MaterialX.PyMaterialXGenShader.ShaderPort

<br>2. find(self: MaterialX.PyMaterialXGenShader.VariableBlock, arg0: Callable[[MaterialX.PyMaterialXGenShader.ShaderPort], bool]) -> MaterialX.PyMaterialXGenShader.ShaderPort

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


    - `getWorldMatrix`: getWorldMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44


    - `setViewMatrix`: setViewMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None


    - `getViewMatrix`: getViewMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44


    - `setProjectionMatrix`: setProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None


    - `getProjectionMatrix`: getProjectionMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44


    - `getWorldViewProjMatrix`: getWorldViewProjMatrix(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Matrix44


    - `getViewPosition`: getViewPosition(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3


    - `getViewDirection`: getViewDirection(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector3


    - `setViewportSize`: setViewportSize(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector2) -> None


    - `getViewportSize`: getViewportSize(self: MaterialX.PyMaterialXRender.Camera) -> MaterialX.PyMaterialXCore.Vector2


    - `projectToViewport`: projectToViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `unprojectFromViewport`: unprojectFromViewport(self: MaterialX.PyMaterialXRender.Camera, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `createViewMatrix`: createViewMatrix(arg0: MaterialX.PyMaterialXCore.Vector3, arg1: MaterialX.PyMaterialXCore.Vector3, arg2: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createPerspectiveMatrix`: createPerspectiveMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `createOrthographicMatrix`: createOrthographicMatrix(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> MaterialX.PyMaterialXCore.Matrix44


    - `transformPointPerspective`: transformPointPerspective(arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


- **CgltfLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.CgltfLoader


    - `load`: load(self: MaterialX.PyMaterialXRender.CgltfLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool


- **ExceptionRenderError**: 

- **GeometryHandler**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.GeometryHandler


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.GeometryLoader) -> None


    - `clearGeometry`: clearGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler) -> None


    - `hasGeometry`: hasGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: str) -> bool


    - `getGeometry`: getGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: list[MaterialX.PyMaterialXRender.Mesh], arg1: str) -> None


    - `loadGeometry`: loadGeometry(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: bool) -> bool


    - `getMeshes`: getMeshes(self: MaterialX.PyMaterialXRender.GeometryHandler) -> list[MaterialX.PyMaterialXRender.Mesh]


    - `findParentMesh`: findParentMesh(self: MaterialX.PyMaterialXRender.GeometryHandler, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> MaterialX.PyMaterialXRender.Mesh


    - `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3


    - `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.GeometryHandler) -> MaterialX.PyMaterialXCore.Vector3


- **GeometryLoader**: 

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.GeometryLoader) -> set[str]


    - `load`: load(self: MaterialX.PyMaterialXRender.GeometryLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool


- **Image**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: int, arg3: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXRender.Image) -> int


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXRender.Image) -> int


    - `getChannelCount`: getChannelCount(self: MaterialX.PyMaterialXRender.Image) -> int


    - `getBaseType`: getBaseType(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.BaseType


    - `getBaseStride`: getBaseStride(self: MaterialX.PyMaterialXRender.Image) -> int


    - `getMaxMipCount`: getMaxMipCount(self: MaterialX.PyMaterialXRender.Image) -> int


    - `setTexelColor`: setTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int, arg2: MaterialX.PyMaterialXCore.Color4) -> None


    - `getTexelColor`: getTexelColor(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: int) -> MaterialX.PyMaterialXCore.Color4


    - `isUniformColor`: isUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> bool


    - `setUniformColor`: setUniformColor(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Color4) -> None


    - `applyMatrixTransform`: applyMatrixTransform(self: MaterialX.PyMaterialXRender.Image, arg0: MaterialX.PyMaterialXCore.Matrix33) -> None


    - `applyGammaTransform`: applyGammaTransform(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> None


    - `copy`: copy(self: MaterialX.PyMaterialXRender.Image, arg0: int, arg1: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRender.Image


    - `applyBoxBlur`: applyBoxBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image


    - `applyGaussianBlur`: applyGaussianBlur(self: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image


    - `applyBoxDownsample`: applyBoxDownsample(self: MaterialX.PyMaterialXRender.Image, arg0: int) -> MaterialX.PyMaterialXRender.Image


    - `splitByLuminance`: splitByLuminance(self: MaterialX.PyMaterialXRender.Image, arg0: float) -> tuple[MaterialX.PyMaterialXRender.Image, MaterialX.PyMaterialXRender.Image]


    - `setResourceBuffer`: setResourceBuffer(self: MaterialX.PyMaterialXRender.Image, arg0: capsule) -> None


    - `getResourceBuffer`: getResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> capsule


    - `createResourceBuffer`: createResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None


    - `releaseResourceBuffer`: releaseResourceBuffer(self: MaterialX.PyMaterialXRender.Image) -> None


    - `setResourceBufferDeallocator`: setResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image, arg0: Callable[[capsule], None]) -> None


    - `getResourceBufferDeallocator`: getResourceBufferDeallocator(self: MaterialX.PyMaterialXRender.Image) -> Callable[[capsule], None]


- **ImageBufferDeallocator**: 

- **ImageHandler**: 

  - Methods:

    - `create`: create(arg0: MaterialX.PyMaterialXRender.ImageLoader) -> MaterialX.PyMaterialXRender.ImageHandler


    - `addLoader`: addLoader(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.ImageLoader) -> None


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, image: MaterialX.PyMaterialXRender.Image, verticalFlip: bool = False) -> bool


    - `acquireImage`: acquireImage(self: MaterialX.PyMaterialXRender.ImageHandler, filePath: MaterialX.PyMaterialXFormat.FilePath, defaultColor: MaterialX.PyMaterialXCore.Color4 = <MaterialX.PyMaterialXCore.Color4 object at 0x0000022A30BA9CB0>) -> MaterialX.PyMaterialXRender.Image


    - `bindImage`: bindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: MaterialX.PyMaterialXRender.ImageSamplingProperties) -> bool


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool


    - `unbindImages`: unbindImages(self: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `setSearchPath`: setSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `getSearchPath`: getSearchPath(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXFormat.FileSearchPath


    - `setFilenameResolver`: setFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.StringResolver) -> None


    - `getFilenameResolver`: getFilenameResolver(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXCore.StringResolver


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRender.ImageHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None


    - `clearImageCache`: clearImageCache(self: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `getZeroImage`: getZeroImage(self: MaterialX.PyMaterialXRender.ImageHandler) -> MaterialX.PyMaterialXRender.Image


    - `getReferencedImages`: getReferencedImages(self: MaterialX.PyMaterialXRender.ImageHandler, arg0: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXRender.Image]


- **ImageLoader**: 

  - Methods:

    - `supportedExtensions`: supportedExtensions(self: MaterialX.PyMaterialXRender.ImageLoader) -> set[str]


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.ImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image


  - Attributes: BMP_EXTENSION, EXR_EXTENSION, GIF_EXTENSION, HDR_EXTENSION, JPG_EXTENSION, JPEG_EXTENSION, PIC_EXTENSION, PNG_EXTENSION, PSD_EXTENSION, TGA_EXTENSION, TIF_EXTENSION, TIFF_EXTENSION, TXT_EXTENSION

- **ImageSamplingProperties**: 

  - Attributes: uaddressMode, vaddressMode, filterType, defaultColor

- **LightHandler**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.LightHandler


    - `setLightTransform`: setLightTransform(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None


    - `getLightTransform`: getLightTransform(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX.PyMaterialXCore.Matrix44


    - `setDirectLighting`: setDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None


    - `getDirectLighting`: getDirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool


    - `setIndirectLighting`: setIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None


    - `getIndirectLighting`: getIndirectLighting(self: MaterialX.PyMaterialXRender.LightHandler) -> bool


    - `setEnvRadianceMap`: setEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None


    - `getEnvRadianceMap`: getEnvRadianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image


    - `setEnvIrradianceMap`: setEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None


    - `getEnvIrradianceMap`: getEnvIrradianceMap(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image


    - `setAlbedoTable`: setAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX_v1_39_5::Image) -> None


    - `getAlbedoTable`: getAlbedoTable(self: MaterialX.PyMaterialXRender.LightHandler) -> MaterialX_v1_39_5::Image


    - `setEnvSampleCount`: setEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler, arg0: int) -> None


    - `getEnvSampleCount`: getEnvSampleCount(self: MaterialX.PyMaterialXRender.LightHandler) -> int


    - `setRefractionTwoSided`: setRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler, arg0: bool) -> None


    - `getRefractionTwoSided`: getRefractionTwoSided(self: MaterialX.PyMaterialXRender.LightHandler) -> int


    - `addLightSource`: addLightSource(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Node) -> None


    - `setLightSources`: setLightSources(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> None


    - `getLightSources`: getLightSources(self: MaterialX.PyMaterialXRender.LightHandler) -> list[MaterialX.PyMaterialXCore.Node]


    - `getFirstLightOfCategory`: getFirstLightOfCategory(self: MaterialX.PyMaterialXRender.LightHandler, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `getLightIdMap`: getLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler) -> dict[str, int]


    - `computeLightIdMap`: computeLightIdMap(self: MaterialX.PyMaterialXRender.LightHandler, arg0: list[MaterialX.PyMaterialXCore.Node]) -> dict[str, int]


    - `findLights`: findLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node]) -> None


    - `registerLights`: registerLights(self: MaterialX.PyMaterialXRender.LightHandler, arg0: MaterialX.PyMaterialXCore.Document, arg1: list[MaterialX.PyMaterialXCore.Node], arg2: MaterialX.PyMaterialXGenShader.GenContext) -> None


- **Mesh**: 

  - Methods:

    - `create`: create(arg0: str) -> MaterialX.PyMaterialXRender.Mesh


    - `getName`: getName(self: MaterialX.PyMaterialXRender.Mesh) -> str


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> None


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> bool


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXRender.Mesh) -> str


    - `getStream`: Overloaded function.

<br>1. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str) -> MaterialX.PyMaterialXRender.MeshStream

<br>2. getStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: str, arg1: int) -> MaterialX.PyMaterialXRender.MeshStream

    - `addStream`: addStream(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> None


    - `setVertexCount`: setVertexCount(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> None


    - `getVertexCount`: getVertexCount(self: MaterialX.PyMaterialXRender.Mesh) -> int


    - `setMinimumBounds`: setMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None


    - `getMinimumBounds`: getMinimumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3


    - `setMaximumBounds`: setMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None


    - `getMaximumBounds`: getMaximumBounds(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3


    - `setSphereCenter`: setSphereCenter(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXCore.Vector3) -> None


    - `getSphereCenter`: getSphereCenter(self: MaterialX.PyMaterialXRender.Mesh) -> MaterialX.PyMaterialXCore.Vector3


    - `setSphereRadius`: setSphereRadius(self: MaterialX.PyMaterialXRender.Mesh, arg0: float) -> None


    - `getSphereRadius`: getSphereRadius(self: MaterialX.PyMaterialXRender.Mesh) -> float


    - `getPartitionCount`: getPartitionCount(self: MaterialX.PyMaterialXRender.Mesh) -> int


    - `addPartition`: addPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None


    - `getPartition`: getPartition(self: MaterialX.PyMaterialXRender.Mesh, arg0: int) -> MaterialX.PyMaterialXRender.MeshPartition


    - `generateTextureCoordinates`: generateTextureCoordinates(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream


    - `generateNormals`: generateNormals(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream


    - `generateTangents`: generateTangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream, arg2: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream


    - `generateBitangents`: generateBitangents(self: MaterialX.PyMaterialXRender.Mesh, arg0: MaterialX.PyMaterialXRender.MeshStream, arg1: MaterialX.PyMaterialXRender.MeshStream) -> MaterialX.PyMaterialXRender.MeshStream


    - `mergePartitions`: mergePartitions(self: MaterialX.PyMaterialXRender.Mesh) -> None


    - `splitByUdims`: splitByUdims(self: MaterialX.PyMaterialXRender.Mesh) -> None


- **MeshPartition**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.MeshPartition


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None


    - `setName`: setName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshPartition) -> str


    - `addSourceName`: addSourceName(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: str) -> None


    - `getSourceNames`: getSourceNames(self: MaterialX.PyMaterialXRender.MeshPartition) -> set[str]


    - `getIndices`: getIndices(self: MaterialX.PyMaterialXRender.MeshPartition) -> list[int]


    - `getFaceCount`: getFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition) -> int


    - `setFaceCount`: setFaceCount(self: MaterialX.PyMaterialXRender.MeshPartition, arg0: int) -> None


- **MeshStream**: 

  - Methods:

    - `create`: create(arg0: str, arg1: str, arg2: int) -> MaterialX.PyMaterialXRender.MeshStream


    - `reserve`: reserve(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None


    - `resize`: resize(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXRender.MeshStream) -> str


    - `getType`: getType(self: MaterialX.PyMaterialXRender.MeshStream) -> str


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXRender.MeshStream) -> int


    - `getData`: getData(self: MaterialX.PyMaterialXRender.MeshStream) -> list[float]


    - `getStride`: getStride(self: MaterialX.PyMaterialXRender.MeshStream) -> int


    - `setStride`: setStride(self: MaterialX.PyMaterialXRender.MeshStream, arg0: int) -> None


    - `getSize`: getSize(self: MaterialX.PyMaterialXRender.MeshStream) -> int


    - `transform`: transform(self: MaterialX.PyMaterialXRender.MeshStream, arg0: MaterialX.PyMaterialXCore.Matrix44) -> None


  - Attributes: POSITION_ATTRIBUTE, NORMAL_ATTRIBUTE, TEXCOORD_ATTRIBUTE, TANGENT_ATTRIBUTE, BITANGENT_ATTRIBUTE, COLOR_ATTRIBUTE, GEOMETRY_PROPERTY_ATTRIBUTE

- **ShaderRenderer**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXRender.ShaderRenderer, renderContextHandle: capsule = None) -> None


    - `setCamera`: setCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.Camera) -> None


    - `getCamera`: getCamera(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.Camera


    - `setImageHandler`: setImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `getImageHandler`: getImageHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.ImageHandler


    - `setLightHandler`: setLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.LightHandler) -> None


    - `getLightHandler`: getLightHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.LightHandler


    - `setGeometryHandler`: setGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXRender.GeometryHandler) -> None


    - `getGeometryHandler`: getGeometryHandler(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> MaterialX.PyMaterialXRender.GeometryHandler


    - `createProgram`: Overloaded function.

<br>1. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

<br>2. createProgram(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: dict[str, str]) -> None

    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None


    - `updateUniform`: updateUniform(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: str, arg1: MaterialX.PyMaterialXCore.Value) -> None


    - `setSize`: setSize(self: MaterialX.PyMaterialXRender.ShaderRenderer, arg0: int, arg1: int) -> None


    - `render`: render(self: MaterialX.PyMaterialXRender.ShaderRenderer) -> None


- **StbImageLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.StbImageLoader


    - `saveImage`: saveImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: MaterialX.PyMaterialXRender.Image, arg2: bool) -> bool


    - `loadImage`: loadImage(self: MaterialX.PyMaterialXRender.StbImageLoader, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXRender.Image


- **TinyObjLoader**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRender.TinyObjLoader


    - `load`: load(self: MaterialX.PyMaterialXRender.TinyObjLoader, arg0: MaterialX.PyMaterialXFormat.FilePath, arg1: list[MaterialX.PyMaterialXRender.Mesh], arg2: bool) -> bool


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


    - `unbindImage`: unbindImage(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image) -> bool


    - `createRenderResources`: createRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, arg0: MaterialX.PyMaterialXRender.Image, arg1: bool, arg2: bool) -> bool


    - `releaseRenderResources`: releaseRenderResources(self: MaterialX.PyMaterialXRenderGlsl.GLTextureHandler, image: MaterialX.PyMaterialXRender.Image = None) -> None


- **GlslProgram**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXRenderGlsl.GlslProgram


    - `setStages`: setStages(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None


    - `addStage`: addStage(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: str) -> None


    - `getStageSourceCode`: getStageSourceCode(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str) -> str


    - `getShader`: getShader(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> MaterialX.PyMaterialXGenShader.Shader


    - `build`: build(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None


    - `hasBuiltData`: hasBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool


    - `clearBuiltData`: clearBuiltData(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None


    - `getUniformsList`: getUniformsList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]


    - `getAttributesList`: getAttributesList(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> dict[str, MaterialX_v1_39_5::GlslProgram::Input]


    - `findInputs`: findInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg2: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg3: bool) -> None


    - `bind`: bind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool


    - `hasActiveAttributes`: hasActiveAttributes(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> bool


    - `bindUniform`: bindUniform(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: str, arg1: MaterialX.PyMaterialXCore.Value, arg2: bool) -> None


    - `bindAttribute`: bindAttribute(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: dict[str, MaterialX_v1_39_5::GlslProgram::Input], arg1: MaterialX.PyMaterialXRender.Mesh) -> None


    - `bindPartition`: bindPartition(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.MeshPartition) -> None


    - `bindMesh`: bindMesh(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Mesh) -> None


    - `unbindGeometry`: unbindGeometry(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None


    - `bindTextures`: bindTextures(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `bindLighting`: bindLighting(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.LightHandler, arg1: MaterialX.PyMaterialXRender.ImageHandler) -> None


    - `bindViewInformation`: bindViewInformation(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, arg0: MaterialX.PyMaterialXRender.Camera) -> None


    - `bindTimeAndFrame`: bindTimeAndFrame(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram, time: float = <br>0.0, frame: float = <br>1.0) -> None


    - `unbind`: unbind(self: MaterialX.PyMaterialXRenderGlsl.GlslProgram) -> None


  - Attributes: UNDEFINED_OPENGL_RESOURCE_ID, UNDEFINED_OPENGL_PROGRAM_LOCATION

- **GlslRenderer**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.GlslRenderer


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, renderContextHandle: capsule = None) -> None


    - `createProgram`: Overloaded function.

<br>1. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

<br>2. createProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: dict[str, str]) -> None

    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None


    - `render`: render(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> None


    - `renderTextureSpace`: renderTextureSpace(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: MaterialX.PyMaterialXCore.Vector2) -> None


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image


    - `getProgram`: getProgram(self: MaterialX.PyMaterialXRenderGlsl.GlslRenderer) -> MaterialX.PyMaterialXRenderGlsl.GlslProgram


- **Input**: 

  - Attributes: INVALID_OPENGL_TYPE, location, gltype, size, typeString, value, isConstant, path

- **TextureBaker**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderGlsl.TextureBaker


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


    - `bakeMaterialToDoc`: bakeMaterialToDoc(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: str, arg3: list[str], arg4: str) -> MaterialX.PyMaterialXCore.Document


    - `bakeAllMaterials`: bakeAllMaterials(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FileSearchPath, arg2: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `writeDocumentPerMaterial`: writeDocumentPerMaterial(self: MaterialX.PyMaterialXRenderGlsl.TextureBaker, arg0: bool) -> None



---

## Module: MaterialX.PyMaterialXRenderOsl

### Classes

- **OslRenderer**: 

  - Methods:

    - `create`: create(arg0: int, arg1: int, arg2: MaterialX.PyMaterialXRender.BaseType) -> MaterialX.PyMaterialXRenderOsl.OslRenderer


    - `initialize`: initialize(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, renderContextHandle: capsule = None) -> None


    - `createProgram`: Overloaded function.

<br>1. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXGenShader.Shader) -> None

<br>2. createProgram(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: dict[str, str]) -> None

    - `validateInputs`: validateInputs(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None


    - `render`: render(self: MaterialX.PyMaterialXRenderOsl.OslRenderer) -> None


    - `captureImage`: captureImage(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXRender.Image) -> MaterialX.PyMaterialXRender.Image


    - `setOslCompilerExecutable`: setOslCompilerExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `setOslIncludePath`: setOslIncludePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `setOslOutputFilePath`: setOslOutputFilePath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `setShaderParameterOverrides`: setShaderParameterOverrides(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: list[str]) -> None


    - `setOslShaderOutput`: setOslShaderOutput(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str, arg1: str) -> None


    - `setOslTestShadeExecutable`: setOslTestShadeExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `setOslTestRenderExecutable`: setOslTestRenderExecutable(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `setOslTestRenderSceneTemplateFile`: setOslTestRenderSceneTemplateFile(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `setOslShaderName`: setOslShaderName(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: str) -> None


    - `setOslUtilityOSOPath`: setOslUtilityOSOPath(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `useTestRender`: useTestRender(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: bool) -> None


    - `compileOSL`: compileOSL(self: MaterialX.PyMaterialXRenderOsl.OslRenderer, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


  - Attributes: OSL_CLOSURE_COLOR_STRING


---

## Module: MaterialX.colorspace

### Classes

- **AttributeDef**: 

  - Methods:

    - `setAttrName`: setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

  - Methods:

    - `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]


    - `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]


    - `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]


    - `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value


    - `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]


    - `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]


    - `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look


    - `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look


    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]


    - `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]


    - `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection


    - `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]


    - `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]


    - `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef


    - `addNodeDefFromGraph`: Overloaded function.

<br>1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

<br>2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef

    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef


    - `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]


    - `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]


    - `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]


    - `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]


    - `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]


    - `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]


    - `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]


    - `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]


    - `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str


    - `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str


    - `addMaterial`: (Deprecated) Add a material element to the document.

    - `getMaterials`: (Deprecated) Return a vector of all materials in the document.

- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str


- **Element**: 

  - Methods:

    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]


    - `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str


    - `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element


    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool


    - `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element


    - `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element


    - `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None


    - `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int


    - `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]


    - `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element


    - `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]


    - `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -> None


    - `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_5::StringResolver


    - `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -> str


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


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection


- **GeomInfo**: 

  - Methods:

    - `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]


    - `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element
       to hold the geomprop if needed.

    - `addGeomAttr`: (Deprecated) Add a geomprop to this element.

    - `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.

  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

  - Methods:

    - `setGeomProp`: Overloaded function.

<br>1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

<br>2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

    - `hasGeomProp`: Overloaded function.

<br>1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

<br>2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

    - `getGeomProp`: Overloaded function.

<br>1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

<br>2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

    - `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


    - `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


  - Attributes: CATEGORY

- **GraphElement**: 

  - Methods:

    - `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node


    - `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node


    - `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]


    - `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node


    - `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]


    - `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop


    - `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop


    - `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]


    - `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None


    - `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]


    - `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node


    - `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None


    - `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool


- **Implementation**: 

  - Methods:

    - `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

  - Methods:

    - `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool


    - `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str


    - `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node


    - `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input


  - Attributes: CATEGORY

- **InterfaceElement**: 

  - Methods:

    - `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input


    - `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output


    - `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement


    - `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str


    - `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None


    - `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool


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


    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str


- **Look**: 

  - Methods:

    - `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility


    - `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility


    - `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


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


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None


    - `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.

    - `addShaderRef`: (Deprecated) Add a shader reference to this material element.

    - `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.

    - `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.

  - Attributes: CATEGORY

- **NodeDef**: 

  - Methods:

    - `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `getImplementation`: Overloaded function.

<br>1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

<br>2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement


    - `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input


    - `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None


    - `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

  - Methods:

    - `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

  - Methods:

    - `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection


  - Attributes: CATEGORY

- **PropertySet**: 

  - Methods:

    - `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property


    - `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]


    - `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None


    - `setPropertyValue`: Set the typed value of a property by its name, creating a child element
       to hold the property if needed.

    - `getPropertyValue`: Return the typed value of a property by its name.  If the given property
       is not found, then None is returned.

  - Attributes: CATEGORY

- **PropertySetAssign**: 

  - Methods:

    - `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None


    - `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool


    - `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str


    - `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool


- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member


    - `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member


    - `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


    - `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool


    - `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool


    - `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter


    - `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str


    - `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None


    - `setValue`: Set the typed value of an element.

    - `getValue`: Return the typed value of an element.

    - `getDefaultValue`: Return the default value for this element.

  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

  - Methods:

    - `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


    - `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


  - Attributes: CATEGORY

- **VariantSet**: 

  - Methods:

    - `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant


    - `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant


    - `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]


    - `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

  - Methods:

    - `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None


    - `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool


  - Attributes: CATEGORY

### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `geomStringsMatch`: geomStringsMatch(arg0: str, arg1: str, arg2: bool) -> bool

- `getColorSpaces`: Return a list containing the names of all supported color spaces.
       By default, the OCIO color management system and default MaterialX
       config are used.

- `getConnectedOutputs`: getConnectedOutputs(arg0: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.Output]

- `getDefaultOCIOConfig`: Return the default OCIO config packaged with this Python library.
       Raises ImportError if the PyOpenColorIO module cannot be imported.

- `getGeometryBindings`: getGeometryBindings(materialNode: MaterialX_v1_39_5::Node, geom: str = '/') -> list[MaterialX.PyMaterialXCore.MaterialAssign]

- `getShaderNodes`: getShaderNodes(materialNode: MaterialX.PyMaterialXCore.Node, nodeType: str = 'surfaceshader', target: str = '') -> list[MaterialX.PyMaterialXCore.Node]

- `getVersionIntegers`: getVersionIntegers() -> tuple[int, int, int]

- `getVersionString`: getVersionString() -> str

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

- `transformColor`: Given a MaterialX color and the names of two supported color spaces,
       transform the color from the source to the destination color space.
       By default, the OCIO color management system and default MaterialX
       config are used.

### Globals

ARRAY_PREFERRED_SEPARATOR, ARRAY_VALID_SEPARATORS, BSDF_TYPE_STRING, DEFAULT_TYPE_STRING, DISPLACEMENT_SHADER_TYPE_STRING, EDF_TYPE_STRING, FILENAME_TYPE_STRING, GEOMNAME_TYPE_STRING, GEOM_PATH_SEPARATOR, LIGHT_SHADER_TYPE_STRING, MATERIAL_TYPE_STRING, MULTI_OUTPUT_TYPE_STRING, NAME_PATH_SEPARATOR, NAME_PREFIX_SEPARATOR, NONE_TYPE_STRING, STRING_TYPE_STRING, SURFACE_MATERIAL_NODE_STRING, SURFACE_SHADER_TYPE_STRING, UDIM_SET_PROPERTY, UDIM_TOKEN, UNIVERSAL_GEOM_NAME, UV_TILE_TOKEN, VALUE_STRING_FALSE, VALUE_STRING_TRUE, VDF_TYPE_STRING, VOLUME_MATERIAL_NODE_STRING, VOLUME_SHADER_TYPE_STRING



---

## Module: MaterialX.datatype

### Classes

- **AttributeDef**: 

  - Methods:

    - `setAttrName`: setAttrName(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

  - Methods:

    - `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]


    - `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]


    - `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]


    - `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value


    - `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]


    - `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]


    - `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look


    - `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look


    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]


    - `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]


    - `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection


    - `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]


    - `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]


    - `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef


    - `addNodeDefFromGraph`: Overloaded function.

<br>1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

<br>2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef

    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef


    - `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]


    - `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]


    - `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]


    - `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]


    - `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]


    - `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]


    - `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]


    - `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]


    - `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str


    - `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str


    - `addMaterial`: (Deprecated) Add a material element to the document.

    - `getMaterials`: (Deprecated) Return a vector of all materials in the document.

- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str


- **Element**: 

  - Methods:

    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]


    - `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str


    - `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element


    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool


    - `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element


    - `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element


    - `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None


    - `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int


    - `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]


    - `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element


    - `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]


    - `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -> None


    - `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_5::StringResolver


    - `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -> str


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


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection


- **GeomInfo**: 

  - Methods:

    - `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]


    - `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element
       to hold the geomprop if needed.

    - `addGeomAttr`: (Deprecated) Add a geomprop to this element.

    - `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.

  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

  - Methods:

    - `setGeomProp`: Overloaded function.

<br>1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

<br>2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

    - `hasGeomProp`: Overloaded function.

<br>1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

<br>2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

    - `getGeomProp`: Overloaded function.

<br>1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

<br>2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

    - `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


    - `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


  - Attributes: CATEGORY

- **GraphElement**: 

  - Methods:

    - `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node


    - `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node


    - `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]


    - `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node


    - `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]


    - `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop


    - `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop


    - `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]


    - `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None


    - `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]


    - `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node


    - `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None


    - `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool


- **Implementation**: 

  - Methods:

    - `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

  - Methods:

    - `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool


    - `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str


    - `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node


    - `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input


  - Attributes: CATEGORY

- **InterfaceElement**: 

  - Methods:

    - `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input


    - `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output


    - `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement


    - `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str


    - `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None


    - `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool


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


    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str


- **Look**: 

  - Methods:

    - `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility


    - `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility


    - `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


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


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None


    - `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.

    - `addShaderRef`: (Deprecated) Add a shader reference to this material element.

    - `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.

    - `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.

  - Attributes: CATEGORY

- **NodeDef**: 

  - Methods:

    - `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `getImplementation`: Overloaded function.

<br>1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

<br>2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement


    - `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input


    - `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None


    - `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

  - Methods:

    - `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

  - Methods:

    - `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection


  - Attributes: CATEGORY

- **PropertySet**: 

  - Methods:

    - `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property


    - `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]


    - `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None


    - `setPropertyValue`: Set the typed value of a property by its name, creating a child element
       to hold the property if needed.

    - `getPropertyValue`: Return the typed value of a property by its name.  If the given property
       is not found, then None is returned.

  - Attributes: CATEGORY

- **PropertySetAssign**: 

  - Methods:

    - `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None


    - `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool


    - `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str


    - `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool


- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member


    - `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member


    - `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


    - `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool


    - `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool


    - `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter


    - `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str


    - `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None


    - `setValue`: Set the typed value of an element.

    - `getValue`: Return the typed value of an element.

    - `getDefaultValue`: Return the default value for this element.

  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

  - Methods:

    - `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


    - `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


  - Attributes: CATEGORY

- **VariantSet**: 

  - Methods:

    - `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant


    - `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant


    - `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]


    - `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

  - Methods:

    - `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None


    - `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool


  - Attributes: CATEGORY

### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

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

- `getVersionString`: getVersionString() -> str

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


    - `hasAttrName`: hasAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getAttrName`: getAttrName(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.AttributeDef) -> str


    - `setExportable`: setExportable(self: MaterialX.PyMaterialXCore.AttributeDef, arg0: bool) -> None


    - `getExportable`: getExportable(self: MaterialX.PyMaterialXCore.AttributeDef) -> bool


  - Attributes: CATEGORY

- **Backdrop**: 

  - Methods:

    - `setContainsString`: setContainsString(self: MaterialX.PyMaterialXCore.Backdrop, arg0: str) -> None


    - `hasContainsString`: hasContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getContainsString`: getContainsString(self: MaterialX.PyMaterialXCore.Backdrop) -> str


    - `setWidth`: setWidth(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasWidth`: hasWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getWidth`: getWidth(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setHeight`: setHeight(self: MaterialX.PyMaterialXCore.Backdrop, arg0: float) -> None


    - `hasHeight`: hasHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> bool


    - `getHeight`: getHeight(self: MaterialX.PyMaterialXCore.Backdrop) -> float


    - `setContainsElements`: setContainsElements(self: MaterialX.PyMaterialXCore.Backdrop, arg0: list[MaterialX.PyMaterialXCore.TypedElement]) -> None


    - `getContainsElements`: getContainsElements(self: MaterialX.PyMaterialXCore.Backdrop) -> list[MaterialX.PyMaterialXCore.TypedElement]


  - Attributes: CATEGORY, CONTAINS_ATTRIBUTE, WIDTH_ATTRIBUTE, HEIGHT_ATTRIBUTE

- **Collection**: 

  - Methods:

    - `setIncludeGeom`: setIncludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeGeom`: hasIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeGeom`: getIncludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setExcludeGeom`: setExcludeGeom(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasExcludeGeom`: hasExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getExcludeGeom`: getExcludeGeom(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollectionString`: setIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> None


    - `hasIncludeCollectionString`: hasIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `getIncludeCollectionString`: getIncludeCollectionString(self: MaterialX.PyMaterialXCore.Collection) -> str


    - `setIncludeCollection`: setIncludeCollection(self: MaterialX.PyMaterialXCore.Collection, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `setIncludeCollections`: setIncludeCollections(self: MaterialX.PyMaterialXCore.Collection, arg0: list[MaterialX.PyMaterialXCore.Collection]) -> None


    - `getIncludeCollections`: getIncludeCollections(self: MaterialX.PyMaterialXCore.Collection) -> list[MaterialX.PyMaterialXCore.Collection]


    - `hasIncludeCycle`: hasIncludeCycle(self: MaterialX.PyMaterialXCore.Collection) -> bool


    - `matchesGeomString`: matchesGeomString(self: MaterialX.PyMaterialXCore.Collection, arg0: str) -> bool


  - Attributes: CATEGORY

- **Color3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color3, arg0: MaterialX.PyMaterialXCore.Color3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `linearToSrgb`: linearToSrgb(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `srgbToLinear`: srgbToLinear(self: MaterialX.PyMaterialXCore.Color3) -> MaterialX.PyMaterialXCore.Color3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color3) -> tuple[float, float, float]


- **Color4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Color4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Color4, arg0: MaterialX.PyMaterialXCore.Color4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Color4) -> MaterialX.PyMaterialXCore.Color4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Color4) -> tuple[float, float, float, float]


- **CommentElement**: 

  - Attributes: CATEGORY

- **Document**: 

  - Methods:

    - `initialize`: initialize(self: MaterialX.PyMaterialXCore.Document) -> None


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `setDataLibrary`: setDataLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getDataLibrary`: getDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> MaterialX.PyMaterialXCore.Document


    - `hasDataLibrary`: hasDataLibrary(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `importLibrary`: importLibrary(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.Document) -> None


    - `getReferencedSourceUris`: getReferencedSourceUris(self: MaterialX.PyMaterialXCore.Document) -> set[str]


    - `addNodeGraph`: addNodeGraph(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeGraph


    - `getNodeGraphs`: getNodeGraphs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeGraph]


    - `removeNodeGraph`: removeNodeGraph(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingPorts`: getMatchingPorts(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addGeomInfo`: addGeomInfo(self: MaterialX.PyMaterialXCore.Document, name: str = '', geom: str = '/') -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfo`: getGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomInfo


    - `getGeomInfos`: getGeomInfos(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomInfo]


    - `removeGeomInfo`: removeGeomInfo(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getGeomPropValue`: getGeomPropValue(self: MaterialX.PyMaterialXCore.Document, geomPropName: str, geom: str = '/') -> MaterialX.PyMaterialXCore.Value


    - `addGeomPropDef`: addGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDef`: getGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.GeomPropDef


    - `getGeomPropDefs`: getGeomPropDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.GeomPropDef]


    - `removeGeomPropDef`: removeGeomPropDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Output]


    - `addLook`: addLook(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Look


    - `getLook`: getLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Look


    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Look]


    - `removeLook`: removeLook(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addLookGroup`: addLookGroup(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroup`: getLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.LookGroup


    - `getLookGroups`: getLookGroups(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.LookGroup]


    - `removeLookGroup`: removeLookGroup(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addCollection`: addCollection(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Collection


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Collection


    - `getCollections`: getCollections(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Collection]


    - `removeCollection`: removeCollection(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTypeDef`: addTypeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TypeDef


    - `getTypeDefs`: getTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TypeDef]


    - `removeTypeDef`: removeTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addNodeDef`: addNodeDef(self: MaterialX.PyMaterialXCore.Document, name: str = '', type: str = 'color3', node: str = '') -> MaterialX.PyMaterialXCore.NodeDef


    - `addNodeDefFromGraph`: Overloaded function.

<br>1. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str) -> MaterialX.PyMaterialXCore.NodeDef

<br>2. addNodeDefFromGraph(self: MaterialX.PyMaterialXCore.Document, arg0: MaterialX.PyMaterialXCore.NodeGraph, arg1: str, arg2: str, arg3: str, arg4: bool, arg5: str, arg6: str) -> MaterialX.PyMaterialXCore.NodeDef

    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.NodeDef


    - `getNodeDefs`: getNodeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `removeNodeDef`: removeNodeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingNodeDefs`: getMatchingNodeDefs(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.NodeDef]


    - `addAttributeDef`: addAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDef`: getAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.AttributeDef


    - `getAttributeDefs`: getAttributeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.AttributeDef]


    - `removeAttributeDef`: removeAttributeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addTargetDef`: addTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDef`: getTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.TargetDef


    - `getTargetDefs`: getTargetDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.TargetDef]


    - `removeTargetDef`: removeTargetDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addPropertySet`: addPropertySet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.PropertySet


    - `getPropertySets`: getPropertySets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.PropertySet]


    - `removePropertySet`: removePropertySet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addVariantSet`: addVariantSet(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSet`: getVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.VariantSet


    - `getVariantSets`: getVariantSets(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.VariantSet]


    - `removeVariantSet`: removeVariantSet(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addImplementation`: addImplementation(self: MaterialX.PyMaterialXCore.Document, name: str = '') -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.Implementation


    - `getImplementations`: getImplementations(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.Implementation]


    - `removeImplementation`: removeImplementation(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `getMatchingImplementations`: getMatchingImplementations(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> list[MaterialX.PyMaterialXCore.InterfaceElement]


    - `addUnitDef`: addUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDef`: getUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitDef


    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitDef]


    - `removeUnitDef`: removeUnitDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `addUnitTypeDef`: addUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDef`: getUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> MaterialX.PyMaterialXCore.UnitTypeDef


    - `getUnitTypeDefs`: getUnitTypeDefs(self: MaterialX.PyMaterialXCore.Document) -> list[MaterialX.PyMaterialXCore.UnitTypeDef]


    - `removeUnitTypeDef`: removeUnitTypeDef(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `upgradeVersion`: upgradeVersion(self: MaterialX.PyMaterialXCore.Document) -> None


    - `setColorManagementSystem`: setColorManagementSystem(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementSystem`: hasColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementSystem`: getColorManagementSystem(self: MaterialX.PyMaterialXCore.Document) -> str


    - `setColorManagementConfig`: setColorManagementConfig(self: MaterialX.PyMaterialXCore.Document, arg0: str) -> None


    - `hasColorManagementConfig`: hasColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> bool


    - `getColorManagementConfig`: getColorManagementConfig(self: MaterialX.PyMaterialXCore.Document) -> str


    - `addMaterial`: (Deprecated) Add a material element to the document.

    - `getMaterials`: (Deprecated) Return a vector of all materials in the document.

- **Edge**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Edge) -> MaterialX.PyMaterialXCore.Element


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Edge) -> str


- **Element**: 

  - Methods:

    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: MaterialX_v1_39_5::ElementEquivalenceOptions) -> tuple[bool, str]


    - `setCategory`: setCategory(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getCategory`: getCategory(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setName`: setName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getName`: getName(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getNamePath`: getNamePath(self: MaterialX.PyMaterialXCore.Element, relativeTo: MaterialX.PyMaterialXCore.Element = None) -> str


    - `getDescendant`: getDescendant(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> MaterialX.PyMaterialXCore.Element


    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasFilePrefix`: hasFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveFilePrefix`: getActiveFilePrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasGeomPrefix`: hasGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveGeomPrefix`: getActiveGeomPrefix(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setColorSpace`: setColorSpace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasColorSpace`: hasColorSpace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getColorSpace`: getColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveColorSpace`: getActiveColorSpace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritString`: setInheritString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasInheritString`: hasInheritString(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getInheritString`: getInheritString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `setInheritsFrom`: setInheritsFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `getInheritsFrom`: getInheritsFrom(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `hasInheritedBase`: hasInheritedBase(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> bool


    - `hasInheritanceCycle`: hasInheritanceCycle(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `setNamespace`: setNamespace(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasNamespace`: hasNamespace(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getNamespace`: getNamespace(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getQualifiedName`: getQualifiedName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `setDocString`: setDocString(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getDocString`: getDocString(self: MaterialX.PyMaterialXCore.Element) -> str


    - `addChildOfCategory`: addChildOfCategory(self: MaterialX.PyMaterialXCore.Element, category: str, name: str = '') -> MaterialX.PyMaterialXCore.Element


    - `changeChildCategory`: changeChildCategory(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element, arg1: str) -> MaterialX.PyMaterialXCore.Element


    - `getChildren`: getChildren(self: MaterialX.PyMaterialXCore.Element) -> list[MaterialX.PyMaterialXCore.Element]


    - `setChildIndex`: setChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: int) -> None


    - `getChildIndex`: getChildIndex(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> int


    - `removeChild`: removeChild(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `setAttribute`: setAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str, arg1: str) -> None


    - `hasAttribute`: hasAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> bool


    - `getAttribute`: getAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `getAttributeNames`: getAttributeNames(self: MaterialX.PyMaterialXCore.Element) -> list[str]


    - `removeAttribute`: removeAttribute(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `getSelf`: getSelf(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getParent`: getParent(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getRoot`: getRoot(self: MaterialX.PyMaterialXCore.Element) -> MaterialX.PyMaterialXCore.Element


    - `getDocument`: getDocument(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::Document


    - `traverseTree`: traverseTree(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::TreeIterator


    - `traverseGraph`: traverseGraph(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::GraphIterator


    - `getUpstreamEdge`: getUpstreamEdge(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX_v1_39_5::Edge


    - `getUpstreamEdgeCount`: getUpstreamEdgeCount(self: MaterialX.PyMaterialXCore.Element) -> int


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.Element, index: int = 0) -> MaterialX.PyMaterialXCore.Element


    - `traverseInheritance`: traverseInheritance(self: MaterialX.PyMaterialXCore.Element) -> MaterialX_v1_39_5::InheritanceIterator


    - `setSourceUri`: setSourceUri(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> None


    - `hasSourceUri`: hasSourceUri(self: MaterialX.PyMaterialXCore.Element) -> bool


    - `getSourceUri`: getSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `getActiveSourceUri`: getActiveSourceUri(self: MaterialX.PyMaterialXCore.Element) -> str


    - `validate`: validate(self: MaterialX.PyMaterialXCore.Element) -> tuple[bool, str]


    - `copyContentFrom`: copyContentFrom(self: MaterialX.PyMaterialXCore.Element, arg0: MaterialX.PyMaterialXCore.Element) -> None


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.Element) -> None


    - `createValidChildName`: createValidChildName(self: MaterialX.PyMaterialXCore.Element, arg0: str) -> str


    - `createStringResolver`: createStringResolver(self: MaterialX.PyMaterialXCore.Element, geom: str = '') -> MaterialX_v1_39_5::StringResolver


    - `asString`: asString(self: MaterialX.PyMaterialXCore.Element) -> str


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


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `isAbsolute`: isAbsolute(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `getBaseName`: getBaseName(self: MaterialX.PyMaterialXFormat.FilePath) -> str


    - `getParentPath`: getParentPath(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


    - `getExtension`: getExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> str


    - `addExtension`: addExtension(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> None


    - `removeExtension`: removeExtension(self: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `size`: size(self: MaterialX.PyMaterialXFormat.FilePath) -> int


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


    - `exists`: exists(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `isDirectory`: isDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> bool


    - `getFilesInDirectory`: getFilesInDirectory(self: MaterialX.PyMaterialXFormat.FilePath, arg0: str) -> list[MaterialX.PyMaterialXFormat.FilePath]


    - `getSubDirectories`: getSubDirectories(self: MaterialX.PyMaterialXFormat.FilePath) -> list[MaterialX.PyMaterialXFormat.FilePath]


    - `createDirectory`: createDirectory(self: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `getCurrentPath`: getCurrentPath() -> MaterialX.PyMaterialXFormat.FilePath


    - `getModulePath`: getModulePath() -> MaterialX.PyMaterialXFormat.FilePath


- **FileSearchPath**: 

  - Methods:

    - `asString`: asString(self: MaterialX.PyMaterialXFormat.FileSearchPath, sep: str = ';') -> str


    - `append`: Overloaded function.

<br>1. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None

<br>2. append(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FileSearchPath) -> None

    - `prepend`: prepend(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> None


    - `clear`: clear(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> None


    - `size`: size(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> int


    - `isEmpty`: isEmpty(self: MaterialX.PyMaterialXFormat.FileSearchPath) -> bool


    - `find`: find(self: MaterialX.PyMaterialXFormat.FileSearchPath, arg0: MaterialX.PyMaterialXFormat.FilePath) -> MaterialX.PyMaterialXFormat.FilePath


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


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.GeomElement, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.GeomElement) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.GeomElement, arg0: MaterialX_v1_39_5::Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.GeomElement) -> MaterialX_v1_39_5::Collection


- **GeomInfo**: 

  - Methods:

    - `addGeomProp`: addGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProp`: getGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX_v1_39_5::GeomProp


    - `getGeomProps`: getGeomProps(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX_v1_39_5::GeomProp]


    - `removeGeomProp`: removeGeomProp(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.GeomInfo, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.GeomInfo) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str) -> None


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.GeomInfo, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `setGeomPropValue`: Set the value of a geomprop by its name, creating a child element
       to hold the geomprop if needed.

    - `addGeomAttr`: (Deprecated) Add a geomprop to this element.

    - `setGeomAttrValue`: (Deprecated) Set the value of a geomattr by its name.

  - Attributes: CATEGORY

- **GeomProp**: 

  - Attributes: CATEGORY

- **GeomPropDef**: 

  - Methods:

    - `setGeomProp`: Overloaded function.

<br>1. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

<br>2. setGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None

    - `hasGeomProp`: Overloaded function.

<br>1. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

<br>2. hasGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool

    - `getGeomProp`: Overloaded function.

<br>1. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

<br>2. getGeomProp(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str

    - `setSpace`: setSpace(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasSpace`: hasSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getSpace`: getSpace(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


    - `setIndex`: setIndex(self: MaterialX.PyMaterialXCore.GeomPropDef, arg0: str) -> None


    - `hasIndex`: hasIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> bool


    - `getIndex`: getIndex(self: MaterialX.PyMaterialXCore.GeomPropDef) -> str


  - Attributes: CATEGORY

- **GraphElement**: 

  - Methods:

    - `addNode`: addNode(self: MaterialX.PyMaterialXCore.GraphElement, category: str, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Node


    - `addNodeInstance`: addNodeInstance(self: MaterialX.PyMaterialXCore.GraphElement, nodeDef: MaterialX.PyMaterialXCore.NodeDef, name: str = '') -> MaterialX.PyMaterialXCore.Node


    - `getNode`: getNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `getNodes`: getNodes(self: MaterialX.PyMaterialXCore.GraphElement, category: str = '') -> list[MaterialX.PyMaterialXCore.Node]


    - `removeNode`: removeNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `addMaterialNode`: addMaterialNode(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '', shaderNode: MaterialX.PyMaterialXCore.Node = None) -> MaterialX.PyMaterialXCore.Node


    - `getMaterialNodes`: getMaterialNodes(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Node]


    - `addBackdrop`: addBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, name: str = '') -> MaterialX_v1_39_5::Backdrop


    - `getBackdrop`: getBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> MaterialX_v1_39_5::Backdrop


    - `getBackdrops`: getBackdrops(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX_v1_39_5::Backdrop]


    - `removeBackdrop`: removeBackdrop(self: MaterialX.PyMaterialXCore.GraphElement, arg0: str) -> None


    - `flattenSubgraphs`: flattenSubgraphs(self: MaterialX.PyMaterialXCore.GraphElement, target: str = '', filter: Callable[[MaterialX.PyMaterialXCore.Node], bool] = None) -> None


    - `topologicalSort`: topologicalSort(self: MaterialX.PyMaterialXCore.GraphElement) -> list[MaterialX.PyMaterialXCore.Element]


    - `addGeomNode`: addGeomNode(self: MaterialX.PyMaterialXCore.GraphElement, arg0: MaterialX.PyMaterialXCore.GeomPropDef, arg1: str) -> MaterialX.PyMaterialXCore.Node


    - `asStringDot`: asStringDot(self: MaterialX.PyMaterialXCore.GraphElement) -> str


- **GraphIterator**: 

  - Methods:

    - `getDownstreamElement`: getDownstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getConnectingElement`: getConnectingElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamElement`: getUpstreamElement(self: MaterialX.PyMaterialXCore.GraphIterator) -> MaterialX.PyMaterialXCore.Element


    - `getUpstreamIndex`: getUpstreamIndex(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `getNodeDepth`: getNodeDepth(self: MaterialX.PyMaterialXCore.GraphIterator) -> int


    - `setPruneSubgraph`: setPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator, arg0: bool) -> None


    - `getPruneSubgraph`: getPruneSubgraph(self: MaterialX.PyMaterialXCore.GraphIterator) -> bool


- **Implementation**: 

  - Methods:

    - `setFile`: setFile(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFile`: hasFile(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFile`: getFile(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setFunction`: setFunction(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasFunction`: hasFunction(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getFunction`: getFunction(self: MaterialX.PyMaterialXCore.Implementation) -> str


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.Implementation, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Implementation) -> MaterialX.PyMaterialXCore.NodeDef


    - `setNodeGraph`: setNodeGraph(self: MaterialX.PyMaterialXCore.Implementation, arg0: str) -> None


    - `hasNodeGraph`: hasNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> bool


    - `getNodeGraph`: getNodeGraph(self: MaterialX.PyMaterialXCore.Implementation) -> str


  - Attributes: CATEGORY, FILE_ATTRIBUTE, FUNCTION_ATTRIBUTE

- **InheritanceIterator**: 

- **Input**: 

  - Methods:

    - `setDefaultGeomPropString`: setDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `hasDefaultGeomPropString`: hasDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> bool


    - `getDefaultGeomPropString`: getDefaultGeomPropString(self: MaterialX.PyMaterialXCore.Input) -> str


    - `getDefaultGeomProp`: getDefaultGeomProp(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::GeomPropDef


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Input) -> MaterialX_v1_39_5::Node


    - `setConnectedInterfaceName`: setConnectedInterfaceName(self: MaterialX.PyMaterialXCore.Input, arg0: str) -> None


    - `getInterfaceInput`: getInterfaceInput(self: MaterialX.PyMaterialXCore.Input) -> MaterialX.PyMaterialXCore.Input


  - Attributes: CATEGORY

- **InterfaceElement**: 

  - Methods:

    - `setNodeDefString`: setNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasNodeDefString`: hasNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getNodeDefString`: getNodeDefString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `addInput`: addInput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Input


    - `getInput`: getInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getInputs`: getInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `getInputCount`: getInputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeInput`: removeInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveInput`: getActiveInput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `getActiveInputs`: getActiveInputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Input]


    - `addOutput`: addOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = '', type: str = 'color3') -> MaterialX.PyMaterialXCore.Output


    - `getOutput`: getOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getOutputs`: getOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `getOutputCount`: getOutputCount(self: MaterialX.PyMaterialXCore.InterfaceElement) -> int


    - `removeOutput`: removeOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveOutput`: getActiveOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `getActiveOutputs`: getActiveOutputs(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Output]


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: MaterialX.PyMaterialXCore.Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Output


    - `addToken`: addToken(self: MaterialX.PyMaterialXCore.InterfaceElement, name: str = 'color3') -> MaterialX.PyMaterialXCore.Token


    - `getToken`: getToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokens`: getTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `removeToken`: removeToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `getActiveToken`: getActiveToken(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.Token


    - `getActiveTokens`: getActiveTokens(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.Token]


    - `getActiveValueElement`: getActiveValueElement(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> MaterialX.PyMaterialXCore.ValueElement


    - `getActiveValueElements`: getActiveValueElements(self: MaterialX.PyMaterialXCore.InterfaceElement) -> list[MaterialX.PyMaterialXCore.ValueElement]


    - `setTokenValue`: setTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Token


    - `getTokenValue`: getTokenValue(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> str


    - `setTarget`: setTarget(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasTarget`: hasTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getTarget`: getTarget(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionString`: setVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: str) -> None


    - `hasVersionString`: hasVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getVersionString`: getVersionString(self: MaterialX.PyMaterialXCore.InterfaceElement) -> str


    - `setVersionIntegers`: setVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: int, arg1: int) -> None


    - `getVersionIntegers`: getVersionIntegers(self: MaterialX.PyMaterialXCore.InterfaceElement) -> tuple[int, int]


    - `setDefaultVersion`: setDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement, arg0: bool) -> None


    - `getDefaultVersion`: getDefaultVersion(self: MaterialX.PyMaterialXCore.InterfaceElement) -> bool


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.InterfaceElement, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `clearContent`: clearContent(self: MaterialX.PyMaterialXCore.InterfaceElement) -> None


    - `hasExactInputMatch`: hasExactInputMatch(self: MaterialX.PyMaterialXCore.InterfaceElement, declaration: MaterialX.PyMaterialXCore.InterfaceElement, message: str = None) -> bool


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


    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.LinearUnitConverter, arg0: int) -> str


- **Look**: 

  - Methods:

    - `addMaterialAssign`: addMaterialAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '', material: str = '') -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssign`: getMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::MaterialAssign


    - `getMaterialAssigns`: getMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `getActiveMaterialAssigns`: getActiveMaterialAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::MaterialAssign]


    - `removeMaterialAssign`: removeMaterialAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertyAssign`: addPropertyAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssign`: getPropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertyAssign


    - `getPropertyAssigns`: getPropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `getActivePropertyAssigns`: getActivePropertyAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertyAssign]


    - `removePropertyAssign`: removePropertyAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addPropertySetAssign`: addPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssign`: getPropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX.PyMaterialXCore.PropertySetAssign


    - `getPropertySetAssigns`: getPropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `getActivePropertySetAssigns`: getActivePropertySetAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX.PyMaterialXCore.PropertySetAssign]


    - `removePropertySetAssign`: removePropertySetAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVariantAssign`: addVariantAssign(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssign`: getVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::VariantAssign


    - `getVariantAssigns`: getVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `getActiveVariantAssigns`: getActiveVariantAssigns(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::VariantAssign]


    - `removeVariantAssign`: removeVariantAssign(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


    - `addVisibility`: addVisibility(self: MaterialX.PyMaterialXCore.Look, name: str = '') -> MaterialX_v1_39_5::Visibility


    - `getVisibility`: getVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> MaterialX_v1_39_5::Visibility


    - `getVisibilities`: getVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `getActiveVisibilities`: getActiveVisibilities(self: MaterialX.PyMaterialXCore.Look) -> list[MaterialX_v1_39_5::Visibility]


    - `removeVisibility`: removeVisibility(self: MaterialX.PyMaterialXCore.Look, arg0: str) -> None


  - Attributes: CATEGORY

- **LookGroup**: 

  - Methods:

    - `getLooks`: getLooks(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setLooks`: setLooks(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


    - `getActiveLook`: getActiveLook(self: MaterialX.PyMaterialXCore.LookGroup) -> str


    - `setActiveLook`: setActiveLook(self: MaterialX.PyMaterialXCore.LookGroup, arg0: str) -> None


  - Attributes: CATEGORY, LOOKS_ATTRIBUTE, ACTIVE_ATTRIBUTE

- **MaterialAssign**: 

  - Methods:

    - `setMaterial`: setMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: str) -> None


    - `hasMaterial`: hasMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getMaterial`: getMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> str


    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.MaterialAssign) -> list[MaterialX.PyMaterialXCore.Output]


    - `setExclusive`: setExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign, arg0: bool) -> None


    - `getExclusive`: getExclusive(self: MaterialX.PyMaterialXCore.MaterialAssign) -> bool


    - `getReferencedMaterial`: getReferencedMaterial(self: MaterialX.PyMaterialXCore.MaterialAssign) -> MaterialX_v1_39_5::Node


  - Attributes: CATEGORY

- **Matrix33**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Matrix33, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix33) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix33) -> MaterialX.PyMaterialXCore.Matrix33


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Matrix33


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix33, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `createRotation`: createRotation(arg0: float) -> MaterialX.PyMaterialXCore.Matrix33


  - Attributes: IDENTITY

- **Matrix44**: 

  - Methods:

    - `copy`: copy(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `isEquivalent`: isEquivalent(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Matrix44, arg1: float) -> bool


    - `getTranspose`: getTranspose(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getDeterminant`: getDeterminant(self: MaterialX.PyMaterialXCore.Matrix44) -> float


    - `getAdjugate`: getAdjugate(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `getInverse`: getInverse(self: MaterialX.PyMaterialXCore.Matrix44) -> MaterialX.PyMaterialXCore.Matrix44


    - `createScale`: createScale(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `createTranslation`: createTranslation(arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Matrix44


    - `numRows`: numRows() -> int


    - `numColumns`: numColumns() -> int


    - `multiply`: multiply(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `transformPoint`: transformPoint(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformVector`: transformVector(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `transformNormal`: transformNormal(self: MaterialX.PyMaterialXCore.Matrix44, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


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


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Node


    - `setConnectedNodeName`: setConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str, arg1: str) -> None


    - `getConnectedNodeName`: getConnectedNodeName(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> str


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.Node, target: str = '', allowRoughMatch: bool = False) -> MaterialX.PyMaterialXCore.NodeDef


    - `getImplementation`: getImplementation(self: MaterialX.PyMaterialXCore.Node, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.Node) -> list[MaterialX.PyMaterialXCore.PortElement]


    - `addInputFromNodeDef`: addInputFromNodeDef(self: MaterialX.PyMaterialXCore.Node, arg0: str) -> MaterialX.PyMaterialXCore.Input


    - `addInputsFromNodeDef`: addInputsFromNodeDef(self: MaterialX.PyMaterialXCore.Node) -> None


    - `getReferencedNodeDef`: (Deprecated) Return the first NodeDef that declares this node.

    - `addShaderRef`: (Deprecated) Add a shader reference to this material element.

    - `getShaderRefs`: (Deprecated) Return a vector of all shader references in this material element.

    - `getActiveShaderRefs`: (Deprecated) Return a vector of all shader references in this material element, taking material inheritance into account.

  - Attributes: CATEGORY

- **NodeDef**: 

  - Methods:

    - `setNodeString`: setNodeString(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeString`: hasNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeString`: getNodeString(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `setNodeGroup`: setNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> None


    - `hasNodeGroup`: hasNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> bool


    - `getNodeGroup`: getNodeGroup(self: MaterialX.PyMaterialXCore.NodeDef) -> str


    - `getImplementation`: Overloaded function.

<br>1. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement

<br>2. getImplementation(self: MaterialX.PyMaterialXCore.NodeDef, target: str = '') -> MaterialX.PyMaterialXCore.InterfaceElement

    - `isVersionCompatible`: isVersionCompatible(self: MaterialX.PyMaterialXCore.NodeDef, arg0: str) -> bool


  - Attributes: CATEGORY, NODE_ATTRIBUTE, TEXTURE_NODE_GROUP, PROCEDURAL_NODE_GROUP, GEOMETRIC_NODE_GROUP, ADJUSTMENT_NODE_GROUP, CONDITIONAL_NODE_GROUP, CHANNEL_NODE_GROUP, ORGANIZATION_NODE_GROUP, TRANSLATION_NODE_GROUP

- **NodeGraph**: 

  - Methods:

    - `getMaterialOutputs`: getMaterialOutputs(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.Output]


    - `setNodeDef`: setNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: MaterialX.PyMaterialXCore.NodeDef) -> None


    - `getNodeDef`: getNodeDef(self: MaterialX.PyMaterialXCore.NodeGraph) -> MaterialX.PyMaterialXCore.NodeDef


    - `getDeclaration`: getDeclaration(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> MaterialX.PyMaterialXCore.InterfaceElement


    - `addInterfaceName`: addInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> MaterialX.PyMaterialXCore.Input


    - `removeInterfaceName`: removeInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str) -> None


    - `modifyInterfaceName`: modifyInterfaceName(self: MaterialX.PyMaterialXCore.NodeGraph, arg0: str, arg1: str) -> None


    - `getDownstreamPorts`: getDownstreamPorts(self: MaterialX.PyMaterialXCore.NodeGraph) -> list[MaterialX.PyMaterialXCore.PortElement]


  - Attributes: CATEGORY

- **NodePredicate**: 

- **Output**: 

  - Methods:

    - `hasUpstreamCycle`: hasUpstreamCycle(self: MaterialX.PyMaterialXCore.Output) -> bool


  - Attributes: CATEGORY, DEFAULT_INPUT_ATTRIBUTE

- **PortElement**: 

  - Methods:

    - `setNodeName`: setNodeName(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `getNodeName`: getNodeName(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setNodeGraphString`: setNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasNodeGraphString`: hasNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getNodeGraphString`: getNodeGraphString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setOutputString`: setOutputString(self: MaterialX.PyMaterialXCore.PortElement, arg0: str) -> None


    - `hasOutputString`: hasOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> bool


    - `getOutputString`: getOutputString(self: MaterialX.PyMaterialXCore.PortElement) -> str


    - `setConnectedNode`: setConnectedNode(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Node) -> None


    - `getConnectedNode`: getConnectedNode(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Node


    - `setConnectedOutput`: setConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement, arg0: MaterialX_v1_39_5::Output) -> None


    - `getConnectedOutput`: getConnectedOutput(self: MaterialX.PyMaterialXCore.PortElement) -> MaterialX_v1_39_5::Output


- **Property**: 

  - Attributes: CATEGORY

- **PropertyAssign**: 

  - Methods:

    - `setProperty`: setProperty(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasProperty`: hasProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getProperty`: getProperty(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setGeom`: setGeom(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasGeom`: hasGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getGeom`: getGeom(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollectionString`: setCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: str) -> None


    - `hasCollectionString`: hasCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> bool


    - `getCollectionString`: getCollectionString(self: MaterialX.PyMaterialXCore.PropertyAssign) -> str


    - `setCollection`: setCollection(self: MaterialX.PyMaterialXCore.PropertyAssign, arg0: MaterialX.PyMaterialXCore.Collection) -> None


    - `getCollection`: getCollection(self: MaterialX.PyMaterialXCore.PropertyAssign) -> MaterialX.PyMaterialXCore.Collection


  - Attributes: CATEGORY

- **PropertySet**: 

  - Methods:

    - `addProperty`: addProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> MaterialX.PyMaterialXCore.Property


    - `getProperties`: getProperties(self: MaterialX.PyMaterialXCore.PropertySet) -> list[MaterialX.PyMaterialXCore.Property]


    - `removeProperty`: removeProperty(self: MaterialX.PyMaterialXCore.PropertySet, arg0: str) -> None


    - `setPropertyValue`: Set the typed value of a property by its name, creating a child element
       to hold the property if needed.

    - `getPropertyValue`: Return the typed value of a property by its name.  If the given property
       is not found, then None is returned.

  - Attributes: CATEGORY

- **PropertySetAssign**: 

  - Methods:

    - `setPropertySetString`: setPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: str) -> None


    - `hasPropertySetString`: hasPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> bool


    - `getPropertySetString`: getPropertySetString(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> str


    - `setPropertySet`: setPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign, arg0: MaterialX.PyMaterialXCore.PropertySet) -> None


    - `getPropertySet`: getPropertySet(self: MaterialX.PyMaterialXCore.PropertySetAssign) -> MaterialX.PyMaterialXCore.PropertySet


  - Attributes: CATEGORY

- **StringResolver**: 

  - Methods:

    - `setFilePrefix`: setFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getFilePrefix`: getFilePrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setGeomPrefix`: setGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `getGeomPrefix`: getGeomPrefix(self: MaterialX.PyMaterialXCore.StringResolver) -> str


    - `setUdimString`: setUdimString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setUvTileString`: setUvTileString(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str) -> None


    - `setFilenameSubstitution`: setFilenameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getFilenameSubstitutions`: getFilenameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `setGeomNameSubstitution`: setGeomNameSubstitution(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> None


    - `getGeomNameSubstitutions`: getGeomNameSubstitutions(self: MaterialX.PyMaterialXCore.StringResolver) -> dict[str, str]


    - `resolve`: resolve(self: MaterialX.PyMaterialXCore.StringResolver, arg0: str, arg1: str) -> str


- **TargetDef**: 

  - Methods:

    - `getMatchingTargets`: getMatchingTargets(self: MaterialX.PyMaterialXCore.TargetDef) -> list[str]


  - Attributes: CATEGORY

- **Token**: 

  - Attributes: CATEGORY

- **TreeIterator**: 

  - Methods:

    - `getElement`: getElement(self: MaterialX.PyMaterialXCore.TreeIterator) -> MaterialX.PyMaterialXCore.Element


    - `getElementDepth`: getElementDepth(self: MaterialX.PyMaterialXCore.TreeIterator) -> int


    - `setPruneSubtree`: setPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator, arg0: bool) -> None


    - `getPruneSubtree`: getPruneSubtree(self: MaterialX.PyMaterialXCore.TreeIterator) -> bool


- **Type**: Members:

  TypeRelative

  TypeAbsolute

  TypeNetwork

  - Attributes: name, value, TypeRelative, TypeAbsolute, TypeNetwork

- **TypeDef**: 

  - Methods:

    - `setSemantic`: setSemantic(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasSemantic`: hasSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getSemantic`: getSemantic(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `setContext`: setContext(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


    - `hasContext`: hasContext(self: MaterialX.PyMaterialXCore.TypeDef) -> bool


    - `getContext`: getContext(self: MaterialX.PyMaterialXCore.TypeDef) -> str


    - `addMember`: addMember(self: MaterialX.PyMaterialXCore.TypeDef, name: str = '') -> MaterialX_v1_39_5::Member


    - `getMember`: getMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> MaterialX_v1_39_5::Member


    - `getMembers`: getMembers(self: MaterialX.PyMaterialXCore.TypeDef) -> list[MaterialX_v1_39_5::Member]


    - `removeMember`: removeMember(self: MaterialX.PyMaterialXCore.TypeDef, arg0: str) -> None


  - Attributes: CATEGORY, SEMANTIC_ATTRIBUTE, CONTEXT_ATTRIBUTE

- **TypedElement**: 

  - Methods:

    - `setType`: setType(self: MaterialX.PyMaterialXCore.TypedElement, arg0: str) -> None


    - `hasType`: hasType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getType`: getType(self: MaterialX.PyMaterialXCore.TypedElement) -> str


    - `isColorType`: isColorType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `isMultiOutputType`: isMultiOutputType(self: MaterialX.PyMaterialXCore.TypedElement) -> bool


    - `getTypeDef`: getTypeDef(self: MaterialX.PyMaterialXCore.TypedElement) -> MaterialX_v1_39_5::TypeDef


  - Attributes: TYPE_ATTRIBUTE

- **TypedValue_boolean**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_boolean) -> str


    - `createValue`: createValue(arg0: bool) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_booleanarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> list[bool]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_booleanarray) -> str


    - `createValue`: createValue(arg0: list[bool]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> MaterialX_v1_39_5::Color3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_color4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> MaterialX_v1_39_5::Color4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_color4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Color4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_float**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_float) -> float


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_float) -> str


    - `createValue`: createValue(arg0: float) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_floatarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> list[float]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_floatarray) -> str


    - `createValue`: createValue(arg0: list[float]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integer**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> int


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integer) -> str


    - `createValue`: createValue(arg0: int) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_integerarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> list[int]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_integerarray) -> str


    - `createValue`: createValue(arg0: list[int]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix33**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> MaterialX_v1_39_5::Matrix33


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix33) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix33) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_matrix44**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> MaterialX_v1_39_5::Matrix44


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_matrix44) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Matrix44) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_string**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_string) -> str


    - `createValue`: createValue(arg0: str) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_stringarray**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> list[str]


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_stringarray) -> str


    - `createValue`: createValue(arg0: list[str]) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector2**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> MaterialX_v1_39_5::Vector2


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector2) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector2) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector3**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> MaterialX_v1_39_5::Vector3


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector3) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector3) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **TypedValue_vector4**: 

  - Methods:

    - `getData`: getData(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> MaterialX_v1_39_5::Vector4


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.TypedValue_vector4) -> str


    - `createValue`: createValue(arg0: MaterialX_v1_39_5::Vector4) -> MaterialX.PyMaterialXCore.Value


  - Attributes: TYPE

- **Unit**: 

  - Attributes: CATEGORY

- **UnitConverter**: 

  - Methods:

    - `convert`: Overloaded function.

<br>1. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: float, arg1: str, arg2: str) -> float

<br>2. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector2, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector2

<br>3. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector3, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector3

<br>4. convert(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: MaterialX.PyMaterialXCore.Vector4, arg1: str, arg2: str) -> MaterialX.PyMaterialXCore.Vector4

    - `getUnitAsInteger`: getUnitAsInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: str) -> int


    - `getUnitFromInteger`: getUnitFromInteger(self: MaterialX.PyMaterialXCore.UnitConverter, arg0: int) -> str


- **UnitConverterRegistry**: 

  - Methods:

    - `create`: create() -> MaterialX.PyMaterialXCore.UnitConverterRegistry


    - `addUnitConverter`: addUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef, arg1: MaterialX.PyMaterialXCore.UnitConverter) -> bool


    - `removeUnitConverter`: removeUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> bool


    - `getUnitConverter`: getUnitConverter(self: MaterialX.PyMaterialXCore.UnitConverterRegistry, arg0: MaterialX.PyMaterialXCore.UnitTypeDef) -> MaterialX.PyMaterialXCore.UnitConverter


    - `clearUnitConverters`: clearUnitConverters(self: MaterialX.PyMaterialXCore.UnitConverterRegistry) -> None


- **UnitDef**: 

  - Methods:

    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.UnitDef) -> str


    - `addUnit`: addUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.UnitDef, arg0: str) -> MaterialX.PyMaterialXCore.Unit


    - `getUnits`: getUnits(self: MaterialX.PyMaterialXCore.UnitDef) -> list[MaterialX.PyMaterialXCore.Unit]


  - Attributes: CATEGORY, UNITTYPE_ATTRIBUTE

- **UnitTypeDef**: 

  - Methods:

    - `getUnitDefs`: getUnitDefs(self: MaterialX.PyMaterialXCore.UnitTypeDef) -> list[MaterialX.PyMaterialXCore.UnitDef]


  - Attributes: CATEGORY

- **Value**: 

  - Methods:

    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `getTypeString`: getTypeString(self: MaterialX.PyMaterialXCore.Value) -> str


    - `createValueFromStrings`: createValueFromStrings(value: str, type: str, typeDefPtr: MaterialX_v1_39_5::TypeDef = None) -> MaterialX.PyMaterialXCore.Value


- **ValueElement**: 

  - Methods:

    - `setValueString`: setValueString(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasValueString`: hasValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getValueString`: getValueString(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getResolvedValueString`: getResolvedValueString(self: MaterialX.PyMaterialXCore.ValueElement, resolver: MaterialX_v1_39_5::StringResolver = None) -> str


    - `setInterfaceName`: setInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasInterfaceName`: hasInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getInterfaceName`: getInterfaceName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setImplementationName`: setImplementationName(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasImplementationName`: hasImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getImplementationName`: getImplementationName(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnit`: setUnit(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnit`: hasUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnit`: getUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getActiveUnit`: getActiveUnit(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `setUnitType`: setUnitType(self: MaterialX.PyMaterialXCore.ValueElement, arg0: str) -> None


    - `hasUnitType`: hasUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `getUnitType`: getUnitType(self: MaterialX.PyMaterialXCore.ValueElement) -> str


    - `getIsUniform`: getIsUniform(self: MaterialX.PyMaterialXCore.ValueElement) -> bool


    - `setIsUniform`: setIsUniform(self: MaterialX.PyMaterialXCore.ValueElement, arg0: bool) -> None


    - `setValue`: Set the typed value of an element.

    - `getValue`: Return the typed value of an element.

    - `getDefaultValue`: Return the default value for this element.

  - Attributes: VALUE_ATTRIBUTE, INTERFACE_NAME_ATTRIBUTE, IMPLEMENTATION_NAME_ATTRIBUTE, IMPLEMENTATION_TYPE_ATTRIBUTE, ENUM_ATTRIBUTE, ENUM_VALUES_ATTRIBUTE, UNIT_ATTRIBUTE, UI_NAME_ATTRIBUTE, UI_FOLDER_ATTRIBUTE, UI_MIN_ATTRIBUTE, UI_MAX_ATTRIBUTE, UI_SOFT_MIN_ATTRIBUTE, UI_SOFT_MAX_ATTRIBUTE, UI_STEP_ATTRIBUTE, UI_ADVANCED_ATTRIBUTE

- **Variant**: 

  - Attributes: CATEGORY

- **VariantAssign**: 

  - Methods:

    - `setVariantSetString`: setVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantSetString`: hasVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantSetString`: getVariantSetString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


    - `setVariantString`: setVariantString(self: MaterialX.PyMaterialXCore.VariantAssign, arg0: str) -> None


    - `hasVariantString`: hasVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> bool


    - `getVariantString`: getVariantString(self: MaterialX.PyMaterialXCore.VariantAssign) -> str


  - Attributes: CATEGORY

- **VariantSet**: 

  - Methods:

    - `addVariant`: addVariant(self: MaterialX.PyMaterialXCore.VariantSet, name: str = '') -> MaterialX.PyMaterialXCore.Variant


    - `getVariant`: getVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> MaterialX.PyMaterialXCore.Variant


    - `getVariants`: getVariants(self: MaterialX.PyMaterialXCore.VariantSet) -> list[MaterialX.PyMaterialXCore.Variant]


    - `removeVariant`: removeVariant(self: MaterialX.PyMaterialXCore.VariantSet, arg0: str) -> None


  - Attributes: CATEGORY

- **Vector2**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector2) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector2) -> MaterialX.PyMaterialXCore.Vector2


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector2, arg0: MaterialX.PyMaterialXCore.Vector2) -> float


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector2) -> tuple[float, float]


- **Vector3**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector3) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `cross`: cross(self: MaterialX.PyMaterialXCore.Vector3, arg0: MaterialX.PyMaterialXCore.Vector3) -> MaterialX.PyMaterialXCore.Vector3


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector3) -> tuple[float, float, float]


- **Vector4**: 

  - Methods:

    - `getMagnitude`: getMagnitude(self: MaterialX.PyMaterialXCore.Vector4) -> float


    - `getNormalized`: getNormalized(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `dot`: dot(self: MaterialX.PyMaterialXCore.Vector4, arg0: MaterialX.PyMaterialXCore.Vector4) -> float


    - `copy`: copy(self: MaterialX.PyMaterialXCore.Vector4) -> MaterialX.PyMaterialXCore.Vector4


    - `asTuple`: asTuple(self: MaterialX.PyMaterialXCore.Vector4) -> tuple[float, float, float, float]


- **VectorBase**: 

- **Visibility**: 

  - Methods:

    - `setViewerGeom`: setViewerGeom(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerGeom`: hasViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerGeom`: getViewerGeom(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setViewerCollection`: setViewerCollection(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasViewerCollection`: hasViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getViewerCollection`: getViewerCollection(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisibilityType`: setVisibilityType(self: MaterialX.PyMaterialXCore.Visibility, arg0: str) -> None


    - `hasVisibilityType`: hasVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> bool


    - `getVisibilityType`: getVisibilityType(self: MaterialX.PyMaterialXCore.Visibility) -> str


    - `setVisible`: setVisible(self: MaterialX.PyMaterialXCore.Visibility, arg0: bool) -> None


    - `getVisible`: getVisible(self: MaterialX.PyMaterialXCore.Visibility) -> bool


  - Attributes: CATEGORY

- **XmlReadOptions**: 

  - Attributes: readXIncludeFunction, readComments, readNewlines, upgradeVersion, parentXIncludes

- **XmlWriteOptions**: 

  - Attributes: writeXIncludeEnable, elementPredicate

### Functions

- `createDocument`: createDocument() -> MaterialX_v1_39_5::Document

- `createNamePath`: createNamePath(arg0: list[str]) -> str

- `createValidName`: createValidName(name: str, replaceChar: str = '_') -> str

- `createValueFromStrings`: Convert a MaterialX value and type strings to the corresponding
       Python value.  If the given conversion cannot be performed, then None
       is returned.

       Examples:
           createValueFromStrings('0.1', 'float') -> 0.1
           createValueFromStrings('0.1, 0.2, 0.3', 'color3') -> mx.Color3(0.1, 0.2, 0.3)

- `flattenFilenames`: flattenFilenames(doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A3068A6F0>, customResolver: MaterialX.PyMaterialXCore.StringResolver = None) -> None

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

- `getVersionString`: getVersionString() -> str

- `incrementName`: incrementName(arg0: str) -> str

- `isColorType`: Return True if the given type is a MaterialX color.

- `isColorValue`: Return True if the given value is a MaterialX color.

- `isValidName`: isValidName(arg0: str) -> bool

- `joinStrings`: joinStrings(arg0: list[str], arg1: str) -> str

- `loadDocuments`: loadDocuments(rootPath: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, skipFiles: set[str], includeFiles: set[str], documents: list[MaterialX.PyMaterialXCore.Document], documentsPaths: list[str], readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None, errors: list[str] = None) -> None

- `loadLibraries`: loadLibraries(libraryFolders: list[MaterialX.PyMaterialXFormat.FilePath], searchPath: MaterialX.PyMaterialXFormat.FileSearchPath, doc: MaterialX.PyMaterialXCore.Document, excludeFiles: set[str] = set(), readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> set[str]

- `loadLibrary`: loadLibrary(file: MaterialX.PyMaterialXFormat.FilePath, doc: MaterialX.PyMaterialXCore.Document, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A30688BF0>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `parentNamePath`: parentNamePath(arg0: str) -> str

- `prependXInclude`: prependXInclude(arg0: MaterialX.PyMaterialXCore.Document, arg1: MaterialX.PyMaterialXFormat.FilePath) -> None

- `prettyPrint`: prettyPrint(arg0: MaterialX.PyMaterialXCore.Element) -> str

- `readFile`: readFile(arg0: MaterialX.PyMaterialXFormat.FilePath) -> str

- `readFromXmlFile`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A30658930>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlFileBase`: readFromXmlFileBase(doc: MaterialX.PyMaterialXCore.Document, filename: MaterialX.PyMaterialXFormat.FilePath, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A30658930>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

- `readFromXmlString`: readFromXmlString(doc: MaterialX.PyMaterialXCore.Document, str: str, searchPath: MaterialX.PyMaterialXFormat.FileSearchPath = <MaterialX.PyMaterialXFormat.FileSearchPath object at 0x0000022A3064BB30>, readOptions: MaterialX.PyMaterialXFormat.XmlReadOptions = None) -> None

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
