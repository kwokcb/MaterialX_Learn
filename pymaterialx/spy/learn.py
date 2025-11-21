# %%
import slangpy as spy
import pathlib
import MaterialX as mx

currentFolder = pathlib.Path().cwd()
# Create a Slang device with the current folder included in the search paths.
device = spy.create_device(include_paths=[str(currentFolder),
])

slang_source = """
// A simple function that adds two numbers together
float add(float a, float b)
{
    return a + b;
}
"""

# A Slang module represents a collection of Slang code that can be compiled and executed on the device. 
#module = spy.Module.load_from_file(device, "example.slang")
module = spy.Module.load_from_source(device, "example.slang", slang_source)
funct = module.find_function("add")
if funct:
  a = 3.0
  b = 4.5  
  result = funct.call(b=b, a=a)
  print(f"Result of add({a}, {b}): {result}")
#help(funct)

# %%
import numpy as np

# Create a couple of buffers containing 1,000,000 random floats
a = np.random.rand(1000000).astype(np.float32)
b = np.random.rand(1000000).astype(np.float32)

# Call our function and request a numpy array as the result (the default would be a buffer)
result = module.add(a, b, _result='numpy')

# Print the first N results
print(result[:20])

# %%
import numpy as np

# Create a couple of buffers with 128x128 random floats
a = np.random.rand(128, 128).astype(np.float32)
b = np.random.rand(128, 128).astype(np.float32)

# Call our function and ask for a texture back
result = module.add(a, b, _result='texture')

# Print the first 5x5 values
print(result.to_numpy()[:5, :5])

# Display the result using tev.
# A tev is a simple image viewer that comes with SlangPy.
spy.tev.show(result, name='add random')


