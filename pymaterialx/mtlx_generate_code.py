# %% [markdown]
# # Using Generative AI (Source Code)
# 
# In this notebook we will start looking at how we can take advantage of code generation for creating new node definitions.
# While this is not definitive at least a starting point is possible as opposed to staring with nothing or performing 
# code searches.
# 
# The initial interface will just be using text prompts using ChatGPT.
# 
# ## Versioning is Important
# 
# Note that when generating it is quite important to explicitly specify the version of the library, tools, or shading language to avoid creating something unexpected. 
# 
# For now, at least with ChatGPT, just using it directly will **not** recognize current versions of MaterialX. It is possible to run this through an upgrade process however.
# 
# ## Languages "Required"
# 
# To create a base level node the following languages should be implemented:
# 
# * `GLSL`
# * `OSL`
# * `NVIDIA MDL`
# * `Apple MSL (Metal)`
# 
# `Vulkan` and `ESSL` are not required as they are created via generator variants of the`GLSL` generator.
# 
# If you have a custom language then there may be tools available for you to use for node graphs but at time
# of writing unknown if there are tools for writing base nodes. E.g. There is a VEX translator for implementations
# which are defined as functional nodegraphs.
# 
# ## Creating a Graph From Source
# 
# This is still being experimented with but it is possible to a graph from source code via generative AI, though it may not match the syntax expected. A possible starting target is to create a Mermaid graph which can be written in text form.  
# 

# %% [markdown]
# 
# ## 1. ChatGPT prompts 
# 
# In this example we will write a prompt for creating a "Gooch" shader. As the ultimate goal is to create a node we want this to be written as a callable function. We can start with GLSL as the intent is to make this work as a hardware shader.
# 

# %% [markdown]
# The initial prompt is insufficient as it just writes code without even a callable function: `write glsl a gooch shader`

# %% [markdown]
# Certainly! Here's an example of a Gooch shader implemented in GLSL:
# 
# ```glsl
# #version 460
# 
# uniform vec3 lightDirection; // Direction of the light source
# uniform vec3 surfaceColor;   // Color of the surface
# uniform vec3 warmColor;      // Warm color for the shading
# uniform vec3 coolColor;      // Cool color for the shading
# uniform float alpha;         // Ambient color mixing factor
# uniform float beta;          // Diffuse color mixing factor
# 
# in vec3 surfaceNormal;       // Surface normal
# out vec4 fragColor;          // Output fragment color
# 
# void main() {
#     vec3 N = normalize(surfaceNormal);
#     vec3 L = normalize(lightDirection);
#     float intensity = dot(N, L);
# 
#     vec3 warmTerm = mix(warmColor, coolColor, intensity);
#     vec3 coolTerm = mix(coolColor, warmColor, intensity);
# 
#     vec3 diffuseColor = mix(warmTerm, coolTerm, beta);
#     vec3 ambientColor = mix(coolColor, warmColor, alpha);
# 
#     vec3 finalColor = mix(diffuseColor, ambientColor, intensity);
#     
#     fragColor = vec4(finalColor * surfaceColor, 1.0);
# }
# ```
# 
# In the above code, we have a Gooch shader that takes in several uniform variables: `lightDirection` represents the direction of the light source, `surfaceColor` is the color of the surface, `warmColor` is the warm color used for shading, `coolColor` is the cool color used for shading, `alpha` controls the mixing of ambient color, and `beta` controls the mixing of diffuse color.
# 
# The `surfaceNormal` is an input attribute representing the normal vector of the surface. The shader calculates the intensity of the light hitting the surface using the dot product of the surface normal and the light direction.
# 
# Based on the intensity, the shader interpolates between the warm and cool colors to create the diffuse color. It also interpolates between the cool and warm colors to generate the ambient color. The final color is obtained by mixing the diffuse and ambient colors based on the intensity.
# 
# The resulting color is then assigned to the `fragColor` output variable, which represents the final fragment color.
# 
# Please note that this code represents a basic implementation of the Gooch shading technique, and you may need to adjust it based on your specific requirements and rendering pipeline.

# %% [markdown]
# 
# #### GLSL generation
# 
# The results are below. 
# > Note that from the Web interface the text can be copied out directly as Markdown as is done here.

# %% [markdown]
# Certainly! Here's an example of a Gooch shader implemented in GLSL:
# 
# ```glsl
# uniform vec3 lightDirection; // Direction of the light source
# uniform vec3 surfaceColor;   // Color of the surface
# uniform vec3 warmColor;      // Warm color for the shading
# uniform vec3 coolColor;      // Cool color for the shading
# uniform float alpha;         // Ambient color mixing factor
# uniform float beta;          // Diffuse color mixing factor
# 
# in vec3 surfaceNormal;       // Surface normal
# out vec4 fragColor;          // Output fragment color
# 
# void main() {
#     vec3 N = normalize(surfaceNormal);
#     vec3 L = normalize(lightDirection);
#     float intensity = dot(N, L);
# 
#     vec3 warmTerm = mix(warmColor, coolColor, intensity);
#     vec3 coolTerm = mix(coolColor, warmColor, intensity);
# 
#     vec3 diffuseColor = mix(warmTerm, coolTerm, beta);
#     vec3 ambientColor = mix(coolColor, warmColor, alpha);
# 
#     vec3 finalColor = mix(diffuseColor, ambientColor, intensity);
#     
#     fragColor = vec4(finalColor * surfaceColor, 1.0);
# }
# ```
# 
# In the above code, we have a Gooch shader that takes in several uniform variables: `lightDirection` represents the direction of the light source, `surfaceColor` is the color of the surface, `warmColor` is the warm color used for shading, `coolColor` is the cool color used for shading, `alpha` controls the mixing of ambient color, and `beta` controls the mixing of diffuse color.
# 
# The `surfaceNormal` is an input attribute representing the normal vector of the surface. The shader calculates the intensity of the light hitting the surface using the dot product of the surface normal and the light direction.
# 
# Based on the intensity, the shader interpolates between the warm and cool colors to create the diffuse color. It also interpolates between the cool and warm colors to generate the ambient color. The final color is obtained by mixing the diffuse and ambient colors based on the intensity.
# 
# The resulting color is then assigned to the `fragColor` output variable, which represents the final fragment color.
# 
# Please note that this code represents a basic implementation of the Gooch shading technique, and you may need to adjust it based on your specific requirements and rendering pipeline.

# %% [markdown]
# After a few iterations we come up with something more suitable, making sure to use the coding "conventions" for code snippets and that we will need polymorphic versions for different output types -- in this case `color3` and `color4`.
# 
# The prompt is: `Write glsl version 4.6  function for a gooch shader with all parameters as arguments. Do not include an example using the function. Name the function "mx_gooch_" followed by the name of the output type. Prefix all parameter names with "mx_". Create both a 3 color and a 4 color version. `

# %% [markdown]
# Certainly! Here's the GLSL version 4.6 function for a Gooch shader with all parameters as arguments, including both a 3-color and a 4-color version. The function is named "mx_gooch_" followed by the name of the output type, and all parameter names are prefixed with "mx_":
# 
# ```glsl
# #version 460
# 
# // Gooch shader function for 3-color output
# vec3 mx_gooch_vec3(
#     vec3 mx_lightDirection,
#     vec3 mx_surfaceNormal,
#     vec3 mx_surfaceColor,
#     vec3 mx_warmColor,
#     vec3 mx_coolColor,
#     float mx_alpha,
#     float mx_beta
# ) {
#     vec3 N = normalize(mx_surfaceNormal);
#     vec3 L = normalize(mx_lightDirection);
#     float intensity = dot(N, L);
# 
#     vec3 warmTerm = mix(mx_warmColor, mx_coolColor, intensity);
#     vec3 coolTerm = mix(mx_coolColor, mx_warmColor, intensity);
#     
#     vec3 diffuseColor = mix(warmTerm, coolTerm, mx_beta);
#     vec3 ambientColor = mix(mx_coolColor, mx_warmColor, mx_alpha);
#     
#     vec3 finalColor = mix(diffuseColor, ambientColor, intensity);
#     
#     return finalColor * mx_surfaceColor;
# }
# 
# // Gooch shader function for 4-color output
# vec4 mx_gooch_vec4(
#     vec3 mx_lightDirection,
#     vec3 mx_surfaceNormal,
#     vec4 mx_surfaceColor,
#     vec4 mx_warmColor,
#     vec4 mx_coolColor,
#     float mx_alpha,
#     float mx_beta
# ) {
#     vec3 N = normalize(mx_surfaceNormal);
#     vec3 L = normalize(mx_lightDirection);
#     float intensity = dot(N, L);
# 
#     vec4 warmTerm = mix(mx_warmColor, mx_coolColor, intensity);
#     vec4 coolTerm = mix(mx_coolColor, mx_warmColor, intensity);
#     
#     vec4 diffuseColor = mix(warmTerm, coolTerm, mx_beta);
#     vec4 ambientColor = mix(mx_coolColor, mx_warmColor, mx_alpha);
#     
#     vec4 finalColor = mix(diffuseColor, ambientColor, intensity);
#     
#     return finalColor * mx_surfaceColor;
# }
# ```
# 
# In the above code, the `mx_gooch_vec3` function takes in the light direction (`mx_lightDirection`), surface normal (`mx_surfaceNormal`), surface color (`mx_surfaceColor`), warm color (`mx_warmColor`), cool color (`mx_coolColor`), alpha (`mx_alpha`), and beta (`mx_beta`) as parameters. It computes the Gooch shading equation for 3-color output and returns the final color.
# 
# Similarly, the `mx_gooch_vec4` function takes the same parameters but with `vec4` types for surface color, warm color, and cool color, and returns a 4-color output.
# 
# Please note that the code assumes the necessary uniforms and vertex attributes are provided externally and that you will need to integrate this function into a complete GLSL shader program for it to work properly.

# %% [markdown]
# Next we will derive the OSL, MDL, MSL versions from this.

# %% [markdown]
# ## 2. Github Co-Pilot
# 
# Co-Pilot supports both <a href="https://code.visualstudio.com/docs/editor/artificial-intelligence#_chat-view" target="_blank">prompt</a> and in-code for Visual Studio code. Both have been installed here.
# * For in-code generation, a comment can be added as "commands" for generating code. 
# * It is not very "smart" for using local libraries. TBD if there is a way to scan in local code to aid in code
# generation.
# * It is worthwhile for the case of MaterialX to allow usage of "public" code when generating. 
# * It is still not very good a recognizing the arguments required for a interface as it seems to use the bare minimum of arguments.
# * Oft times the incorrect code is currently being generated which makes it of very limited use for now as only very logic
# can be created. This may be due to limited usage of Python and thus availability of Python examples ?

# %% [markdown]
# ### Code-Pilot Code Generation

# %%
import MaterialX as mx
import mtlxutils as mtlxu

# Create a document.
doc = mx.createDocument()

# Find a child node named "abc" in the document. 
node = doc.getChild("abc")

# If the node is found the delete the node
if node:
    doc.removeChild(node)
    
# Create a node graph called "myNodeGraph"
nodeGraph = doc.addNodeGraph("myNodeGraph")

# Create a nodedef from the nod egraph
nodeDef = nodeGraph.addNodeDef("myNodeDef", "myNodeType")


# %% [markdown]
# ## Co-Pilot Chat


