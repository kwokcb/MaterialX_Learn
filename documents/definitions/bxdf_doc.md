### Node Group: geometric
* [UsdPrimvarReader](#node-UsdPrimvarReader) 
---------
### Node Group: math
* [UsdTransform2d](#node-UsdTransform2d) 
---------
### Node Group: pbr
* [LamaAdd](#node-LamaAdd) [LamaConductor](#node-LamaConductor) [LamaDielectric](#node-LamaDielectric) [LamaDiffuse](#node-LamaDiffuse) [LamaEmission](#node-LamaEmission) [LamaLayer](#node-LamaLayer) [LamaMix](#node-LamaMix) [LamaSSS](#node-LamaSSS) [LamaSheen](#node-LamaSheen) [LamaTranslucent](#node-LamaTranslucent) [UsdPreviewSurface](#node-UsdPreviewSurface) [disney_brdf_2012](#node-disney_brdf_2012) [disney_bsdf_2015](#node-disney_bsdf_2015) [gltf_pbr](#node-gltf_pbr) [open_pbr_surface](#node-open_pbr_surface) [standard_surface](#node-standard_surface) 
---------
### Node Group: texture2d
* [UsdUVTexture](#node-UsdUVTexture) [gltf_colorimage](#node-gltf_colorimage) [gltf_image](#node-gltf_image) [gltf_iridescence_thickness](#node-gltf_iridescence_thickness) [gltf_normalmap](#node-gltf_normalmap) 
---------
### Node Group: translation
* [standard_surface_to_UsdPreviewSurface](#node-standard_surface_to_UsdPreviewSurface) [standard_surface_to_gltf_pbr](#node-standard_surface_to_gltf_pbr) 
---------
 
### Category: *disney_brdf_2012*
<details open><summary>ND_disney_brdf_2012_surface</summary>
<p>
 
* *Nodedef*: ND_disney_brdf_2012_surface
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **baseColor** | color3 | 0.16, 0.16, 0.16 |  |  |  |  |  |  |  |  |  |  |
| **metallic** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **subsurface** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **specular** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **specularTint** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **anisotropic** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheen** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheenTint** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **clearcoat** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **clearcoatGloss** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *disney_bsdf_2015*
<details open><summary>ND_disney_bsdf_2015_surface</summary>
<p>
 
* *Nodedef*: ND_disney_bsdf_2015_surface
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **baseColor** | color3 | 0.16, 0.16, 0.16 |  |  |  |  |  |  |  |  |  |  |
| **metallic** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **anisotropic** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **specularTint** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheen** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheenTint** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **clearcoat** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **clearcoatGloss** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| **specTrans** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **ior** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **scatterDistance** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **flatness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **diffTrans** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **thin** | boolean | False |  |  |  |  |  |  |  |  |  | true |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *gltf_pbr*
<details open><summary>ND_gltf_pbr_surfaceshader</summary>
<p>
 
* *Nodedef*: ND_gltf_pbr_surfaceshader
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 2.0.1. Is default: True
* *Doc*: glTF PBR
* *Nodegraph*: IMPL_gltf_pbr_surfaceshader


```mermaid
graph TB
    subgraph IMPL_gltf_pbr_surfaceshader
    IMPL_gltf_pbr_surfaceshader_attenuation_color_vec[attenuation_color_vec]
    IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec[ln_attenuation_color_vec]
    IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec_over_distance[ln_attenuation_color_vec_over_distance]
    IMPL_gltf_pbr_surfaceshader_attenuation_coeff[attenuation_coeff]
    IMPL_gltf_pbr_surfaceshader_isotropic_volume[isotropic_volume]
    IMPL_gltf_pbr_surfaceshader_one_minus_ior[one_minus_ior]
    IMPL_gltf_pbr_surfaceshader_one_plus_ior[one_plus_ior]
    IMPL_gltf_pbr_surfaceshader_ior_div[ior_div]
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior[dielectric_f0_from_ior]
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color[dielectric_f0_from_ior_specular_color]
    IMPL_gltf_pbr_surfaceshader_clamped_dielectric_f0_from_ior_specular_color[clamped_dielectric_f0_from_ior_specular_color]
    IMPL_gltf_pbr_surfaceshader_dielectric_f0[dielectric_f0]
    IMPL_gltf_pbr_surfaceshader_dielectric_f90[dielectric_f90]
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_uv]
    IMPL_gltf_pbr_surfaceshader_diffuse_bsdf[diffuse_bsdf]
    IMPL_gltf_pbr_surfaceshader_transmission_bsdf[transmission_bsdf]
    IMPL_gltf_pbr_surfaceshader_reflection_bsdf[reflection_bsdf]
    IMPL_gltf_pbr_surfaceshader_transmission_mix[transmission_mix]
    IMPL_gltf_pbr_surfaceshader_dielectric_bsdf[dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[tf_transmission_bsdf]
    IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[tf_reflection_bsdf]
    IMPL_gltf_pbr_surfaceshader_tf_transmission_mix[tf_transmission_mix]
    IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf[tf_dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf[mix_iridescent_dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_metal_bsdf[metal_bsdf]
    IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[tf_metal_bsdf]
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf[mix_iridescent_metal_bsdf]
    IMPL_gltf_pbr_surfaceshader_base_mix[base_mix]
    IMPL_gltf_pbr_surfaceshader_sheen_color_r[sheen_color_r]
    IMPL_gltf_pbr_surfaceshader_sheen_color_g[sheen_color_g]
    IMPL_gltf_pbr_surfaceshader_sheen_color_b[sheen_color_b]
    IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg[sheen_color_max_rg]
    IMPL_gltf_pbr_surfaceshader_sheen_intensity[sheen_intensity]
    IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq[sheen_roughness_sq]
    IMPL_gltf_pbr_surfaceshader_sheen_color_normalized[sheen_color_normalized]
    IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf]
    IMPL_gltf_pbr_surfaceshader_sheen_layer[sheen_layer]
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughness_uv[clearcoat_roughness_uv]
    IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[clearcoat_bsdf]
    IMPL_gltf_pbr_surfaceshader_clearcoat_layer[clearcoat_layer]
    IMPL_gltf_pbr_surfaceshader_emission_color[emission_color]
    IMPL_gltf_pbr_surfaceshader_emission[emission]
    style IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff  fill:#C72, color:#FFF
    IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff{opacity_mask_cutoff}
    style IMPL_gltf_pbr_surfaceshader_opacity_mask  fill:#C72, color:#FFF
    IMPL_gltf_pbr_surfaceshader_opacity_mask{opacity_mask}
    style IMPL_gltf_pbr_surfaceshader_opacity  fill:#C72, color:#FFF
    IMPL_gltf_pbr_surfaceshader_opacity{opacity}
    IMPL_gltf_pbr_surfaceshader_shader_constructor[shader_constructor]
    style IMPL_gltf_pbr_surfaceshader_out  fill:#0C0, color:#FFF
    IMPL_gltf_pbr_surfaceshader_out([out])
    style IMPL_gltf_pbr_surfaceshader_attenuation_color  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_attenuation_color([attenuation_color])
    style IMPL_gltf_pbr_surfaceshader_attenuation_distance  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_attenuation_distance([attenuation_distance])
    style IMPL_gltf_pbr_surfaceshader_ior  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_ior([ior])
    style IMPL_gltf_pbr_surfaceshader_specular_color  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_specular_color([specular_color])
    style IMPL_gltf_pbr_surfaceshader_specular  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_specular([specular])
    style IMPL_gltf_pbr_surfaceshader_roughness  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_roughness([roughness])
    style IMPL_gltf_pbr_surfaceshader_base_color  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_base_color([base_color])
    style IMPL_gltf_pbr_surfaceshader_normal  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_normal([normal])
    style IMPL_gltf_pbr_surfaceshader_tangent  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_tangent([tangent])
    style IMPL_gltf_pbr_surfaceshader_transmission  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_transmission([transmission])
    style IMPL_gltf_pbr_surfaceshader_iridescence_thickness  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_iridescence_thickness([iridescence_thickness])
    style IMPL_gltf_pbr_surfaceshader_iridescence_ior  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_iridescence_ior([iridescence_ior])
    style IMPL_gltf_pbr_surfaceshader_iridescence  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_iridescence([iridescence])
    style IMPL_gltf_pbr_surfaceshader_metallic  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_metallic([metallic])
    style IMPL_gltf_pbr_surfaceshader_sheen_color  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_sheen_color([sheen_color])
    style IMPL_gltf_pbr_surfaceshader_sheen_roughness  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_sheen_roughness([sheen_roughness])
    style IMPL_gltf_pbr_surfaceshader_clearcoat_roughness  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughness([clearcoat_roughness])
    style IMPL_gltf_pbr_surfaceshader_clearcoat  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_clearcoat([clearcoat])
    style IMPL_gltf_pbr_surfaceshader_clearcoat_normal  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_clearcoat_normal([clearcoat_normal])
    style IMPL_gltf_pbr_surfaceshader_emissive  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_emissive([emissive])
    style IMPL_gltf_pbr_surfaceshader_emissive_strength  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_emissive_strength([emissive_strength])
    style IMPL_gltf_pbr_surfaceshader_alpha  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_alpha([alpha])
    style IMPL_gltf_pbr_surfaceshader_alpha_cutoff  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_alpha_cutoff([alpha_cutoff])
    style IMPL_gltf_pbr_surfaceshader_alpha_mode  fill:#09D, color:#FFF
    IMPL_gltf_pbr_surfaceshader_alpha_mode([alpha_mode])
    end
    IMPL_gltf_pbr_surfaceshader_attenuation_color --"in"--> IMPL_gltf_pbr_surfaceshader_attenuation_color_vec
    IMPL_gltf_pbr_surfaceshader_attenuation_color_vec --"in"--> IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec
    IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec --"in1"--> IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec_over_distance
    IMPL_gltf_pbr_surfaceshader_attenuation_distance --"in2"--> IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec_over_distance
    IMPL_gltf_pbr_surfaceshader_ln_attenuation_color_vec_over_distance --"in1"--> IMPL_gltf_pbr_surfaceshader_attenuation_coeff
    IMPL_gltf_pbr_surfaceshader_attenuation_coeff --"absorption"--> IMPL_gltf_pbr_surfaceshader_isotropic_volume
    IMPL_gltf_pbr_surfaceshader_ior --"in2"--> IMPL_gltf_pbr_surfaceshader_one_minus_ior
    IMPL_gltf_pbr_surfaceshader_ior --"in2"--> IMPL_gltf_pbr_surfaceshader_one_plus_ior
    IMPL_gltf_pbr_surfaceshader_one_minus_ior --"in1"--> IMPL_gltf_pbr_surfaceshader_ior_div
    IMPL_gltf_pbr_surfaceshader_one_plus_ior --"in2"--> IMPL_gltf_pbr_surfaceshader_ior_div
    IMPL_gltf_pbr_surfaceshader_ior_div --"in1"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior
    IMPL_gltf_pbr_surfaceshader_ior_div --"in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior
    IMPL_gltf_pbr_surfaceshader_specular_color --"in1"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior --"in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color --"in1"--> IMPL_gltf_pbr_surfaceshader_clamped_dielectric_f0_from_ior_specular_color
    IMPL_gltf_pbr_surfaceshader_clamped_dielectric_f0_from_ior_specular_color --"in1"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0
    IMPL_gltf_pbr_surfaceshader_specular --"in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0
    IMPL_gltf_pbr_surfaceshader_specular --"in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f90
    IMPL_gltf_pbr_surfaceshader_roughness --"roughness"--> IMPL_gltf_pbr_surfaceshader_roughness_uv
    IMPL_gltf_pbr_surfaceshader_base_color --"color"--> IMPL_gltf_pbr_surfaceshader_diffuse_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_diffuse_bsdf
    IMPL_gltf_pbr_surfaceshader_base_color --"tint"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_ior --"ior"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_dielectric_f0 --"color0"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_dielectric_f90 --"color90"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_diffuse_bsdf --"bg"--> IMPL_gltf_pbr_surfaceshader_transmission_mix
    IMPL_gltf_pbr_surfaceshader_transmission_bsdf --"fg"--> IMPL_gltf_pbr_surfaceshader_transmission_mix
    IMPL_gltf_pbr_surfaceshader_transmission --"mix"--> IMPL_gltf_pbr_surfaceshader_transmission_mix
    IMPL_gltf_pbr_surfaceshader_reflection_bsdf --"top"--> IMPL_gltf_pbr_surfaceshader_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_transmission_mix --"base"--> IMPL_gltf_pbr_surfaceshader_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_base_color --"tint"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_ior --"ior"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf
    IMPL_gltf_pbr_surfaceshader_dielectric_f0 --"color0"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_dielectric_f90 --"color90"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence_thickness --"thinfilm_thickness"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence_ior --"thinfilm_ior"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf
    IMPL_gltf_pbr_surfaceshader_diffuse_bsdf --"bg"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix
    IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf --"fg"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix
    IMPL_gltf_pbr_surfaceshader_transmission --"mix"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix
    IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf --"top"--> IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_tf_transmission_mix --"base"--> IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_dielectric_bsdf --"bg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf --"fg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence --"mix"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf
    IMPL_gltf_pbr_surfaceshader_base_color --"color0"--> IMPL_gltf_pbr_surfaceshader_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_base_color --"color0"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence_thickness --"thinfilm_thickness"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence_ior --"thinfilm_ior"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_metal_bsdf --"bg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf --"fg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_iridescence --"mix"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf --"bg"--> IMPL_gltf_pbr_surfaceshader_base_mix
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf --"fg"--> IMPL_gltf_pbr_surfaceshader_base_mix
    IMPL_gltf_pbr_surfaceshader_metallic --"mix"--> IMPL_gltf_pbr_surfaceshader_base_mix
    IMPL_gltf_pbr_surfaceshader_sheen_color --"in"--> IMPL_gltf_pbr_surfaceshader_sheen_color_r
    IMPL_gltf_pbr_surfaceshader_sheen_color --"in"--> IMPL_gltf_pbr_surfaceshader_sheen_color_g
    IMPL_gltf_pbr_surfaceshader_sheen_color --"in"--> IMPL_gltf_pbr_surfaceshader_sheen_color_b
    IMPL_gltf_pbr_surfaceshader_sheen_color_r --"in1"--> IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg
    IMPL_gltf_pbr_surfaceshader_sheen_color_g --"in2"--> IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg
    IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg --"in1"--> IMPL_gltf_pbr_surfaceshader_sheen_intensity
    IMPL_gltf_pbr_surfaceshader_sheen_color_b --"in2"--> IMPL_gltf_pbr_surfaceshader_sheen_intensity
    IMPL_gltf_pbr_surfaceshader_sheen_roughness --"in1"--> IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq
    IMPL_gltf_pbr_surfaceshader_sheen_roughness --"in2"--> IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq
    IMPL_gltf_pbr_surfaceshader_sheen_color --"in1"--> IMPL_gltf_pbr_surfaceshader_sheen_color_normalized
    IMPL_gltf_pbr_surfaceshader_sheen_intensity --"in2"--> IMPL_gltf_pbr_surfaceshader_sheen_color_normalized
    IMPL_gltf_pbr_surfaceshader_sheen_intensity --"weight"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf
    IMPL_gltf_pbr_surfaceshader_sheen_color_normalized --"color"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf
    IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq --"roughness"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf
    IMPL_gltf_pbr_surfaceshader_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf
    IMPL_gltf_pbr_surfaceshader_sheen_bsdf --"top"--> IMPL_gltf_pbr_surfaceshader_sheen_layer
    IMPL_gltf_pbr_surfaceshader_base_mix --"base"--> IMPL_gltf_pbr_surfaceshader_sheen_layer
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughness --"roughness"--> IMPL_gltf_pbr_surfaceshader_clearcoat_roughness_uv
    IMPL_gltf_pbr_surfaceshader_clearcoat --"weight"--> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughness_uv --"roughness"--> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf
    IMPL_gltf_pbr_surfaceshader_clearcoat_normal --"normal"--> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf
    IMPL_gltf_pbr_surfaceshader_tangent --"tangent"--> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf
    IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf --"top"--> IMPL_gltf_pbr_surfaceshader_clearcoat_layer
    IMPL_gltf_pbr_surfaceshader_sheen_layer --"base"--> IMPL_gltf_pbr_surfaceshader_clearcoat_layer
    IMPL_gltf_pbr_surfaceshader_emissive --"in1"--> IMPL_gltf_pbr_surfaceshader_emission_color
    IMPL_gltf_pbr_surfaceshader_emissive_strength --"in2"--> IMPL_gltf_pbr_surfaceshader_emission_color
    IMPL_gltf_pbr_surfaceshader_emission_color --"color"--> IMPL_gltf_pbr_surfaceshader_emission
    IMPL_gltf_pbr_surfaceshader_alpha --"value1"--> IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff
    IMPL_gltf_pbr_surfaceshader_alpha_cutoff --"value2"--> IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff
    IMPL_gltf_pbr_surfaceshader_alpha_mode --"value1"--> IMPL_gltf_pbr_surfaceshader_opacity_mask
    IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff --"in1"--> IMPL_gltf_pbr_surfaceshader_opacity_mask
    IMPL_gltf_pbr_surfaceshader_alpha --"in2"--> IMPL_gltf_pbr_surfaceshader_opacity_mask
    IMPL_gltf_pbr_surfaceshader_alpha_mode --"value1"--> IMPL_gltf_pbr_surfaceshader_opacity
    IMPL_gltf_pbr_surfaceshader_opacity_mask --"in2"--> IMPL_gltf_pbr_surfaceshader_opacity
    IMPL_gltf_pbr_surfaceshader_clearcoat_layer --"bsdf"--> IMPL_gltf_pbr_surfaceshader_shader_constructor
    IMPL_gltf_pbr_surfaceshader_emission --"edf"--> IMPL_gltf_pbr_surfaceshader_shader_constructor
    IMPL_gltf_pbr_surfaceshader_opacity --"opacity"--> IMPL_gltf_pbr_surfaceshader_shader_constructor
    IMPL_gltf_pbr_surfaceshader_shader_constructor --> IMPL_gltf_pbr_surfaceshader_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **base_color** | color3 | 1, 1, 1 | Base Color | 0, 0, 0 | 1, 1, 1 |  |  |  | Base |  |  |  |
| **metallic** | float | 1.0 | Metallic | 0 | 1 |  |  |  | Base |  |  |  |
| **roughness** | float | 1.0 | Roughness | 0 | 1 |  |  |  | Base |  |  |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Base |  |  |  |
| **tangent** | vector3 | None | Tangent |  |  |  |  |  | Base |  |  |  |
| **occlusion** | float | 1.0 | Occlusion | 0 | 1 |  |  |  | Base |  |  |  |
| **transmission** | float | 0.0 | Transmission | 0 | 1 |  |  |  | Base |  |  |  |
| **specular** | float | 1.0 | Specular | 0 | 1 |  |  |  | Base |  |  |  |
| **specular_color** | color3 | 1, 1, 1 | Specular Color | 0, 0, 0 |  |  | 1, 1, 1 |  | Base |  |  |  |
| **ior** | float | 1.5 | Index of Refraction | 1 |  |  | 3 |  | Base |  |  | true |
| **alpha** | float | 1.0 | Alpha | 0 | 1 |  |  |  | Alpha |  |  |  |
| **alpha_mode** | integer | 0 | Alpha Mode |  |  |  |  |  | Alpha |  |  | true |
| **alpha_cutoff** | float | 0.5 | Alpha Cutoff | 0 | 1 |  |  |  | Alpha |  |  | true |
| **iridescence** | float | 0.0 | Iridescence | 0 | 1 |  |  |  | Iridescence |  |  |  |
| **iridescence_ior** | float | 1.3 | Iridescence Index of Refraction | 1 |  |  | 3 |  | Iridescence |  |  | true |
| **iridescence_thickness** | float | 100.0 | Iridescence Thickness | 0 |  | 100 | 400 |  | Iridescence |  |  |  |
| **sheen_color** | color3 | 0, 0, 0 | Sheen Color | 0, 0, 0 | 1, 1, 1 |  |  |  | Sheen |  |  |  |
| **sheen_roughness** | float | 0.0 | Sheen Roughness | 0 | 1 |  |  |  | Sheen |  |  |  |
| **clearcoat** | float | 0.0 | Clearcoat | 0 | 1 |  |  |  | Clearcoat |  |  |  |
| **clearcoat_roughness** | float | 0.0 | Clearcoat Roughness | 0 | 1 |  |  |  | Clearcoat |  |  |  |
| **clearcoat_normal** | vector3 | None | Clearcoat Normal |  |  |  |  |  | Clearcoat |  |  |  |
| **emissive** | color3 | 0, 0, 0 | Emissive | 0, 0, 0 | 1, 1, 1 |  |  |  | Emission |  |  |  |
| **emissive_strength** | float | 1.0 | Emissive Strength | 0 |  |  |  |  | Emission |  |  | true |
| **thickness** | float | 0.0 | Thickness | 0 |  |  |  |  | Volume |  |  | false |
| **attenuation_distance** | float | None | Attenuation Distance | 0 |  |  |  |  | Volume |  |  | true |
| **attenuation_color** | color3 | 1, 1, 1 | Attenuation Color | 0, 0, 0 | 1, 1, 1 |  |  |  | Volume |  |  | true |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *gltf_colorimage*
<details open><summary>ND_gltf_colorimage</summary>
<p>
 
* *Nodedef*: ND_gltf_colorimage
* *Type*: multioutput
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_colorimage


```mermaid
graph TB
    subgraph NG_gltf_colorimage
    NG_gltf_colorimage_image[image]
    NG_gltf_colorimage_modulate_color[modulate_color]
    NG_gltf_colorimage_modulate_geomcolor[modulate_geomcolor]
    NG_gltf_colorimage_separate_color[separate_color]
    NG_gltf_colorimage_combine_color[combine_color]
    NG_gltf_colorimage_separate_alpha[separate_alpha]
    style NG_gltf_colorimage_outcolor  fill:#0C0, color:#FFF
    NG_gltf_colorimage_outcolor([outcolor])
    style NG_gltf_colorimage_outa  fill:#0C0, color:#FFF
    NG_gltf_colorimage_outa([outa])
    style NG_gltf_colorimage_file  fill:#09D, color:#FFF
    NG_gltf_colorimage_file([file])
    style NG_gltf_colorimage_default1  fill:#09D, color:#FFF
    NG_gltf_colorimage_default1([default])
    style NG_gltf_colorimage_texcoord  fill:#09D, color:#FFF
    NG_gltf_colorimage_texcoord([texcoord])
    style NG_gltf_colorimage_pivot  fill:#09D, color:#FFF
    NG_gltf_colorimage_pivot([pivot])
    style NG_gltf_colorimage_scale  fill:#09D, color:#FFF
    NG_gltf_colorimage_scale([scale])
    style NG_gltf_colorimage_rotate  fill:#09D, color:#FFF
    NG_gltf_colorimage_rotate([rotate])
    style NG_gltf_colorimage_offset  fill:#09D, color:#FFF
    NG_gltf_colorimage_offset([offset])
    style NG_gltf_colorimage_filtertype  fill:#09D, color:#FFF
    NG_gltf_colorimage_filtertype([filtertype])
    style NG_gltf_colorimage_color  fill:#09D, color:#FFF
    NG_gltf_colorimage_color([color])
    style NG_gltf_colorimage_geomcolor  fill:#09D, color:#FFF
    NG_gltf_colorimage_geomcolor([geomcolor])
    end
    NG_gltf_colorimage_file --"file"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_default1 --"default"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_texcoord --"texcoord"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_pivot --"pivot"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_scale --"scale"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_rotate --"rotate"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_offset --"offset"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_filtertype --"filtertype"--> NG_gltf_colorimage_image
    NG_gltf_colorimage_color --"in1"--> NG_gltf_colorimage_modulate_color
    NG_gltf_colorimage_image --"in2"--> NG_gltf_colorimage_modulate_color
    NG_gltf_colorimage_modulate_color --"in1"--> NG_gltf_colorimage_modulate_geomcolor
    NG_gltf_colorimage_geomcolor --"in2"--> NG_gltf_colorimage_modulate_geomcolor
    NG_gltf_colorimage_modulate_geomcolor --"in"--> NG_gltf_colorimage_separate_color
    NG_gltf_colorimage_separate_color --"outr-->in1"--> NG_gltf_colorimage_combine_color
    NG_gltf_colorimage_separate_color --"outg-->in2"--> NG_gltf_colorimage_combine_color
    NG_gltf_colorimage_separate_color --"outb-->in3"--> NG_gltf_colorimage_combine_color
    NG_gltf_colorimage_separate_color --"outa-->in"--> NG_gltf_colorimage_separate_alpha
    NG_gltf_colorimage_combine_color --> NG_gltf_colorimage_outcolor
    NG_gltf_colorimage_separate_alpha --> NG_gltf_colorimage_outa
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  | Image |  |  | true |
| **default** | color4 | 0, 0, 0, 0 |  |  |  |  |  |  | Image |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  | Image |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  | Image |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  | Image |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  | Image |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  | Image |  |  |  |
| **operationorder** | integer | 1 |  |  |  |  |  |  | Image |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  | Image |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  | Image |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  | Image |  |  | true |
| **color** | color4 | 1, 1, 1, 1 |  |  |  |  |  |  | Color |  |  |  |
| **geomcolor** | color4 | 1, 1, 1, 1 | Geometry Color |  |  |  |  |  | Color |  |  |  |
| *outcolor* | color3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *outa* | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
### Category: *gltf_image*
<details open><summary>ND_gltf_image_color3_color3_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_image_color3_color3_1_0
* *Type*: color3
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_NG_gltf_image_color3_color3_1_0


```mermaid
graph TB
    subgraph NG_NG_gltf_image_color3_color3_1_0
    NG_NG_gltf_image_color3_color3_1_0_image[image]
    NG_NG_gltf_image_color3_color3_1_0_invert_scale[invert_scale]
    NG_NG_gltf_image_color3_color3_1_0_negate_rotate[negate_rotate]
    NG_NG_gltf_image_color3_color3_1_0_negate_offset[negate_offset]
    NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    NG_NG_gltf_image_color3_color3_1_0_scale_image[scale_image]
    style NG_NG_gltf_image_color3_color3_1_0_out  fill:#0C0, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_out([out])
    style NG_NG_gltf_image_color3_color3_1_0_file  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_file([file])
    style NG_NG_gltf_image_color3_color3_1_0_default1  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_default1([default])
    style NG_NG_gltf_image_color3_color3_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_uaddressmode([uaddressmode])
    style NG_NG_gltf_image_color3_color3_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_vaddressmode([vaddressmode])
    style NG_NG_gltf_image_color3_color3_1_0_filtertype  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_filtertype([filtertype])
    style NG_NG_gltf_image_color3_color3_1_0_scale  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_scale([scale])
    style NG_NG_gltf_image_color3_color3_1_0_rotate  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_rotate([rotate])
    style NG_NG_gltf_image_color3_color3_1_0_offset  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_offset([offset])
    style NG_NG_gltf_image_color3_color3_1_0_texcoord  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_texcoord([texcoord])
    style NG_NG_gltf_image_color3_color3_1_0_pivot  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_pivot([pivot])
    style NG_NG_gltf_image_color3_color3_1_0_operationorder  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_operationorder([operationorder])
    style NG_NG_gltf_image_color3_color3_1_0_factor  fill:#09D, color:#FFF
    NG_NG_gltf_image_color3_color3_1_0_factor([factor])
    end
    NG_NG_gltf_image_color3_color3_1_0_file --"file"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_default1 --"default"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_place2d --"texcoord"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_uaddressmode --"uaddressmode"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_vaddressmode --"vaddressmode"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_filtertype --"filtertype"--> NG_NG_gltf_image_color3_color3_1_0_image
    NG_NG_gltf_image_color3_color3_1_0_scale --"in2"--> NG_NG_gltf_image_color3_color3_1_0_invert_scale
    NG_NG_gltf_image_color3_color3_1_0_rotate --"in1"--> NG_NG_gltf_image_color3_color3_1_0_negate_rotate
    NG_NG_gltf_image_color3_color3_1_0_offset --"in1"--> NG_NG_gltf_image_color3_color3_1_0_negate_offset
    NG_NG_gltf_image_color3_color3_1_0_texcoord --"texcoord"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_pivot --"pivot"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_invert_scale --"scale"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_negate_rotate --"rotate"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_negate_offset --"offset"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_operationorder --"operationorder"--> NG_NG_gltf_image_color3_color3_1_0_place2d
    NG_NG_gltf_image_color3_color3_1_0_factor --"in1"--> NG_NG_gltf_image_color3_color3_1_0_scale_image
    NG_NG_gltf_image_color3_color3_1_0_image --"in2"--> NG_NG_gltf_image_color3_color3_1_0_scale_image
    NG_NG_gltf_image_color3_color3_1_0_scale_image --> NG_NG_gltf_image_color3_color3_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **factor** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **default** | color3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  |  |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **operationorder** | integer | 0 |  |  |  |  |  |  |  |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  |  |  |  | true |
| *out* | color3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_gltf_image_color4_color4_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_image_color4_color4_1_0
* *Type*: color4
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_image_color4_color4_1_0


```mermaid
graph TB
    subgraph NG_gltf_image_color4_color4_1_0
    NG_gltf_image_color4_color4_1_0_image[image]
    NG_gltf_image_color4_color4_1_0_invert_scale[invert_scale]
    NG_gltf_image_color4_color4_1_0_negate_rotate[negate_rotate]
    NG_gltf_image_color4_color4_1_0_negate_offset[negate_offset]
    NG_gltf_image_color4_color4_1_0_place2d[place2d]
    NG_gltf_image_color4_color4_1_0_scale_image[scale_image]
    style NG_gltf_image_color4_color4_1_0_out  fill:#0C0, color:#FFF
    NG_gltf_image_color4_color4_1_0_out([out])
    style NG_gltf_image_color4_color4_1_0_file  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_file([file])
    style NG_gltf_image_color4_color4_1_0_default1  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_default1([default])
    style NG_gltf_image_color4_color4_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_uaddressmode([uaddressmode])
    style NG_gltf_image_color4_color4_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_vaddressmode([vaddressmode])
    style NG_gltf_image_color4_color4_1_0_filtertype  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_filtertype([filtertype])
    style NG_gltf_image_color4_color4_1_0_scale  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_scale([scale])
    style NG_gltf_image_color4_color4_1_0_rotate  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_rotate([rotate])
    style NG_gltf_image_color4_color4_1_0_offset  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_offset([offset])
    style NG_gltf_image_color4_color4_1_0_texcoord  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_texcoord([texcoord])
    style NG_gltf_image_color4_color4_1_0_pivot  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_pivot([pivot])
    style NG_gltf_image_color4_color4_1_0_operationorder  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_operationorder([operationorder])
    style NG_gltf_image_color4_color4_1_0_factor  fill:#09D, color:#FFF
    NG_gltf_image_color4_color4_1_0_factor([factor])
    end
    NG_gltf_image_color4_color4_1_0_file --"file"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_default1 --"default"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_place2d --"texcoord"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_uaddressmode --"uaddressmode"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_vaddressmode --"vaddressmode"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_filtertype --"filtertype"--> NG_gltf_image_color4_color4_1_0_image
    NG_gltf_image_color4_color4_1_0_scale --"in2"--> NG_gltf_image_color4_color4_1_0_invert_scale
    NG_gltf_image_color4_color4_1_0_rotate --"in1"--> NG_gltf_image_color4_color4_1_0_negate_rotate
    NG_gltf_image_color4_color4_1_0_offset --"in1"--> NG_gltf_image_color4_color4_1_0_negate_offset
    NG_gltf_image_color4_color4_1_0_texcoord --"texcoord"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_pivot --"pivot"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_invert_scale --"scale"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_negate_rotate --"rotate"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_negate_offset --"offset"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_operationorder --"operationorder"--> NG_gltf_image_color4_color4_1_0_place2d
    NG_gltf_image_color4_color4_1_0_factor --"in1"--> NG_gltf_image_color4_color4_1_0_scale_image
    NG_gltf_image_color4_color4_1_0_image --"in2"--> NG_gltf_image_color4_color4_1_0_scale_image
    NG_gltf_image_color4_color4_1_0_scale_image --> NG_gltf_image_color4_color4_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **factor** | color4 | 1, 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **default** | color4 | 0, 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  |  |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **operationorder** | integer | 1 |  |  |  |  |  |  |  |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  |  |  |  | true |
| *out* | color4 | 0, 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_gltf_image_float_float_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_image_float_float_1_0
* *Type*: float
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_image_float_float_1_0


```mermaid
graph TB
    subgraph NG_gltf_image_float_float_1_0
    NG_gltf_image_float_float_1_0_image[image]
    NG_gltf_image_float_float_1_0_invert_scale[invert_scale]
    NG_gltf_image_float_float_1_0_negate_rotate[negate_rotate]
    NG_gltf_image_float_float_1_0_negate_offset[negate_offset]
    NG_gltf_image_float_float_1_0_place2d[place2d]
    NG_gltf_image_float_float_1_0_scale_image[scale_image]
    style NG_gltf_image_float_float_1_0_out  fill:#0C0, color:#FFF
    NG_gltf_image_float_float_1_0_out([out])
    style NG_gltf_image_float_float_1_0_file  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_file([file])
    style NG_gltf_image_float_float_1_0_default1  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_default1([default])
    style NG_gltf_image_float_float_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_uaddressmode([uaddressmode])
    style NG_gltf_image_float_float_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_vaddressmode([vaddressmode])
    style NG_gltf_image_float_float_1_0_filtertype  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_filtertype([filtertype])
    style NG_gltf_image_float_float_1_0_scale  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_scale([scale])
    style NG_gltf_image_float_float_1_0_rotate  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_rotate([rotate])
    style NG_gltf_image_float_float_1_0_offset  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_offset([offset])
    style NG_gltf_image_float_float_1_0_texcoord  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_texcoord([texcoord])
    style NG_gltf_image_float_float_1_0_pivot  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_pivot([pivot])
    style NG_gltf_image_float_float_1_0_operationorder  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_operationorder([operationorder])
    style NG_gltf_image_float_float_1_0_factor  fill:#09D, color:#FFF
    NG_gltf_image_float_float_1_0_factor([factor])
    end
    NG_gltf_image_float_float_1_0_file --"file"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_default1 --"default"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_place2d --"texcoord"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_uaddressmode --"uaddressmode"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_vaddressmode --"vaddressmode"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_filtertype --"filtertype"--> NG_gltf_image_float_float_1_0_image
    NG_gltf_image_float_float_1_0_scale --"in2"--> NG_gltf_image_float_float_1_0_invert_scale
    NG_gltf_image_float_float_1_0_rotate --"in1"--> NG_gltf_image_float_float_1_0_negate_rotate
    NG_gltf_image_float_float_1_0_offset --"in1"--> NG_gltf_image_float_float_1_0_negate_offset
    NG_gltf_image_float_float_1_0_texcoord --"texcoord"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_pivot --"pivot"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_invert_scale --"scale"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_negate_rotate --"rotate"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_negate_offset --"offset"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_operationorder --"operationorder"--> NG_gltf_image_float_float_1_0_place2d
    NG_gltf_image_float_float_1_0_factor --"in1"--> NG_gltf_image_float_float_1_0_scale_image
    NG_gltf_image_float_float_1_0_image --"in2"--> NG_gltf_image_float_float_1_0_scale_image
    NG_gltf_image_float_float_1_0_scale_image --> NG_gltf_image_float_float_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **factor** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| **default** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  |  |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **operationorder** | integer | 0 |  |  |  |  |  |  |  |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  |  |  |  | true |
| *out* | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_gltf_image_vector3_vector3_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_image_vector3_vector3_1_0
* *Type*: vector3
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_image_vector3_vector3_1_0


```mermaid
graph TB
    subgraph NG_gltf_image_vector3_vector3_1_0
    NG_gltf_image_vector3_vector3_1_0_image[image]
    NG_gltf_image_vector3_vector3_1_0_invert_scale[invert_scale]
    NG_gltf_image_vector3_vector3_1_0_negate_rotate[negate_rotate]
    NG_gltf_image_vector3_vector3_1_0_negate_offset[negate_offset]
    NG_gltf_image_vector3_vector3_1_0_place2d[place2d]
    style NG_gltf_image_vector3_vector3_1_0_out  fill:#0C0, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_out([out])
    style NG_gltf_image_vector3_vector3_1_0_file  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_file([file])
    style NG_gltf_image_vector3_vector3_1_0_default1  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_default1([default])
    style NG_gltf_image_vector3_vector3_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_uaddressmode([uaddressmode])
    style NG_gltf_image_vector3_vector3_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_vaddressmode([vaddressmode])
    style NG_gltf_image_vector3_vector3_1_0_filtertype  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_filtertype([filtertype])
    style NG_gltf_image_vector3_vector3_1_0_scale  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_scale([scale])
    style NG_gltf_image_vector3_vector3_1_0_rotate  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_rotate([rotate])
    style NG_gltf_image_vector3_vector3_1_0_offset  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_offset([offset])
    style NG_gltf_image_vector3_vector3_1_0_texcoord  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_texcoord([texcoord])
    style NG_gltf_image_vector3_vector3_1_0_pivot  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_pivot([pivot])
    style NG_gltf_image_vector3_vector3_1_0_operationorder  fill:#09D, color:#FFF
    NG_gltf_image_vector3_vector3_1_0_operationorder([operationorder])
    end
    NG_gltf_image_vector3_vector3_1_0_file --"file"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_default1 --"default"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_place2d --"texcoord"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_uaddressmode --"uaddressmode"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_vaddressmode --"vaddressmode"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_filtertype --"filtertype"--> NG_gltf_image_vector3_vector3_1_0_image
    NG_gltf_image_vector3_vector3_1_0_scale --"in2"--> NG_gltf_image_vector3_vector3_1_0_invert_scale
    NG_gltf_image_vector3_vector3_1_0_rotate --"in1"--> NG_gltf_image_vector3_vector3_1_0_negate_rotate
    NG_gltf_image_vector3_vector3_1_0_offset --"in1"--> NG_gltf_image_vector3_vector3_1_0_negate_offset
    NG_gltf_image_vector3_vector3_1_0_texcoord --"texcoord"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_pivot --"pivot"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_invert_scale --"scale"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_negate_rotate --"rotate"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_negate_offset --"offset"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_operationorder --"operationorder"--> NG_gltf_image_vector3_vector3_1_0_place2d
    NG_gltf_image_vector3_vector3_1_0_image --> NG_gltf_image_vector3_vector3_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **default** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  |  |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **operationorder** | integer | 0 |  |  |  |  |  |  |  |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  |  |  |  | true |
| *out* | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
### Category: *gltf_normalmap*
<details open><summary>ND_gltf_normalmap_vector3_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_normalmap_vector3_1_0
* *Type*: vector3
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_normalmap_vector3_1_0


```mermaid
graph TB
    subgraph NG_gltf_normalmap_vector3_1_0
    NG_gltf_normalmap_vector3_1_0_image[image]
    NG_gltf_normalmap_vector3_1_0_normalmap[normalmap]
    NG_gltf_normalmap_vector3_1_0_invert_scale[invert_scale]
    NG_gltf_normalmap_vector3_1_0_negate_rotate[negate_rotate]
    NG_gltf_normalmap_vector3_1_0_negate_offset[negate_offset]
    NG_gltf_normalmap_vector3_1_0_place2d[place2d]
    style NG_gltf_normalmap_vector3_1_0_out  fill:#0C0, color:#FFF
    NG_gltf_normalmap_vector3_1_0_out([out])
    style NG_gltf_normalmap_vector3_1_0_file  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_file([file])
    style NG_gltf_normalmap_vector3_1_0_default1  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_default1([default])
    style NG_gltf_normalmap_vector3_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_uaddressmode([uaddressmode])
    style NG_gltf_normalmap_vector3_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_vaddressmode([vaddressmode])
    style NG_gltf_normalmap_vector3_1_0_filtertype  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_filtertype([filtertype])
    style NG_gltf_normalmap_vector3_1_0_scale  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_scale([scale])
    style NG_gltf_normalmap_vector3_1_0_rotate  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_rotate([rotate])
    style NG_gltf_normalmap_vector3_1_0_offset  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_offset([offset])
    style NG_gltf_normalmap_vector3_1_0_texcoord  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_texcoord([texcoord])
    style NG_gltf_normalmap_vector3_1_0_pivot  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_pivot([pivot])
    style NG_gltf_normalmap_vector3_1_0_operationorder  fill:#09D, color:#FFF
    NG_gltf_normalmap_vector3_1_0_operationorder([operationorder])
    end
    NG_gltf_normalmap_vector3_1_0_file --"file"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_default1 --"default"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_place2d --"texcoord"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_uaddressmode --"uaddressmode"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_vaddressmode --"vaddressmode"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_filtertype --"filtertype"--> NG_gltf_normalmap_vector3_1_0_image
    NG_gltf_normalmap_vector3_1_0_image --"in"--> NG_gltf_normalmap_vector3_1_0_normalmap
    NG_gltf_normalmap_vector3_1_0_scale --"in2"--> NG_gltf_normalmap_vector3_1_0_invert_scale
    NG_gltf_normalmap_vector3_1_0_rotate --"in1"--> NG_gltf_normalmap_vector3_1_0_negate_rotate
    NG_gltf_normalmap_vector3_1_0_offset --"in1"--> NG_gltf_normalmap_vector3_1_0_negate_offset
    NG_gltf_normalmap_vector3_1_0_texcoord --"texcoord"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_pivot --"pivot"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_invert_scale --"scale"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_negate_rotate --"rotate"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_negate_offset --"offset"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_operationorder --"operationorder"--> NG_gltf_normalmap_vector3_1_0_place2d
    NG_gltf_normalmap_vector3_1_0_normalmap --> NG_gltf_normalmap_vector3_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **default** | vector3 | 0.5, 0.5, 1 |  |  |  |  |  |  |  |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **pivot** | vector2 | 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **rotate** | float | 0.0 |  | 0 | 360 |  |  |  |  |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **operationorder** | integer | 0 |  |  |  |  |  |  |  |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  |  |  |  | true |
| *out* | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
### Category: *gltf_iridescence_thickness*
<details open><summary>ND_gltf_iridescence_thickness_float_1_0</summary>
<p>
 
* *Nodedef*: ND_gltf_iridescence_thickness_float_1_0
* *Type*: float
* *Group*: texture2d
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_gltf_iridescence_thickness_float_1_0


```mermaid
graph TB
    subgraph NG_gltf_iridescence_thickness_float_1_0
    NG_gltf_iridescence_thickness_float_1_0_mixThickness[mixThickness]
    NG_gltf_iridescence_thickness_float_1_0_thickness_image[thickness_image]
    NG_gltf_iridescence_thickness_float_1_0_extract[extract]
    style NG_gltf_iridescence_thickness_float_1_0_out  fill:#0C0, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_out([out])
    style NG_gltf_iridescence_thickness_float_1_0_thicknessMin  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_thicknessMin([thicknessMin])
    style NG_gltf_iridescence_thickness_float_1_0_thicknessMax  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_thicknessMax([thicknessMax])
    style NG_gltf_iridescence_thickness_float_1_0_file  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_file([file])
    style NG_gltf_iridescence_thickness_float_1_0_default1  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_default1([default])
    style NG_gltf_iridescence_thickness_float_1_0_texcoord  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_texcoord([texcoord])
    style NG_gltf_iridescence_thickness_float_1_0_pivot  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_pivot([pivot])
    style NG_gltf_iridescence_thickness_float_1_0_scale  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_scale([scale])
    style NG_gltf_iridescence_thickness_float_1_0_rotate  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_rotate([rotate])
    style NG_gltf_iridescence_thickness_float_1_0_offset  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_offset([offset])
    style NG_gltf_iridescence_thickness_float_1_0_uaddressmode  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_uaddressmode([uaddressmode])
    style NG_gltf_iridescence_thickness_float_1_0_vaddressmode  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_vaddressmode([vaddressmode])
    style NG_gltf_iridescence_thickness_float_1_0_filtertype  fill:#09D, color:#FFF
    NG_gltf_iridescence_thickness_float_1_0_filtertype([filtertype])
    end
    NG_gltf_iridescence_thickness_float_1_0_thicknessMin --"fg"--> NG_gltf_iridescence_thickness_float_1_0_mixThickness
    NG_gltf_iridescence_thickness_float_1_0_thicknessMax --"bg"--> NG_gltf_iridescence_thickness_float_1_0_mixThickness
    NG_gltf_iridescence_thickness_float_1_0_extract --"mix"--> NG_gltf_iridescence_thickness_float_1_0_mixThickness
    NG_gltf_iridescence_thickness_float_1_0_file --"file"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_default1 --"default"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_texcoord --"texcoord"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_pivot --"pivot"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_scale --"scale"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_rotate --"rotate"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_offset --"offset"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_uaddressmode --"uaddressmode"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_vaddressmode --"vaddressmode"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_filtertype --"filtertype"--> NG_gltf_iridescence_thickness_float_1_0_thickness_image
    NG_gltf_iridescence_thickness_float_1_0_thickness_image --"in"--> NG_gltf_iridescence_thickness_float_1_0_extract
    NG_gltf_iridescence_thickness_float_1_0_mixThickness --> NG_gltf_iridescence_thickness_float_1_0_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  | Image |  |  | true |
| **default** | vector3 | 0, 0, 0 |  |  |  |  |  |  | Image |  |  |  |
| **texcoord** | vector2 | None |  |  |  |  |  |  | Image |  |  |  |
| **pivot** | vector2 | 0, 0 |  |  |  |  |  |  | Image |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  | Image |  |  |  |
| **rotate** | float | 0.0 |  |  |  |  |  |  | Image |  |  |  |
| **offset** | vector2 | 0, 0 |  |  |  |  |  |  | Image |  |  |  |
| **uaddressmode** | string | periodic |  |  |  |  |  |  | Image |  |  | true |
| **vaddressmode** | string | periodic |  |  |  |  |  |  | Image |  |  | true |
| **filtertype** | string | linear |  |  |  |  |  |  | Image |  |  | true |
| **thicknessMin** | float | 100.0 |  |  |  |  |  |  | Thickness |  |  |  |
| **thicknessMax** | float | 400.0 |  |  |  |  |  |  | Thickness |  |  |  |
| *out* | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
### Category: *open_pbr_surface*
<details open><summary>ND_open_pbr_surface_surfaceshader</summary>
<p>
 
* *Nodedef*: ND_open_pbr_surface_surfaceshader
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 0.2. Is default: True
* *Doc*: OpenPBR Surface Shading Model
* *Nodegraph*: NG_open_pbr_surface_surfaceshader


```mermaid
graph TB
    subgraph NG_open_pbr_surface_surfaceshader
    NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply1[coat_affect_roughness_multiply1]
    NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply2[coat_affect_roughness_multiply2]
    NG_open_pbr_surface_surfaceshader_coat_affected_roughness[coat_affected_roughness]
    NG_open_pbr_surface_surfaceshader_main_roughness[main_roughness]
    NG_open_pbr_surface_surfaceshader_transmission_roughness_clamped[transmission_roughness_clamped]
    NG_open_pbr_surface_surfaceshader_coat_affected_transmission_roughness[coat_affected_transmission_roughness]
    NG_open_pbr_surface_surfaceshader_transmission_roughness[transmission_roughness]
    NG_open_pbr_surface_surfaceshader_tangent_rotate_degree[tangent_rotate_degree]
    NG_open_pbr_surface_surfaceshader_tangent_rotate[tangent_rotate]
    NG_open_pbr_surface_surfaceshader_tangent_rotate_normalize[tangent_rotate_normalize]
    NG_open_pbr_surface_surfaceshader_main_tangent[main_tangent]
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_degree[coat_tangent_rotate_degree]
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate[coat_tangent_rotate]
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_normalize[coat_tangent_rotate_normalize]
    NG_open_pbr_surface_surfaceshader_coat_tangent[coat_tangent]
    NG_open_pbr_surface_surfaceshader_coat_clamped[coat_clamped]
    NG_open_pbr_surface_surfaceshader_coat_gamma_multiply[coat_gamma_multiply]
    NG_open_pbr_surface_surfaceshader_coat_gamma[coat_gamma]
    NG_open_pbr_surface_surfaceshader_base_color_nonnegative[base_color_nonnegative]
    NG_open_pbr_surface_surfaceshader_coat_affected_diffuse_color[coat_affected_diffuse_color]
    NG_open_pbr_surface_surfaceshader_subsurface_color_nonnegative[subsurface_color_nonnegative]
    NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color[coat_affected_subsurface_color]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection_bsdf[subsurface_thin_walled_reflection_bsdf]
    NG_open_pbr_surface_surfaceshader_one_minus_subsurface_anisotropy[one_minus_subsurface_anisotropy]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_brdf_factor[subsurface_thin_walled_brdf_factor]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection[subsurface_thin_walled_reflection]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission_bsdf[subsurface_thin_walled_transmission_bsdf]
    NG_open_pbr_surface_surfaceshader_one_plus_subsurface_anisotropy[one_plus_subsurface_anisotropy]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_btdf_factor[subsurface_thin_walled_btdf_factor]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission[subsurface_thin_walled_transmission]
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled[subsurface_thin_walled]
    NG_open_pbr_surface_surfaceshader_subsurface_radius_vector[subsurface_radius_vector]
    NG_open_pbr_surface_surfaceshader_subsurface_radius_scaled[subsurface_radius_scaled]
    NG_open_pbr_surface_surfaceshader_subsurface_bsdf[subsurface_bsdf]
    NG_open_pbr_surface_surfaceshader_diffuse_bsdf[diffuse_bsdf]
    NG_open_pbr_surface_surfaceshader_subsurface_selector[subsurface_selector]
    NG_open_pbr_surface_surfaceshader_selected_subsurface[selected_subsurface]
    NG_open_pbr_surface_surfaceshader_opaque_base[opaque_base]
    NG_open_pbr_surface_surfaceshader_specular_to_coat_ior_ratio[specular_to_coat_ior_ratio]
    NG_open_pbr_surface_surfaceshader_specular_ior_minus_one[specular_ior_minus_one]
    NG_open_pbr_surface_surfaceshader_specular_ior_plus_one[specular_ior_plus_one]
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0_sqrt[specular_ior_to_F0_sqrt]
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0[specular_ior_to_F0]
    NG_open_pbr_surface_surfaceshader_half_over_specular_F0[half_over_specular_F0]
    NG_open_pbr_surface_surfaceshader_specular_ior_level_upper_bound[specular_ior_level_upper_bound]
    NG_open_pbr_surface_surfaceshader_specular_ior_level_clamped[specular_ior_level_clamped]
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity1[modulated_specular_reflectivity1]
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity2[modulated_specular_reflectivity2]
    NG_open_pbr_surface_surfaceshader_sqrt_modulated_specular_reflectivity[sqrt_modulated_specular_reflectivity]
    NG_open_pbr_surface_surfaceshader_sign_specular_ior_minus_one[sign_specular_ior_minus_one]
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity3[modulated_specular_reflectivity3]
    NG_open_pbr_surface_surfaceshader_one_minus_modulated_specular_reflectivity3[one_minus_modulated_specular_reflectivity3]
    NG_open_pbr_surface_surfaceshader_one_plus_modulated_specular_reflectivity3[one_plus_modulated_specular_reflectivity3]
    NG_open_pbr_surface_surfaceshader_modulated_specular_ior_ratio[modulated_specular_ior_ratio]
    NG_open_pbr_surface_surfaceshader_dielectric_transmission[dielectric_transmission]
    NG_open_pbr_surface_surfaceshader_dielectric_substrate[dielectric_substrate]
    NG_open_pbr_surface_surfaceshader_dielectric_reflection[dielectric_reflection]
    NG_open_pbr_surface_surfaceshader_dielectric_base[dielectric_base]
    NG_open_pbr_surface_surfaceshader_metal_reflectivity[metal_reflectivity]
    NG_open_pbr_surface_surfaceshader_metal_edgecolor[metal_edgecolor]
    NG_open_pbr_surface_surfaceshader_metal_bsdf[metal_bsdf]
    NG_open_pbr_surface_surfaceshader_base_substrate[base_substrate]
    NG_open_pbr_surface_surfaceshader_half_over_coat_F0[half_over_coat_F0]
    NG_open_pbr_surface_surfaceshader_coat_ior_level_upper_bound[coat_ior_level_upper_bound]
    NG_open_pbr_surface_surfaceshader_coat_ior_level_clamped[coat_ior_level_clamped]
    NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity1[modulated_coat_reflectivity1]
    NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity2[modulated_coat_reflectivity2]
    NG_open_pbr_surface_surfaceshader_sqrt_modulated_coat_reflectivity[sqrt_modulated_coat_reflectivity]
    NG_open_pbr_surface_surfaceshader_one_minus_sqrt_modulated_coat_reflectivity[one_minus_sqrt_modulated_coat_reflectivity]
    NG_open_pbr_surface_surfaceshader_one_plus_sqrt_modulated_coat_reflectivity[one_plus_sqrt_modulated_coat_reflectivity]
    NG_open_pbr_surface_surfaceshader_modulated_coat_ior_ratio[modulated_coat_ior_ratio]
    NG_open_pbr_surface_surfaceshader_modulated_coat_ior[modulated_coat_ior]
    NG_open_pbr_surface_surfaceshader_coat_attenuation[coat_attenuation]
    NG_open_pbr_surface_surfaceshader_coat_substrate_attenuated[coat_substrate_attenuated]
    NG_open_pbr_surface_surfaceshader_coat_roughness_vector[coat_roughness_vector]
    NG_open_pbr_surface_surfaceshader_coat_bsdf[coat_bsdf]
    NG_open_pbr_surface_surfaceshader_coat_layer[coat_layer]
    NG_open_pbr_surface_surfaceshader_fuzz_bsdf[fuzz_bsdf]
    NG_open_pbr_surface_surfaceshader_fuzz_layer[fuzz_layer]
    NG_open_pbr_surface_surfaceshader_coat_ior_minus_one[coat_ior_minus_one]
    NG_open_pbr_surface_surfaceshader_coat_ior_plus_one[coat_ior_plus_one]
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0_sqrt[coat_ior_to_F0_sqrt]
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0[coat_ior_to_F0]
    NG_open_pbr_surface_surfaceshader_emission_weight[emission_weight]
    NG_open_pbr_surface_surfaceshader_uncoated_emission_edf[uncoated_emission_edf]
    NG_open_pbr_surface_surfaceshader_coat_tinted_emission_edf[coat_tinted_emission_edf]
    NG_open_pbr_surface_surfaceshader_one_minus_coat_F0[one_minus_coat_F0]
    NG_open_pbr_surface_surfaceshader_swizzle[swizzle]
    NG_open_pbr_surface_surfaceshader_coated_emission_edf[coated_emission_edf]
    NG_open_pbr_surface_surfaceshader_emission_edf[emission_edf]
    NG_open_pbr_surface_surfaceshader_opacity_luminance[opacity_luminance]
    NG_open_pbr_surface_surfaceshader_swizzle2[swizzle2]
    NG_open_pbr_surface_surfaceshader_shader_constructor[shader_constructor]
    style NG_open_pbr_surface_surfaceshader_out  fill:#0C0, color:#FFF
    NG_open_pbr_surface_surfaceshader_out([out])
    NG_open_pbr_surface_surfaceshader_convert[convert]
    style NG_open_pbr_surface_surfaceshader_coat_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_weight([coat_weight])
    style NG_open_pbr_surface_surfaceshader_coat_roughness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_roughness([coat_roughness])
    style NG_open_pbr_surface_surfaceshader_specular_roughness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_roughness([specular_roughness])
    style NG_open_pbr_surface_surfaceshader_specular_anisotropy  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_anisotropy([specular_anisotropy])
    style NG_open_pbr_surface_surfaceshader_specular_rotation  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_rotation([specular_rotation])
    style NG_open_pbr_surface_surfaceshader_geometry_tangent  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_geometry_tangent([geometry_tangent])
    style NG_open_pbr_surface_surfaceshader_geometry_normal  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_geometry_normal([geometry_normal])
    style NG_open_pbr_surface_surfaceshader_coat_rotation  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_rotation([coat_rotation])
    style NG_open_pbr_surface_surfaceshader_geometry_coat_normal  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_geometry_coat_normal([geometry_coat_normal])
    style NG_open_pbr_surface_surfaceshader_coat_anisotropy  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_anisotropy([coat_anisotropy])
    style NG_open_pbr_surface_surfaceshader_base_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_base_color([base_color])
    style NG_open_pbr_surface_surfaceshader_subsurface_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_subsurface_color([subsurface_color])
    style NG_open_pbr_surface_surfaceshader_base_roughness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_base_roughness([base_roughness])
    style NG_open_pbr_surface_surfaceshader_subsurface_anisotropy  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_subsurface_anisotropy([subsurface_anisotropy])
    style NG_open_pbr_surface_surfaceshader_subsurface_radius_scale  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_subsurface_radius_scale([subsurface_radius_scale])
    style NG_open_pbr_surface_surfaceshader_subsurface_radius  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_subsurface_radius([subsurface_radius])
    style NG_open_pbr_surface_surfaceshader_base_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_base_weight([base_weight])
    style NG_open_pbr_surface_surfaceshader_geometry_thin_walled  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_geometry_thin_walled([geometry_thin_walled])
    style NG_open_pbr_surface_surfaceshader_subsurface_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_subsurface_weight([subsurface_weight])
    style NG_open_pbr_surface_surfaceshader_specular_ior  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_ior([specular_ior])
    style NG_open_pbr_surface_surfaceshader_specular_ior_level  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_ior_level([specular_ior_level])
    style NG_open_pbr_surface_surfaceshader_transmission_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_transmission_color([transmission_color])
    style NG_open_pbr_surface_surfaceshader_transmission_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_transmission_weight([transmission_weight])
    style NG_open_pbr_surface_surfaceshader_specular_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_weight([specular_weight])
    style NG_open_pbr_surface_surfaceshader_specular_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_specular_color([specular_color])
    style NG_open_pbr_surface_surfaceshader_thin_film_thickness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_thin_film_thickness([thin_film_thickness])
    style NG_open_pbr_surface_surfaceshader_thin_film_ior  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_thin_film_ior([thin_film_ior])
    style NG_open_pbr_surface_surfaceshader_base_metalness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_base_metalness([base_metalness])
    style NG_open_pbr_surface_surfaceshader_coat_ior_level  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_ior_level([coat_ior_level])
    style NG_open_pbr_surface_surfaceshader_coat_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_color([coat_color])
    style NG_open_pbr_surface_surfaceshader_fuzz_weight  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_fuzz_weight([fuzz_weight])
    style NG_open_pbr_surface_surfaceshader_fuzz_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_fuzz_color([fuzz_color])
    style NG_open_pbr_surface_surfaceshader_fuzz_roughness  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_fuzz_roughness([fuzz_roughness])
    style NG_open_pbr_surface_surfaceshader_coat_ior  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_coat_ior([coat_ior])
    style NG_open_pbr_surface_surfaceshader_emission_color  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_emission_color([emission_color])
    style NG_open_pbr_surface_surfaceshader_emission_luminance  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_emission_luminance([emission_luminance])
    style NG_open_pbr_surface_surfaceshader_geometry_opacity  fill:#09D, color:#FFF
    NG_open_pbr_surface_surfaceshader_geometry_opacity([geometry_opacity])
    end
    NG_open_pbr_surface_surfaceshader_coat_weight --"in2"--> NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply1
    NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply1 --"in1"--> NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply2
    NG_open_pbr_surface_surfaceshader_coat_roughness --"in2"--> NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply2
    NG_open_pbr_surface_surfaceshader_specular_roughness --"bg"--> NG_open_pbr_surface_surfaceshader_coat_affected_roughness
    NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply2 --"mix"--> NG_open_pbr_surface_surfaceshader_coat_affected_roughness
    NG_open_pbr_surface_surfaceshader_coat_affected_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_main_roughness
    NG_open_pbr_surface_surfaceshader_specular_anisotropy --"anisotropy"--> NG_open_pbr_surface_surfaceshader_main_roughness
    NG_open_pbr_surface_surfaceshader_specular_roughness --"in"--> NG_open_pbr_surface_surfaceshader_transmission_roughness_clamped
    NG_open_pbr_surface_surfaceshader_transmission_roughness_clamped --"bg"--> NG_open_pbr_surface_surfaceshader_coat_affected_transmission_roughness
    NG_open_pbr_surface_surfaceshader_coat_affect_roughness_multiply2 --"mix"--> NG_open_pbr_surface_surfaceshader_coat_affected_transmission_roughness
    NG_open_pbr_surface_surfaceshader_coat_affected_transmission_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_transmission_roughness
    NG_open_pbr_surface_surfaceshader_specular_anisotropy --"anisotropy"--> NG_open_pbr_surface_surfaceshader_transmission_roughness
    NG_open_pbr_surface_surfaceshader_specular_rotation --"in1"--> NG_open_pbr_surface_surfaceshader_tangent_rotate_degree
    NG_open_pbr_surface_surfaceshader_geometry_tangent --"in"--> NG_open_pbr_surface_surfaceshader_tangent_rotate
    NG_open_pbr_surface_surfaceshader_tangent_rotate_degree --"amount"--> NG_open_pbr_surface_surfaceshader_tangent_rotate
    NG_open_pbr_surface_surfaceshader_geometry_normal --"axis"--> NG_open_pbr_surface_surfaceshader_tangent_rotate
    NG_open_pbr_surface_surfaceshader_tangent_rotate --"in"--> NG_open_pbr_surface_surfaceshader_tangent_rotate_normalize
    NG_open_pbr_surface_surfaceshader_specular_anisotropy --"value1"--> NG_open_pbr_surface_surfaceshader_main_tangent
    NG_open_pbr_surface_surfaceshader_tangent_rotate_normalize --"in1"--> NG_open_pbr_surface_surfaceshader_main_tangent
    NG_open_pbr_surface_surfaceshader_geometry_tangent --"in2"--> NG_open_pbr_surface_surfaceshader_main_tangent
    NG_open_pbr_surface_surfaceshader_coat_rotation --"in1"--> NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_degree
    NG_open_pbr_surface_surfaceshader_geometry_tangent --"in"--> NG_open_pbr_surface_surfaceshader_coat_tangent_rotate
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_degree --"amount"--> NG_open_pbr_surface_surfaceshader_coat_tangent_rotate
    NG_open_pbr_surface_surfaceshader_geometry_coat_normal --"axis"--> NG_open_pbr_surface_surfaceshader_coat_tangent_rotate
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate --"in"--> NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_normalize
    NG_open_pbr_surface_surfaceshader_coat_anisotropy --"value1"--> NG_open_pbr_surface_surfaceshader_coat_tangent
    NG_open_pbr_surface_surfaceshader_coat_tangent_rotate_normalize --"in1"--> NG_open_pbr_surface_surfaceshader_coat_tangent
    NG_open_pbr_surface_surfaceshader_geometry_tangent --"in2"--> NG_open_pbr_surface_surfaceshader_coat_tangent
    NG_open_pbr_surface_surfaceshader_coat_weight --"in"--> NG_open_pbr_surface_surfaceshader_coat_clamped
    NG_open_pbr_surface_surfaceshader_coat_clamped --"in1"--> NG_open_pbr_surface_surfaceshader_coat_gamma_multiply
    NG_open_pbr_surface_surfaceshader_coat_gamma_multiply --"in1"--> NG_open_pbr_surface_surfaceshader_coat_gamma
    NG_open_pbr_surface_surfaceshader_base_color --"in1"--> NG_open_pbr_surface_surfaceshader_base_color_nonnegative
    NG_open_pbr_surface_surfaceshader_base_color_nonnegative --"in1"--> NG_open_pbr_surface_surfaceshader_coat_affected_diffuse_color
    NG_open_pbr_surface_surfaceshader_coat_gamma --"in2"--> NG_open_pbr_surface_surfaceshader_coat_affected_diffuse_color
    NG_open_pbr_surface_surfaceshader_subsurface_color --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_color_nonnegative
    NG_open_pbr_surface_surfaceshader_subsurface_color_nonnegative --"in1"--> NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color
    NG_open_pbr_surface_surfaceshader_coat_gamma --"in2"--> NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color
    NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color --"color"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection_bsdf
    NG_open_pbr_surface_surfaceshader_base_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection_bsdf
    NG_open_pbr_surface_surfaceshader_subsurface_anisotropy --"in2"--> NG_open_pbr_surface_surfaceshader_one_minus_subsurface_anisotropy
    NG_open_pbr_surface_surfaceshader_subsurface_color --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_brdf_factor
    NG_open_pbr_surface_surfaceshader_one_minus_subsurface_anisotropy --"in2"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_brdf_factor
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection_bsdf --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_brdf_factor --"in2"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection
    NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color --"color"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission_bsdf
    NG_open_pbr_surface_surfaceshader_subsurface_anisotropy --"in2"--> NG_open_pbr_surface_surfaceshader_one_plus_subsurface_anisotropy
    NG_open_pbr_surface_surfaceshader_subsurface_color --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_btdf_factor
    NG_open_pbr_surface_surfaceshader_one_plus_subsurface_anisotropy --"in2"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_btdf_factor
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission_bsdf --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_btdf_factor --"in2"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_reflection --"fg"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled_transmission --"bg"--> NG_open_pbr_surface_surfaceshader_subsurface_thin_walled
    NG_open_pbr_surface_surfaceshader_subsurface_radius_scale --"in"--> NG_open_pbr_surface_surfaceshader_subsurface_radius_vector
    NG_open_pbr_surface_surfaceshader_subsurface_radius_vector --"in1"--> NG_open_pbr_surface_surfaceshader_subsurface_radius_scaled
    NG_open_pbr_surface_surfaceshader_subsurface_radius --"in2"--> NG_open_pbr_surface_surfaceshader_subsurface_radius_scaled
    NG_open_pbr_surface_surfaceshader_coat_affected_subsurface_color --"color"--> NG_open_pbr_surface_surfaceshader_subsurface_bsdf
    NG_open_pbr_surface_surfaceshader_convert --"radius"--> NG_open_pbr_surface_surfaceshader_subsurface_bsdf
    NG_open_pbr_surface_surfaceshader_subsurface_anisotropy --"anisotropy"--> NG_open_pbr_surface_surfaceshader_subsurface_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_subsurface_bsdf
    NG_open_pbr_surface_surfaceshader_base_weight --"weight"--> NG_open_pbr_surface_surfaceshader_diffuse_bsdf
    NG_open_pbr_surface_surfaceshader_coat_affected_diffuse_color --"color"--> NG_open_pbr_surface_surfaceshader_diffuse_bsdf
    NG_open_pbr_surface_surfaceshader_base_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_diffuse_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_diffuse_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_thin_walled --"in"--> NG_open_pbr_surface_surfaceshader_subsurface_selector
    NG_open_pbr_surface_surfaceshader_subsurface_thin_walled --"fg"--> NG_open_pbr_surface_surfaceshader_selected_subsurface
    NG_open_pbr_surface_surfaceshader_subsurface_bsdf --"bg"--> NG_open_pbr_surface_surfaceshader_selected_subsurface
    NG_open_pbr_surface_surfaceshader_subsurface_selector --"mix"--> NG_open_pbr_surface_surfaceshader_selected_subsurface
    NG_open_pbr_surface_surfaceshader_selected_subsurface --"fg"--> NG_open_pbr_surface_surfaceshader_opaque_base
    NG_open_pbr_surface_surfaceshader_diffuse_bsdf --"bg"--> NG_open_pbr_surface_surfaceshader_opaque_base
    NG_open_pbr_surface_surfaceshader_subsurface_weight --"mix"--> NG_open_pbr_surface_surfaceshader_opaque_base
    NG_open_pbr_surface_surfaceshader_specular_ior --"in1"--> NG_open_pbr_surface_surfaceshader_specular_to_coat_ior_ratio
    NG_open_pbr_surface_surfaceshader_modulated_coat_ior --"in2"--> NG_open_pbr_surface_surfaceshader_specular_to_coat_ior_ratio
    NG_open_pbr_surface_surfaceshader_specular_to_coat_ior_ratio --"in1"--> NG_open_pbr_surface_surfaceshader_specular_ior_minus_one
    NG_open_pbr_surface_surfaceshader_specular_to_coat_ior_ratio --"in2"--> NG_open_pbr_surface_surfaceshader_specular_ior_plus_one
    NG_open_pbr_surface_surfaceshader_specular_ior_minus_one --"in1"--> NG_open_pbr_surface_surfaceshader_specular_ior_to_F0_sqrt
    NG_open_pbr_surface_surfaceshader_specular_ior_plus_one --"in2"--> NG_open_pbr_surface_surfaceshader_specular_ior_to_F0_sqrt
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0_sqrt --"in1"--> NG_open_pbr_surface_surfaceshader_specular_ior_to_F0
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0_sqrt --"in2"--> NG_open_pbr_surface_surfaceshader_specular_ior_to_F0
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_half_over_specular_F0
    NG_open_pbr_surface_surfaceshader_half_over_specular_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_specular_ior_level_upper_bound
    NG_open_pbr_surface_surfaceshader_specular_ior_level --"in"--> NG_open_pbr_surface_surfaceshader_specular_ior_level_clamped
    NG_open_pbr_surface_surfaceshader_specular_ior_level_upper_bound --"high"--> NG_open_pbr_surface_surfaceshader_specular_ior_level_clamped
    NG_open_pbr_surface_surfaceshader_specular_ior_level_clamped --"in1"--> NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity1
    NG_open_pbr_surface_surfaceshader_specular_ior_to_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity1
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity1 --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity2
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity2 --"in"--> NG_open_pbr_surface_surfaceshader_sqrt_modulated_specular_reflectivity
    NG_open_pbr_surface_surfaceshader_specular_ior_minus_one --"in"--> NG_open_pbr_surface_surfaceshader_sign_specular_ior_minus_one
    NG_open_pbr_surface_surfaceshader_sign_specular_ior_minus_one --"in1"--> NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity3
    NG_open_pbr_surface_surfaceshader_sqrt_modulated_specular_reflectivity --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity3
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity3 --"in2"--> NG_open_pbr_surface_surfaceshader_one_minus_modulated_specular_reflectivity3
    NG_open_pbr_surface_surfaceshader_modulated_specular_reflectivity3 --"in2"--> NG_open_pbr_surface_surfaceshader_one_plus_modulated_specular_reflectivity3
    NG_open_pbr_surface_surfaceshader_one_plus_modulated_specular_reflectivity3 --"in1"--> NG_open_pbr_surface_surfaceshader_modulated_specular_ior_ratio
    NG_open_pbr_surface_surfaceshader_one_minus_modulated_specular_reflectivity3 --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_specular_ior_ratio
    NG_open_pbr_surface_surfaceshader_transmission_color --"tint"--> NG_open_pbr_surface_surfaceshader_dielectric_transmission
    NG_open_pbr_surface_surfaceshader_modulated_specular_ior_ratio --"ior"--> NG_open_pbr_surface_surfaceshader_dielectric_transmission
    NG_open_pbr_surface_surfaceshader_transmission_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_dielectric_transmission
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_dielectric_transmission
    NG_open_pbr_surface_surfaceshader_main_tangent --"tangent"--> NG_open_pbr_surface_surfaceshader_dielectric_transmission
    NG_open_pbr_surface_surfaceshader_dielectric_transmission --"fg"--> NG_open_pbr_surface_surfaceshader_dielectric_substrate
    NG_open_pbr_surface_surfaceshader_opaque_base --"bg"--> NG_open_pbr_surface_surfaceshader_dielectric_substrate
    NG_open_pbr_surface_surfaceshader_transmission_weight --"mix"--> NG_open_pbr_surface_surfaceshader_dielectric_substrate
    NG_open_pbr_surface_surfaceshader_specular_weight --"weight"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_specular_color --"tint"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_modulated_specular_ior_ratio --"ior"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_main_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_main_tangent --"tangent"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_thin_film_thickness --"thinfilm_thickness"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_thin_film_ior --"thinfilm_ior"--> NG_open_pbr_surface_surfaceshader_dielectric_reflection
    NG_open_pbr_surface_surfaceshader_dielectric_reflection --"top"--> NG_open_pbr_surface_surfaceshader_dielectric_base
    NG_open_pbr_surface_surfaceshader_dielectric_substrate --"base"--> NG_open_pbr_surface_surfaceshader_dielectric_base
    NG_open_pbr_surface_surfaceshader_base_color --"in1"--> NG_open_pbr_surface_surfaceshader_metal_reflectivity
    NG_open_pbr_surface_surfaceshader_base_weight --"in2"--> NG_open_pbr_surface_surfaceshader_metal_reflectivity
    NG_open_pbr_surface_surfaceshader_specular_color --"in1"--> NG_open_pbr_surface_surfaceshader_metal_edgecolor
    NG_open_pbr_surface_surfaceshader_specular_weight --"in2"--> NG_open_pbr_surface_surfaceshader_metal_edgecolor
    NG_open_pbr_surface_surfaceshader_metal_reflectivity --"color0"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_metal_edgecolor --"color90"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_main_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_main_tangent --"tangent"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_thin_film_thickness --"thinfilm_thickness"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_thin_film_ior --"thinfilm_ior"--> NG_open_pbr_surface_surfaceshader_metal_bsdf
    NG_open_pbr_surface_surfaceshader_metal_bsdf --"fg"--> NG_open_pbr_surface_surfaceshader_base_substrate
    NG_open_pbr_surface_surfaceshader_dielectric_base --"bg"--> NG_open_pbr_surface_surfaceshader_base_substrate
    NG_open_pbr_surface_surfaceshader_base_metalness --"mix"--> NG_open_pbr_surface_surfaceshader_base_substrate
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_half_over_coat_F0
    NG_open_pbr_surface_surfaceshader_half_over_coat_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_coat_ior_level_upper_bound
    NG_open_pbr_surface_surfaceshader_coat_ior_level --"in"--> NG_open_pbr_surface_surfaceshader_coat_ior_level_clamped
    NG_open_pbr_surface_surfaceshader_coat_ior_level_upper_bound --"high"--> NG_open_pbr_surface_surfaceshader_coat_ior_level_clamped
    NG_open_pbr_surface_surfaceshader_coat_ior_level_clamped --"in1"--> NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity1
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity1
    NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity1 --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity2
    NG_open_pbr_surface_surfaceshader_modulated_coat_reflectivity2 --"in"--> NG_open_pbr_surface_surfaceshader_sqrt_modulated_coat_reflectivity
    NG_open_pbr_surface_surfaceshader_sqrt_modulated_coat_reflectivity --"in2"--> NG_open_pbr_surface_surfaceshader_one_minus_sqrt_modulated_coat_reflectivity
    NG_open_pbr_surface_surfaceshader_sqrt_modulated_coat_reflectivity --"in2"--> NG_open_pbr_surface_surfaceshader_one_plus_sqrt_modulated_coat_reflectivity
    NG_open_pbr_surface_surfaceshader_one_plus_sqrt_modulated_coat_reflectivity --"in1"--> NG_open_pbr_surface_surfaceshader_modulated_coat_ior_ratio
    NG_open_pbr_surface_surfaceshader_one_minus_sqrt_modulated_coat_reflectivity --"in2"--> NG_open_pbr_surface_surfaceshader_modulated_coat_ior_ratio
    NG_open_pbr_surface_surfaceshader_modulated_coat_ior_ratio --"fg"--> NG_open_pbr_surface_surfaceshader_modulated_coat_ior
    NG_open_pbr_surface_surfaceshader_coat_weight --"mix"--> NG_open_pbr_surface_surfaceshader_modulated_coat_ior
    NG_open_pbr_surface_surfaceshader_coat_color --"fg"--> NG_open_pbr_surface_surfaceshader_coat_attenuation
    NG_open_pbr_surface_surfaceshader_coat_weight --"mix"--> NG_open_pbr_surface_surfaceshader_coat_attenuation
    NG_open_pbr_surface_surfaceshader_base_substrate --"in1"--> NG_open_pbr_surface_surfaceshader_coat_substrate_attenuated
    NG_open_pbr_surface_surfaceshader_coat_attenuation --"in2"--> NG_open_pbr_surface_surfaceshader_coat_substrate_attenuated
    NG_open_pbr_surface_surfaceshader_coat_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_coat_roughness_vector
    NG_open_pbr_surface_surfaceshader_coat_anisotropy --"anisotropy"--> NG_open_pbr_surface_surfaceshader_coat_roughness_vector
    NG_open_pbr_surface_surfaceshader_coat_weight --"weight"--> NG_open_pbr_surface_surfaceshader_coat_bsdf
    NG_open_pbr_surface_surfaceshader_modulated_coat_ior --"ior"--> NG_open_pbr_surface_surfaceshader_coat_bsdf
    NG_open_pbr_surface_surfaceshader_coat_roughness_vector --"roughness"--> NG_open_pbr_surface_surfaceshader_coat_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_coat_normal --"normal"--> NG_open_pbr_surface_surfaceshader_coat_bsdf
    NG_open_pbr_surface_surfaceshader_coat_tangent --"tangent"--> NG_open_pbr_surface_surfaceshader_coat_bsdf
    NG_open_pbr_surface_surfaceshader_coat_bsdf --"top"--> NG_open_pbr_surface_surfaceshader_coat_layer
    NG_open_pbr_surface_surfaceshader_coat_substrate_attenuated --"base"--> NG_open_pbr_surface_surfaceshader_coat_layer
    NG_open_pbr_surface_surfaceshader_fuzz_weight --"weight"--> NG_open_pbr_surface_surfaceshader_fuzz_bsdf
    NG_open_pbr_surface_surfaceshader_fuzz_color --"color"--> NG_open_pbr_surface_surfaceshader_fuzz_bsdf
    NG_open_pbr_surface_surfaceshader_fuzz_roughness --"roughness"--> NG_open_pbr_surface_surfaceshader_fuzz_bsdf
    NG_open_pbr_surface_surfaceshader_geometry_normal --"normal"--> NG_open_pbr_surface_surfaceshader_fuzz_bsdf
    NG_open_pbr_surface_surfaceshader_fuzz_bsdf --"top"--> NG_open_pbr_surface_surfaceshader_fuzz_layer
    NG_open_pbr_surface_surfaceshader_coat_layer --"base"--> NG_open_pbr_surface_surfaceshader_fuzz_layer
    NG_open_pbr_surface_surfaceshader_coat_ior --"in1"--> NG_open_pbr_surface_surfaceshader_coat_ior_minus_one
    NG_open_pbr_surface_surfaceshader_coat_ior --"in2"--> NG_open_pbr_surface_surfaceshader_coat_ior_plus_one
    NG_open_pbr_surface_surfaceshader_coat_ior_minus_one --"in1"--> NG_open_pbr_surface_surfaceshader_coat_ior_to_F0_sqrt
    NG_open_pbr_surface_surfaceshader_coat_ior_plus_one --"in2"--> NG_open_pbr_surface_surfaceshader_coat_ior_to_F0_sqrt
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0_sqrt --"in1"--> NG_open_pbr_surface_surfaceshader_coat_ior_to_F0
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0_sqrt --"in2"--> NG_open_pbr_surface_surfaceshader_coat_ior_to_F0
    NG_open_pbr_surface_surfaceshader_emission_color --"in1"--> NG_open_pbr_surface_surfaceshader_emission_weight
    NG_open_pbr_surface_surfaceshader_emission_luminance --"in2"--> NG_open_pbr_surface_surfaceshader_emission_weight
    NG_open_pbr_surface_surfaceshader_emission_weight --"color"--> NG_open_pbr_surface_surfaceshader_uncoated_emission_edf
    NG_open_pbr_surface_surfaceshader_uncoated_emission_edf --"in1"--> NG_open_pbr_surface_surfaceshader_coat_tinted_emission_edf
    NG_open_pbr_surface_surfaceshader_coat_color --"in2"--> NG_open_pbr_surface_surfaceshader_coat_tinted_emission_edf
    NG_open_pbr_surface_surfaceshader_coat_ior_to_F0 --"in2"--> NG_open_pbr_surface_surfaceshader_one_minus_coat_F0
    NG_open_pbr_surface_surfaceshader_one_minus_coat_F0 --"in"--> NG_open_pbr_surface_surfaceshader_swizzle
    NG_open_pbr_surface_surfaceshader_swizzle --"color0"--> NG_open_pbr_surface_surfaceshader_coated_emission_edf
    NG_open_pbr_surface_surfaceshader_coat_tinted_emission_edf --"base"--> NG_open_pbr_surface_surfaceshader_coated_emission_edf
    NG_open_pbr_surface_surfaceshader_coated_emission_edf --"fg"--> NG_open_pbr_surface_surfaceshader_emission_edf
    NG_open_pbr_surface_surfaceshader_uncoated_emission_edf --"bg"--> NG_open_pbr_surface_surfaceshader_emission_edf
    NG_open_pbr_surface_surfaceshader_coat_weight --"mix"--> NG_open_pbr_surface_surfaceshader_emission_edf
    NG_open_pbr_surface_surfaceshader_geometry_opacity --"in"--> NG_open_pbr_surface_surfaceshader_opacity_luminance
    NG_open_pbr_surface_surfaceshader_opacity_luminance --"in"--> NG_open_pbr_surface_surfaceshader_swizzle2
    NG_open_pbr_surface_surfaceshader_fuzz_layer --"bsdf"--> NG_open_pbr_surface_surfaceshader_shader_constructor
    NG_open_pbr_surface_surfaceshader_emission_edf --"edf"--> NG_open_pbr_surface_surfaceshader_shader_constructor
    NG_open_pbr_surface_surfaceshader_swizzle2 --"opacity"--> NG_open_pbr_surface_surfaceshader_shader_constructor
    NG_open_pbr_surface_surfaceshader_shader_constructor --> NG_open_pbr_surface_surfaceshader_out
    NG_open_pbr_surface_surfaceshader_subsurface_radius_scaled --"in"--> NG_open_pbr_surface_surfaceshader_convert
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **base_weight** | float | 1.0 | Base Weight | 0.0 | 1.0 |  |  |  | Base |  | Multiplier on the intensity of the reflection from the diffuse and metallic base. |  |
| **base_color** | color3 | 0.8, 0.8, 0.8 | Base Color | 0,0,0 | 1,1,1 |  |  |  | Base |  | Color of the reflection from the diffuse and metallic base. |  |
| **base_roughness** | float | 0.0 | Base Roughness | 0.0 | 1.0 |  |  |  | Base | true | Roughness of the diffuse reflection. Higher values cause the surface to appear flatter. |  |
| **base_metalness** | float | 0.0 | Base Metalness | 0.0 | 1.0 |  |  |  | Base |  | Specifies how metallic the base material appears (dials the base from pure dielectric to pure metal). |  |
| **specular_weight** | float | 1.0 | Specular Weight | 0.0 | 1.0 |  |  |  | Specular |  | Multiplier on the intensity of the specular reflection. |  |
| **specular_color** | color3 | 1, 1, 1 | Specular Color | 0,0,0 | 1,1,1 |  |  |  | Specular |  | Color of the specular reflection (controls the physical edge-tint for metals, and a non-physical overall tint for dielectrics). |  |
| **specular_roughness** | float | 0.3 | Specular Roughness | 0.0 | 1.0 |  |  |  | Specular |  | The roughness of the specular reflection. Lower numbers produce sharper reflections, higher numbers produce blurrier reflections. |  |
| **specular_ior** | float | 1.5 | Specular Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Specular |  | Index of refraction of the dielectric base. |  |
| **specular_ior_level** | float | 0.5 | Specular IOR Level | 0.0 | 1.0 |  |  |  | Specular |  | Modulates the dielectric reflectivity at normal incidence between zero and double the original. |  |
| **specular_anisotropy** | float | 0.0 | Specular Anisotropy | 0.0 | 1.0 |  |  |  | Specular | true | The directional bias of the roughness of the metal/dielectric base, resulting in increasingly stretched highlights along the tangent direction. |  |
| **specular_rotation** | float | 0.0 | Specular Rotation | 0.0 | 1.0 |  |  |  | Specular | true | Rotation of the axis of specular roughness anisotropy around the surface normal. |  |
| **transmission_weight** | float | 0.0 | Transmission Weight | 0.0 | 1.0 |  |  |  | Transmission | true | Mixture weight between the transparent and opaque dielectric base. The greater the value the more transparent the material. |  |
| **transmission_color** | color3 | 1, 1, 1 | Transmission Color | 0,0,0 | 1,1,1 |  |  |  | Transmission | true | Controls color of the transparent base due to Beer's law volumetric absorption under the surface (reverts to a non-physical tint when transmission_depth is zero). |  |
| **transmission_depth** | float | 0.0 | Transmission Depth | 0.0 |  |  | 1.0 |  | Transmission | true | Specifies the distance light travels inside the transparent base before it becomes exactly the transmission_color according to Beer's law. |  |
| **transmission_scatter** | color3 | 0, 0, 0 | Transmission Scatter | 0,0,0 | 1,1,1 |  |  |  | Transmission | true | Controls the color of light volumetrically scattered inside the transparent base. Suitable for materials with visually significant scattering such as honey, fruit juice, murky water, opalescent glass, or milky glass. |  |
| **transmission_scatter_anisotropy** | float | 0.0 | Transmission Anisotropy | 0.0 | 1.0 |  |  |  | Transmission | true | The amount of directional bias, or anisotropy, of the volumetric scattering in the transparent base. |  |
| **transmission_dispersion** | float | 0.0 | Transmission Dispersion | 0.0 |  |  | 100.0 |  | Transmission | true | Dispersion amount, describing how much the dielectric index of refraction varies across wavelengths. |  |
| **subsurface_weight** | float | 0.0 | Subsurface | 0.0 | 1.0 |  |  |  | Subsurface Weight | true | Mixture weight which dials the opaque dielectric base between diffuse reflection and subsurface scattering. A value of 1.0 indicates full subsurface scattering and a value 0 for diffuse reflection only. |  |
| **subsurface_color** | color3 | 0.8, 0.8, 0.8 | Subsurface Color | 0,0,0 | 1,1,1 |  |  |  | Subsurface | true | The overall reflected color of the subsurface scattering effect. |  |
| **subsurface_radius** | float | 1.0 | Subsurface Radius | 0.0 |  |  | 1.0 |  | Subsurface | true | Length scale of the subsurface diffusion blur profile on the surface. |  |
| **subsurface_radius_scale** | color3 | 1, 0.5, 0.25 | Subsurface Radius Scale | 0,0,0 | 1,1,1 |  |  |  | Subsurface | true | RGB multiplier to subsurface_radius, giving the per-channel diffusion blur profile size. |  |
| **subsurface_anisotropy** | float | 0.0 | Subsurface Anisotropy | -1.0 | 1.0 |  |  |  | Subsurface | true | Controls the phase-function of subsurface scattering, where zero scatters light evenly, positive values scatter forward, and negative values scatter backward. |  |
| **fuzz_weight** | float | 0.0 | Fuzz Weight | 0.0 | 1.0 |  |  |  | Fuzz | true | The weight of a fuzz layer that can be used to approximate microfibers, for fabrics such as velvet and satin as well as dust grains. |  |
| **fuzz_color** | color3 | 1, 1, 1 | Fuzz Color | 0,0,0 | 1,1,1 |  |  |  | Fuzz | true | The color of the fuzz layer. |  |
| **fuzz_roughness** | float | 0.5 | Fuzz Roughness | 0.0 | 1.0 |  |  |  | Fuzz | true | The roughness of the fuzz layer. |  |
| **coat_weight** | float | 0.0 | Coat Weight | 0.0 | 1.0 |  |  |  | Coat |  | The weight of a reflective clear-coat layer on top of the material. Use for materials such as car paint or an oily layer. |  |
| **coat_color** | color3 | 1, 1, 1 | Coat Color | 0,0,0 | 1,1,1 |  |  |  | Coat |  | The color of the clear-coat layer's transparency, due to absorption in the coat. |  |
| **coat_roughness** | float | 0.0 | Coat Roughness | 0.0 | 1.0 |  |  |  | Coat |  | The roughness of the clear-coat reflections. The lower the value, the sharper the reflection. |  |
| **coat_anisotropy** | float | 0.0 | Coat Anisotropy | 0.0 | 1.0 |  |  |  | Coat | true | The directional bias of the roughness of the clear-coat layer, resulting in increasingly stretched highlights along the coat tangent direction. |  |
| **coat_rotation** | float | 0.0 | Coat Rotation | 0.0 | 1.0 |  |  |  | Coat | true | Rotation of the axis of clear-coat roughness anisotropy around the coat normal. |  |
| **coat_ior** | float | 1.6 | Coat Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Coat |  | The index of refraction of the clear-coat layer. |  |
| **coat_ior_level** | float | 0.5 | Coat IOR Level | 0.0 | 1.0 |  |  |  | Specular |  | Modulates the clear-coat reflectivity at normal incidence between zero and double the original. |  |
| **thin_film_thickness** | float | 0.0 | Thin Film Thickness | 0.0 |  |  | 2000.0 |  | Thin Film | true | The thickness of the thin film layer on the base (in nanometers). Use for materials such as multi-tone car paint or soap bubbles. |  |
| **thin_film_ior** | float | 1.5 | Thin Film Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Thin Film | true | The index of refraction of the thin-film. |  |
| **emission_luminance** | float | 0.0 | Emission Luminance | 0.0 |  |  | 1000.0 |  | Emission |  | The amount of emitted light, as a luminance in nits. |  |
| **emission_color** | color3 | 1, 1, 1 | Emission Color | 0,0,0 | 1,1,1 |  |  |  | Emission |  | The color of the emitted light. |  |
| **geometry_opacity** | color3 | 1, 1, 1 | Opacity | 0,0,0 | 1,1,1 |  |  |  | Geometry |  | The opacity of the entire material. |  |
| **geometry_thin_walled** | boolean | False | Thin Walled |  |  |  |  |  | Geometry | true | If true the surface is double-sided and represents an infinitesimally thin shell. Suitable for extremely geometrically thin objects such as leaves or paper. |  |
| **geometry_normal** | vector3 | None | Normal |  |  |  |  |  | Geometry |  | Input geometric normal |  |
| **geometry_coat_normal** | vector3 | None | Coat Normal |  |  |  |  |  | Geometry |  | Input normal for clear-coat layer |  |
| **geometry_tangent** | vector3 | None | Tangent Input |  |  |  |  |  | Geometry |  | Input geometric tangent |  |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *standard_surface*
<details open><summary>ND_standard_surface_surfaceshader</summary>
<p>
 
* *Nodedef*: ND_standard_surface_surfaceshader
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 1.0.1. Is default: True
- *Inherits From*: ND_standard_surface_surfaceshader_100
* *Doc*: Autodesk standard surface shader
* *Nodegraph*: NG_standard_surface_surfaceshader_100


```mermaid
graph TB
    subgraph NG_standard_surface_surfaceshader_100
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1[coat_affect_roughness_multiply1]
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[coat_affect_roughness_multiply2]
    NG_standard_surface_surfaceshader_100_coat_affected_roughness[coat_affected_roughness]
    NG_standard_surface_surfaceshader_100_main_roughness[main_roughness]
    NG_standard_surface_surfaceshader_100_transmission_roughness_add[transmission_roughness_add]
    NG_standard_surface_surfaceshader_100_transmission_roughness_clamped[transmission_roughness_clamped]
    NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness[coat_affected_transmission_roughness]
    NG_standard_surface_surfaceshader_100_transmission_roughness[transmission_roughness]
    NG_standard_surface_surfaceshader_100_tangent_rotate_degree[tangent_rotate_degree]
    NG_standard_surface_surfaceshader_100_tangent_rotate[tangent_rotate]
    NG_standard_surface_surfaceshader_100_tangent_rotate_normalize[tangent_rotate_normalize]
    NG_standard_surface_surfaceshader_100_main_tangent[main_tangent]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree[coat_tangent_rotate_degree]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate[coat_tangent_rotate]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize[coat_tangent_rotate_normalize]
    NG_standard_surface_surfaceshader_100_coat_tangent[coat_tangent]
    NG_standard_surface_surfaceshader_100_coat_clamped[coat_clamped]
    NG_standard_surface_surfaceshader_100_coat_gamma_multiply[coat_gamma_multiply]
    NG_standard_surface_surfaceshader_100_coat_gamma[coat_gamma]
    NG_standard_surface_surfaceshader_100_base_color_nonnegative[base_color_nonnegative]
    NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color[coat_affected_diffuse_color]
    NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative[subsurface_color_nonnegative]
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[coat_affected_subsurface_color]
    NG_standard_surface_surfaceshader_100_diffuse_bsdf[diffuse_bsdf]
    NG_standard_surface_surfaceshader_100_translucent_bsdf[translucent_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_radius_vector[subsurface_radius_vector]
    NG_standard_surface_surfaceshader_100_subsurface_radius_scaled[subsurface_radius_scaled]
    NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_selector[subsurface_selector]
    NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[selected_subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_mix[subsurface_mix]
    NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    NG_standard_surface_surfaceshader_100_sheen_layer[sheen_layer]
    NG_standard_surface_surfaceshader_100_transmission_bsdf[transmission_bsdf]
    NG_standard_surface_surfaceshader_100_transmission_mix[transmission_mix]
    NG_standard_surface_surfaceshader_100_specular_bsdf[specular_bsdf]
    NG_standard_surface_surfaceshader_100_specular_layer[specular_layer]
    NG_standard_surface_surfaceshader_100_metal_reflectivity[metal_reflectivity]
    NG_standard_surface_surfaceshader_100_metal_edgecolor[metal_edgecolor]
    NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior]
    NG_standard_surface_surfaceshader_100_metal_bsdf[metal_bsdf]
    NG_standard_surface_surfaceshader_100_metalness_mix[metalness_mix]
    NG_standard_surface_surfaceshader_100_coat_attenuation[coat_attenuation]
    NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated[thin_film_layer_attenuated]
    NG_standard_surface_surfaceshader_100_coat_roughness_vector[coat_roughness_vector]
    NG_standard_surface_surfaceshader_100_coat_bsdf[coat_bsdf]
    NG_standard_surface_surfaceshader_100_coat_layer[coat_layer]
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior[one_minus_coat_ior]
    NG_standard_surface_surfaceshader_100_one_plus_coat_ior[one_plus_coat_ior]
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt[coat_ior_to_F0_sqrt]
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0[coat_ior_to_F0]
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0[one_minus_coat_ior_to_F0]
    NG_standard_surface_surfaceshader_100_emission_weight[emission_weight]
    NG_standard_surface_surfaceshader_100_emission_edf[emission_edf]
    NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf[coat_tinted_emission_edf]
    NG_standard_surface_surfaceshader_100_swizzle[swizzle]
    NG_standard_surface_surfaceshader_100_coat_emission_edf[coat_emission_edf]
    NG_standard_surface_surfaceshader_100_blended_coat_emission_edf[blended_coat_emission_edf]
    NG_standard_surface_surfaceshader_100_opacity_luminance[opacity_luminance]
    NG_standard_surface_surfaceshader_100_swizzle2[swizzle2]
    NG_standard_surface_surfaceshader_100_shader_constructor[shader_constructor]
    style NG_standard_surface_surfaceshader_100_out  fill:#0C0, color:#FFF
    NG_standard_surface_surfaceshader_100_out([out])
    NG_standard_surface_surfaceshader_100_convert[convert]
    style NG_standard_surface_surfaceshader_100_coat_affect_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_affect_roughness([coat_affect_roughness])
    style NG_standard_surface_surfaceshader_100_coat  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat([coat])
    style NG_standard_surface_surfaceshader_100_coat_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_roughness([coat_roughness])
    style NG_standard_surface_surfaceshader_100_specular_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_roughness([specular_roughness])
    style NG_standard_surface_surfaceshader_100_specular_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_anisotropy([specular_anisotropy])
    style NG_standard_surface_surfaceshader_100_transmission_extra_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission_extra_roughness([transmission_extra_roughness])
    style NG_standard_surface_surfaceshader_100_specular_rotation  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_rotation([specular_rotation])
    style NG_standard_surface_surfaceshader_100_tangent  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_tangent([tangent])
    style NG_standard_surface_surfaceshader_100_normal  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_normal([normal])
    style NG_standard_surface_surfaceshader_100_coat_rotation  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_rotation([coat_rotation])
    style NG_standard_surface_surfaceshader_100_coat_normal  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_normal([coat_normal])
    style NG_standard_surface_surfaceshader_100_coat_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_anisotropy([coat_anisotropy])
    style NG_standard_surface_surfaceshader_100_coat_affect_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_affect_color([coat_affect_color])
    style NG_standard_surface_surfaceshader_100_base_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_base_color([base_color])
    style NG_standard_surface_surfaceshader_100_subsurface_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_color([subsurface_color])
    style NG_standard_surface_surfaceshader_100_base  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_base([base])
    style NG_standard_surface_surfaceshader_100_diffuse_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_diffuse_roughness([diffuse_roughness])
    style NG_standard_surface_surfaceshader_100_subsurface_radius  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_radius([subsurface_radius])
    style NG_standard_surface_surfaceshader_100_subsurface_scale  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_scale([subsurface_scale])
    style NG_standard_surface_surfaceshader_100_subsurface_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_anisotropy([subsurface_anisotropy])
    style NG_standard_surface_surfaceshader_100_thin_walled  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_walled([thin_walled])
    style NG_standard_surface_surfaceshader_100_subsurface  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface([subsurface])
    style NG_standard_surface_surfaceshader_100_sheen  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen([sheen])
    style NG_standard_surface_surfaceshader_100_sheen_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen_color([sheen_color])
    style NG_standard_surface_surfaceshader_100_sheen_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen_roughness([sheen_roughness])
    style NG_standard_surface_surfaceshader_100_transmission_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission_color([transmission_color])
    style NG_standard_surface_surfaceshader_100_specular_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_IOR([specular_IOR])
    style NG_standard_surface_surfaceshader_100_transmission  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission([transmission])
    style NG_standard_surface_surfaceshader_100_specular  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular([specular])
    style NG_standard_surface_surfaceshader_100_specular_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_color([specular_color])
    style NG_standard_surface_surfaceshader_100_thin_film_thickness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_film_thickness([thin_film_thickness])
    style NG_standard_surface_surfaceshader_100_thin_film_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_film_IOR([thin_film_IOR])
    style NG_standard_surface_surfaceshader_100_metalness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_metalness([metalness])
    style NG_standard_surface_surfaceshader_100_coat_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_color([coat_color])
    style NG_standard_surface_surfaceshader_100_coat_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_IOR([coat_IOR])
    style NG_standard_surface_surfaceshader_100_emission_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_emission_color([emission_color])
    style NG_standard_surface_surfaceshader_100_emission  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_emission([emission])
    style NG_standard_surface_surfaceshader_100_opacity  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_opacity([opacity])
    end
    NG_standard_surface_surfaceshader_100_coat_affect_roughness --"in1"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1
    NG_standard_surface_surfaceshader_100_coat --"in2"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1 --"in1"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2
    NG_standard_surface_surfaceshader_100_coat_roughness --"in2"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2
    NG_standard_surface_surfaceshader_100_specular_roughness --"bg"--> NG_standard_surface_surfaceshader_100_coat_affected_roughness
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2 --"mix"--> NG_standard_surface_surfaceshader_100_coat_affected_roughness
    NG_standard_surface_surfaceshader_100_coat_affected_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_main_roughness
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_main_roughness
    NG_standard_surface_surfaceshader_100_specular_roughness --"in1"--> NG_standard_surface_surfaceshader_100_transmission_roughness_add
    NG_standard_surface_surfaceshader_100_transmission_extra_roughness --"in2"--> NG_standard_surface_surfaceshader_100_transmission_roughness_add
    NG_standard_surface_surfaceshader_100_transmission_roughness_add --"in"--> NG_standard_surface_surfaceshader_100_transmission_roughness_clamped
    NG_standard_surface_surfaceshader_100_transmission_roughness_clamped --"bg"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2 --"mix"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness
    NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_transmission_roughness
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_transmission_roughness
    NG_standard_surface_surfaceshader_100_specular_rotation --"in1"--> NG_standard_surface_surfaceshader_100_tangent_rotate_degree
    NG_standard_surface_surfaceshader_100_tangent --"in"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_tangent_rotate_degree --"amount"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_normal --"axis"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_tangent_rotate --"in"--> NG_standard_surface_surfaceshader_100_tangent_rotate_normalize
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"value1"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_tangent_rotate_normalize --"in1"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_tangent --"in2"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_coat_rotation --"in1"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree
    NG_standard_surface_surfaceshader_100_tangent --"in"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree --"amount"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_normal --"axis"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate --"in"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize
    NG_standard_surface_surfaceshader_100_coat_anisotropy --"value1"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize --"in1"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_tangent --"in2"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_coat --"in"--> NG_standard_surface_surfaceshader_100_coat_clamped
    NG_standard_surface_surfaceshader_100_coat_clamped --"in1"--> NG_standard_surface_surfaceshader_100_coat_gamma_multiply
    NG_standard_surface_surfaceshader_100_coat_affect_color --"in2"--> NG_standard_surface_surfaceshader_100_coat_gamma_multiply
    NG_standard_surface_surfaceshader_100_coat_gamma_multiply --"in1"--> NG_standard_surface_surfaceshader_100_coat_gamma
    NG_standard_surface_surfaceshader_100_base_color --"in1"--> NG_standard_surface_surfaceshader_100_base_color_nonnegative
    NG_standard_surface_surfaceshader_100_base_color_nonnegative --"in1"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color
    NG_standard_surface_surfaceshader_100_coat_gamma --"in2"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color
    NG_standard_surface_surfaceshader_100_subsurface_color --"in1"--> NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative
    NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative --"in1"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color
    NG_standard_surface_surfaceshader_100_coat_gamma --"in2"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color
    NG_standard_surface_surfaceshader_100_base --"weight"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color --"color"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_diffuse_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color --"color"--> NG_standard_surface_surfaceshader_100_translucent_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_translucent_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_radius --"in"--> NG_standard_surface_surfaceshader_100_subsurface_radius_vector
    NG_standard_surface_surfaceshader_100_subsurface_radius_vector --"in1"--> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled
    NG_standard_surface_surfaceshader_100_subsurface_scale --"in2"--> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color --"color"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_convert --"radius"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_thin_walled --"in"--> NG_standard_surface_surfaceshader_100_subsurface_selector
    NG_standard_surface_surfaceshader_100_translucent_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_bsdf --"bg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_selector --"mix"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_diffuse_bsdf --"bg"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_subsurface --"mix"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_sheen --"weight"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_color --"color"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_bsdf --"top"--> NG_standard_surface_surfaceshader_100_sheen_layer
    NG_standard_surface_surfaceshader_100_subsurface_mix --"base"--> NG_standard_surface_surfaceshader_100_sheen_layer
    NG_standard_surface_surfaceshader_100_transmission_color --"tint"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_specular_IOR --"ior"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_transmission_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_transmission_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_sheen_layer --"bg"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_transmission --"mix"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_specular --"weight"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_color --"tint"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_IOR --"ior"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_main_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_thickness --"thinfilm_thickness"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_IOR --"thinfilm_ior"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_bsdf --"top"--> NG_standard_surface_surfaceshader_100_specular_layer
    NG_standard_surface_surfaceshader_100_transmission_mix --"base"--> NG_standard_surface_surfaceshader_100_specular_layer
    NG_standard_surface_surfaceshader_100_base_color --"in1"--> NG_standard_surface_surfaceshader_100_metal_reflectivity
    NG_standard_surface_surfaceshader_100_base --"in2"--> NG_standard_surface_surfaceshader_100_metal_reflectivity
    NG_standard_surface_surfaceshader_100_specular_color --"in1"--> NG_standard_surface_surfaceshader_100_metal_edgecolor
    NG_standard_surface_surfaceshader_100_specular --"in2"--> NG_standard_surface_surfaceshader_100_metal_edgecolor
    NG_standard_surface_surfaceshader_100_metal_reflectivity --"reflectivity"--> NG_standard_surface_surfaceshader_100_artistic_ior
    NG_standard_surface_surfaceshader_100_metal_edgecolor --"edge_color"--> NG_standard_surface_surfaceshader_100_artistic_ior
    NG_standard_surface_surfaceshader_100_artistic_ior --"ior-->ior"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_artistic_ior --"extinction-->extinction"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_main_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_thickness --"thinfilm_thickness"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_IOR --"thinfilm_ior"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_metal_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_specular_layer --"bg"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_metalness --"mix"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_coat_color --"fg"--> NG_standard_surface_surfaceshader_100_coat_attenuation
    NG_standard_surface_surfaceshader_100_coat --"mix"--> NG_standard_surface_surfaceshader_100_coat_attenuation
    NG_standard_surface_surfaceshader_100_metalness_mix --"in1"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated
    NG_standard_surface_surfaceshader_100_coat_attenuation --"in2"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated
    NG_standard_surface_surfaceshader_100_coat_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_coat_roughness_vector
    NG_standard_surface_surfaceshader_100_coat_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_coat_roughness_vector
    NG_standard_surface_surfaceshader_100_coat --"weight"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_IOR --"ior"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_roughness_vector --"roughness"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_normal --"normal"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_bsdf --"top"--> NG_standard_surface_surfaceshader_100_coat_layer
    NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated --"base"--> NG_standard_surface_surfaceshader_100_coat_layer
    NG_standard_surface_surfaceshader_100_coat_IOR --"in2"--> NG_standard_surface_surfaceshader_100_one_minus_coat_ior
    NG_standard_surface_surfaceshader_100_coat_IOR --"in2"--> NG_standard_surface_surfaceshader_100_one_plus_coat_ior
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior --"in1"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt
    NG_standard_surface_surfaceshader_100_one_plus_coat_ior --"in2"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt --"in1"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt --"in2"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0 --"in2"--> NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_emission_color --"in1"--> NG_standard_surface_surfaceshader_100_emission_weight
    NG_standard_surface_surfaceshader_100_emission --"in2"--> NG_standard_surface_surfaceshader_100_emission_weight
    NG_standard_surface_surfaceshader_100_emission_weight --"color"--> NG_standard_surface_surfaceshader_100_emission_edf
    NG_standard_surface_surfaceshader_100_emission_edf --"in1"--> NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf
    NG_standard_surface_surfaceshader_100_coat_color --"in2"--> NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0 --"in"--> NG_standard_surface_surfaceshader_100_swizzle
    NG_standard_surface_surfaceshader_100_swizzle --"color0"--> NG_standard_surface_surfaceshader_100_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf --"base"--> NG_standard_surface_surfaceshader_100_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat_emission_edf --"fg"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_emission_edf --"bg"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat --"mix"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_opacity --"in"--> NG_standard_surface_surfaceshader_100_opacity_luminance
    NG_standard_surface_surfaceshader_100_opacity_luminance --"in"--> NG_standard_surface_surfaceshader_100_swizzle2
    NG_standard_surface_surfaceshader_100_coat_layer --"bsdf"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_blended_coat_emission_edf --"edf"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_swizzle2 --"opacity"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_shader_constructor --> NG_standard_surface_surfaceshader_100_out
    NG_standard_surface_surfaceshader_100_subsurface_radius_scaled --"in"--> NG_standard_surface_surfaceshader_100_convert
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **base** | float | 1.0 | Base | 0.0 | 1.0 |  |  |  | Base |  | Multiplier on the intensity of the diffuse reflection. |  |
| **base_color** | color3 | 0.8, 0.8, 0.8 | Base Color | 0,0,0 | 1,1,1 |  |  |  | Base |  | Color of the diffuse reflection. |  |
<details open><summary>ND_standard_surface_surfaceshader_100</summary>
<p>
 
* *Nodedef*: ND_standard_surface_surfaceshader_100
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 1.0.0. Is default: False
* *Doc*: Autodesk standard surface shader
* *Nodegraph*: NG_standard_surface_surfaceshader_100


```mermaid
graph TB
    subgraph NG_standard_surface_surfaceshader_100
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1[coat_affect_roughness_multiply1]
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[coat_affect_roughness_multiply2]
    NG_standard_surface_surfaceshader_100_coat_affected_roughness[coat_affected_roughness]
    NG_standard_surface_surfaceshader_100_main_roughness[main_roughness]
    NG_standard_surface_surfaceshader_100_transmission_roughness_add[transmission_roughness_add]
    NG_standard_surface_surfaceshader_100_transmission_roughness_clamped[transmission_roughness_clamped]
    NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness[coat_affected_transmission_roughness]
    NG_standard_surface_surfaceshader_100_transmission_roughness[transmission_roughness]
    NG_standard_surface_surfaceshader_100_tangent_rotate_degree[tangent_rotate_degree]
    NG_standard_surface_surfaceshader_100_tangent_rotate[tangent_rotate]
    NG_standard_surface_surfaceshader_100_tangent_rotate_normalize[tangent_rotate_normalize]
    NG_standard_surface_surfaceshader_100_main_tangent[main_tangent]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree[coat_tangent_rotate_degree]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate[coat_tangent_rotate]
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize[coat_tangent_rotate_normalize]
    NG_standard_surface_surfaceshader_100_coat_tangent[coat_tangent]
    NG_standard_surface_surfaceshader_100_coat_clamped[coat_clamped]
    NG_standard_surface_surfaceshader_100_coat_gamma_multiply[coat_gamma_multiply]
    NG_standard_surface_surfaceshader_100_coat_gamma[coat_gamma]
    NG_standard_surface_surfaceshader_100_base_color_nonnegative[base_color_nonnegative]
    NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color[coat_affected_diffuse_color]
    NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative[subsurface_color_nonnegative]
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[coat_affected_subsurface_color]
    NG_standard_surface_surfaceshader_100_diffuse_bsdf[diffuse_bsdf]
    NG_standard_surface_surfaceshader_100_translucent_bsdf[translucent_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_radius_vector[subsurface_radius_vector]
    NG_standard_surface_surfaceshader_100_subsurface_radius_scaled[subsurface_radius_scaled]
    NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_selector[subsurface_selector]
    NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[selected_subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_mix[subsurface_mix]
    NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    NG_standard_surface_surfaceshader_100_sheen_layer[sheen_layer]
    NG_standard_surface_surfaceshader_100_transmission_bsdf[transmission_bsdf]
    NG_standard_surface_surfaceshader_100_transmission_mix[transmission_mix]
    NG_standard_surface_surfaceshader_100_specular_bsdf[specular_bsdf]
    NG_standard_surface_surfaceshader_100_specular_layer[specular_layer]
    NG_standard_surface_surfaceshader_100_metal_reflectivity[metal_reflectivity]
    NG_standard_surface_surfaceshader_100_metal_edgecolor[metal_edgecolor]
    NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior]
    NG_standard_surface_surfaceshader_100_metal_bsdf[metal_bsdf]
    NG_standard_surface_surfaceshader_100_metalness_mix[metalness_mix]
    NG_standard_surface_surfaceshader_100_coat_attenuation[coat_attenuation]
    NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated[thin_film_layer_attenuated]
    NG_standard_surface_surfaceshader_100_coat_roughness_vector[coat_roughness_vector]
    NG_standard_surface_surfaceshader_100_coat_bsdf[coat_bsdf]
    NG_standard_surface_surfaceshader_100_coat_layer[coat_layer]
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior[one_minus_coat_ior]
    NG_standard_surface_surfaceshader_100_one_plus_coat_ior[one_plus_coat_ior]
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt[coat_ior_to_F0_sqrt]
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0[coat_ior_to_F0]
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0[one_minus_coat_ior_to_F0]
    NG_standard_surface_surfaceshader_100_emission_weight[emission_weight]
    NG_standard_surface_surfaceshader_100_emission_edf[emission_edf]
    NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf[coat_tinted_emission_edf]
    NG_standard_surface_surfaceshader_100_swizzle[swizzle]
    NG_standard_surface_surfaceshader_100_coat_emission_edf[coat_emission_edf]
    NG_standard_surface_surfaceshader_100_blended_coat_emission_edf[blended_coat_emission_edf]
    NG_standard_surface_surfaceshader_100_opacity_luminance[opacity_luminance]
    NG_standard_surface_surfaceshader_100_swizzle2[swizzle2]
    NG_standard_surface_surfaceshader_100_shader_constructor[shader_constructor]
    style NG_standard_surface_surfaceshader_100_out  fill:#0C0, color:#FFF
    NG_standard_surface_surfaceshader_100_out([out])
    NG_standard_surface_surfaceshader_100_convert[convert]
    style NG_standard_surface_surfaceshader_100_coat_affect_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_affect_roughness([coat_affect_roughness])
    style NG_standard_surface_surfaceshader_100_coat  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat([coat])
    style NG_standard_surface_surfaceshader_100_coat_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_roughness([coat_roughness])
    style NG_standard_surface_surfaceshader_100_specular_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_roughness([specular_roughness])
    style NG_standard_surface_surfaceshader_100_specular_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_anisotropy([specular_anisotropy])
    style NG_standard_surface_surfaceshader_100_transmission_extra_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission_extra_roughness([transmission_extra_roughness])
    style NG_standard_surface_surfaceshader_100_specular_rotation  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_rotation([specular_rotation])
    style NG_standard_surface_surfaceshader_100_tangent  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_tangent([tangent])
    style NG_standard_surface_surfaceshader_100_normal  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_normal([normal])
    style NG_standard_surface_surfaceshader_100_coat_rotation  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_rotation([coat_rotation])
    style NG_standard_surface_surfaceshader_100_coat_normal  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_normal([coat_normal])
    style NG_standard_surface_surfaceshader_100_coat_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_anisotropy([coat_anisotropy])
    style NG_standard_surface_surfaceshader_100_coat_affect_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_affect_color([coat_affect_color])
    style NG_standard_surface_surfaceshader_100_base_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_base_color([base_color])
    style NG_standard_surface_surfaceshader_100_subsurface_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_color([subsurface_color])
    style NG_standard_surface_surfaceshader_100_base  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_base([base])
    style NG_standard_surface_surfaceshader_100_diffuse_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_diffuse_roughness([diffuse_roughness])
    style NG_standard_surface_surfaceshader_100_subsurface_radius  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_radius([subsurface_radius])
    style NG_standard_surface_surfaceshader_100_subsurface_scale  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_scale([subsurface_scale])
    style NG_standard_surface_surfaceshader_100_subsurface_anisotropy  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface_anisotropy([subsurface_anisotropy])
    style NG_standard_surface_surfaceshader_100_thin_walled  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_walled([thin_walled])
    style NG_standard_surface_surfaceshader_100_subsurface  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_subsurface([subsurface])
    style NG_standard_surface_surfaceshader_100_sheen  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen([sheen])
    style NG_standard_surface_surfaceshader_100_sheen_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen_color([sheen_color])
    style NG_standard_surface_surfaceshader_100_sheen_roughness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_sheen_roughness([sheen_roughness])
    style NG_standard_surface_surfaceshader_100_transmission_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission_color([transmission_color])
    style NG_standard_surface_surfaceshader_100_specular_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_IOR([specular_IOR])
    style NG_standard_surface_surfaceshader_100_transmission  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_transmission([transmission])
    style NG_standard_surface_surfaceshader_100_specular  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular([specular])
    style NG_standard_surface_surfaceshader_100_specular_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_specular_color([specular_color])
    style NG_standard_surface_surfaceshader_100_thin_film_thickness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_film_thickness([thin_film_thickness])
    style NG_standard_surface_surfaceshader_100_thin_film_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_thin_film_IOR([thin_film_IOR])
    style NG_standard_surface_surfaceshader_100_metalness  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_metalness([metalness])
    style NG_standard_surface_surfaceshader_100_coat_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_color([coat_color])
    style NG_standard_surface_surfaceshader_100_coat_IOR  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_coat_IOR([coat_IOR])
    style NG_standard_surface_surfaceshader_100_emission_color  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_emission_color([emission_color])
    style NG_standard_surface_surfaceshader_100_emission  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_emission([emission])
    style NG_standard_surface_surfaceshader_100_opacity  fill:#09D, color:#FFF
    NG_standard_surface_surfaceshader_100_opacity([opacity])
    end
    NG_standard_surface_surfaceshader_100_coat_affect_roughness --"in1"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1
    NG_standard_surface_surfaceshader_100_coat --"in2"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1 --"in1"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2
    NG_standard_surface_surfaceshader_100_coat_roughness --"in2"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2
    NG_standard_surface_surfaceshader_100_specular_roughness --"bg"--> NG_standard_surface_surfaceshader_100_coat_affected_roughness
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2 --"mix"--> NG_standard_surface_surfaceshader_100_coat_affected_roughness
    NG_standard_surface_surfaceshader_100_coat_affected_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_main_roughness
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_main_roughness
    NG_standard_surface_surfaceshader_100_specular_roughness --"in1"--> NG_standard_surface_surfaceshader_100_transmission_roughness_add
    NG_standard_surface_surfaceshader_100_transmission_extra_roughness --"in2"--> NG_standard_surface_surfaceshader_100_transmission_roughness_add
    NG_standard_surface_surfaceshader_100_transmission_roughness_add --"in"--> NG_standard_surface_surfaceshader_100_transmission_roughness_clamped
    NG_standard_surface_surfaceshader_100_transmission_roughness_clamped --"bg"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2 --"mix"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness
    NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_transmission_roughness
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_transmission_roughness
    NG_standard_surface_surfaceshader_100_specular_rotation --"in1"--> NG_standard_surface_surfaceshader_100_tangent_rotate_degree
    NG_standard_surface_surfaceshader_100_tangent --"in"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_tangent_rotate_degree --"amount"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_normal --"axis"--> NG_standard_surface_surfaceshader_100_tangent_rotate
    NG_standard_surface_surfaceshader_100_tangent_rotate --"in"--> NG_standard_surface_surfaceshader_100_tangent_rotate_normalize
    NG_standard_surface_surfaceshader_100_specular_anisotropy --"value1"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_tangent_rotate_normalize --"in1"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_tangent --"in2"--> NG_standard_surface_surfaceshader_100_main_tangent
    NG_standard_surface_surfaceshader_100_coat_rotation --"in1"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree
    NG_standard_surface_surfaceshader_100_tangent --"in"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree --"amount"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_normal --"axis"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate --"in"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize
    NG_standard_surface_surfaceshader_100_coat_anisotropy --"value1"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize --"in1"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_tangent --"in2"--> NG_standard_surface_surfaceshader_100_coat_tangent
    NG_standard_surface_surfaceshader_100_coat --"in"--> NG_standard_surface_surfaceshader_100_coat_clamped
    NG_standard_surface_surfaceshader_100_coat_clamped --"in1"--> NG_standard_surface_surfaceshader_100_coat_gamma_multiply
    NG_standard_surface_surfaceshader_100_coat_affect_color --"in2"--> NG_standard_surface_surfaceshader_100_coat_gamma_multiply
    NG_standard_surface_surfaceshader_100_coat_gamma_multiply --"in1"--> NG_standard_surface_surfaceshader_100_coat_gamma
    NG_standard_surface_surfaceshader_100_base_color --"in1"--> NG_standard_surface_surfaceshader_100_base_color_nonnegative
    NG_standard_surface_surfaceshader_100_base_color_nonnegative --"in1"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color
    NG_standard_surface_surfaceshader_100_coat_gamma --"in2"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color
    NG_standard_surface_surfaceshader_100_subsurface_color --"in1"--> NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative
    NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative --"in1"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color
    NG_standard_surface_surfaceshader_100_coat_gamma --"in2"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color
    NG_standard_surface_surfaceshader_100_base --"weight"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color --"color"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_diffuse_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color --"color"--> NG_standard_surface_surfaceshader_100_translucent_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_translucent_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_radius --"in"--> NG_standard_surface_surfaceshader_100_subsurface_radius_vector
    NG_standard_surface_surfaceshader_100_subsurface_radius_vector --"in1"--> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled
    NG_standard_surface_surfaceshader_100_subsurface_scale --"in2"--> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color --"color"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_convert --"radius"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_thin_walled --"in"--> NG_standard_surface_surfaceshader_100_subsurface_selector
    NG_standard_surface_surfaceshader_100_translucent_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_bsdf --"bg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_subsurface_selector --"mix"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf
    NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_diffuse_bsdf --"bg"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_subsurface --"mix"--> NG_standard_surface_surfaceshader_100_subsurface_mix
    NG_standard_surface_surfaceshader_100_sheen --"weight"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_color --"color"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_sheen_bsdf
    NG_standard_surface_surfaceshader_100_sheen_bsdf --"top"--> NG_standard_surface_surfaceshader_100_sheen_layer
    NG_standard_surface_surfaceshader_100_subsurface_mix --"base"--> NG_standard_surface_surfaceshader_100_sheen_layer
    NG_standard_surface_surfaceshader_100_transmission_color --"tint"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_specular_IOR --"ior"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_transmission_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_transmission_bsdf
    NG_standard_surface_surfaceshader_100_transmission_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_sheen_layer --"bg"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_transmission --"mix"--> NG_standard_surface_surfaceshader_100_transmission_mix
    NG_standard_surface_surfaceshader_100_specular --"weight"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_color --"tint"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_IOR --"ior"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_main_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_thickness --"thinfilm_thickness"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_IOR --"thinfilm_ior"--> NG_standard_surface_surfaceshader_100_specular_bsdf
    NG_standard_surface_surfaceshader_100_specular_bsdf --"top"--> NG_standard_surface_surfaceshader_100_specular_layer
    NG_standard_surface_surfaceshader_100_transmission_mix --"base"--> NG_standard_surface_surfaceshader_100_specular_layer
    NG_standard_surface_surfaceshader_100_base_color --"in1"--> NG_standard_surface_surfaceshader_100_metal_reflectivity
    NG_standard_surface_surfaceshader_100_base --"in2"--> NG_standard_surface_surfaceshader_100_metal_reflectivity
    NG_standard_surface_surfaceshader_100_specular_color --"in1"--> NG_standard_surface_surfaceshader_100_metal_edgecolor
    NG_standard_surface_surfaceshader_100_specular --"in2"--> NG_standard_surface_surfaceshader_100_metal_edgecolor
    NG_standard_surface_surfaceshader_100_metal_reflectivity --"reflectivity"--> NG_standard_surface_surfaceshader_100_artistic_ior
    NG_standard_surface_surfaceshader_100_metal_edgecolor --"edge_color"--> NG_standard_surface_surfaceshader_100_artistic_ior
    NG_standard_surface_surfaceshader_100_artistic_ior --"ior-->ior"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_artistic_ior --"extinction-->extinction"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_main_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_normal --"normal"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_main_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_thickness --"thinfilm_thickness"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_thin_film_IOR --"thinfilm_ior"--> NG_standard_surface_surfaceshader_100_metal_bsdf
    NG_standard_surface_surfaceshader_100_metal_bsdf --"fg"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_specular_layer --"bg"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_metalness --"mix"--> NG_standard_surface_surfaceshader_100_metalness_mix
    NG_standard_surface_surfaceshader_100_coat_color --"fg"--> NG_standard_surface_surfaceshader_100_coat_attenuation
    NG_standard_surface_surfaceshader_100_coat --"mix"--> NG_standard_surface_surfaceshader_100_coat_attenuation
    NG_standard_surface_surfaceshader_100_metalness_mix --"in1"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated
    NG_standard_surface_surfaceshader_100_coat_attenuation --"in2"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated
    NG_standard_surface_surfaceshader_100_coat_roughness --"roughness"--> NG_standard_surface_surfaceshader_100_coat_roughness_vector
    NG_standard_surface_surfaceshader_100_coat_anisotropy --"anisotropy"--> NG_standard_surface_surfaceshader_100_coat_roughness_vector
    NG_standard_surface_surfaceshader_100_coat --"weight"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_IOR --"ior"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_roughness_vector --"roughness"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_normal --"normal"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_tangent --"tangent"--> NG_standard_surface_surfaceshader_100_coat_bsdf
    NG_standard_surface_surfaceshader_100_coat_bsdf --"top"--> NG_standard_surface_surfaceshader_100_coat_layer
    NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated --"base"--> NG_standard_surface_surfaceshader_100_coat_layer
    NG_standard_surface_surfaceshader_100_coat_IOR --"in2"--> NG_standard_surface_surfaceshader_100_one_minus_coat_ior
    NG_standard_surface_surfaceshader_100_coat_IOR --"in2"--> NG_standard_surface_surfaceshader_100_one_plus_coat_ior
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior --"in1"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt
    NG_standard_surface_surfaceshader_100_one_plus_coat_ior --"in2"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt --"in1"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0_sqrt --"in2"--> NG_standard_surface_surfaceshader_100_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_coat_ior_to_F0 --"in2"--> NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0
    NG_standard_surface_surfaceshader_100_emission_color --"in1"--> NG_standard_surface_surfaceshader_100_emission_weight
    NG_standard_surface_surfaceshader_100_emission --"in2"--> NG_standard_surface_surfaceshader_100_emission_weight
    NG_standard_surface_surfaceshader_100_emission_weight --"color"--> NG_standard_surface_surfaceshader_100_emission_edf
    NG_standard_surface_surfaceshader_100_emission_edf --"in1"--> NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf
    NG_standard_surface_surfaceshader_100_coat_color --"in2"--> NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf
    NG_standard_surface_surfaceshader_100_one_minus_coat_ior_to_F0 --"in"--> NG_standard_surface_surfaceshader_100_swizzle
    NG_standard_surface_surfaceshader_100_swizzle --"color0"--> NG_standard_surface_surfaceshader_100_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat_tinted_emission_edf --"base"--> NG_standard_surface_surfaceshader_100_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat_emission_edf --"fg"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_emission_edf --"bg"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_coat --"mix"--> NG_standard_surface_surfaceshader_100_blended_coat_emission_edf
    NG_standard_surface_surfaceshader_100_opacity --"in"--> NG_standard_surface_surfaceshader_100_opacity_luminance
    NG_standard_surface_surfaceshader_100_opacity_luminance --"in"--> NG_standard_surface_surfaceshader_100_swizzle2
    NG_standard_surface_surfaceshader_100_coat_layer --"bsdf"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_blended_coat_emission_edf --"edf"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_swizzle2 --"opacity"--> NG_standard_surface_surfaceshader_100_shader_constructor
    NG_standard_surface_surfaceshader_100_shader_constructor --> NG_standard_surface_surfaceshader_100_out
    NG_standard_surface_surfaceshader_100_subsurface_radius_scaled --"in"--> NG_standard_surface_surfaceshader_100_convert
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **base** | float | 0.8 | Base | 0.0 | 1.0 |  |  |  | Base |  | Multiplier on the intensity of the diffuse reflection. |  |
| **base_color** | color3 | 1, 1, 1 | Base Color | 0,0,0 | 1,1,1 |  |  |  | Base |  | Color of the diffuse reflection. |  |
| **diffuse_roughness** | float | 0.0 | Diffuse Roughness | 0.0 | 1.0 |  |  |  | Base | true | Roughness of the diffuse reflection. Higher values cause the surface to appear flatter and darker. |  |
| **metalness** | float | 0.0 | Metalness | 0.0 | 1.0 |  |  |  | Base |  | Specifies how metallic the material appears. At its maximum, the surface behaves like a metal, using fully specular reflection and complex fresnel. |  |
| **specular** | float | 1.0 | Specular | 0.0 | 1.0 |  |  |  | Specular |  | Multiplier on the intensity of the specular reflection. |  |
| **specular_color** | color3 | 1, 1, 1 | Specular Color | 0,0,0 | 1,1,1 |  |  |  | Specular |  | Color tint on the specular reflection. |  |
| **specular_roughness** | float | 0.2 | Specular Roughness | 0.0 | 1.0 |  |  |  | Specular |  | The roughness of the specular reflection. Lower numbers produce sharper reflections, higher numbers produce blurrier reflections. |  |
| **specular_IOR** | float | 1.5 | Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Specular |  | Index of refraction for specular reflection. |  |
| **specular_anisotropy** | float | 0.0 | Specular Anisotropy | 0.0 | 1.0 |  |  |  | Specular | true | The directional bias of reflected and transmitted light resulting in materials appearing rougher or glossier in certain directions. |  |
| **specular_rotation** | float | 0.0 | Specular Rotation | 0.0 | 1.0 |  |  |  | Specular | true | Rotation of the axis of specular anisotropy around the surface normal. |  |
| **transmission** | float | 0.0 | Transmission | 0.0 | 1.0 |  |  |  | Transmission | true | Transmission of light through the surface for materials such as glass or water. The greater the value the more transparent the material. |  |
| **transmission_color** | color3 | 1, 1, 1 | Transmission Color | 0,0,0 | 1,1,1 |  |  |  | Transmission | true | Color tint on the transmitted light. |  |
| **transmission_depth** | float | 0.0 | Transmission Depth | 0.0 |  |  | 100.0 |  | Transmission | true | Specifies the distance light travels inside the material before its becomes exactly the transmission color according to Beer's law. |  |
| **transmission_scatter** | color3 | 0, 0, 0 | Transmission Scatter | 0,0,0 | 1,1,1 |  |  |  | Transmission | true | Scattering coefficient of the interior medium. Suitable for a large body of liquid or one that is fairly thick, such as an ocean, honey, ice, or frosted glass. |  |
| **transmission_scatter_anisotropy** | float | 0.0 | Transmission Anisotropy | 0.0 | 1.0 |  |  |  | Transmission | true | The amount of directional bias, or anisotropy, of the scattering. |  |
| **transmission_dispersion** | float | 0.0 | Transmission Dispersion | 0.0 |  |  | 100.0 |  | Transmission | true | Dispersion amount, describing how much the index of refraction varies across wavelengths. |  |
| **transmission_extra_roughness** | float | 0.0 | Transmission Roughness | -1.0 | 1.0 | 0.0 |  |  | Transmission | true | Additional roughness on top of specular roughness. Positive values blur refractions more than reflections, and negative values blur refractions less. |  |
| **subsurface** | float | 0.0 | Subsurface | 0.0 | 1.0 |  |  |  | Subsurface | true | The blend between diffuse reflection and subsurface scattering. A value of 1.0 indicates full subsurface scattering and a value 0 for diffuse reflection only. |  |
| **subsurface_color** | color3 | 1, 1, 1 | Subsurface Color | 0,0,0 | 1,1,1 |  |  |  | Subsurface | true | The color of the subsurface scattering effect. |  |
| **subsurface_radius** | color3 | 1, 1, 1 | Subsurface Radius | 0,0,0 | 1,1,1 |  |  |  | Subsurface | true | The mean free path. The distance which light can travel before being scattered inside the surface. |  |
| **subsurface_scale** | float | 1.0 | Subsurface Scale | 0.0 |  |  | 10.0 |  | Subsurface | true | Scalar weight for the subsurface radius value. |  |
| **subsurface_anisotropy** | float | 0.0 | Subsurface Anisotropy | -1.0 | 1.0 |  |  |  | Subsurface | true | The direction of subsurface scattering. 0 scatters light evenly, positive values scatter forward and negative values scatter backward. |  |
| **sheen** | float | 0.0 | Sheen | 0.0 | 1.0 |  |  |  | Sheen | true | The weight of a sheen layer that can be used to approximate microfibers or fabrics such as velvet and satin. |  |
| **sheen_color** | color3 | 1, 1, 1 | Sheen Color | 0,0,0 | 1,1,1 |  |  |  | Sheen | true | The color of the sheen layer. |  |
| **sheen_roughness** | float | 0.3 | Sheen Roughness | 0.0 | 1.0 |  |  |  | Sheen | true | The roughness of the sheen layer. |  |
| **coat** | float | 0.0 | Coat | 0.0 | 1.0 |  |  |  | Coat |  | The weight of a reflective clear-coat layer on top of the material. Use for materials such as car paint or an oily layer. |  |
| **coat_color** | color3 | 1, 1, 1 | Coat Color | 0,0,0 | 1,1,1 |  |  |  | Coat |  | The color of the clear-coat layer's transparency. |  |
| **coat_roughness** | float | 0.1 | Coat Roughness | 0.0 | 1.0 |  |  |  | Coat |  | The roughness of the clear-coat reflections. The lower the value, the sharper the reflection. |  |
| **coat_anisotropy** | float | 0.0 | Coat Anisotropy | 0.0 | 1.0 |  |  |  | Coat | true | The amount of directional bias, or anisotropy, of the clear-coat layer. |  |
| **coat_rotation** | float | 0.0 | Coat Rotation | 0.0 | 1.0 |  |  |  | Coat | true | The rotation of the anisotropic effect of the clear-coat layer. |  |
| **coat_IOR** | float | 1.5 | Coat Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Coat |  | The index of refraction of the clear-coat layer. |  |
| **coat_normal** | vector3 | None | Coat normal |  |  |  |  |  | Coat |  | Input normal for clear-coat layer |  |
| **coat_affect_color** | float | 0.0 | Coat Affect Color | 0 | 1 |  |  |  | Coat | true | Controls the saturation of diffuse reflection and subsurface scattering below the clear-coat. |  |
| **coat_affect_roughness** | float | 0.0 | Coat Affect Roughness | 0 | 1 |  |  |  | Coat | true | Controls the roughness of the specular reflection in the layers below the clear-coat. |  |
| **thin_film_thickness** | float | 0.0 | Thin Film Thickness | 0.0 |  |  | 2000.0 |  | Thin Film | true | The thickness of the thin film layer on a surface. Use for materials such as multitone car paint or soap bubbles. |  |
| **thin_film_IOR** | float | 1.5 | Thin Film Index of Refraction | 0.0 |  | 1.0 | 3.0 |  | Thin Film | true | The index of refraction of the medium surrounding the material. |  |
| **emission** | float | 0.0 | Emission | 0.0 |  |  | 1.0 |  | Emission |  | The amount of emitted incandescent light. |  |
| **emission_color** | color3 | 1, 1, 1 | Emission Color | 0,0,0 | 1,1,1 |  |  |  | Emission |  | The color of the emitted light. |  |
| **opacity** | color3 | 1, 1, 1 | Opacity | 0,0,0 | 1,1,1 |  |  |  | Geometry |  | The opacity of the entire material. |  |
| **thin_walled** | boolean | False | Thin Walled |  |  |  |  |  | Geometry | true | If true the surface is double-sided and represents an infinitely thin shell. Suitable for thin objects such as tree leaves or paper. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Geometry |  | Input geometric normal |  |
| **tangent** | vector3 | None | Tangent Input |  |  |  |  |  | Geometry |  | Input geometric tangent |  |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *UsdPreviewSurface*
<details open><summary>ND_UsdPreviewSurface_surfaceshader</summary>
<p>
 
* *Nodedef*: ND_UsdPreviewSurface_surfaceshader
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 2.3. Is default: True
* *Doc*: USD preview surface shader
* *Nodegraph*: IMP_UsdPreviewSurface_surfaceshader


```mermaid
graph TB
    subgraph IMP_UsdPreviewSurface_surfaceshader
    IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float[use_specular_workflow_float]
    IMP_UsdPreviewSurface_surfaceshader_scale_normal[scale_normal]
    IMP_UsdPreviewSurface_surfaceshader_bias_normal[bias_normal]
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[surface_normal]
    IMP_UsdPreviewSurface_surfaceshader_inverse_metalness[inverse_metalness]
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight[diffuse_bsdf_weight]
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf[diffuse_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf[transmission_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_transmission_mix[transmission_mix]
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness[specular_roughness]
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1[specular_bsdf1]
    IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf[specular_workflow_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_one_minus_ior[one_minus_ior]
    IMP_UsdPreviewSurface_surfaceshader_one_plus_ior[one_plus_ior]
    IMP_UsdPreviewSurface_surfaceshader_R[R]
    IMP_UsdPreviewSurface_surfaceshader_R_sq[R_sq]
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[specular_color_metallic]
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq[specular_color_metallic_R_sq]
    IMP_UsdPreviewSurface_surfaceshader_F0[F0]
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[specular_bsdf2]
    IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf[metalness_specular_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_artistic_ior[artistic_ior]
    IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[metalness_metal_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf[metalness_workflow_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf[workflow_selector_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_coat_roughness[coat_roughness]
    IMP_UsdPreviewSurface_surfaceshader_coat_F0[coat_F0]
    IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[coat_dielectric_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_coat_bsdf[coat_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_emission_edf[emission_edf]
    style IMP_UsdPreviewSurface_surfaceshader_cutout_opacity  fill:#C72, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_cutout_opacity{cutout_opacity}
    IMP_UsdPreviewSurface_surfaceshader_surface_constructor[surface_constructor]
    style IMP_UsdPreviewSurface_surfaceshader_out  fill:#0C0, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_out([out])
    style IMP_UsdPreviewSurface_surfaceshader_useSpecularWorkflow  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_useSpecularWorkflow([useSpecularWorkflow])
    style IMP_UsdPreviewSurface_surfaceshader_normal  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_normal([normal])
    style IMP_UsdPreviewSurface_surfaceshader_metallic  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_metallic([metallic])
    style IMP_UsdPreviewSurface_surfaceshader_diffuseColor  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_diffuseColor([diffuseColor])
    style IMP_UsdPreviewSurface_surfaceshader_ior  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_ior([ior])
    style IMP_UsdPreviewSurface_surfaceshader_opacity  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_opacity([opacity])
    style IMP_UsdPreviewSurface_surfaceshader_roughness  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_roughness([roughness])
    style IMP_UsdPreviewSurface_surfaceshader_specularColor  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_specularColor([specularColor])
    style IMP_UsdPreviewSurface_surfaceshader_clearcoatRoughness  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_clearcoatRoughness([clearcoatRoughness])
    style IMP_UsdPreviewSurface_surfaceshader_clearcoat  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_clearcoat([clearcoat])
    style IMP_UsdPreviewSurface_surfaceshader_emissiveColor  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_emissiveColor([emissiveColor])
    style IMP_UsdPreviewSurface_surfaceshader_opacityThreshold  fill:#09D, color:#FFF
    IMP_UsdPreviewSurface_surfaceshader_opacityThreshold([opacityThreshold])
    end
    IMP_UsdPreviewSurface_surfaceshader_useSpecularWorkflow --"in"--> IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float
    IMP_UsdPreviewSurface_surfaceshader_normal --"in1"--> IMP_UsdPreviewSurface_surfaceshader_scale_normal
    IMP_UsdPreviewSurface_surfaceshader_scale_normal --"in1"--> IMP_UsdPreviewSurface_surfaceshader_bias_normal
    IMP_UsdPreviewSurface_surfaceshader_bias_normal --"in"--> IMP_UsdPreviewSurface_surfaceshader_surface_normal
    IMP_UsdPreviewSurface_surfaceshader_metallic --"in2"--> IMP_UsdPreviewSurface_surfaceshader_inverse_metalness
    IMP_UsdPreviewSurface_surfaceshader_inverse_metalness --"bg"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight
    IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float --"mix"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight --"weight"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf
    IMP_UsdPreviewSurface_surfaceshader_diffuseColor --"color"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf
    IMP_UsdPreviewSurface_surfaceshader_ior --"ior"--> IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf --"fg"--> IMP_UsdPreviewSurface_surfaceshader_transmission_mix
    IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf --"bg"--> IMP_UsdPreviewSurface_surfaceshader_transmission_mix
    IMP_UsdPreviewSurface_surfaceshader_opacity --"mix"--> IMP_UsdPreviewSurface_surfaceshader_transmission_mix
    IMP_UsdPreviewSurface_surfaceshader_roughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_specular_roughness
    IMP_UsdPreviewSurface_surfaceshader_specularColor --"color0"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1 --"top"--> IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf
    IMP_UsdPreviewSurface_surfaceshader_transmission_mix --"base"--> IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf
    IMP_UsdPreviewSurface_surfaceshader_ior --"in2"--> IMP_UsdPreviewSurface_surfaceshader_one_minus_ior
    IMP_UsdPreviewSurface_surfaceshader_ior --"in2"--> IMP_UsdPreviewSurface_surfaceshader_one_plus_ior
    IMP_UsdPreviewSurface_surfaceshader_one_minus_ior --"in1"--> IMP_UsdPreviewSurface_surfaceshader_R
    IMP_UsdPreviewSurface_surfaceshader_one_plus_ior --"in2"--> IMP_UsdPreviewSurface_surfaceshader_R
    IMP_UsdPreviewSurface_surfaceshader_R --"in1"--> IMP_UsdPreviewSurface_surfaceshader_R_sq
    IMP_UsdPreviewSurface_surfaceshader_R --"in2"--> IMP_UsdPreviewSurface_surfaceshader_R_sq
    IMP_UsdPreviewSurface_surfaceshader_diffuseColor --"fg"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic
    IMP_UsdPreviewSurface_surfaceshader_metallic --"mix"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic --"in1"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq
    IMP_UsdPreviewSurface_surfaceshader_R_sq --"in2"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic --"fg"--> IMP_UsdPreviewSurface_surfaceshader_F0
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq --"bg"--> IMP_UsdPreviewSurface_surfaceshader_F0
    IMP_UsdPreviewSurface_surfaceshader_metallic --"mix"--> IMP_UsdPreviewSurface_surfaceshader_F0
    IMP_UsdPreviewSurface_surfaceshader_F0 --"color0"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic --"color90"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2 --"top"--> IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf
    IMP_UsdPreviewSurface_surfaceshader_transmission_mix --"base"--> IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf
    IMP_UsdPreviewSurface_surfaceshader_diffuseColor --"reflectivity"--> IMP_UsdPreviewSurface_surfaceshader_artistic_ior
    IMP_UsdPreviewSurface_surfaceshader_diffuseColor --"edge_color"--> IMP_UsdPreviewSurface_surfaceshader_artistic_ior
    IMP_UsdPreviewSurface_surfaceshader_artistic_ior --"ior-->ior"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf
    IMP_UsdPreviewSurface_surfaceshader_artistic_ior --"extinction-->extinction"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf
    IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf --"fg"--> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf
    IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf --"bg"--> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf
    IMP_UsdPreviewSurface_surfaceshader_metallic --"mix"--> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf
    IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf --"fg"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf
    IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf --"bg"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf
    IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float --"mix"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf
    IMP_UsdPreviewSurface_surfaceshader_clearcoatRoughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_coat_roughness
    IMP_UsdPreviewSurface_surfaceshader_R_sq --"in"--> IMP_UsdPreviewSurface_surfaceshader_coat_F0
    IMP_UsdPreviewSurface_surfaceshader_clearcoat --"weight"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf
    IMP_UsdPreviewSurface_surfaceshader_coat_F0 --"color0"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf
    IMP_UsdPreviewSurface_surfaceshader_coat_roughness --"roughness"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf
    IMP_UsdPreviewSurface_surfaceshader_surface_normal --"normal"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf
    IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf --"top"--> IMP_UsdPreviewSurface_surfaceshader_coat_bsdf
    IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf --"base"--> IMP_UsdPreviewSurface_surfaceshader_coat_bsdf
    IMP_UsdPreviewSurface_surfaceshader_emissiveColor --"color"--> IMP_UsdPreviewSurface_surfaceshader_emission_edf
    IMP_UsdPreviewSurface_surfaceshader_opacity --"value1"--> IMP_UsdPreviewSurface_surfaceshader_cutout_opacity
    IMP_UsdPreviewSurface_surfaceshader_opacityThreshold --"value2"--> IMP_UsdPreviewSurface_surfaceshader_cutout_opacity
    IMP_UsdPreviewSurface_surfaceshader_coat_bsdf --"bsdf"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor
    IMP_UsdPreviewSurface_surfaceshader_emission_edf --"edf"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor
    IMP_UsdPreviewSurface_surfaceshader_cutout_opacity --"opacity"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor
    IMP_UsdPreviewSurface_surfaceshader_surface_constructor --> IMP_UsdPreviewSurface_surfaceshader_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **diffuseColor** | color3 | 0.18, 0.18, 0.18 |  | 0,0,0 | 1,1,1 |  |  |  |  |  |  |  |
| **emissiveColor** | color3 | 0, 0, 0 |  | 0,0,0 |  |  | 1,1,1 |  |  |  |  |  |
| **useSpecularWorkflow** | integer | 0 |  | 0 | 1 |  |  | 1 |  |  |  |  |
| **specularColor** | color3 | 0, 0, 0 |  | 0,0,0 | 1,1,1 |  |  |  |  |  |  |  |
| **metallic** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **roughness** | float | 0.5 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **clearcoat** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **clearcoatRoughness** | float | 0.01 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **opacity** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **opacityThreshold** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **ior** | float | 1.5 |  | 0.0 |  | 1.0 | 3.0 |  |  |  |  |  |
| **normal** | vector3 | 0, 0, 1 |  | -1.0,-1.0,-1.0 | 1.0,1.0,1.0 |  |  | 0.01 |  |  |  |  |
| **displacement** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **occlusion** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *UsdUVTexture*
<details open><summary>ND_UsdUVTexture</summary>
<p>
 
* *Nodedef*: ND_UsdUVTexture
* *Type*: multioutput
* *Group*: texture2d
* *Version*: 2.2. Is default: False
- *Inherits From*: ND_UsdUVTexture_23
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdUVTexture_22


```mermaid
graph TB
    subgraph IMP_UsdUVTexture_22
    IMP_UsdUVTexture_22_image_reader[image_reader]
    IMP_UsdUVTexture_22_image_scale[image_scale]
    IMP_UsdUVTexture_22_image_bias[image_bias]
    IMP_UsdUVTexture_22_swizzle[swizzle]
    style IMP_UsdUVTexture_22_r  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_r([r])
    IMP_UsdUVTexture_22_swizzle2[swizzle2]
    style IMP_UsdUVTexture_22_g  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_g([g])
    IMP_UsdUVTexture_22_swizzle3[swizzle3]
    style IMP_UsdUVTexture_22_b  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_b([b])
    IMP_UsdUVTexture_22_swizzle4[swizzle4]
    style IMP_UsdUVTexture_22_a  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_a([a])
    IMP_UsdUVTexture_22_swizzle5[swizzle5]
    style IMP_UsdUVTexture_22_rgb  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_rgb([rgb])
    style IMP_UsdUVTexture_22_rgba  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_22_rgba([rgba])
    style IMP_UsdUVTexture_22_file  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_file([file])
    style IMP_UsdUVTexture_22_fallback  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_fallback([fallback])
    style IMP_UsdUVTexture_22_st  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_st([st])
    style IMP_UsdUVTexture_22_wrapS  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_wrapS([wrapS])
    style IMP_UsdUVTexture_22_wrapT  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_wrapT([wrapT])
    style IMP_UsdUVTexture_22_scale  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_scale([scale])
    style IMP_UsdUVTexture_22_bias  fill:#09D, color:#FFF
    IMP_UsdUVTexture_22_bias([bias])
    end
    IMP_UsdUVTexture_22_file --"file"--> IMP_UsdUVTexture_22_image_reader
    IMP_UsdUVTexture_22_fallback --"default"--> IMP_UsdUVTexture_22_image_reader
    IMP_UsdUVTexture_22_st --"texcoord"--> IMP_UsdUVTexture_22_image_reader
    IMP_UsdUVTexture_22_wrapS --"uaddressmode"--> IMP_UsdUVTexture_22_image_reader
    IMP_UsdUVTexture_22_wrapT --"vaddressmode"--> IMP_UsdUVTexture_22_image_reader
    IMP_UsdUVTexture_22_image_reader --"in1"--> IMP_UsdUVTexture_22_image_scale
    IMP_UsdUVTexture_22_scale --"in2"--> IMP_UsdUVTexture_22_image_scale
    IMP_UsdUVTexture_22_image_scale --"in1"--> IMP_UsdUVTexture_22_image_bias
    IMP_UsdUVTexture_22_bias --"in2"--> IMP_UsdUVTexture_22_image_bias
    IMP_UsdUVTexture_22_image_bias --"in"--> IMP_UsdUVTexture_22_swizzle
    IMP_UsdUVTexture_22_swizzle --> IMP_UsdUVTexture_22_r
    IMP_UsdUVTexture_22_image_bias --"in"--> IMP_UsdUVTexture_22_swizzle2
    IMP_UsdUVTexture_22_swizzle2 --> IMP_UsdUVTexture_22_g
    IMP_UsdUVTexture_22_image_bias --"in"--> IMP_UsdUVTexture_22_swizzle3
    IMP_UsdUVTexture_22_swizzle3 --> IMP_UsdUVTexture_22_b
    IMP_UsdUVTexture_22_image_bias --"in"--> IMP_UsdUVTexture_22_swizzle4
    IMP_UsdUVTexture_22_swizzle4 --> IMP_UsdUVTexture_22_a
    IMP_UsdUVTexture_22_image_bias --"in"--> IMP_UsdUVTexture_22_swizzle5
    IMP_UsdUVTexture_22_swizzle5 --> IMP_UsdUVTexture_22_rgb
    IMP_UsdUVTexture_22_image_bias --> IMP_UsdUVTexture_22_rgba
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| *r* | float | None |  |  |  |  |  |  |  |  |  |  |
| *g* | float | None |  |  |  |  |  |  |  |  |  |  |
| *b* | float | None |  |  |  |  |  |  |  |  |  |  |
| *a* | float | None |  |  |  |  |  |  |  |  |  |  |
| *rgb* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *rgba* | color4 | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdUVTexture_23</summary>
<p>
 
* *Nodedef*: ND_UsdUVTexture_23
* *Type*: multioutput
* *Group*: texture2d
* *Version*: 2.3. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdUVTexture_23


```mermaid
graph TB
    subgraph IMP_UsdUVTexture_23
    IMP_UsdUVTexture_23_image_reader[image_reader]
    IMP_UsdUVTexture_23_image_scale[image_scale]
    IMP_UsdUVTexture_23_image_bias[image_bias]
    IMP_UsdUVTexture_23_swizzle[swizzle]
    style IMP_UsdUVTexture_23_r  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_23_r([r])
    IMP_UsdUVTexture_23_swizzle2[swizzle2]
    style IMP_UsdUVTexture_23_g  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_23_g([g])
    IMP_UsdUVTexture_23_swizzle3[swizzle3]
    style IMP_UsdUVTexture_23_b  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_23_b([b])
    IMP_UsdUVTexture_23_swizzle4[swizzle4]
    style IMP_UsdUVTexture_23_a  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_23_a([a])
    IMP_UsdUVTexture_23_swizzle5[swizzle5]
    style IMP_UsdUVTexture_23_rgb  fill:#0C0, color:#FFF
    IMP_UsdUVTexture_23_rgb([rgb])
    style IMP_UsdUVTexture_23_file  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_file([file])
    style IMP_UsdUVTexture_23_fallback  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_fallback([fallback])
    style IMP_UsdUVTexture_23_st  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_st([st])
    style IMP_UsdUVTexture_23_wrapS  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_wrapS([wrapS])
    style IMP_UsdUVTexture_23_wrapT  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_wrapT([wrapT])
    style IMP_UsdUVTexture_23_scale  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_scale([scale])
    style IMP_UsdUVTexture_23_bias  fill:#09D, color:#FFF
    IMP_UsdUVTexture_23_bias([bias])
    end
    IMP_UsdUVTexture_23_file --"file"--> IMP_UsdUVTexture_23_image_reader
    IMP_UsdUVTexture_23_fallback --"default"--> IMP_UsdUVTexture_23_image_reader
    IMP_UsdUVTexture_23_st --"texcoord"--> IMP_UsdUVTexture_23_image_reader
    IMP_UsdUVTexture_23_wrapS --"uaddressmode"--> IMP_UsdUVTexture_23_image_reader
    IMP_UsdUVTexture_23_wrapT --"vaddressmode"--> IMP_UsdUVTexture_23_image_reader
    IMP_UsdUVTexture_23_image_reader --"in1"--> IMP_UsdUVTexture_23_image_scale
    IMP_UsdUVTexture_23_scale --"in2"--> IMP_UsdUVTexture_23_image_scale
    IMP_UsdUVTexture_23_image_scale --"in1"--> IMP_UsdUVTexture_23_image_bias
    IMP_UsdUVTexture_23_bias --"in2"--> IMP_UsdUVTexture_23_image_bias
    IMP_UsdUVTexture_23_image_bias --"in"--> IMP_UsdUVTexture_23_swizzle
    IMP_UsdUVTexture_23_swizzle --> IMP_UsdUVTexture_23_r
    IMP_UsdUVTexture_23_image_bias --"in"--> IMP_UsdUVTexture_23_swizzle2
    IMP_UsdUVTexture_23_swizzle2 --> IMP_UsdUVTexture_23_g
    IMP_UsdUVTexture_23_image_bias --"in"--> IMP_UsdUVTexture_23_swizzle3
    IMP_UsdUVTexture_23_swizzle3 --> IMP_UsdUVTexture_23_b
    IMP_UsdUVTexture_23_image_bias --"in"--> IMP_UsdUVTexture_23_swizzle4
    IMP_UsdUVTexture_23_swizzle4 --> IMP_UsdUVTexture_23_a
    IMP_UsdUVTexture_23_image_bias --"in"--> IMP_UsdUVTexture_23_swizzle5
    IMP_UsdUVTexture_23_swizzle5 --> IMP_UsdUVTexture_23_rgb
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| **st** | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| **wrapS** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **wrapT** | string | periodic |  |  |  |  |  |  |  |  |  | true |
| **fallback** | color4 | 0, 0, 0, 1 |  |  |  |  |  |  |  |  |  |  |
| **scale** | color4 | 1, 1, 1, 1 |  |  |  |  |  |  |  |  |  | true |
| **bias** | color4 | 0, 0, 0, 0 |  |  |  |  |  |  |  |  |  | true |
| *r* | float | None |  |  |  |  |  |  |  |  |  |  |
| *g* | float | None |  |  |  |  |  |  |  |  |  |  |
| *b* | float | None |  |  |  |  |  |  |  |  |  |  |
| *a* | float | None |  |  |  |  |  |  |  |  |  |  |
| *rgb* | color3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *UsdPrimvarReader*
<details open><summary>ND_UsdPrimvarReader_integer</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_integer
* *Type*: integer
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_integer


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_integer
    IMP_UsdPrimvarReader_integer_primvar[primvar]
    style IMP_UsdPrimvarReader_integer_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_integer_out([out])
    style IMP_UsdPrimvarReader_integer_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_integer_varname([varname])
    style IMP_UsdPrimvarReader_integer_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_integer_fallback([fallback])
    end
    IMP_UsdPrimvarReader_integer_varname --"geomprop"--> IMP_UsdPrimvarReader_integer_primvar
    IMP_UsdPrimvarReader_integer_fallback --"default"--> IMP_UsdPrimvarReader_integer_primvar
    IMP_UsdPrimvarReader_integer_primvar --> IMP_UsdPrimvarReader_integer_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | integer | 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | integer | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_boolean</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_boolean
* *Type*: boolean
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_boolean


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_boolean
    IMP_UsdPrimvarReader_boolean_primvar[primvar]
    style IMP_UsdPrimvarReader_boolean_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_boolean_out([out])
    style IMP_UsdPrimvarReader_boolean_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_boolean_varname([varname])
    style IMP_UsdPrimvarReader_boolean_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_boolean_fallback([fallback])
    end
    IMP_UsdPrimvarReader_boolean_varname --"geomprop"--> IMP_UsdPrimvarReader_boolean_primvar
    IMP_UsdPrimvarReader_boolean_fallback --"default"--> IMP_UsdPrimvarReader_boolean_primvar
    IMP_UsdPrimvarReader_boolean_primvar --> IMP_UsdPrimvarReader_boolean_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | boolean | False |  |  |  |  |  |  |  |  |  |  |
| *out* | boolean | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_string</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_string
* *Type*: string
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_string


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_string
    IMP_UsdPrimvarReader_string_primvar[primvar]
    style IMP_UsdPrimvarReader_string_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_string_out([out])
    style IMP_UsdPrimvarReader_string_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_string_varname([varname])
    style IMP_UsdPrimvarReader_string_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_string_fallback([fallback])
    end
    IMP_UsdPrimvarReader_string_varname --"geomprop"--> IMP_UsdPrimvarReader_string_primvar
    IMP_UsdPrimvarReader_string_fallback --"default"--> IMP_UsdPrimvarReader_string_primvar
    IMP_UsdPrimvarReader_string_primvar --> IMP_UsdPrimvarReader_string_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | string |  |  |  |  |  |  |  |  |  |  |  |
| *out* | string | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_float</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_float
* *Type*: float
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_float


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_float
    IMP_UsdPrimvarReader_float_primvar[primvar]
    style IMP_UsdPrimvarReader_float_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_float_out([out])
    style IMP_UsdPrimvarReader_float_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_float_varname([varname])
    style IMP_UsdPrimvarReader_float_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_float_fallback([fallback])
    end
    IMP_UsdPrimvarReader_float_varname --"geomprop"--> IMP_UsdPrimvarReader_float_primvar
    IMP_UsdPrimvarReader_float_fallback --"default"--> IMP_UsdPrimvarReader_float_primvar
    IMP_UsdPrimvarReader_float_primvar --> IMP_UsdPrimvarReader_float_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | float | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_vector2</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_vector2
* *Type*: vector2
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_vector2


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_vector2
    IMP_UsdPrimvarReader_vector2_primvar[primvar]
    style IMP_UsdPrimvarReader_vector2_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_vector2_out([out])
    style IMP_UsdPrimvarReader_vector2_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector2_varname([varname])
    style IMP_UsdPrimvarReader_vector2_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector2_fallback([fallback])
    end
    IMP_UsdPrimvarReader_vector2_varname --"geomprop"--> IMP_UsdPrimvarReader_vector2_primvar
    IMP_UsdPrimvarReader_vector2_fallback --"default"--> IMP_UsdPrimvarReader_vector2_primvar
    IMP_UsdPrimvarReader_vector2_primvar --> IMP_UsdPrimvarReader_vector2_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_vector3</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_vector3
* *Type*: vector3
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_vector3


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_vector3
    IMP_UsdPrimvarReader_vector3_primvar[primvar]
    style IMP_UsdPrimvarReader_vector3_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_vector3_out([out])
    style IMP_UsdPrimvarReader_vector3_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector3_varname([varname])
    style IMP_UsdPrimvarReader_vector3_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector3_fallback([fallback])
    end
    IMP_UsdPrimvarReader_vector3_varname --"geomprop"--> IMP_UsdPrimvarReader_vector3_primvar
    IMP_UsdPrimvarReader_vector3_fallback --"default"--> IMP_UsdPrimvarReader_vector3_primvar
    IMP_UsdPrimvarReader_vector3_primvar --> IMP_UsdPrimvarReader_vector3_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector3 | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_UsdPrimvarReader_vector4</summary>
<p>
 
* *Nodedef*: ND_UsdPrimvarReader_vector4
* *Type*: vector4
* *Group*: geometric
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdPrimvarReader_vector4


```mermaid
graph TB
    subgraph IMP_UsdPrimvarReader_vector4
    IMP_UsdPrimvarReader_vector4_primvar[primvar]
    style IMP_UsdPrimvarReader_vector4_out  fill:#0C0, color:#FFF
    IMP_UsdPrimvarReader_vector4_out([out])
    style IMP_UsdPrimvarReader_vector4_varname  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector4_varname([varname])
    style IMP_UsdPrimvarReader_vector4_fallback  fill:#09D, color:#FFF
    IMP_UsdPrimvarReader_vector4_fallback([fallback])
    end
    IMP_UsdPrimvarReader_vector4_varname --"geomprop"--> IMP_UsdPrimvarReader_vector4_primvar
    IMP_UsdPrimvarReader_vector4_fallback --"default"--> IMP_UsdPrimvarReader_vector4_primvar
    IMP_UsdPrimvarReader_vector4_primvar --> IMP_UsdPrimvarReader_vector4_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **varname** | string |  |  |  |  |  |  |  |  |  |  | true |
| **fallback** | vector4 | 0, 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector4 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *UsdTransform2d*
<details open><summary>ND_UsdTransform2d</summary>
<p>
 
* *Nodedef*: ND_UsdTransform2d
* *Type*: vector2
* *Group*: math
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: IMP_UsdTransform2d


```mermaid
graph TB
    subgraph IMP_UsdTransform2d
    IMP_UsdTransform2d_placement[placement]
    style IMP_UsdTransform2d_out  fill:#0C0, color:#FFF
    IMP_UsdTransform2d_out([out])
    style IMP_UsdTransform2d_in  fill:#09D, color:#FFF
    IMP_UsdTransform2d_in([in])
    style IMP_UsdTransform2d_scale  fill:#09D, color:#FFF
    IMP_UsdTransform2d_scale([scale])
    style IMP_UsdTransform2d_rotation  fill:#09D, color:#FFF
    IMP_UsdTransform2d_rotation([rotation])
    style IMP_UsdTransform2d_translation  fill:#09D, color:#FFF
    IMP_UsdTransform2d_translation([translation])
    end
    IMP_UsdTransform2d_in --"texcoord"--> IMP_UsdTransform2d_placement
    IMP_UsdTransform2d_scale --"scale"--> IMP_UsdTransform2d_placement
    IMP_UsdTransform2d_rotation --"rotate"--> IMP_UsdTransform2d_placement
    IMP_UsdTransform2d_translation --"offset"--> IMP_UsdTransform2d_placement
    IMP_UsdTransform2d_placement --> IMP_UsdTransform2d_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **rotation** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **scale** | vector2 | 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **translation** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaAdd*
<details open><summary>ND_lama_add_bsdf</summary>
<p>
 
* *Nodedef*: ND_lama_add_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_add_bsdf


```mermaid
graph TB
    subgraph NG_lama_add_bsdf
    NG_lama_add_bsdf_mul1[mul1]
    NG_lama_add_bsdf_mul2[mul2]
    NG_lama_add_bsdf_add1[add1]
    style NG_lama_add_bsdf_out  fill:#0C0, color:#FFF
    NG_lama_add_bsdf_out([out])
    style NG_lama_add_bsdf_material1  fill:#09D, color:#FFF
    NG_lama_add_bsdf_material1([material1])
    style NG_lama_add_bsdf_weight1  fill:#09D, color:#FFF
    NG_lama_add_bsdf_weight1([weight1])
    style NG_lama_add_bsdf_material2  fill:#09D, color:#FFF
    NG_lama_add_bsdf_material2([material2])
    style NG_lama_add_bsdf_weight2  fill:#09D, color:#FFF
    NG_lama_add_bsdf_weight2([weight2])
    end
    NG_lama_add_bsdf_material1 --"in1"--> NG_lama_add_bsdf_mul1
    NG_lama_add_bsdf_weight1 --"in2"--> NG_lama_add_bsdf_mul1
    NG_lama_add_bsdf_material2 --"in1"--> NG_lama_add_bsdf_mul2
    NG_lama_add_bsdf_weight2 --"in2"--> NG_lama_add_bsdf_mul2
    NG_lama_add_bsdf_mul1 --"in1"--> NG_lama_add_bsdf_add1
    NG_lama_add_bsdf_mul2 --"in2"--> NG_lama_add_bsdf_add1
    NG_lama_add_bsdf_add1 --> NG_lama_add_bsdf_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **material1** | BSDF | None | Material 1 |  |  |  |  |  |  |  | First material to add. |  |
| **material2** | BSDF | None | Material 2 |  |  |  |  |  |  |  | Second material to add. |  |
| **weight1** | float | 1.0 | Weight 1 | 0.0 | 1.0 |  |  |  |  |  | Weight of the first material. |  |
| **weight2** | float | 0.0 | Weight 2 | 0.0 | 1.0 |  |  |  |  |  | Weight of the second material. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_lama_add_edf</summary>
<p>
 
* *Nodedef*: ND_lama_add_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_add_edf


```mermaid
graph TB
    subgraph NG_lama_add_edf
    NG_lama_add_edf_mul1[mul1]
    NG_lama_add_edf_mul2[mul2]
    NG_lama_add_edf_add1[add1]
    style NG_lama_add_edf_out  fill:#0C0, color:#FFF
    NG_lama_add_edf_out([out])
    style NG_lama_add_edf_material1  fill:#09D, color:#FFF
    NG_lama_add_edf_material1([material1])
    style NG_lama_add_edf_weight1  fill:#09D, color:#FFF
    NG_lama_add_edf_weight1([weight1])
    style NG_lama_add_edf_material2  fill:#09D, color:#FFF
    NG_lama_add_edf_material2([material2])
    style NG_lama_add_edf_weight2  fill:#09D, color:#FFF
    NG_lama_add_edf_weight2([weight2])
    end
    NG_lama_add_edf_material1 --"in1"--> NG_lama_add_edf_mul1
    NG_lama_add_edf_weight1 --"in2"--> NG_lama_add_edf_mul1
    NG_lama_add_edf_material2 --"in1"--> NG_lama_add_edf_mul2
    NG_lama_add_edf_weight2 --"in2"--> NG_lama_add_edf_mul2
    NG_lama_add_edf_mul1 --"in1"--> NG_lama_add_edf_add1
    NG_lama_add_edf_mul2 --"in2"--> NG_lama_add_edf_add1
    NG_lama_add_edf_add1 --> NG_lama_add_edf_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **material1** | EDF | None | Material 1 |  |  |  |  |  |  |  | First material to add. |  |
| **material2** | EDF | None | Material 2 |  |  |  |  |  |  |  | Second material to add. |  |
| **weight1** | float | 1.0 | Weight 1 | 0.0 | 1.0 |  |  |  |  |  | Weight of the first material. |  |
| **weight2** | float | 0.0 | Weight 2 | 0.0 | 1.0 |  |  |  |  |  | Weight of the second material. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaConductor*
<details open><summary>ND_lama_conductor</summary>
<p>
 
* *Nodedef*: ND_lama_conductor
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: Lama conductor
* *Nodegraph*: IMPL_lama_conductor


```mermaid
graph TB
    subgraph IMPL_lama_conductor
    IMPL_lama_conductor_exterior_ior_switch[exterior_ior_switch]
    IMPL_lama_conductor_artistic_ior[artistic_ior]
    IMPL_lama_conductor_convert_ior[convert_ior]
    IMPL_lama_conductor_convert_extinction[convert_extinction]
    style IMPL_lama_conductor_eta_switch  fill:#C72, color:#FFF
    IMPL_lama_conductor_eta_switch{eta_switch}
    style IMPL_lama_conductor_kappa_switch  fill:#C72, color:#FFF
    IMPL_lama_conductor_kappa_switch{kappa_switch}
    IMPL_lama_conductor_relative_eta[relative_eta]
    IMPL_lama_conductor_relative_kappa[relative_kappa]
    IMPL_lama_conductor_roughness_inverse[roughness_inverse]
    style IMPL_lama_conductor_delta  fill:#C72, color:#FFF
    IMPL_lama_conductor_delta{delta}
    IMPL_lama_conductor_roughness_additional[roughness_additional]
    IMPL_lama_conductor_roughness_bitangent[roughness_bitangent]
    IMPL_lama_conductor_roughness_bitangent_clamped[roughness_bitangent_clamped]
    IMPL_lama_conductor_roughness_linear[roughness_linear]
    IMPL_lama_conductor_roughness_anisotropic_squared[roughness_anisotropic_squared]
    IMPL_lama_conductor_roughness_anisotropic_squared_clamped[roughness_anisotropic_squared_clamped]
    IMPL_lama_conductor_tangent_rotate_degree[tangent_rotate_degree]
    IMPL_lama_conductor_tangent_rotate[tangent_rotate]
    IMPL_lama_conductor_tangent_rotate_normalize[tangent_rotate_normalize]
    IMPL_lama_conductor_conductor_bsdf[conductor_bsdf]
    IMPL_lama_conductor_iridescence_relative_ior[iridescence_relative_ior]
    IMPL_lama_conductor_tinted_bsdf[tinted_bsdf]
    style IMPL_lama_conductor_out  fill:#0C0, color:#FFF
    IMPL_lama_conductor_out([out])
    style IMPL_lama_conductor_iridescenceIOR  fill:#09D, color:#FFF
    IMPL_lama_conductor_iridescenceIOR([iridescenceIOR])
    style IMPL_lama_conductor_exteriorIOR  fill:#09D, color:#FFF
    IMPL_lama_conductor_exteriorIOR([exteriorIOR])
    style IMPL_lama_conductor_iridescenceThickness  fill:#09D, color:#FFF
    IMPL_lama_conductor_iridescenceThickness([iridescenceThickness])
    style IMPL_lama_conductor_reflectivity  fill:#09D, color:#FFF
    IMPL_lama_conductor_reflectivity([reflectivity])
    style IMPL_lama_conductor_edgeColor  fill:#09D, color:#FFF
    IMPL_lama_conductor_edgeColor([edgeColor])
    style IMPL_lama_conductor_IOR  fill:#09D, color:#FFF
    IMPL_lama_conductor_IOR([IOR])
    style IMPL_lama_conductor_extinction  fill:#09D, color:#FFF
    IMPL_lama_conductor_extinction([extinction])
    style IMPL_lama_conductor_fresnelMode  fill:#09D, color:#FFF
    IMPL_lama_conductor_fresnelMode([fresnelMode])
    style IMPL_lama_conductor_roughness  fill:#09D, color:#FFF
    IMPL_lama_conductor_roughness([roughness])
    style IMPL_lama_conductor_anisotropy  fill:#09D, color:#FFF
    IMPL_lama_conductor_anisotropy([anisotropy])
    style IMPL_lama_conductor_anisotropyRotation  fill:#09D, color:#FFF
    IMPL_lama_conductor_anisotropyRotation([anisotropyRotation])
    style IMPL_lama_conductor_anisotropyDirection  fill:#09D, color:#FFF
    IMPL_lama_conductor_anisotropyDirection([anisotropyDirection])
    style IMPL_lama_conductor_normal  fill:#09D, color:#FFF
    IMPL_lama_conductor_normal([normal])
    style IMPL_lama_conductor_tint  fill:#09D, color:#FFF
    IMPL_lama_conductor_tint([tint])
    end
    IMPL_lama_conductor_iridescenceIOR --"in1"--> IMPL_lama_conductor_exterior_ior_switch
    IMPL_lama_conductor_exteriorIOR --"in2"--> IMPL_lama_conductor_exterior_ior_switch
    IMPL_lama_conductor_iridescenceThickness --"value1"--> IMPL_lama_conductor_exterior_ior_switch
    IMPL_lama_conductor_reflectivity --"reflectivity"--> IMPL_lama_conductor_artistic_ior
    IMPL_lama_conductor_edgeColor --"edge_color"--> IMPL_lama_conductor_artistic_ior
    IMPL_lama_conductor_IOR --"in"--> IMPL_lama_conductor_convert_ior
    IMPL_lama_conductor_extinction --"in"--> IMPL_lama_conductor_convert_extinction
    IMPL_lama_conductor_convert_ior --"in1"--> IMPL_lama_conductor_eta_switch
    IMPL_lama_conductor_artistic_ior --"ior-->in2"--> IMPL_lama_conductor_eta_switch
    IMPL_lama_conductor_fresnelMode --"which"--> IMPL_lama_conductor_eta_switch
    IMPL_lama_conductor_convert_extinction --"in1"--> IMPL_lama_conductor_kappa_switch
    IMPL_lama_conductor_artistic_ior --"extinction-->in2"--> IMPL_lama_conductor_kappa_switch
    IMPL_lama_conductor_fresnelMode --"which"--> IMPL_lama_conductor_kappa_switch
    IMPL_lama_conductor_eta_switch --"in1"--> IMPL_lama_conductor_relative_eta
    IMPL_lama_conductor_exterior_ior_switch --"in2"--> IMPL_lama_conductor_relative_eta
    IMPL_lama_conductor_kappa_switch --"in1"--> IMPL_lama_conductor_relative_kappa
    IMPL_lama_conductor_exterior_ior_switch --"in2"--> IMPL_lama_conductor_relative_kappa
    IMPL_lama_conductor_roughness --"in2"--> IMPL_lama_conductor_roughness_inverse
    IMPL_lama_conductor_roughness_inverse --"in1"--> IMPL_lama_conductor_delta
    IMPL_lama_conductor_roughness --"in2"--> IMPL_lama_conductor_delta
    IMPL_lama_conductor_anisotropy --"value1"--> IMPL_lama_conductor_delta
    IMPL_lama_conductor_anisotropy --"in1"--> IMPL_lama_conductor_roughness_additional
    IMPL_lama_conductor_delta --"in2"--> IMPL_lama_conductor_roughness_additional
    IMPL_lama_conductor_roughness --"in1"--> IMPL_lama_conductor_roughness_bitangent
    IMPL_lama_conductor_roughness_additional --"in2"--> IMPL_lama_conductor_roughness_bitangent
    IMPL_lama_conductor_roughness_bitangent --"in"--> IMPL_lama_conductor_roughness_bitangent_clamped
    IMPL_lama_conductor_roughness --"in1"--> IMPL_lama_conductor_roughness_linear
    IMPL_lama_conductor_roughness_bitangent_clamped --"in2"--> IMPL_lama_conductor_roughness_linear
    IMPL_lama_conductor_roughness_linear --"in1"--> IMPL_lama_conductor_roughness_anisotropic_squared
    IMPL_lama_conductor_roughness_anisotropic_squared --"in1"--> IMPL_lama_conductor_roughness_anisotropic_squared_clamped
    IMPL_lama_conductor_anisotropyRotation --"in1"--> IMPL_lama_conductor_tangent_rotate_degree
    IMPL_lama_conductor_anisotropyDirection --"in"--> IMPL_lama_conductor_tangent_rotate
    IMPL_lama_conductor_tangent_rotate_degree --"amount"--> IMPL_lama_conductor_tangent_rotate
    IMPL_lama_conductor_normal --"axis"--> IMPL_lama_conductor_tangent_rotate
    IMPL_lama_conductor_tangent_rotate --"in"--> IMPL_lama_conductor_tangent_rotate_normalize
    IMPL_lama_conductor_relative_eta --"ior"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_relative_kappa --"extinction"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_roughness_anisotropic_squared_clamped --"roughness"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_normal --"normal"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_tangent_rotate_normalize --"tangent"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_iridescenceThickness --"thinfilm_thickness"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_iridescence_relative_ior --"thinfilm_ior"--> IMPL_lama_conductor_conductor_bsdf
    IMPL_lama_conductor_iridescenceIOR --"in1"--> IMPL_lama_conductor_iridescence_relative_ior
    IMPL_lama_conductor_exteriorIOR --"in2"--> IMPL_lama_conductor_iridescence_relative_ior
    IMPL_lama_conductor_conductor_bsdf --"in1"--> IMPL_lama_conductor_tinted_bsdf
    IMPL_lama_conductor_tint --"in2"--> IMPL_lama_conductor_tinted_bsdf
    IMPL_lama_conductor_tinted_bsdf --> IMPL_lama_conductor_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **tint** | color3 | 1, 1, 1 | Tint |  |  |  |  |  | Main |  | Overall color multiplier. It should be used with parcimony, as a non-white value breaks physicality. The prefered way to define the color of a conductor is through the Fresnel attributes right below. |  |
| **fresnelMode** | integer | 0 | Fresnel Mode |  |  |  |  |  | Main |  | Fresnel mode | true |
| **IOR** | vector3 | 0.18, 0.42, 1.37 | IOR |  |  |  |  |  | Main |  | Index of refraction (often denoted by eta), defining the color reflected by the surface in the normal direction. |  |
| **extinction** | vector3 | 3.42, 2.35, 1.77 | Extinction |  |  |  |  |  | Main |  | Extinction coefficient (often denoted by kappa), influencing how the reflected color curve evolves between its value in the normal direction (or 0 degree), and 1 when reaching 90 degrees. A null value does not deviate the curve at all. |  |
| **reflectivity** | color3 | 0.945, 0.7772, 0.3737 | Reflectivity |  |  |  |  |  | Main |  | Color reflected by the surface in the normal direction. |  |
| **edgeColor** | color3 | 0.9979, 0.9813, 0.7523 | Edge Color |  |  |  |  |  | Main |  | Indicates how the reflected color curve evolves between its value in the normal direction (or 0 degree), and 1 when reaching 90 degrees. Note that this color is unlikely to be reached, and just bends the curve towards it when reaching grazing angles. A null value does not deviate the curve at all. |  |
| **roughness** | float | 0.1 | Roughness | 0.0 | 1.0 |  |  |  | Main |  | Micro-facet distribution roughness. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Main |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| **anisotropy** | float | 0.0 | Anisotropy | -1.0 | 1.0 |  |  |  | Anisotropy |  | Defines the amount of anisotropy, changing the co-tangent axis roughness from the original value to 1 (or to 0 with a negative value). |  |
| **anisotropyDirection** | vector3 | None | Direction |  |  |  |  |  | Anisotropy |  | Overrides the surface tangent as the anisotropy direction. |  |
| **anisotropyRotation** | float | 0.0 | Rotation |  |  |  |  |  | Anisotropy |  | Rotates the anisotropy direction (possibly overriden by the previous attribute) around the normal, from 0 to 360 degrees. |  |
| **iridescenceThickness** | float | 0.0 | Thickness | 0.0 |  |  | 200.0 |  | Iridescence |  | Thin film thickness in nanometers, driving the iridescent effect. |  |
| **iridescenceIOR** | float | 1.5 | IOR | 1.0 | 3.0 |  |  |  | Iridescence |  | Thin film index of refraction, driving the iridescent effect. |  |
| **exteriorIOR** | float | 1.0 | Exterior IOR | 1.0 | 3.0 |  |  |  | Advanced |  | Defines what the IOR of the exterior medium is (can be either the outside medium, eg. air or water, or in case of a layered material, the top layer medium, like plexiglass or varnish). |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaDielectric*
<details open><summary>ND_lama_dielectric</summary>
<p>
 
* *Nodedef*: ND_lama_dielectric
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: Lama dielectric
* *Nodegraph*: IMPL_lama_dielectric


```mermaid
graph TB
    subgraph IMPL_lama_dielectric
    IMPL_lama_dielectric_reflectivity_color[reflectivity_color]
    IMPL_lama_dielectric_artistic_ior[artistic_ior]
    IMPL_lama_dielectric_swizzle[swizzle]
    style IMPL_lama_dielectric_fresnel_mode_switch  fill:#C72, color:#FFF
    IMPL_lama_dielectric_fresnel_mode_switch{fresnel_mode_switch}
    IMPL_lama_dielectric_relative_ior[relative_ior]
    IMPL_lama_dielectric_roughness_inverse[roughness_inverse]
    style IMPL_lama_dielectric_delta  fill:#C72, color:#FFF
    IMPL_lama_dielectric_delta{delta}
    IMPL_lama_dielectric_roughness_additional[roughness_additional]
    IMPL_lama_dielectric_roughness_bitangent[roughness_bitangent]
    IMPL_lama_dielectric_roughness_bitangent_clamped[roughness_bitangent_clamped]
    IMPL_lama_dielectric_roughness_linear[roughness_linear]
    IMPL_lama_dielectric_roughness_anisotropic_squared[roughness_anisotropic_squared]
    IMPL_lama_dielectric_roughness_anisotropic_squared_clamped[roughness_anisotropic_squared_clamped]
    IMPL_lama_dielectric_tangent_rotate_degree[tangent_rotate_degree]
    IMPL_lama_dielectric_tangent_rotate_degree_offset[tangent_rotate_degree_offset]
    IMPL_lama_dielectric_tangent_rotate[tangent_rotate]
    IMPL_lama_dielectric_tangent_rotate_normalize[tangent_rotate_normalize]
    IMPL_lama_dielectric_absorption[absorption]
    IMPL_lama_dielectric_absorption_vector[absorption_vector]
    IMPL_lama_dielectric_scatter_vector[scatter_vector]
    IMPL_lama_dielectric_interior_vdf[interior_vdf]
    IMPL_lama_dielectric_transmission_bsdf[transmission_bsdf]
    IMPL_lama_dielectric_transmission_layer[transmission_layer]
    IMPL_lama_dielectric_reflection_bsdf[reflection_bsdf]
    IMPL_lama_dielectric_dielectric_bsdf[dielectric_bsdf]
    style IMPL_lama_dielectric_out  fill:#0C0, color:#FFF
    IMPL_lama_dielectric_out([out])
    style IMPL_lama_dielectric_reflectivity  fill:#09D, color:#FFF
    IMPL_lama_dielectric_reflectivity([reflectivity])
    style IMPL_lama_dielectric_IOR  fill:#09D, color:#FFF
    IMPL_lama_dielectric_IOR([IOR])
    style IMPL_lama_dielectric_fresnelMode  fill:#09D, color:#FFF
    IMPL_lama_dielectric_fresnelMode([fresnelMode])
    style IMPL_lama_dielectric_exteriorIOR  fill:#09D, color:#FFF
    IMPL_lama_dielectric_exteriorIOR([exteriorIOR])
    style IMPL_lama_dielectric_roughness  fill:#09D, color:#FFF
    IMPL_lama_dielectric_roughness([roughness])
    style IMPL_lama_dielectric_anisotropy  fill:#09D, color:#FFF
    IMPL_lama_dielectric_anisotropy([anisotropy])
    style IMPL_lama_dielectric_rotation  fill:#09D, color:#FFF
    IMPL_lama_dielectric_rotation([rotation])
    style IMPL_lama_dielectric_direction  fill:#09D, color:#FFF
    IMPL_lama_dielectric_direction([direction])
    style IMPL_lama_dielectric_normal  fill:#09D, color:#FFF
    IMPL_lama_dielectric_normal([normal])
    style IMPL_lama_dielectric_absorptionColor  fill:#09D, color:#FFF
    IMPL_lama_dielectric_absorptionColor([absorptionColor])
    style IMPL_lama_dielectric_absorptionRadius  fill:#09D, color:#FFF
    IMPL_lama_dielectric_absorptionRadius([absorptionRadius])
    style IMPL_lama_dielectric_scatterColor  fill:#09D, color:#FFF
    IMPL_lama_dielectric_scatterColor([scatterColor])
    style IMPL_lama_dielectric_scatterAnisotropy  fill:#09D, color:#FFF
    IMPL_lama_dielectric_scatterAnisotropy([scatterAnisotropy])
    style IMPL_lama_dielectric_transmissionTint  fill:#09D, color:#FFF
    IMPL_lama_dielectric_transmissionTint([transmissionTint])
    style IMPL_lama_dielectric_reflectionTint  fill:#09D, color:#FFF
    IMPL_lama_dielectric_reflectionTint([reflectionTint])
    end
    IMPL_lama_dielectric_reflectivity --"in"--> IMPL_lama_dielectric_reflectivity_color
    IMPL_lama_dielectric_reflectivity_color --"reflectivity"--> IMPL_lama_dielectric_artistic_ior
    IMPL_lama_dielectric_artistic_ior --"ior-->in"--> IMPL_lama_dielectric_swizzle
    IMPL_lama_dielectric_IOR --"in1"--> IMPL_lama_dielectric_fresnel_mode_switch
    IMPL_lama_dielectric_swizzle --"in2"--> IMPL_lama_dielectric_fresnel_mode_switch
    IMPL_lama_dielectric_fresnelMode --"which"--> IMPL_lama_dielectric_fresnel_mode_switch
    IMPL_lama_dielectric_fresnel_mode_switch --"in1"--> IMPL_lama_dielectric_relative_ior
    IMPL_lama_dielectric_exteriorIOR --"in2"--> IMPL_lama_dielectric_relative_ior
    IMPL_lama_dielectric_roughness --"in2"--> IMPL_lama_dielectric_roughness_inverse
    IMPL_lama_dielectric_roughness_inverse --"in1"--> IMPL_lama_dielectric_delta
    IMPL_lama_dielectric_roughness --"in2"--> IMPL_lama_dielectric_delta
    IMPL_lama_dielectric_anisotropy --"value1"--> IMPL_lama_dielectric_delta
    IMPL_lama_dielectric_anisotropy --"in1"--> IMPL_lama_dielectric_roughness_additional
    IMPL_lama_dielectric_delta --"in2"--> IMPL_lama_dielectric_roughness_additional
    IMPL_lama_dielectric_roughness --"in1"--> IMPL_lama_dielectric_roughness_bitangent
    IMPL_lama_dielectric_roughness_additional --"in2"--> IMPL_lama_dielectric_roughness_bitangent
    IMPL_lama_dielectric_roughness_bitangent --"in"--> IMPL_lama_dielectric_roughness_bitangent_clamped
    IMPL_lama_dielectric_roughness --"in1"--> IMPL_lama_dielectric_roughness_linear
    IMPL_lama_dielectric_roughness_bitangent_clamped --"in2"--> IMPL_lama_dielectric_roughness_linear
    IMPL_lama_dielectric_roughness_linear --"in1"--> IMPL_lama_dielectric_roughness_anisotropic_squared
    IMPL_lama_dielectric_roughness_anisotropic_squared --"in1"--> IMPL_lama_dielectric_roughness_anisotropic_squared_clamped
    IMPL_lama_dielectric_rotation --"in1"--> IMPL_lama_dielectric_tangent_rotate_degree
    IMPL_lama_dielectric_tangent_rotate_degree --"in1"--> IMPL_lama_dielectric_tangent_rotate_degree_offset
    IMPL_lama_dielectric_direction --"in"--> IMPL_lama_dielectric_tangent_rotate
    IMPL_lama_dielectric_tangent_rotate_degree_offset --"amount"--> IMPL_lama_dielectric_tangent_rotate
    IMPL_lama_dielectric_normal --"axis"--> IMPL_lama_dielectric_tangent_rotate
    IMPL_lama_dielectric_tangent_rotate --"in"--> IMPL_lama_dielectric_tangent_rotate_normalize
    IMPL_lama_dielectric_absorptionColor --"in1"--> IMPL_lama_dielectric_absorption
    IMPL_lama_dielectric_absorptionRadius --"in2"--> IMPL_lama_dielectric_absorption
    IMPL_lama_dielectric_absorption --"in"--> IMPL_lama_dielectric_absorption_vector
    IMPL_lama_dielectric_scatterColor --"in"--> IMPL_lama_dielectric_scatter_vector
    IMPL_lama_dielectric_absorption_vector --"absorption"--> IMPL_lama_dielectric_interior_vdf
    IMPL_lama_dielectric_scatter_vector --"scattering"--> IMPL_lama_dielectric_interior_vdf
    IMPL_lama_dielectric_scatterAnisotropy --"anisotropy"--> IMPL_lama_dielectric_interior_vdf
    IMPL_lama_dielectric_transmissionTint --"tint"--> IMPL_lama_dielectric_transmission_bsdf
    IMPL_lama_dielectric_relative_ior --"ior"--> IMPL_lama_dielectric_transmission_bsdf
    IMPL_lama_dielectric_roughness_anisotropic_squared_clamped --"roughness"--> IMPL_lama_dielectric_transmission_bsdf
    IMPL_lama_dielectric_normal --"normal"--> IMPL_lama_dielectric_transmission_bsdf
    IMPL_lama_dielectric_tangent_rotate_normalize --"tangent"--> IMPL_lama_dielectric_transmission_bsdf
    IMPL_lama_dielectric_transmission_bsdf --"top"--> IMPL_lama_dielectric_transmission_layer
    IMPL_lama_dielectric_interior_vdf --"base"--> IMPL_lama_dielectric_transmission_layer
    IMPL_lama_dielectric_reflectionTint --"tint"--> IMPL_lama_dielectric_reflection_bsdf
    IMPL_lama_dielectric_relative_ior --"ior"--> IMPL_lama_dielectric_reflection_bsdf
    IMPL_lama_dielectric_roughness_anisotropic_squared_clamped --"roughness"--> IMPL_lama_dielectric_reflection_bsdf
    IMPL_lama_dielectric_normal --"normal"--> IMPL_lama_dielectric_reflection_bsdf
    IMPL_lama_dielectric_tangent_rotate_normalize --"tangent"--> IMPL_lama_dielectric_reflection_bsdf
    IMPL_lama_dielectric_reflection_bsdf --"top"--> IMPL_lama_dielectric_dielectric_bsdf
    IMPL_lama_dielectric_transmission_layer --"base"--> IMPL_lama_dielectric_dielectric_bsdf
    IMPL_lama_dielectric_dielectric_bsdf --> IMPL_lama_dielectric_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **reflectionTint** | color3 | 1, 1, 1 | Reflection Tint |  |  |  |  |  | Main |  | Color multiplier for external reflection. It should be used with parcimony, as a non-white value breaks physicality. |  |
| **transmissionTint** | color3 | 1, 1, 1 | Transmission Tint |  |  |  |  |  | Main |  | Color multiplier for rays going inside the medium (covers external transmission and internal reflection). It should be used with parcimony, as a non-white value breaks physicality. The prefered way to define the color of a dielectric is through the Interior attributes right below. |  |
| **fresnelMode** | integer | 0 | Fresnel Mode |  |  |  |  |  | Main |  | Fresnel mode | true |
| **IOR** | float | 1.5 | IOR | 1.0 | 3.0 |  |  |  | Main |  | Index of refraction (often denoted by eta), defining the amount reflected by the surface in the normal direction, and how the rays are bent by refraction. |  |
| **reflectivity** | float | 0.04 | Reflectivity |  |  |  |  |  | Main |  | Reflectivity |  |
| **roughness** | float | 0.1 | Roughness | 0.0 | 1.0 |  |  |  | Main |  | Micro-facet distribution roughness. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Main |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| **anisotropy** | float | 0.0 | Anisotropy | -1.0 | 1.0 |  |  |  | Anisotropy |  | Defines the amount of anisotropy, changing the co-tangent axis roughness from the original value to 1 (or to 0 with a negative value). |  |
| **direction** | vector3 | None | Direction |  |  |  |  |  | Anisotropy |  | Overrides the surface tangent as the anisotropy direction. |  |
| **rotation** | float | 0.0 | Rotation |  |  |  |  |  | Anisotropy |  | Rotates the anisotropy direction (possibly overriden by the previous attribute) around the normal, from 0 to 360 degrees. |  |
| **exteriorIOR** | float | 1.0 | Exterior IOR | 1.0 | 3.0 |  |  |  | Advanced |  | Defines what the IOR of the exterior medium is (can be either the outside medium, eg. air or water, or in case of a layered material, the top layer medium, like plexiglass or varnish). |  |
| **absorptionColor** | color3 | 1, 1, 1 | Absorption Color |  |  |  |  |  | Interior |  | Absorption color |  |
| **absorptionRadius** | float | 1.0 | Absorption Radius |  |  |  |  |  | Interior |  | Absorption radius |  |
| **scatterColor** | color3 | 0, 0, 0 | Scatter Color |  |  |  |  |  | Interior |  | Scatter color |  |
| **scatterAnisotropy** | float | 0.0 | Scatter Anisotropy | -1.0 | 1.0 |  |  |  | Interior |  | Scatter anisotropy |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaDiffuse*
<details open><summary>ND_lama_diffuse</summary>
<p>
 
* *Nodedef*: ND_lama_diffuse
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_diffuse


```mermaid
graph TB
    subgraph NG_lama_diffuse
    NG_lama_diffuse_roughness_squared[roughness_squared]
    NG_lama_diffuse_half_roughness_squared[half_roughness_squared]
    NG_lama_diffuse_oren_nayar[oren_nayar]
    style NG_lama_diffuse_out  fill:#0C0, color:#FFF
    NG_lama_diffuse_out([out])
    style NG_lama_diffuse_roughness  fill:#09D, color:#FFF
    NG_lama_diffuse_roughness([roughness])
    style NG_lama_diffuse_color  fill:#09D, color:#FFF
    NG_lama_diffuse_color([color])
    style NG_lama_diffuse_normal  fill:#09D, color:#FFF
    NG_lama_diffuse_normal([normal])
    end
    NG_lama_diffuse_roughness --"in1"--> NG_lama_diffuse_roughness_squared
    NG_lama_diffuse_roughness --"in2"--> NG_lama_diffuse_roughness_squared
    NG_lama_diffuse_roughness_squared --"in1"--> NG_lama_diffuse_half_roughness_squared
    NG_lama_diffuse_color --"color"--> NG_lama_diffuse_oren_nayar
    NG_lama_diffuse_half_roughness_squared --"roughness"--> NG_lama_diffuse_oren_nayar
    NG_lama_diffuse_normal --"normal"--> NG_lama_diffuse_oren_nayar
    NG_lama_diffuse_oren_nayar --> NG_lama_diffuse_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 0.18, 0.18, 0.18 | Color |  |  |  |  |  |  |  | Diffuse color (aka albedo), defining what ratio of light is reflected for each color channel. |  |
| **roughness** | float | 0.0 | Roughness | 0.0 | 1.0 |  |  |  |  |  | Micro-facet distribution (Oren-Nayar) roughness. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  |  |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| **energyCompensation** | float | 1.0 | Energy Compensation | 0.0 | 1.0 |  |  |  | Advanced |  | Indicates how much energy should be added to compensate for the loss inherent to the Oren-Nayar model, ranging from no compensation at all, to the expected energy from multiple scattering between the micro-facets. This prevents overly dark results when roughness is high. | true |
| **lobeName** | string | diffuse | Lobe Name |  |  |  |  |  | Advanced |  | Defines the name that can be used in LPE AOVs for this lobe. | true |
| **matte** | string |  | Matte |  |  |  |  |  | Advanced |  | Defines the name that can be used by the matte system, to output the weight of this lobe in the final material as an AOV. | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaEmission*
<details open><summary>ND_lama_emission</summary>
<p>
 
* *Nodedef*: ND_lama_emission
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: Lama emission
* *Nodegraph*: IMPL_lama_emission


```mermaid
graph TB
    subgraph IMPL_lama_emission
    IMPL_lama_emission_emission[emission]
    style IMPL_lama_emission_out  fill:#0C0, color:#FFF
    IMPL_lama_emission_out([out])
    style IMPL_lama_emission_color  fill:#09D, color:#FFF
    IMPL_lama_emission_color([color])
    end
    IMPL_lama_emission_color --"color"--> IMPL_lama_emission_emission
    IMPL_lama_emission_emission --> IMPL_lama_emission_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 | Color |  |  |  |  |  | Main |  | Color being uniformly emitted in all directions above the surface. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaLayer*
<details open><summary>ND_lama_layer_bsdf</summary>
<p>
 
* *Nodedef*: ND_lama_layer_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_layer_bsdf


```mermaid
graph TB
    subgraph NG_lama_layer_bsdf
    NG_lama_layer_bsdf_mul[mul]
    NG_lama_layer_bsdf_layer[layer]
    style NG_lama_layer_bsdf_out  fill:#0C0, color:#FFF
    NG_lama_layer_bsdf_out([out])
    style NG_lama_layer_bsdf_materialTop  fill:#09D, color:#FFF
    NG_lama_layer_bsdf_materialTop([materialTop])
    style NG_lama_layer_bsdf_topMix  fill:#09D, color:#FFF
    NG_lama_layer_bsdf_topMix([topMix])
    style NG_lama_layer_bsdf_materialBase  fill:#09D, color:#FFF
    NG_lama_layer_bsdf_materialBase([materialBase])
    end
    NG_lama_layer_bsdf_materialTop --"in1"--> NG_lama_layer_bsdf_mul
    NG_lama_layer_bsdf_topMix --"in2"--> NG_lama_layer_bsdf_mul
    NG_lama_layer_bsdf_mul --"top"--> NG_lama_layer_bsdf_layer
    NG_lama_layer_bsdf_materialBase --"base"--> NG_lama_layer_bsdf_layer
    NG_lama_layer_bsdf_layer --> NG_lama_layer_bsdf_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **materialTop** | BSDF | None | Material Top |  |  |  |  |  |  |  | Material used for the top slab. If not set, the base material will be used by itself. |  |
| **materialBase** | BSDF | None | Material Base |  |  |  |  |  |  |  | Base material, right under the top one. |  |
| **topMix** | float | 1.0 | Top Mix | 0.0 | 1.0 |  |  |  |  |  | Defines how visible the top material is. |  |
| **topThickness** | float | 0.0 | Top Thickness | 0.0 |  |  |  |  |  |  | Thickness of the top slab. It is only relevant for interior effects associated with the top material, such as absorption. If the top material is itself a layer node, this value is passed on to its base component. And if the top material is a mix or add, this value is passed on to both child materials. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaMix*
<details open><summary>ND_lama_mix_bsdf</summary>
<p>
 
* *Nodedef*: ND_lama_mix_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_mix_bsdf


```mermaid
graph TB
    subgraph NG_lama_mix_bsdf
    NG_lama_mix_bsdf_mix[mix]
    style NG_lama_mix_bsdf_out  fill:#0C0, color:#FFF
    NG_lama_mix_bsdf_out([out])
    style NG_lama_mix_bsdf_material2  fill:#09D, color:#FFF
    NG_lama_mix_bsdf_material2([material2])
    style NG_lama_mix_bsdf_material1  fill:#09D, color:#FFF
    NG_lama_mix_bsdf_material1([material1])
    style NG_lama_mix_bsdf_mix:in  fill:#09D, color:#FFF
    NG_lama_mix_bsdf_mix:in([mix:in])
    end
    NG_lama_mix_bsdf_material2 --"fg"--> NG_lama_mix_bsdf_mix
    NG_lama_mix_bsdf_material1 --"bg"--> NG_lama_mix_bsdf_mix
    NG_lama_mix_bsdf_mix:in --"mix"--> NG_lama_mix_bsdf_mix
    NG_lama_mix_bsdf_mix --> NG_lama_mix_bsdf_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **material1** | BSDF | None | Material 1 |  |  |  |  |  |  |  | First material to mix. |  |
| **material2** | BSDF | None | Material 2 |  |  |  |  |  |  |  | Second material to mix. |  |
| **mix** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  | Defines the balance between the two materials, ranging from 0 (Material 1 only) to 1 (Material 2 only). Can also be seen as a Material 2 over Material 1 mask. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_lama_mix_edf</summary>
<p>
 
* *Nodedef*: ND_lama_mix_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_mix_edf


```mermaid
graph TB
    subgraph NG_lama_mix_edf
    NG_lama_mix_edf_mix[mix]
    style NG_lama_mix_edf_out  fill:#0C0, color:#FFF
    NG_lama_mix_edf_out([out])
    style NG_lama_mix_edf_material2  fill:#09D, color:#FFF
    NG_lama_mix_edf_material2([material2])
    style NG_lama_mix_edf_material1  fill:#09D, color:#FFF
    NG_lama_mix_edf_material1([material1])
    style NG_lama_mix_edf_mix:in  fill:#09D, color:#FFF
    NG_lama_mix_edf_mix:in([mix:in])
    end
    NG_lama_mix_edf_material2 --"fg"--> NG_lama_mix_edf_mix
    NG_lama_mix_edf_material1 --"bg"--> NG_lama_mix_edf_mix
    NG_lama_mix_edf_mix:in --"mix"--> NG_lama_mix_edf_mix
    NG_lama_mix_edf_mix --> NG_lama_mix_edf_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **material1** | EDF | None | Material 1 |  |  |  |  |  |  |  | First material to mix. |  |
| **material2** | EDF | None | Material 2 |  |  |  |  |  |  |  | Second material to mix. |  |
| **mix** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  | Defines the balance between the two materials, ranging from 0 (Material 1 only) to 1 (Material 2 only). Can also be seen as a Material 2 over Material 1 mask. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaSheen*
<details open><summary>ND_lama_sheen</summary>
<p>
 
* *Nodedef*: ND_lama_sheen
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: Lama sheen
* *Nodegraph*: IMPL_lama_sheen


```mermaid
graph TB
    subgraph IMPL_lama_sheen
    IMPL_lama_sheen_roughness_compressed[roughness_compressed]
    IMPL_lama_sheen_roughness_remapped[roughness_remapped]
    IMPL_lama_sheen_roughness_squared[roughness_squared]
    IMPL_lama_sheen_sheen_bsdf[sheen_bsdf]
    style IMPL_lama_sheen_out  fill:#0C0, color:#FFF
    IMPL_lama_sheen_out([out])
    style IMPL_lama_sheen_roughness  fill:#09D, color:#FFF
    IMPL_lama_sheen_roughness([roughness])
    style IMPL_lama_sheen_color  fill:#09D, color:#FFF
    IMPL_lama_sheen_color([color])
    style IMPL_lama_sheen_normal  fill:#09D, color:#FFF
    IMPL_lama_sheen_normal([normal])
    end
    IMPL_lama_sheen_roughness --"in1"--> IMPL_lama_sheen_roughness_compressed
    IMPL_lama_sheen_roughness_compressed --"in1"--> IMPL_lama_sheen_roughness_remapped
    IMPL_lama_sheen_roughness_remapped --"in1"--> IMPL_lama_sheen_roughness_squared
    IMPL_lama_sheen_color --"color"--> IMPL_lama_sheen_sheen_bsdf
    IMPL_lama_sheen_roughness_squared --"roughness"--> IMPL_lama_sheen_sheen_bsdf
    IMPL_lama_sheen_normal --"normal"--> IMPL_lama_sheen_sheen_bsdf
    IMPL_lama_sheen_sheen_bsdf --> IMPL_lama_sheen_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 | Color |  |  |  |  |  | Main |  | Amount of sheen to add, per channel. When this node is used as top material in a stack, the more sheen is added, the less energy will be transmitted to the base material. |  |
| **roughness** | float | 0.1 | Roughness | 0.0 | 1.0 |  |  |  | Main |  | Roughness of the sheen effect. Very rough sheen can be used to create a rough diffuse look (when combined with a diffuse node by a stack or mix). |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Main |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaSSS*
<details open><summary>ND_lama_sss</summary>
<p>
 
* *Nodedef*: ND_lama_sss
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: Lama SSS
* *Nodegraph*: IMPL_lama_sss


```mermaid
graph TB
    subgraph IMPL_lama_sss
    IMPL_lama_sss_subsurface_radius_vector[subsurface_radius_vector]
    IMPL_lama_sss_subsurface_radius_scaled[subsurface_radius_scaled]
    IMPL_lama_sss_subsurface_multiply_unitlength[subsurface_multiply_unitlength]
    IMPL_lama_sss_subsurface_bsdf[subsurface_bsdf]
    style IMPL_lama_sss_out  fill:#0C0, color:#FFF
    IMPL_lama_sss_out([out])
    IMPL_lama_sss_convert[convert]
    style IMPL_lama_sss_sssRadius  fill:#09D, color:#FFF
    IMPL_lama_sss_sssRadius([sssRadius])
    style IMPL_lama_sss_sssScale  fill:#09D, color:#FFF
    IMPL_lama_sss_sssScale([sssScale])
    style IMPL_lama_sss_sssUnitLength  fill:#09D, color:#FFF
    IMPL_lama_sss_sssUnitLength([sssUnitLength])
    style IMPL_lama_sss_color  fill:#09D, color:#FFF
    IMPL_lama_sss_color([color])
    style IMPL_lama_sss_sssAnisotropy  fill:#09D, color:#FFF
    IMPL_lama_sss_sssAnisotropy([sssAnisotropy])
    style IMPL_lama_sss_normal  fill:#09D, color:#FFF
    IMPL_lama_sss_normal([normal])
    end
    IMPL_lama_sss_sssRadius --"in"--> IMPL_lama_sss_subsurface_radius_vector
    IMPL_lama_sss_subsurface_radius_vector --"in1"--> IMPL_lama_sss_subsurface_radius_scaled
    IMPL_lama_sss_sssScale --"in2"--> IMPL_lama_sss_subsurface_radius_scaled
    IMPL_lama_sss_subsurface_radius_scaled --"in1"--> IMPL_lama_sss_subsurface_multiply_unitlength
    IMPL_lama_sss_sssUnitLength --"in2"--> IMPL_lama_sss_subsurface_multiply_unitlength
    IMPL_lama_sss_color --"color"--> IMPL_lama_sss_subsurface_bsdf
    IMPL_lama_sss_convert --"radius"--> IMPL_lama_sss_subsurface_bsdf
    IMPL_lama_sss_sssAnisotropy --"anisotropy"--> IMPL_lama_sss_subsurface_bsdf
    IMPL_lama_sss_normal --"normal"--> IMPL_lama_sss_subsurface_bsdf
    IMPL_lama_sss_subsurface_bsdf --> IMPL_lama_sss_out
    IMPL_lama_sss_subsurface_multiply_unitlength --"in"--> IMPL_lama_sss_convert
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 0.18, 0.18, 0.18 | Color |  |  |  |  |  | Main |  | Diffuse color (aka albedo), defining what ratio of light is reflected -- or transmitted -- for each color channel. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  | Main |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| **sssRadius** | color3 | 0, 0, 0 | Radius |  |  |  |  |  | SSS |  | Diffuse Mean Free Path, expressed for each color channel in mm. Indicates on average how much the light travels under the surface before being scattered. The higher the value, the softer the result will be. If null, the computation simplifies to a Lambertian lobe. |  |
| **sssScale** | float | 1.0 | Scale |  |  |  |  |  | SSS |  | Multiplies the radius, to adjust its scale to the scene at hand. If null, the computation simplifies to a Lambertian lobe. |  |
| **sssMode** | integer | 0 | Mode |  |  |  |  |  | Main |  | Selects what method should be used to compute sub-surface scattering. Proposes two path-traced variants, and a more traditional approximate diffusion model. | true |
| **sssIOR** | float | 1.0 | IOR | 1.0 | 2.0 |  |  |  | SSS |  | Index of refraction use to trigger cases of total internal reflections, when the paths are reaching the surface after having travelled under it. Can be used to avoid excessive glow in highly curved regions (corners, creases, ...). |  |
| **sssAnisotropy** | float | 0.0 | Anisotropy | -1.0 | 1.0 |  |  |  | SSS |  | Higher values makes light scatter predominantly forward under the surface, making the object look less diffuse and more transparent. |  |
| **sssBleed** | float | 0.0 | Bleed | 0.0 | 1.0 |  |  |  | SSS |  | Controls the depth of light bleed in the subsurface medium. Has the effect of increasing the distance light travels in the medium while preserving fine detail, compared to increasing the Mean Free Path. |  |
| **sssFollowTopology** | float | 0.0 | Follow Topology | 0.0 | 1.0 |  |  |  | SSS |  | Controls how strongly normals are considered in the subsurface computation. |  |
| **sssSubset** | string |  | Subset |  |  |  |  |  | SSS |  | Specifies trace subset for inclusion/exclusion when struck by a ray indirectly. | true |
| **sssContinuationRays** | integer | 0 | Continuation Rays |  |  |  |  |  | SSS |  | When enabled, ignores internal geometry and jumps to the last surface. |  |
| **sssUnitLength** | float | 0.00328 | Unit Length |  |  |  |  |  | SSS |  | Specifies what unit length the scene is using. It is a multiplier on the mean free path or diffuse mean free path which is expressed in mm. The default value of 0.00328 converts between feet and mm. |  |
| **mode** | integer | 0 | Mode |  |  |  |  |  | Advanced |  | If the subsurface is enabled, Reflection: should be used when both the camera and the light are outside of the object. Reflection(with direct illumination): should be used when both the camera and the light are outside of the object. This mode also computes the direct illumination at the sss ray exit point. Transmission: should be used when the light is inside the object while the camera is outside.  | true |
| **albedoInversionMethod** | integer | 0 | Albedo Inversion Method |  |  |  |  |  | Advanced |  | Decides which albedo inversion methods is used. Pixar: Does the Pixar Path Traced SSS default albedo inversion. Chiang: Does Chiang's albedo inversion (with no dmfp remapping). The look is closer to Arnold Standard Surface randomwalk. |  |
| **diffuseLobeName** | string | diffuse | Diffuse Lobe Name |  |  |  |  |  | Advanced |  | Defines the name that can be used in LPE AOVs for the diffuse lobe (when the SSS radius is null). | true |
| **sssEntryLobeName** | string | irradiance | SSS Entry Lobe Name |  |  |  |  |  | Advanced |  | Defines the name that can be used in LPE AOVs for the SSS Entry lobe. | true |
| **sssExitLobeName** | string |  | SSS Exit Lobe Name |  |  |  |  |  | Advanced |  | Defines the name that can be used in LPE AOVs for the SSS Exit lobe. | true |
| **sssId** | integer | 0 | SSS Id |  |  |  |  |  | Advanced |  | SSS ID | true |
| **matte** | string |  | Matte |  |  |  |  |  | Advanced |  | Defines the name that can be used by the matte system, to output the weight of this lobe in the final material as an AOV. | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *LamaTranslucent*
<details open><summary>ND_lama_translucent</summary>
<p>
 
* *Nodedef*: ND_lama_translucent
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: True
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_lama_translucent


```mermaid
graph TB
    subgraph NG_lama_translucent
    NG_lama_translucent_translucent_bsdf1[translucent_bsdf1]
    style NG_lama_translucent_out  fill:#0C0, color:#FFF
    NG_lama_translucent_out([out])
    style NG_lama_translucent_color  fill:#09D, color:#FFF
    NG_lama_translucent_color([color])
    style NG_lama_translucent_normal  fill:#09D, color:#FFF
    NG_lama_translucent_normal([normal])
    end
    NG_lama_translucent_color --"color"--> NG_lama_translucent_translucent_bsdf1
    NG_lama_translucent_normal --"normal"--> NG_lama_translucent_translucent_bsdf1
    NG_lama_translucent_translucent_bsdf1 --> NG_lama_translucent_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 0.18, 0.18, 0.18 | Color |  |  |  |  |  |  |  | Translucent color (aka albedo), defining what ratio of light is transmitted for each color channel. |  |
| **roughness** | float | 0.0 | Roughness | 0.0 | 1.0 |  |  |  |  |  | Micro-facet distribution (Oren-Nayar) roughness. |  |
| **normal** | vector3 | None | Normal |  |  |  |  |  |  |  | Shading normal, typically defined by bump or normal mapping. Defaults to the smooth surface normal if not set. |  |
| **energyCompensation** | float | 1.0 | Energy Compensation | 0.0 | 1.0 |  |  |  | Advanced |  | Indicates how much energy should be added to compensate for the loss inherent to the Oren-Nayar model, ranging from no compensation at all, to the expected energy from multiple scattering between the micro-facets. This prevents overly dark results when roughness is high. | true |
| **lobeName** | string | diffuse | Lobe Name |  |  |  |  |  | Advanced |  | Defines the name that can be used in LPE AOVs for this lobe. | true |
| **matte** | string |  | Matte |  |  |  |  |  | Advanced |  | Defines the name that can be used by the matte system, to output the weight of this lobe in the final material as an AOV. | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *standard_surface_to_gltf_pbr*
<details open><summary>ND_standard_surface_to_gltf_pbr</summary>
<p>
 
* *Nodedef*: ND_standard_surface_to_gltf_pbr
* *Type*: multioutput
* *Group*: translation
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_standard_surface_to_gltf_pbr


```mermaid
graph TB
    subgraph NG_standard_surface_to_gltf_pbr
    NG_standard_surface_to_gltf_pbr_swizzle[swizzle]
    NG_standard_surface_to_gltf_pbr_has_coat_color[has_coat_color]
    NG_standard_surface_to_gltf_pbr_scaledBaseColor[scaledBaseColor]
    NG_standard_surface_to_gltf_pbr_coatAttenuation[coatAttenuation]
    NG_standard_surface_to_gltf_pbr_mixedBaseColor[mixedBaseColor]
    NG_standard_surface_to_gltf_pbr_constantOneThird[constantOneThird]
    NG_standard_surface_to_gltf_pbr_coatColor[coatColor]
    NG_standard_surface_to_gltf_pbr_swizzle2[swizzle2]
    NG_standard_surface_to_gltf_pbr_swizzle3[swizzle3]
    NG_standard_surface_to_gltf_pbr_weightedCoat[weightedCoat]
    style NG_standard_surface_to_gltf_pbr_base_color  fill:#C72, color:#FFF
    NG_standard_surface_to_gltf_pbr_base_color{base_color}
    NG_standard_surface_to_gltf_pbr_metallic[metallic]
    NG_standard_surface_to_gltf_pbr_roughness[roughness]
    NG_standard_surface_to_gltf_pbr_transmission[transmission]
    NG_standard_surface_to_gltf_pbr_thickness[thickness]
    NG_standard_surface_to_gltf_pbr_attenuation_color[attenuation_color]
    NG_standard_surface_to_gltf_pbr_sheen_color[sheen_color]
    NG_standard_surface_to_gltf_pbr_sheen_roughness[sheen_roughness]
    style NG_standard_surface_to_gltf_pbr_clearcoat  fill:#C72, color:#FFF
    NG_standard_surface_to_gltf_pbr_clearcoat{clearcoat}
    NG_standard_surface_to_gltf_pbr_clearcoat_roughness[clearcoat_roughness]
    NG_standard_surface_to_gltf_pbr_emissive[emissive]
    style NG_standard_surface_to_gltf_pbr_base_color_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_base_color_out([base_color_out])
    style NG_standard_surface_to_gltf_pbr_metallic_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_metallic_out([metallic_out])
    style NG_standard_surface_to_gltf_pbr_roughness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_roughness_out([roughness_out])
    style NG_standard_surface_to_gltf_pbr_transmission_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_transmission_out([transmission_out])
    style NG_standard_surface_to_gltf_pbr_thickness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_thickness_out([thickness_out])
    style NG_standard_surface_to_gltf_pbr_attenuation_color_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_attenuation_color_out([attenuation_color_out])
    style NG_standard_surface_to_gltf_pbr_sheen_color_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_sheen_color_out([sheen_color_out])
    style NG_standard_surface_to_gltf_pbr_sheen_roughness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_sheen_roughness_out([sheen_roughness_out])
    style NG_standard_surface_to_gltf_pbr_clearcoat_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_clearcoat_out([clearcoat_out])
    style NG_standard_surface_to_gltf_pbr_clearcoat_roughness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_clearcoat_roughness_out([clearcoat_roughness_out])
    style NG_standard_surface_to_gltf_pbr_emissive_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_gltf_pbr_emissive_out([emissive_out])
    style NG_standard_surface_to_gltf_pbr_coat_color  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_coat_color([coat_color])
    style NG_standard_surface_to_gltf_pbr_base  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_base([base])
    style NG_standard_surface_to_gltf_pbr_coat  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_coat([coat])
    style NG_standard_surface_to_gltf_pbr_metalness  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_metalness([metalness])
    style NG_standard_surface_to_gltf_pbr_specular_roughness  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_specular_roughness([specular_roughness])
    style NG_standard_surface_to_gltf_pbr_transmission:in  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_transmission:in([transmission:in])
    style NG_standard_surface_to_gltf_pbr_transmission_depth  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_transmission_depth([transmission_depth])
    style NG_standard_surface_to_gltf_pbr_transmission_color  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_transmission_color([transmission_color])
    style NG_standard_surface_to_gltf_pbr_sheen_color:in  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_sheen_color:in([sheen_color:in])
    style NG_standard_surface_to_gltf_pbr_sheen  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_sheen([sheen])
    style NG_standard_surface_to_gltf_pbr_sheen_roughness:in  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_sheen_roughness:in([sheen_roughness:in])
    style NG_standard_surface_to_gltf_pbr_coat_roughness  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_coat_roughness([coat_roughness])
    style NG_standard_surface_to_gltf_pbr_emission_color  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_emission_color([emission_color])
    style NG_standard_surface_to_gltf_pbr_emission  fill:#09D, color:#FFF
    NG_standard_surface_to_gltf_pbr_emission([emission])
    end
    NG_standard_surface_to_gltf_pbr_coat_color --"in"--> NG_standard_surface_to_gltf_pbr_swizzle
    NG_standard_surface_to_gltf_pbr_swizzle --"in1"--> NG_standard_surface_to_gltf_pbr_has_coat_color
    NG_standard_surface_to_gltf_pbr_base_color --"in1"--> NG_standard_surface_to_gltf_pbr_scaledBaseColor
    NG_standard_surface_to_gltf_pbr_base --"in2"--> NG_standard_surface_to_gltf_pbr_scaledBaseColor
    NG_standard_surface_to_gltf_pbr_coat_color --"fg"--> NG_standard_surface_to_gltf_pbr_coatAttenuation
    NG_standard_surface_to_gltf_pbr_coat --"mix"--> NG_standard_surface_to_gltf_pbr_coatAttenuation
    NG_standard_surface_to_gltf_pbr_scaledBaseColor --"in1"--> NG_standard_surface_to_gltf_pbr_mixedBaseColor
    NG_standard_surface_to_gltf_pbr_coatAttenuation --"in2"--> NG_standard_surface_to_gltf_pbr_mixedBaseColor
    NG_standard_surface_to_gltf_pbr_coat_color --"in1"--> NG_standard_surface_to_gltf_pbr_coatColor
    NG_standard_surface_to_gltf_pbr_coat --"in2"--> NG_standard_surface_to_gltf_pbr_coatColor
    NG_standard_surface_to_gltf_pbr_coatColor --"in"--> NG_standard_surface_to_gltf_pbr_swizzle2
    NG_standard_surface_to_gltf_pbr_constantOneThird --"in"--> NG_standard_surface_to_gltf_pbr_swizzle3
    NG_standard_surface_to_gltf_pbr_swizzle2 --"in1"--> NG_standard_surface_to_gltf_pbr_weightedCoat
    NG_standard_surface_to_gltf_pbr_swizzle3 --"in2"--> NG_standard_surface_to_gltf_pbr_weightedCoat
    NG_standard_surface_to_gltf_pbr_has_coat_color --"value1"--> NG_standard_surface_to_gltf_pbr_base_color
    NG_standard_surface_to_gltf_pbr_scaledBaseColor --"in1"--> NG_standard_surface_to_gltf_pbr_base_color
    NG_standard_surface_to_gltf_pbr_mixedBaseColor --"in2"--> NG_standard_surface_to_gltf_pbr_base_color
    NG_standard_surface_to_gltf_pbr_metalness --"in"--> NG_standard_surface_to_gltf_pbr_metallic
    NG_standard_surface_to_gltf_pbr_specular_roughness --"in"--> NG_standard_surface_to_gltf_pbr_roughness
    NG_standard_surface_to_gltf_pbr_transmission:in --"in"--> NG_standard_surface_to_gltf_pbr_transmission
    NG_standard_surface_to_gltf_pbr_transmission_depth --"in"--> NG_standard_surface_to_gltf_pbr_thickness
    NG_standard_surface_to_gltf_pbr_transmission_color --"in"--> NG_standard_surface_to_gltf_pbr_attenuation_color
    NG_standard_surface_to_gltf_pbr_sheen_color:in --"in1"--> NG_standard_surface_to_gltf_pbr_sheen_color
    NG_standard_surface_to_gltf_pbr_sheen --"in2"--> NG_standard_surface_to_gltf_pbr_sheen_color
    NG_standard_surface_to_gltf_pbr_sheen --"value1"--> NG_standard_surface_to_gltf_pbr_sheen_roughness
    NG_standard_surface_to_gltf_pbr_sheen_roughness:in --"in1"--> NG_standard_surface_to_gltf_pbr_sheen_roughness
    NG_standard_surface_to_gltf_pbr_has_coat_color --"value1"--> NG_standard_surface_to_gltf_pbr_clearcoat
    NG_standard_surface_to_gltf_pbr_coat --"in1"--> NG_standard_surface_to_gltf_pbr_clearcoat
    NG_standard_surface_to_gltf_pbr_weightedCoat --"in2"--> NG_standard_surface_to_gltf_pbr_clearcoat
    NG_standard_surface_to_gltf_pbr_coat_roughness --"in"--> NG_standard_surface_to_gltf_pbr_clearcoat_roughness
    NG_standard_surface_to_gltf_pbr_emission_color --"in1"--> NG_standard_surface_to_gltf_pbr_emissive
    NG_standard_surface_to_gltf_pbr_emission --"in2"--> NG_standard_surface_to_gltf_pbr_emissive
    NG_standard_surface_to_gltf_pbr_base_color --> NG_standard_surface_to_gltf_pbr_base_color_out
    NG_standard_surface_to_gltf_pbr_metallic --> NG_standard_surface_to_gltf_pbr_metallic_out
    NG_standard_surface_to_gltf_pbr_roughness --> NG_standard_surface_to_gltf_pbr_roughness_out
    NG_standard_surface_to_gltf_pbr_transmission --> NG_standard_surface_to_gltf_pbr_transmission_out
    NG_standard_surface_to_gltf_pbr_thickness --> NG_standard_surface_to_gltf_pbr_thickness_out
    NG_standard_surface_to_gltf_pbr_attenuation_color --> NG_standard_surface_to_gltf_pbr_attenuation_color_out
    NG_standard_surface_to_gltf_pbr_sheen_color --> NG_standard_surface_to_gltf_pbr_sheen_color_out
    NG_standard_surface_to_gltf_pbr_sheen_roughness --> NG_standard_surface_to_gltf_pbr_sheen_roughness_out
    NG_standard_surface_to_gltf_pbr_clearcoat --> NG_standard_surface_to_gltf_pbr_clearcoat_out
    NG_standard_surface_to_gltf_pbr_clearcoat_roughness --> NG_standard_surface_to_gltf_pbr_clearcoat_roughness_out
    NG_standard_surface_to_gltf_pbr_emissive --> NG_standard_surface_to_gltf_pbr_emissive_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **base** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| **base_color** | color3 | 0.8, 0.8, 0.8 |  |  |  |  |  |  |  |  |  |  |
| **metalness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **specular_roughness** | float | 0.2 |  |  |  |  |  |  |  |  |  |  |
| **transmission** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **transmission_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **transmission_depth** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheen** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **sheen_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **sheen_roughness** | float | 0.3 |  |  |  |  |  |  |  |  |  |  |
| **coat** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **coat_color** | color3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **coat_roughness** | float | 0.1 |  |  |  |  |  |  |  |  |  |  |
| **emission** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **emission_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| *base_color_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *metallic_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *roughness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *transmission_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *thickness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *attenuation_color_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *sheen_color_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *sheen_roughness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *clearcoat_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *clearcoat_roughness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *emissive_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *standard_surface_to_UsdPreviewSurface*
<details open><summary>ND_standard_surface_to_UsdPreviewSurface</summary>
<p>
 
* *Nodedef*: ND_standard_surface_to_UsdPreviewSurface
* *Type*: multioutput
* *Group*: translation
* *Version*: 1.0. Is default: False
* *Doc*: UNDOCUMENTED
* *Nodegraph*: NG_standard_surface_to_UsdPreviewSurface


```mermaid
graph TB
    subgraph NG_standard_surface_to_UsdPreviewSurface
    NG_standard_surface_to_UsdPreviewSurface_constantOneThird[constantOneThird]
    NG_standard_surface_to_UsdPreviewSurface_metallic[metallic]
    NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor[scaledBaseColor]
    NG_standard_surface_to_UsdPreviewSurface_coatAttenuation[coatAttenuation]
    NG_standard_surface_to_UsdPreviewSurface_diffuseColor[diffuseColor]
    NG_standard_surface_to_UsdPreviewSurface_roughness[roughness]
    NG_standard_surface_to_UsdPreviewSurface_ior[ior]
    NG_standard_surface_to_UsdPreviewSurface_coatColor[coatColor]
    NG_standard_surface_to_UsdPreviewSurface_swizzle[swizzle]
    NG_standard_surface_to_UsdPreviewSurface_swizzle2[swizzle2]
    NG_standard_surface_to_UsdPreviewSurface_clearcoat[clearcoat]
    NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness[clearcoatRoughness]
    NG_standard_surface_to_UsdPreviewSurface_emissiveColor[emissiveColor]
    NG_standard_surface_to_UsdPreviewSurface_swizzle3[swizzle3]
    NG_standard_surface_to_UsdPreviewSurface_swizzle4[swizzle4]
    NG_standard_surface_to_UsdPreviewSurface_opacity[opacity]
    NG_standard_surface_to_UsdPreviewSurface_biasNormal[biasNormal]
    NG_standard_surface_to_UsdPreviewSurface_normal[normal]
    style NG_standard_surface_to_UsdPreviewSurface_diffuseColor_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_diffuseColor_out([diffuseColor_out])
    style NG_standard_surface_to_UsdPreviewSurface_emissiveColor_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_emissiveColor_out([emissiveColor_out])
    style NG_standard_surface_to_UsdPreviewSurface_metallic_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_metallic_out([metallic_out])
    style NG_standard_surface_to_UsdPreviewSurface_roughness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_roughness_out([roughness_out])
    style NG_standard_surface_to_UsdPreviewSurface_clearcoat_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_clearcoat_out([clearcoat_out])
    style NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness_out([clearcoatRoughness_out])
    style NG_standard_surface_to_UsdPreviewSurface_opacity_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_opacity_out([opacity_out])
    style NG_standard_surface_to_UsdPreviewSurface_ior_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_ior_out([ior_out])
    style NG_standard_surface_to_UsdPreviewSurface_normal_out  fill:#0C0, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_normal_out([normal_out])
    style NG_standard_surface_to_UsdPreviewSurface_metalness  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_metalness([metalness])
    style NG_standard_surface_to_UsdPreviewSurface_base_color  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_base_color([base_color])
    style NG_standard_surface_to_UsdPreviewSurface_base  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_base([base])
    style NG_standard_surface_to_UsdPreviewSurface_coat_color  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_coat_color([coat_color])
    style NG_standard_surface_to_UsdPreviewSurface_coat  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_coat([coat])
    style NG_standard_surface_to_UsdPreviewSurface_specular_roughness  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_specular_roughness([specular_roughness])
    style NG_standard_surface_to_UsdPreviewSurface_specular_IOR  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_specular_IOR([specular_IOR])
    style NG_standard_surface_to_UsdPreviewSurface_coat_roughness  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_coat_roughness([coat_roughness])
    style NG_standard_surface_to_UsdPreviewSurface_emission_color  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_emission_color([emission_color])
    style NG_standard_surface_to_UsdPreviewSurface_emission  fill:#09D, color:#FFF
    NG_standard_surface_to_UsdPreviewSurface_emission([emission])
    end
    NG_standard_surface_to_UsdPreviewSurface_metalness --"in"--> NG_standard_surface_to_UsdPreviewSurface_metallic
    NG_standard_surface_to_UsdPreviewSurface_base_color --"in1"--> NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor
    NG_standard_surface_to_UsdPreviewSurface_base --"in2"--> NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor
    NG_standard_surface_to_UsdPreviewSurface_coat_color --"fg"--> NG_standard_surface_to_UsdPreviewSurface_coatAttenuation
    NG_standard_surface_to_UsdPreviewSurface_coat --"mix"--> NG_standard_surface_to_UsdPreviewSurface_coatAttenuation
    NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor --"in1"--> NG_standard_surface_to_UsdPreviewSurface_diffuseColor
    NG_standard_surface_to_UsdPreviewSurface_coatAttenuation --"in2"--> NG_standard_surface_to_UsdPreviewSurface_diffuseColor
    NG_standard_surface_to_UsdPreviewSurface_specular_roughness --"in"--> NG_standard_surface_to_UsdPreviewSurface_roughness
    NG_standard_surface_to_UsdPreviewSurface_specular_IOR --"in"--> NG_standard_surface_to_UsdPreviewSurface_ior
    NG_standard_surface_to_UsdPreviewSurface_coat_color --"in1"--> NG_standard_surface_to_UsdPreviewSurface_coatColor
    NG_standard_surface_to_UsdPreviewSurface_coat --"in2"--> NG_standard_surface_to_UsdPreviewSurface_coatColor
    NG_standard_surface_to_UsdPreviewSurface_coatColor --"in"--> NG_standard_surface_to_UsdPreviewSurface_swizzle
    NG_standard_surface_to_UsdPreviewSurface_constantOneThird --"in"--> NG_standard_surface_to_UsdPreviewSurface_swizzle2
    NG_standard_surface_to_UsdPreviewSurface_swizzle --"in1"--> NG_standard_surface_to_UsdPreviewSurface_clearcoat
    NG_standard_surface_to_UsdPreviewSurface_swizzle2 --"in2"--> NG_standard_surface_to_UsdPreviewSurface_clearcoat
    NG_standard_surface_to_UsdPreviewSurface_coat_roughness --"in"--> NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness
    NG_standard_surface_to_UsdPreviewSurface_emission_color --"in1"--> NG_standard_surface_to_UsdPreviewSurface_emissiveColor
    NG_standard_surface_to_UsdPreviewSurface_emission --"in2"--> NG_standard_surface_to_UsdPreviewSurface_emissiveColor
    NG_standard_surface_to_UsdPreviewSurface_opacity --"in"--> NG_standard_surface_to_UsdPreviewSurface_swizzle3
    NG_standard_surface_to_UsdPreviewSurface_constantOneThird --"in"--> NG_standard_surface_to_UsdPreviewSurface_swizzle4
    NG_standard_surface_to_UsdPreviewSurface_swizzle3 --"in1"--> NG_standard_surface_to_UsdPreviewSurface_opacity
    NG_standard_surface_to_UsdPreviewSurface_swizzle4 --"in2"--> NG_standard_surface_to_UsdPreviewSurface_opacity
    NG_standard_surface_to_UsdPreviewSurface_normal --"in1"--> NG_standard_surface_to_UsdPreviewSurface_biasNormal
    NG_standard_surface_to_UsdPreviewSurface_biasNormal --"in1"--> NG_standard_surface_to_UsdPreviewSurface_normal
    NG_standard_surface_to_UsdPreviewSurface_diffuseColor --> NG_standard_surface_to_UsdPreviewSurface_diffuseColor_out
    NG_standard_surface_to_UsdPreviewSurface_emissiveColor --> NG_standard_surface_to_UsdPreviewSurface_emissiveColor_out
    NG_standard_surface_to_UsdPreviewSurface_metallic --> NG_standard_surface_to_UsdPreviewSurface_metallic_out
    NG_standard_surface_to_UsdPreviewSurface_roughness --> NG_standard_surface_to_UsdPreviewSurface_roughness_out
    NG_standard_surface_to_UsdPreviewSurface_clearcoat --> NG_standard_surface_to_UsdPreviewSurface_clearcoat_out
    NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness --> NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness_out
    NG_standard_surface_to_UsdPreviewSurface_opacity --> NG_standard_surface_to_UsdPreviewSurface_opacity_out
    NG_standard_surface_to_UsdPreviewSurface_ior --> NG_standard_surface_to_UsdPreviewSurface_ior_out
    NG_standard_surface_to_UsdPreviewSurface_normal --> NG_standard_surface_to_UsdPreviewSurface_normal_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **metalness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **base** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| **base_color** | color3 | 0.8, 0.8, 0.8 |  |  |  |  |  |  |  |  |  |  |
| **specular** | float | 1.0 |  |  |  |  |  |  |  |  |  |  |
| **specular_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **specular_IOR** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **specular_roughness** | float | 0.2 |  |  |  |  |  |  |  |  |  |  |
| **coat** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **coat_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **coat_roughness** | float | 0.1 |  |  |  |  |  |  |  |  |  |  |
| **emission** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **emission_color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **opacity** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | 0.5, 0.5, 1 |  |  |  |  |  |  |  |  |  |  |
| *diffuseColor_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *emissiveColor_out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *metallic_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *roughness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *clearcoat_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *clearcoatRoughness_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *opacity_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *ior_out* | float | None |  |  |  |  |  |  |  |  |  |  |
| *normal_out* | vector3 | None |  |  |  |  |  |  |  |  |  |  |
</p></details>
 
