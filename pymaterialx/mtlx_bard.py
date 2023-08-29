# %% [markdown]
# ## Google Bard Experiment
# 
# Unlike ChatGPT (using `davinci-002`), Bard actually appears to scan for recent information about MaterialX and returns a reasonable answer for the simple query of what's the latest version.
# 
# <img src="./images/google_bard_version_prompt.png">
# 
# It does however provide links to the the source material if available which is useful to jump to the original content. For example the reply here was linked to the MaterialX (`materialx.org`) site.

# %% [markdown]
# ### Basic Knowledge
# 
# Bard also appears to not be able to extract out basic knowledge of even node graphs. A couple of prompts to ask about nodegraph properties and how to group nodes returned mostly non-factual or "nonsense" replies.
# 
# As neither had any source material attribution it is unclear where the information came from.
# 
# <img src="./images/google_bard_nodegraph_prompt.png">
# 
# Note that while the it nice that the online Bard interface provides multiple "drafts", none were remotely close to the correct answer.
# 
# <img src="./images/google_bard_nodegraph_prompt.png">

# %% [markdown]
# ### Source Code Assistance

# %% [markdown]
# Like ChatGPT, Bard will also "make up" code using APIs which don't exist. The following is the result of asking Bard to create a MaterialX node of type "image". Even the import statement is incorrect...

# %%
import materialx as mx

def create_image_node():
  # Create a new node of type "image"
  node = mx.nodes.Image()

  # Set the node's label
  node.label = 'Image'

  # Set the node's image
  node.image = mx.File()
  node.image.filename = 'path_to_the_image'

  # Return the node
  return node

# Create the node
node = create_image_node()

# Add the node to the scene
mx.MaterialX.current_scene().nodes.append(node)

# %% [markdown]
# As the C++ API is published online the hope was that C++ code generation would be better. This is not the case as the APIs used are the same "fictional" ones.  
# 
# ```cpp
# #include <materialx/materialx.h>
# 
# mx::Node* create_image_node() {
#   // Create a new node of type "image"
#   mx::Node* node = new mx::nodes::Image();
# 
#   // Set the node's label
#   node->set_label("Image");
# 
#   // Set the node's image
#   mx::File* image = new mx::File();
#   image->set_filename("path_to_the_image");
#   node->set_image(image);
# 
#   // Return the node
#   return node;
# }
# ```


