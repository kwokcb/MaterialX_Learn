```mermaid
graph LR; 
    NG_standard_surface_to_gltf_pbr_base_color{ifequal} --> NG_standard_surface_to_gltf_pbr_base_color_out([base_color_out])
    style NG_standard_surface_to_gltf_pbr_base_color_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_has_coat_color[dotproduct] --".value1"--> NG_standard_surface_to_gltf_pbr_base_color{ifequal}
    NG_standard_surface_to_gltf_pbr_coat_colorINT([coat_color]) ==.in1==> NG_standard_surface_to_gltf_pbr_has_coat_color[dotproduct]
    style NG_standard_surface_to_gltf_pbr_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_scaledBaseColor[multiply] --".in1"--> NG_standard_surface_to_gltf_pbr_base_color{ifequal}
    NG_standard_surface_to_gltf_pbr_base_colorINT([base_color]) ==.in1==> NG_standard_surface_to_gltf_pbr_scaledBaseColor[multiply]
    style NG_standard_surface_to_gltf_pbr_base_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_baseINT([base]) ==.in2==> NG_standard_surface_to_gltf_pbr_scaledBaseColor[multiply]
    style NG_standard_surface_to_gltf_pbr_baseINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_mixedBaseColor[multiply] --".in2"--> NG_standard_surface_to_gltf_pbr_base_color{ifequal}
    NG_standard_surface_to_gltf_pbr_scaledBaseColor[multiply] --".in1"--> NG_standard_surface_to_gltf_pbr_mixedBaseColor[multiply]
    NG_standard_surface_to_gltf_pbr_coatAttenuation[mix] --".in2"--> NG_standard_surface_to_gltf_pbr_mixedBaseColor[multiply]
    NG_standard_surface_to_gltf_pbr_coat_colorINT([coat_color]) ==.fg==> NG_standard_surface_to_gltf_pbr_coatAttenuation[mix]
    style NG_standard_surface_to_gltf_pbr_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_coatINT([coat]) ==.mix==> NG_standard_surface_to_gltf_pbr_coatAttenuation[mix]
    style NG_standard_surface_to_gltf_pbr_coatINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_metallic[dot] --> NG_standard_surface_to_gltf_pbr_metallic_out([metallic_out])
    style NG_standard_surface_to_gltf_pbr_metallic_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_metalnessINT([metalness]) ==.in==> NG_standard_surface_to_gltf_pbr_metallic[dot]
    style NG_standard_surface_to_gltf_pbr_metalnessINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_roughness[dot] --> NG_standard_surface_to_gltf_pbr_roughness_out([roughness_out])
    style NG_standard_surface_to_gltf_pbr_roughness_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_specular_roughnessINT([specular_roughness]) ==.in==> NG_standard_surface_to_gltf_pbr_roughness[dot]
    style NG_standard_surface_to_gltf_pbr_specular_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_transmission[dot] --> NG_standard_surface_to_gltf_pbr_transmission_out([transmission_out])
    style NG_standard_surface_to_gltf_pbr_transmission_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_transmissionINT([transmission]) ==.in==> NG_standard_surface_to_gltf_pbr_transmission[dot]
    style NG_standard_surface_to_gltf_pbr_transmissionINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_thickness[dot] --> NG_standard_surface_to_gltf_pbr_thickness_out([thickness_out])
    style NG_standard_surface_to_gltf_pbr_thickness_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_transmission_depthINT([transmission_depth]) ==.in==> NG_standard_surface_to_gltf_pbr_thickness[dot]
    style NG_standard_surface_to_gltf_pbr_transmission_depthINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_attenuation_color[dot] --> NG_standard_surface_to_gltf_pbr_attenuation_color_out([attenuation_color_out])
    style NG_standard_surface_to_gltf_pbr_attenuation_color_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_transmission_colorINT([transmission_color]) ==.in==> NG_standard_surface_to_gltf_pbr_attenuation_color[dot]
    style NG_standard_surface_to_gltf_pbr_transmission_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_sheen_color[multiply] --> NG_standard_surface_to_gltf_pbr_sheen_color_out([sheen_color_out])
    style NG_standard_surface_to_gltf_pbr_sheen_color_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_sheen_colorINT([sheen_color]) ==.in1==> NG_standard_surface_to_gltf_pbr_sheen_color[multiply]
    style NG_standard_surface_to_gltf_pbr_sheen_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_sheenINT([sheen]) ==.in2==> NG_standard_surface_to_gltf_pbr_sheen_color[multiply]
    style NG_standard_surface_to_gltf_pbr_sheenINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_sheen_roughness{ifgreater} --> NG_standard_surface_to_gltf_pbr_sheen_roughness_out([sheen_roughness_out])
    style NG_standard_surface_to_gltf_pbr_sheen_roughness_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_sheenINT([sheen]) ==.value1==> NG_standard_surface_to_gltf_pbr_sheen_roughness[ifgreater]
    style NG_standard_surface_to_gltf_pbr_sheenINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_sheen_roughnessINT([sheen_roughness]) ==.in1==> NG_standard_surface_to_gltf_pbr_sheen_roughness[ifgreater]
    style NG_standard_surface_to_gltf_pbr_sheen_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_clearcoat{ifequal} --> NG_standard_surface_to_gltf_pbr_clearcoat_out([clearcoat_out])
    style NG_standard_surface_to_gltf_pbr_clearcoat_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_coatINT([coat]) ==.in1==> NG_standard_surface_to_gltf_pbr_clearcoat[ifequal]
    style NG_standard_surface_to_gltf_pbr_coatINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_has_coat_color[dotproduct] --".value1"--> NG_standard_surface_to_gltf_pbr_clearcoat{ifequal}
    NG_standard_surface_to_gltf_pbr_weightedCoat[dotproduct] --".in2"--> NG_standard_surface_to_gltf_pbr_clearcoat{ifequal}
    NG_standard_surface_to_gltf_pbr_coatColor[multiply] --".rgb -> .in1"--> NG_standard_surface_to_gltf_pbr_weightedCoat[dotproduct]
    NG_standard_surface_to_gltf_pbr_coat_colorINT([coat_color]) ==.in1==> NG_standard_surface_to_gltf_pbr_coatColor[multiply]
    style NG_standard_surface_to_gltf_pbr_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_coatINT([coat]) ==.in2==> NG_standard_surface_to_gltf_pbr_coatColor[multiply]
    style NG_standard_surface_to_gltf_pbr_coatINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_constantOneThird[divide] --".xxx -> .in2"--> NG_standard_surface_to_gltf_pbr_weightedCoat[dotproduct]
    NG_standard_surface_to_gltf_pbr_clearcoat_roughness[dot] --> NG_standard_surface_to_gltf_pbr_clearcoat_roughness_out([clearcoat_roughness_out])
    style NG_standard_surface_to_gltf_pbr_clearcoat_roughness_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_coat_roughnessINT([coat_roughness]) ==.in==> NG_standard_surface_to_gltf_pbr_clearcoat_roughness[dot]
    style NG_standard_surface_to_gltf_pbr_coat_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_emissive[multiply] --> NG_standard_surface_to_gltf_pbr_emissive_out([emissive_out])
    style NG_standard_surface_to_gltf_pbr_emissive_out fill:#1b1, color:#111
    NG_standard_surface_to_gltf_pbr_emission_colorINT([emission_color]) ==.in1==> NG_standard_surface_to_gltf_pbr_emissive[multiply]
    style NG_standard_surface_to_gltf_pbr_emission_colorINT fill:#0bb, color:#111
    NG_standard_surface_to_gltf_pbr_emissionINT([emission]) ==.in2==> NG_standard_surface_to_gltf_pbr_emissive[multiply]
    style NG_standard_surface_to_gltf_pbr_emissionINT fill:#0bb, color:#111
```
