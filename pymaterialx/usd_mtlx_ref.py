import sys
import os
from pxr import Usd, UsdShade, Sdf
import MaterialX

def create_material_reference(materialx_file, usda_file):
    # Check if MaterialX file exists
    if not os.path.exists(materialx_file):
        print(f"Error: The MaterialX file '{materialx_file}' does not exist.")
        sys.exit(1)
    
    # Create a new USD stage (scene)
    stage = Usd.Stage.CreateNew(usda_file)
    
    # Define a material in the USD stage (root location)
    material_path = '/Root/Material'
    material_prim = UsdShade.Material.Define(stage, Sdf.Path(material_path))
    
    # Reference the MaterialX file as the source for this material
    # Create an SdfReference object to use in AddReference()
    materialx_reference = Sdf.Reference(materialx_file)
    material_prim.GetPrim().GetReferences().AddReference(materialx_reference)

    # Optionally, you can create a placeholder mesh or other items that can use this material
    mesh_path = '/Root/mesh'
    
    # Correctly create an Xform prim (Xform is the standard transform prim in USD)
    mesh_prim = stage.DefinePrim(Sdf.Path(mesh_path), 'Xform')

    # Assign the material to the mesh (you could add additional shaders or properties here)
    material_binding = UsdShade.MaterialBindingAPI(mesh_prim)
    material_binding.Bind(material_prim)

    # Save the stage as a USDA file
    stage.GetRootLayer().Save()

    print(f"Material reference creation successful! The USDA file is saved as: {usda_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python create_material_reference.py <input_materialx_file> <output_usda_file>")
        sys.exit(1)

    materialx_file = sys.argv[1]
    usda_file = sys.argv[2]

    create_material_reference(materialx_file, usda_file)

if __name__ == "__main__":
    main()
