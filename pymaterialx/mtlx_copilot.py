# %% [markdown]
# ## Github Copilot  Usage
# 
# ### Introduction
# 
# This notebook will go over usage of github Copilot  for Open Source projects which
# are part of a eco-system of other projects within a standards body. 
# 
# An initial aim in this case is to find out it's usefulness for day-today MaterialX 
# code development. The hope is that since it is using [OpenAI Codex](https://openai.com/blog/openai-codex) 
# that it can leverage existing open source github repositories for MaterialX as well as
# related ASWF projects.
# 
# We concentrate on source code since that appears to be the main focus of Copilot .
# When asked non programming questions Copilot  will reply: `Sorry, but I can only assist with programming related questions.` Strangely the prompt `What is the latest version of MaterialX`` returns this answer?
# 
# As a complimentary tool, the public beta of <a href="https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat" target="_blank">Copilot Chat</a> was also installed.
# 
# > See [Sectup section](#setup) at the end test setup for Visual Studio / Visual Studio Code.
# 
# ### Gating Factors
# 
# We will look at the following factors
# 
# - **Validity** and Correctness: Can code and documentation be generated that is correct and from a validated source?
# - **Accountability**: If code is generated can it be traced back to the original source? 
# - **Efficiency**: Can it save time and effort in development?
# - **Standards**: Does it follow the standards of the project, standard body?
# - **Security**: Does it introduce security risks?
# - **Relevance**: Does it provide suggestions that are up-to-date and relevant to the project?
# - **Repeatability**: Can it be used to repeat the same task over and over again with consistent results?
# 
# Note that notebook was written with Copilot  enabled to test it's usefulness in assisting with writing documentation.
# 
# The general suggestion is to selectively enable Copilot  as it can branch off and suggest text and code which can have no relevance to the task / topic at hand. The guess is much of this is due to lack of context. This includes
# currently logged issues where only the visible editor text is scanned for context.
# 

# %% [markdown]
# ### Correctness and Repeatability
# 
# It it's current state this is one of it's greatest failings. For the most part without providing
# any custom training data it will:
# - Generate code or documentation
# - Complete code or documentation
# which for APIs which do exist or grabs . 
# This is not just return the incorrect version of a call but one of creating "fictional" code calls.
# 
# This not only extends to MaterialX specific code, but also to code from other projects and even
# established APIs such as Python and Javascript. It sometimes will generate calls for one API
# based on existing calls for another API which greatly lowers the "trust" factor.
# 
# Below is a trivial example using comments as hints for code generation.
# `getDefinitions()` does not exist in the API but is suggested by Co-Pilot. Same is true when asking to create
# a definition.
# 
# One useful task would be for generation of test code for existing APIs. But this cannot even be considered
# since the code generated will mostly likely be invalid.

# %%
import MaterialX as mx

# Create a document.
doc = mx.createDocument()

# Find all definitions in the document.
def_list = doc.getDefinitions()

# Create a new definition.
def_ = doc.addDefinition("my_def")

# %% [markdown]
# In terms of code completion, it fairs a bit better. At time of writing the MaterialX Python
# libraries are not documented. After using Co-Pilot for a while it was able to suggest API calls and
# argument completions. An example is shown below of additional suggestions added for `Document` calls.`
# 
# <img src="../documents/images/copilot_function_complete.png" width="60%">
# 
# For the example below, it was able to suggest the correct call node graph creation, but the complete
# code including the import and doc creation must be visible on screen and within the same
# notebook cell for this to work. Sometimes it will just not come up with anything so there is
# a repeatability issue.
# 
# When correct it can save quite a bit of time, but it can waste just as much time by inserting calls or arguments which do not exist in the API. The hope is that correctness and repeatability will improve over time.

# %%
import MaterialX as mx
doc = mx.createDocument()

# Create a new node graph.
graph = doc.addNodeGraph("my_graph")
# Print graph name
print(graph.getName())

# %% [markdown]
# Use the Co-Pilot action to "fix" or explain code is mostly of no use as it will return generic inforamtion about language or environment syntax and not anything specific to the specific code.
# 
# For example querying to "explain" the document `doc.` returns generic information about the need to call a member function, and the "fix" action actually fairs no better, reusing the same non-existent API calls.
# 
# <img src="../documents/images/copilot_fixthis.png" width="80%">

# %% [markdown]
# Using Chat is mostly not recommended. It is unknown how the response is generated but it is pretty well always unusable. As an example the prompt was on how to create a node definition. The example XML returned was:
# ```xml
# <NodeDef id="myNode" type="float">
#   <Input name="input1" type="float" />
#   <Input name="input2" type="float" />
#   <Output name="output" type="float" />
#   <ShaderStage stage="pixel">
#     <ShaderCode>
#       <![CDATA[
#         $output = $input1 + $input2;
#       ]]>
#     </ShaderCode>
#   </ShaderStage>
# </NodeDef>
# ```
# For example the embedding of shader code inside is purely fictitious as is it's explanation:
# Using Chat is mostly not recommended. It is unknown how the response is generated but it is pretty well always | unusable. As an example the prompt was on how to create a node definition. The example XML returned was:
# 
# > The `ShaderStage` element specifies the shader stage where the node will be used, and the `ShaderCode` element contains the shader code that implements the node's functionality. In this case, the node simply adds its two input values together and outputs the result. Note that this is just a simple example, and MaterialX supports much more complex node definitions with multiple shader stages, conditional branching, and other advanced features.
# 

# %% [markdown]
# ### Accountability
# 
# It is important to be able to provide accreditation for any code which is used. This is not possible with Co-Pilot. It is unknown how the code is generated and it is not possible to trace it back to the original source. 
# 
# ### Efficiency
# 
# For efficiency and accuracy, it is much faster to build symbols for a project and used the existing non-Co-Pilot code completion. There are no assumptions as to what code API and version of code to use as this is part of the project itself.
# 
# ### Standards
# 
# There does not seem to be any way to provide formatting rules for Co-Pilot (e.g. such as a Clang format file). When asked to format code it uses some unknown formatting convention. For this aspect it is not worth using Co-Pilot for such as task. Naming convention also seems not possible to perform. Other small consistency items such as ading in a default copyright appears to also not be possible.
# 
# There is no way to add in requirements for version of compiler, platform, and other build dependencies including what test harness is being used. As such it is possible to have code which is compliant being suggested which will not compile or run. 
# 
# For examine move semantics are suggested for performance on a given function, but this may not be available.
# (Strangely, for this example it could not parse the function signature correctly and suggested acting on
# non-existent arguments.)
# 
# <img src="../documents/images/copilot_perffix.png" width="100%">
# 
# ### Relevance
# 
# Using fixed data is one of the major drawbacks. It appears to be possible to add in additional data but
# this has not been attempted for Copilot or any other LLM.
# 
# ### Repeatability
# 
# This is a general issue that tuning can help to alleviate but just from Visual Studio (Code)
# integration it is not possible to tune these parameters.
# 
# 

# %% [markdown]
# ### Appendix: Setup
# 
# As a setup step, the <a href="https://code.visualstudio.com/docs/editor/artificial-intelligence" target="_blank">Copilot</a> and Chat plugins need to be installed.
# 
# <table class="p-2 table table-borderless">
# <tbody>
# <tr>
# <td><img src="../documents/images/copilot_plugin.png"  class="img-fluid" width="80%">
# <td><img src="../documents/images/copilot_chat_plugin.png"  class="img-fluid" width="80%">
# <tr>
# </tbody>
# </table>
# 
# The chat interface for Copilot is available by signing up for the beta program at this time of writing. The chat feature can be used in a similar way to ChatGPT but within the context of a working environment. This has the added advantage of avoiding some context switching. (There are ChatGPT and other unofficial add-ons which are available
# but not considered here)  
# 
# The following is a snapshot with  and chat add-ons installed:
# <img src="../documents/images/copilot_chat_darkmode_example.png"  class="img-fluid" data-bs-toggle="modal" data-bs-target="#imageModal4" width="80%">
# 
# <div class="modal fade" id="imageModal4" tabindex="-1" aria-labelledby="imageModal1Label" aria-hidden="true">
#   <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
#     <div class="modal-content">
#       <div class="modal-body">
#         <img src="../documents/images/copilot_chat_darkmode_example.png" alt="Image 1" width="100%">
#       </div>
#     </div>
#   </div>
# </div>
# 
# If chat is setup, for the Visual Studio Code integration a new tab on the left is available where prompts may be entered.
# 
# Unlike code completion, the responses need to be migrated to their intended location. Options (highlighted on the left) include:
# 
# * Inserting into the editor at a location
# * Export to file
# * Running from terminal.
# 
# The last option (Running from terminal) only makes sense for code which can run as a command. At the current time the response is not checked to see if it's runnable.
# 
# Copilot can be turned on or off via the <img src="../documents/images/copillot.svg"  class="img-fluid" width=16> icon highlighted on the bottom right.


