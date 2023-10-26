# Guide for Change Submissions

The following is a brief guide for what to include when submitting a change (pull request)

All submissions should be from a local branch off of a fork the main repo. 

```mermaid
---
title: Branch Development
---
%%{init: { 'logLevel': 'debug', 'theme': 'dark',
'themeVariables': {
              'git0': '#888888',
              'git1': '#23A3AA',
              'git2': '#0000ff',
              'git3': '#ff00ff',
              'git4': '#00ffff',
              'git5': '#ffff00',
              'git6': '#ff00ff',
              'git7': '#00ffff'},
 'gitGraph': {
    'rotateCommitLabel': true
  }
}}%%
gitGraph
   commit id: "Branch at head"
   branch your_branch
   checkout your_branch
   commit id: "Local Commit 1"
   commit id: "Local Commit 2"
   checkout main
   commit id: "Main commit X"
   commit id: "Main commit Y"
   commit id: "Latest Head"
   checkout your_branch
   commit id: "Local Commit 3"
   merge main id: "Merge main"
   checkout main
   merge your_branch id: "PULL REQUEST" type: HIGHLIGHT
```


```mermaid
---
title: Pull Request Flowchart
---
flowchart LR
    start --> coreChange{Core Change} --> addCoreTest(Add Core Test)
    start --> nodeConfig{Node Config Change} --> addTestGraph(Add Test Graph to resources/Materials/TestSuite)
    start --> addNewDef{Add nodedef} --> addLib(Add to `libaries`)
    addNewDef --> docNewDef(Document nodedef)
    addNewDef --> addTestGraph
    docNewDef --> runDocGen(Run `mxdoc` generation)
    addTestGraph --> needsRes{Need Resources} --> addRes(Add to resource Image / Geometry)
    start --> syntaxChange{Syntax Change} --> addUpdate(Add Upgrade Logic)
    addUpdate --> runUpdateTest(Update mxformat test)
    start --> shaderGenChange{Shader Gen Change} --> addTestGraph
    addTestGraph --> runGenTest(Run ShaderGen tests)
    shaderGenChange --> renderChange
    start --> renderChange{Rendering Change} --> addTestGraph
    addTestGraph --> runRenderTest

    start --> apiChange{C++ API Change} --> addPython[[Add Python Wrapper]]
    apiChange --> deprecateOldAPI[[Depreate old C++ API]]
    apiChange --> runDox(Build documentation - doxygen)
    apiChange --> addJS[[Add Javascript Wrapper]]
    addJS --> addJSTest(Add Javascript Unit Test)
    renderChange --> runRenderTest(Run Render Tests)
    runRenderTest --> glslAffected{GLSL Affected} --> runGLSL(Run GLSL Render Test)
    runRenderTest --> oslAffected{OSL Affected} --> runOSL(Run OSL Render Test)
    runRenderTest --> examineTestGrid(Check Test Grid)
    runRenderTest --> mdlAffected{MDL Affected} --> runMDL(Run MDL Render Test)
    start --> featureChange{Feature Change} 
    featureChange--> addMV[[Add to MaterialXView]]
    addMV --> addMVCmd[[Add MV Command Line]]
    addMV --> addMVUI[[Add MV UI]]
    featureChange --> addGE[[Add to GraphEditor]]
    addMV --> runMVTests(Run MV tests)
    addGE --> runGETests(Run GraphEditor tests)
    start --> addUtility{Add Utility} --> addPyUtil(Add Python Utility)
    addUtility --> addJSUtil(Add Javascript Utility)
```