```mermaid
graph LR; 
    NG_standard_surface_to_UsdPreviewSurface_diffuseColor[multiply] --> NG_standard_surface_to_UsdPreviewSurface_diffuseColor_out([diffuseColor_out])
    style NG_standard_surface_to_UsdPreviewSurface_diffuseColor_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor[multiply] --".in1"--> NG_standard_surface_to_UsdPreviewSurface_diffuseColor[multiply]
    NG_standard_surface_to_UsdPreviewSurface_base_colorINT([base_color]) ==.in1==> NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_base_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_baseINT([base]) ==.in2==> NG_standard_surface_to_UsdPreviewSurface_scaledBaseColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_baseINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_coatAttenuation[mix] --".in2"--> NG_standard_surface_to_UsdPreviewSurface_diffuseColor[multiply]
    NG_standard_surface_to_UsdPreviewSurface_coat_colorINT([coat_color]) ==.fg==> NG_standard_surface_to_UsdPreviewSurface_coatAttenuation[mix]
    style NG_standard_surface_to_UsdPreviewSurface_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_coatINT([coat]) ==.mix==> NG_standard_surface_to_UsdPreviewSurface_coatAttenuation[mix]
    style NG_standard_surface_to_UsdPreviewSurface_coatINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_emissiveColor[multiply] --> NG_standard_surface_to_UsdPreviewSurface_emissiveColor_out([emissiveColor_out])
    style NG_standard_surface_to_UsdPreviewSurface_emissiveColor_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_emission_colorINT([emission_color]) ==.in1==> NG_standard_surface_to_UsdPreviewSurface_emissiveColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_emission_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_emissionINT([emission]) ==.in2==> NG_standard_surface_to_UsdPreviewSurface_emissiveColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_emissionINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_metallic[dot] --> NG_standard_surface_to_UsdPreviewSurface_metallic_out([metallic_out])
    style NG_standard_surface_to_UsdPreviewSurface_metallic_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_metalnessINT([metalness]) ==.in==> NG_standard_surface_to_UsdPreviewSurface_metallic[dot]
    style NG_standard_surface_to_UsdPreviewSurface_metalnessINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_roughness[dot] --> NG_standard_surface_to_UsdPreviewSurface_roughness_out([roughness_out])
    style NG_standard_surface_to_UsdPreviewSurface_roughness_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_specular_roughnessINT([specular_roughness]) ==.in==> NG_standard_surface_to_UsdPreviewSurface_roughness[dot]
    style NG_standard_surface_to_UsdPreviewSurface_specular_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_clearcoat[dotproduct] --> NG_standard_surface_to_UsdPreviewSurface_clearcoat_out([clearcoat_out])
    style NG_standard_surface_to_UsdPreviewSurface_clearcoat_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_coatColor[multiply] --".rgb -> .in1"--> NG_standard_surface_to_UsdPreviewSurface_clearcoat[dotproduct]
    NG_standard_surface_to_UsdPreviewSurface_coat_colorINT([coat_color]) ==.in1==> NG_standard_surface_to_UsdPreviewSurface_coatColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_coatINT([coat]) ==.in2==> NG_standard_surface_to_UsdPreviewSurface_coatColor[multiply]
    style NG_standard_surface_to_UsdPreviewSurface_coatINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_constantOneThird[divide] --".xxx -> .in2"--> NG_standard_surface_to_UsdPreviewSurface_clearcoat[dotproduct]
    NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness[dot] --> NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness_out([clearcoatRoughness_out])
    style NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_coat_roughnessINT([coat_roughness]) ==.in==> NG_standard_surface_to_UsdPreviewSurface_clearcoatRoughness[dot]
    style NG_standard_surface_to_UsdPreviewSurface_coat_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_opacity[dotproduct] --> NG_standard_surface_to_UsdPreviewSurface_opacity_out([opacity_out])
    style NG_standard_surface_to_UsdPreviewSurface_opacity_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_opacityINT([opacity]) ==.in1==> NG_standard_surface_to_UsdPreviewSurface_opacity[dotproduct]
    style NG_standard_surface_to_UsdPreviewSurface_opacityINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_constantOneThird[divide] --".xxx -> .in2"--> NG_standard_surface_to_UsdPreviewSurface_opacity[dotproduct]
    NG_standard_surface_to_UsdPreviewSurface_ior[dot] --> NG_standard_surface_to_UsdPreviewSurface_ior_out([ior_out])
    style NG_standard_surface_to_UsdPreviewSurface_ior_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_specular_IORINT([specular_IOR]) ==.in==> NG_standard_surface_to_UsdPreviewSurface_ior[dot]
    style NG_standard_surface_to_UsdPreviewSurface_specular_IORINT fill:#0bb, color:#111
    NG_standard_surface_to_UsdPreviewSurface_normal[multiply] --> NG_standard_surface_to_UsdPreviewSurface_normal_out([normal_out])
    style NG_standard_surface_to_UsdPreviewSurface_normal_out fill:#1b1, color:#111
    NG_standard_surface_to_UsdPreviewSurface_biasNormal[subtract] --".in1"--> NG_standard_surface_to_UsdPreviewSurface_normal[multiply]
    NG_standard_surface_to_UsdPreviewSurface_normalINT([normal]) ==.in1==> NG_standard_surface_to_UsdPreviewSurface_biasNormal[subtract]
    style NG_standard_surface_to_UsdPreviewSurface_normalINT fill:#0bb, color:#111
```
