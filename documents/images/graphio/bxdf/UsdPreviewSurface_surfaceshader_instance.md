```mermaid
graph LR; 
    IMP_UsdPreviewSurface_surfaceshader_surface_constructor[surface] --> IMP_UsdPreviewSurface_surfaceshader_out([out])
    style IMP_UsdPreviewSurface_surfaceshader_out fill:#1b1, color:#111
    IMP_UsdPreviewSurface_surfaceshader_coat_bsdf[layer] --".bsdf"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor[surface]
    IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[generalized_schlick_bsdf] --".top"--> IMP_UsdPreviewSurface_surfaceshader_coat_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_clearcoatINT([clearcoat]) ==.weight==> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[generalized_schlick_bsdf]
    style IMP_UsdPreviewSurface_surfaceshader_clearcoatINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_coat_F0[convert] --".color0"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_R_sq[multiply] --".in"--> IMP_UsdPreviewSurface_surfaceshader_coat_F0[convert]
    IMP_UsdPreviewSurface_surfaceshader_R[divide] --".in1"--> IMP_UsdPreviewSurface_surfaceshader_R_sq[multiply]
    IMP_UsdPreviewSurface_surfaceshader_one_minus_ior[subtract] --".in1"--> IMP_UsdPreviewSurface_surfaceshader_R[divide]
    IMP_UsdPreviewSurface_surfaceshader_iorINT([ior]) ==.in2==> IMP_UsdPreviewSurface_surfaceshader_one_minus_ior[subtract]
    style IMP_UsdPreviewSurface_surfaceshader_iorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_one_plus_ior[add] --".in2"--> IMP_UsdPreviewSurface_surfaceshader_R[divide]
    IMP_UsdPreviewSurface_surfaceshader_iorINT([ior]) ==.in2==> IMP_UsdPreviewSurface_surfaceshader_one_plus_ior[add]
    style IMP_UsdPreviewSurface_surfaceshader_iorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_R[divide] --".in2"--> IMP_UsdPreviewSurface_surfaceshader_R_sq[multiply]
    IMP_UsdPreviewSurface_surfaceshader_coat_roughness[roughness_anisotropy] --".roughness"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_clearcoatRoughnessINT([clearcoatRoughness]) ==.roughness==> IMP_UsdPreviewSurface_surfaceshader_coat_roughness[roughness_anisotropy]
    style IMP_UsdPreviewSurface_surfaceshader_clearcoatRoughnessINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_coat_dielectric_bsdf[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_bias_normal[add] --".in"--> IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap]
    IMP_UsdPreviewSurface_surfaceshader_scale_normal[multiply] --".in1"--> IMP_UsdPreviewSurface_surfaceshader_bias_normal[add]
    IMP_UsdPreviewSurface_surfaceshader_normalINT([normal]) ==.in1==> IMP_UsdPreviewSurface_surfaceshader_scale_normal[multiply]
    style IMP_UsdPreviewSurface_surfaceshader_normalINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf[mix] --".base"--> IMP_UsdPreviewSurface_surfaceshader_coat_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf[layer] --".fg"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf[mix]
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1[generalized_schlick_bsdf] --".top"--> IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_specularColorINT([specularColor]) ==.color0==> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1[generalized_schlick_bsdf]
    style IMP_UsdPreviewSurface_surfaceshader_specularColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness[roughness_anisotropy] --".roughness"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_roughnessINT([roughness]) ==.roughness==> IMP_UsdPreviewSurface_surfaceshader_specular_roughness[roughness_anisotropy]
    style IMP_UsdPreviewSurface_surfaceshader_roughnessINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf1[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_transmission_mix[mix] --".base"--> IMP_UsdPreviewSurface_surfaceshader_specular_workflow_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_opacityINT([opacity]) ==.mix==> IMP_UsdPreviewSurface_surfaceshader_transmission_mix[mix]
    style IMP_UsdPreviewSurface_surfaceshader_opacityINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf] --".fg"--> IMP_UsdPreviewSurface_surfaceshader_transmission_mix[mix]
    IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT([diffuseColor]) ==.color==> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight[mix] --".weight"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_inverse_metalness[subtract] --".bg"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight[mix]
    IMP_UsdPreviewSurface_surfaceshader_metallicINT([metallic]) ==.in2==> IMP_UsdPreviewSurface_surfaceshader_inverse_metalness[subtract]
    style IMP_UsdPreviewSurface_surfaceshader_metallicINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float[convert] --".mix"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf_weight[mix]
    IMP_UsdPreviewSurface_surfaceshader_useSpecularWorkflowINT([useSpecularWorkflow]) ==.in==> IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float[convert]
    style IMP_UsdPreviewSurface_surfaceshader_useSpecularWorkflowINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf[dielectric_bsdf] --".bg"--> IMP_UsdPreviewSurface_surfaceshader_transmission_mix[mix]
    IMP_UsdPreviewSurface_surfaceshader_iorINT([ior]) ==.ior==> IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf[dielectric_bsdf]
    style IMP_UsdPreviewSurface_surfaceshader_iorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_transmission_bsdf[dielectric_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf[mix] --".bg"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf[mix]
    IMP_UsdPreviewSurface_surfaceshader_metallicINT([metallic]) ==.mix==> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf[mix]
    style IMP_UsdPreviewSurface_surfaceshader_metallicINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[conductor_bsdf] --".fg"--> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf[mix]
    IMP_UsdPreviewSurface_surfaceshader_artistic_ior[artistic_ior] --> IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorior([ior])
    style IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorior fill:#1b1, color:#111
    IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorior --".ior"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[conductor_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT([diffuseColor]) ==.reflectivity==> IMP_UsdPreviewSurface_surfaceshader_artistic_ior[artistic_ior]
    style IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT([diffuseColor]) ==.edge_color==> IMP_UsdPreviewSurface_surfaceshader_artistic_ior[artistic_ior]
    style IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_artistic_ior[artistic_ior] --> IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorextinction([extinction])
    style IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorextinction fill:#1b1, color:#111
    IMP_UsdPreviewSurface_surfaceshader_IMP_UsdPreviewSurface_surfaceshader_artistic_iorextinction --".extinction"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[conductor_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness[roughness_anisotropy] --".roughness"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[conductor_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_metalness_metal_bsdf[conductor_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf[layer] --".bg"--> IMP_UsdPreviewSurface_surfaceshader_metalness_workflow_bsdf[mix]
    IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[generalized_schlick_bsdf] --".top"--> IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_F0[mix] --".color0"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_metallicINT([metallic]) ==.mix==> IMP_UsdPreviewSurface_surfaceshader_F0[mix]
    style IMP_UsdPreviewSurface_surfaceshader_metallicINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[mix] --".fg"--> IMP_UsdPreviewSurface_surfaceshader_F0[mix]
    IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT([diffuseColor]) ==.fg==> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[mix]
    style IMP_UsdPreviewSurface_surfaceshader_diffuseColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_metallicINT([metallic]) ==.mix==> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[mix]
    style IMP_UsdPreviewSurface_surfaceshader_metallicINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq[multiply] --".bg"--> IMP_UsdPreviewSurface_surfaceshader_F0[mix]
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[mix] --".in1"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq[multiply]
    IMP_UsdPreviewSurface_surfaceshader_R_sq[multiply] --".in2"--> IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic_R_sq[multiply]
    IMP_UsdPreviewSurface_surfaceshader_specular_color_metallic[mix] --".color90"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_specular_roughness[roughness_anisotropy] --".roughness"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_surface_normal[normalmap] --".normal"--> IMP_UsdPreviewSurface_surfaceshader_specular_bsdf2[generalized_schlick_bsdf]
    IMP_UsdPreviewSurface_surfaceshader_transmission_mix[mix] --".base"--> IMP_UsdPreviewSurface_surfaceshader_metalness_specular_bsdf[layer]
    IMP_UsdPreviewSurface_surfaceshader_use_specular_workflow_float[convert] --".mix"--> IMP_UsdPreviewSurface_surfaceshader_workflow_selector_bsdf[mix]
    IMP_UsdPreviewSurface_surfaceshader_emission_edf[uniform_edf] --".edf"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor[surface]
    IMP_UsdPreviewSurface_surfaceshader_emissiveColorINT([emissiveColor]) ==.color==> IMP_UsdPreviewSurface_surfaceshader_emission_edf[uniform_edf]
    style IMP_UsdPreviewSurface_surfaceshader_emissiveColorINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_cutout_opacity{ifgreatereq} --".opacity"--> IMP_UsdPreviewSurface_surfaceshader_surface_constructor[surface]
    IMP_UsdPreviewSurface_surfaceshader_opacityThresholdINT([opacityThreshold]) ==.value2==> IMP_UsdPreviewSurface_surfaceshader_cutout_opacity[ifgreatereq]
    style IMP_UsdPreviewSurface_surfaceshader_opacityThresholdINT fill:#0bb, color:#111
    IMP_UsdPreviewSurface_surfaceshader_opacity_clamped[clamp] --".value1"--> IMP_UsdPreviewSurface_surfaceshader_cutout_opacity{ifgreatereq}
    IMP_UsdPreviewSurface_surfaceshader_opacityINT([opacity]) ==.in==> IMP_UsdPreviewSurface_surfaceshader_opacity_clamped[clamp]
    style IMP_UsdPreviewSurface_surfaceshader_opacityINT fill:#0bb, color:#111
```
