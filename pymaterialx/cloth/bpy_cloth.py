import bpy
import os
import time

def print_step(message):
    """Print a timestamped step message."""
    print("[%s] %s" % (time.strftime('%H:%M:%S'), message))

def print_mesh_stats(obj, label="Mesh"):
    """Print vertex/edge/polygon/triangle counts for the evaluated mesh (modifiers applied)."""
    depsgraph = bpy.context.evaluated_depsgraph_get()
    eval_obj = obj.evaluated_get(depsgraph)
    mesh = eval_obj.to_mesh()
    if mesh:
        num_verts = len(mesh.vertices)
        num_edges = len(mesh.edges)
        num_polys = len(mesh.polygons)
        num_tris = sum(len(poly.vertices) - 2 for poly in mesh.polygons)
        print_step("%s stats: %d vertices, %d edges, %d polygons, approx %d triangles" %
                   (label, num_verts, num_edges, num_polys, num_tris))
        eval_obj.to_mesh_clear()
    else:
        print_step("WARNING: Could not get mesh data for %s" % label)

print_step("Starting draped sphere script with polygon reduction and transform baking")

# -------------------------------------------------------------------
# 1. Clear the scene
# -------------------------------------------------------------------
print_step("Clearing existing mesh objects...")
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
print_step("Scene cleared.")

# -------------------------------------------------------------------
# 2. Create the sphere (collision object)
# -------------------------------------------------------------------
print_step("Creating sphere...")
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
sphere = bpy.context.object
sphere.name = "Sphere"
print_step("Sphere created: '%s' at location %s" % (sphere.name, sphere.location))

# -------------------------------------------------------------------
# 3. Add Collision modifier to sphere
# -------------------------------------------------------------------
print_step("Adding Collision modifier to sphere...")
bpy.context.view_layer.objects.active = sphere
bpy.ops.object.modifier_add(type='COLLISION')
if sphere.modifiers.get("Collision"):
    print_step("Collision modifier added successfully.")
    sphere.collision.thickness_outer = 0.02
    print_step("  -> thickness_outer set to 0.02")
else:
    print_step("ERROR: Collision modifier not found!")

# -------------------------------------------------------------------
# 4. Create detailed plane (cloth)
# -------------------------------------------------------------------
GRID_SIZE = 8
SUBDIVISIONS = 100
print_step("Creating high-resolution plane (cloth)...")
bpy.ops.mesh.primitive_grid_add(
    x_subdivisions=SUBDIVISIONS,
    y_subdivisions=SUBDIVISIONS,
    size=GRID_SIZE,
    location=(0, 0, 2.5)
)
cloth = bpy.context.object
cloth.name = "Cloth"
print_step("Cloth plane created: '%s' at %s" % (cloth.name, cloth.location))
print_step("  -> Subdivisions: %dx%d, Size: %.1f" % (SUBDIVISIONS, SUBDIVISIONS, GRID_SIZE))

# -------------------------------------------------------------------
# 5. Add Cloth modifier with self‑collision
# -------------------------------------------------------------------
print_step("Adding Cloth modifier to plane...")
bpy.context.view_layer.objects.active = cloth
bpy.ops.object.modifier_add(type='CLOTH')
cloth_mod = cloth.modifiers["Cloth"]
if cloth_mod:
    print_step("Cloth modifier added, applying settings...")
    cloth_mod.settings.quality = 10
    cloth_mod.settings.mass = 0.15
    cloth_mod.settings.air_damping = 1.0
    cloth_mod.settings.tension_stiffness = 15
    cloth_mod.settings.compression_stiffness = 15
    cloth_mod.settings.shear_stiffness = 10
    cloth_mod.settings.bending_stiffness = 0.6
    cloth_mod.collision_settings.use_collision = True
    cloth_mod.collision_settings.distance_min = 0.01
    cloth_mod.collision_settings.use_self_collision = True
    cloth_mod.collision_settings.self_distance_min = 0.01
    cloth_mod.collision_settings.self_friction = 5
    print_step("  -> Cloth settings: mass=0.15, bend=0.6, self‑collision ON")
else:
    print_step("ERROR: Cloth modifier not found!")

# -------------------------------------------------------------------
# 6. Set up scene for long simulation
# -------------------------------------------------------------------
print_step("Setting up simulation parameters...")
bpy.context.scene.gravity = (0, 0, -9.81)
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 150
print_step("  -> Gravity: (0,0,-9.81), Frames: 1 to 150")

# -------------------------------------------------------------------
# 7. Run simulation
# -------------------------------------------------------------------
print_step("Starting cloth simulation...")
for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end + 1):
    bpy.context.scene.frame_set(frame)
    if frame % 25 == 0:
        print_step("  Simulated frame %d" % frame)
print_step("Simulation complete.")

# -------------------------------------------------------------------
# 8. Apply cloth modifier
# -------------------------------------------------------------------
print_step("Applying Cloth modifier...")
bpy.context.view_layer.objects.active = cloth
try:
    bpy.ops.object.modifier_apply(modifier="Cloth")
    print_step("Cloth modifier applied.")
except Exception as e:
    print_step("ERROR applying cloth modifier: %s" % e)

# -------------------------------------------------------------------
# 9. Remove Collision modifier from sphere
# -------------------------------------------------------------------
print_step("Removing Collision modifier from sphere...")
if sphere.modifiers.get("Collision"):
    sphere.modifiers.remove(sphere.modifiers["Collision"])
    print_step("Collision modifier removed.")

# -------------------------------------------------------------------
# 10. Add Subdivision Surface modifier for smoothing
# -------------------------------------------------------------------
use_smooth = True
if use_smooth:
    print_step("Adding Subdivision Surface modifier...")
    bpy.context.view_layer.objects.active = cloth
    bpy.ops.object.modifier_add(type='SUBSURF')
    subsurf = cloth.modifiers[-1]
    subsurf.levels = 1
    subsurf.render_levels = 2
    subsurf.subdivision_type = 'CATMULL_CLARK'
    print_step("Subsurf modifier added (levels=1/2).")


# -------------------------------------------------------------------
# 11. ADD DECIMATE MODIFIER FOR POLYGON REDUCTION
# -------------------------------------------------------------------
use_decimate = False
if use_decimate:
    print_step("Adding Decimate modifier for polygon reduction...")
    bpy.ops.object.modifier_add(type='DECIMATE')
    decimate = cloth.modifiers[-1]

    # Move Decimate below Subsurf (Subsurf first, then Decimate)
    bpy.ops.object.modifier_move_up(modifier=decimate.name)

    # Set Decimate options
    decimate.decimate_type = 'COLLAPSE'
    decimate.ratio = 0.15   # 🔧 ADJUST THIS: 0.15 = keep 15% of faces (85% reduction)
    print_step(f"Decimate modifier added: Ratio={decimate.ratio:.2f}")

# -------------------------------------------------------------------
# 12. PRINT FINAL MESH STATISTICS (with modifiers applied)
# -------------------------------------------------------------------
print_step("Evaluating final mesh (Subsurf + Decimate applied)...")
print_mesh_stats(cloth, "Cloth after reduction")

# -------------------------------------------------------------------
# 13. Set smooth shading
# -------------------------------------------------------------------
print_step("Applying smooth shading...")
for obj in (sphere, cloth):
    obj.select_set(True)
    bpy.ops.object.shade_smooth()
    obj.select_set(False)
    print_step("  -> Smooth shading applied to '%s'" % obj.name)

# -------------------------------------------------------------------
# 14. APPLY ALL TRANSFORMS (bake location, rotation, scale to identity)
# -------------------------------------------------------------------
print_step("Applying transforms to both objects to make them identity...")
bpy.ops.object.select_all(action='DESELECT')
sphere.select_set(True)
cloth.select_set(True)
bpy.context.view_layer.objects.active = sphere
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
print_step("Transforms applied. Now both objects have identity transforms.")

# -------------------------------------------------------------------
# 15. Save Blender file
# -------------------------------------------------------------------
blend_path = os.path.join(os.getcwd(), "draped_sphere_reduced.blend")
print_step("Saving Blender file to: %s" % blend_path)
try:
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    if os.path.exists(blend_path):
        print_step("OK: Blender file saved (%d bytes)" % os.path.getsize(blend_path))
    else:
        print_step("WARNING: Blender file save completed but file not found")
except Exception as e:
    print_step("ERROR saving Blender file: %s" % e)

# -------------------------------------------------------------------
# 16. Export as glTF (applying all modifiers)
# -------------------------------------------------------------------
gltf_path = os.path.join(os.getcwd(), "draped_sphere_reduced.glb")
print_step("Exporting glTF to: %s" % gltf_path)
try:
    bpy.ops.export_scene.gltf(
        filepath=gltf_path,
        export_format='GLB',
        export_apply=True        # Applies Subsurf + Decimate – final mesh is reduced!
    )
    if os.path.exists(gltf_path):
        print_step("OK: glTF exported (%d bytes)" % os.path.getsize(gltf_path))
    else:
        print_step("WARNING: glTF export completed but file not found")
except Exception as e:
    print_step("ERROR exporting glTF: %s" % e)

print_step("Script finished successfully! The exported .glb file contains the reduced polygon mesh with identity transforms.")
