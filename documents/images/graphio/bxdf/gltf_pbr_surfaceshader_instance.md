```mermaid
graph LR; 
    IMPL_gltf_pbr_surfaceshader_shader_constructor[surface] --> IMPL_gltf_pbr_surfaceshader_out([out])
    style IMPL_gltf_pbr_surfaceshader_out fill:#1b1, color:#111
    IMPL_gltf_pbr_surfaceshader_clearcoat_layer[layer] --".bsdf"--> IMPL_gltf_pbr_surfaceshader_shader_constructor[surface]
    IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[dielectric_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_clearcoat_layer[layer]
    IMPL_gltf_pbr_surfaceshader_clearcoatINT([clearcoat]) ==.weight==> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_clearcoatINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_clearcoat_normalINT([clearcoat_normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_clearcoat_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_clearcoat_bsdf[dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_clearcoat_roughnessINT([clearcoat_roughness]) ==.roughness==> IMPL_gltf_pbr_surfaceshader_clearcoat_roughness_uv[roughness_anisotropy]
    style IMPL_gltf_pbr_surfaceshader_clearcoat_roughnessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_layer[layer] --".base"--> IMPL_gltf_pbr_surfaceshader_clearcoat_layer[layer]
    IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_sheen_layer[layer]
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_intensity[max] --".weight"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf]
    IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg[max] --".in1"--> IMPL_gltf_pbr_surfaceshader_sheen_intensity[max]
    IMPL_gltf_pbr_surfaceshader_sheen_color_r[extract] --".in1"--> IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg[max]
    IMPL_gltf_pbr_surfaceshader_sheen_colorINT([sheen_color]) ==.in==> IMPL_gltf_pbr_surfaceshader_sheen_color_r[extract]
    style IMPL_gltf_pbr_surfaceshader_sheen_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_color_g[extract] --".in2"--> IMPL_gltf_pbr_surfaceshader_sheen_color_max_rg[max]
    IMPL_gltf_pbr_surfaceshader_sheen_colorINT([sheen_color]) ==.in==> IMPL_gltf_pbr_surfaceshader_sheen_color_g[extract]
    style IMPL_gltf_pbr_surfaceshader_sheen_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_color_b[extract] --".in2"--> IMPL_gltf_pbr_surfaceshader_sheen_intensity[max]
    IMPL_gltf_pbr_surfaceshader_sheen_colorINT([sheen_color]) ==.in==> IMPL_gltf_pbr_surfaceshader_sheen_color_b[extract]
    style IMPL_gltf_pbr_surfaceshader_sheen_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_color_normalized[divide] --".color"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf]
    IMPL_gltf_pbr_surfaceshader_sheen_colorINT([sheen_color]) ==.in1==> IMPL_gltf_pbr_surfaceshader_sheen_color_normalized[divide]
    style IMPL_gltf_pbr_surfaceshader_sheen_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_intensity[max] --".in2"--> IMPL_gltf_pbr_surfaceshader_sheen_color_normalized[divide]
    IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq[multiply] --".roughness"--> IMPL_gltf_pbr_surfaceshader_sheen_bsdf[sheen_bsdf]
    IMPL_gltf_pbr_surfaceshader_sheen_roughnessINT([sheen_roughness]) ==.in1==> IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq[multiply]
    style IMPL_gltf_pbr_surfaceshader_sheen_roughnessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_sheen_roughnessINT([sheen_roughness]) ==.in2==> IMPL_gltf_pbr_surfaceshader_sheen_roughness_sq[multiply]
    style IMPL_gltf_pbr_surfaceshader_sheen_roughnessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_base_mix[mix] --".base"--> IMPL_gltf_pbr_surfaceshader_sheen_layer[layer]
    IMPL_gltf_pbr_surfaceshader_metallicINT([metallic]) ==.mix==> IMPL_gltf_pbr_surfaceshader_base_mix[mix]
    style IMPL_gltf_pbr_surfaceshader_metallicINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf[mix] --".bg"--> IMPL_gltf_pbr_surfaceshader_base_mix[mix]
    IMPL_gltf_pbr_surfaceshader_iridescenceINT([iridescence]) ==.mix==> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf[mix]
    style IMPL_gltf_pbr_surfaceshader_iridescenceINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_dielectric_bsdf[layer] --".bg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf[mix]
    IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_dielectric_f0[multiply] --".color0"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_specularINT([specular]) ==.in2==> IMPL_gltf_pbr_surfaceshader_dielectric_f0[multiply]
    style IMPL_gltf_pbr_surfaceshader_specularINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_clamped_dielectric_f0_from_ior_specular_color[min] --".in1"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0[multiply]
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color[multiply] --".in1"--> IMPL_gltf_pbr_surfaceshader_clamped_dielectric_f0_from_ior_specular_color[min]
    IMPL_gltf_pbr_surfaceshader_specular_colorINT([specular_color]) ==.in1==> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color[multiply]
    style IMPL_gltf_pbr_surfaceshader_specular_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior[multiply] --".in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior_specular_color[multiply]
    IMPL_gltf_pbr_surfaceshader_ior_div[divide] --".in1"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior[multiply]
    IMPL_gltf_pbr_surfaceshader_one_minus_ior[subtract] --".in1"--> IMPL_gltf_pbr_surfaceshader_ior_div[divide]
    IMPL_gltf_pbr_surfaceshader_iorINT([ior]) ==.in2==> IMPL_gltf_pbr_surfaceshader_one_minus_ior[subtract]
    style IMPL_gltf_pbr_surfaceshader_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_one_plus_ior[add] --".in2"--> IMPL_gltf_pbr_surfaceshader_ior_div[divide]
    IMPL_gltf_pbr_surfaceshader_iorINT([ior]) ==.in2==> IMPL_gltf_pbr_surfaceshader_one_plus_ior[add]
    style IMPL_gltf_pbr_surfaceshader_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_ior_div[divide] --".in2"--> IMPL_gltf_pbr_surfaceshader_dielectric_f0_from_ior[multiply]
    IMPL_gltf_pbr_surfaceshader_dielectric_f90[multiply] --".color90"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_specularINT([specular]) ==.in2==> IMPL_gltf_pbr_surfaceshader_dielectric_f90[multiply]
    style IMPL_gltf_pbr_surfaceshader_specularINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_roughnessINT([roughness]) ==.roughness==> IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy]
    style IMPL_gltf_pbr_surfaceshader_roughnessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_transmission_mix[mix] --".base"--> IMPL_gltf_pbr_surfaceshader_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_transmissionINT([transmission]) ==.mix==> IMPL_gltf_pbr_surfaceshader_transmission_mix[mix]
    style IMPL_gltf_pbr_surfaceshader_transmissionINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf] --".bg"--> IMPL_gltf_pbr_surfaceshader_transmission_mix[mix]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.color==> IMPL_gltf_pbr_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf] --".fg"--> IMPL_gltf_pbr_surfaceshader_transmission_mix[mix]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.tint==> IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_iorINT([ior]) ==.ior==> IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_transmission_bsdf[dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_iridescent_dielectric_bsdf[layer] --".fg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_dielectric_bsdf[mix]
    IMPL_gltf_pbr_surfaceshader_dielectric_thinfilm_bsdf[thin_film_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_iridescent_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_iridescence_thicknessINT([iridescence_thickness]) ==.thickness==> IMPL_gltf_pbr_surfaceshader_dielectric_thinfilm_bsdf[thin_film_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iridescence_thicknessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_iridescence_iorINT([iridescence_ior]) ==.ior==> IMPL_gltf_pbr_surfaceshader_dielectric_thinfilm_bsdf[thin_film_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iridescence_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf[layer] --".base"--> IMPL_gltf_pbr_surfaceshader_iridescent_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_dielectric_f0[multiply] --".color0"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_dielectric_f90[multiply] --".color90"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_tf_reflection_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_tf_transmission_mix[mix] --".base"--> IMPL_gltf_pbr_surfaceshader_tf_dielectric_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_transmissionINT([transmission]) ==.mix==> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix[mix]
    style IMPL_gltf_pbr_surfaceshader_transmissionINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tf_diffuse_bsdf[oren_nayar_diffuse_bsdf] --".bg"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix[mix]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.color==> IMPL_gltf_pbr_surfaceshader_tf_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_tf_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf] --".fg"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_mix[mix]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.tint==> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_iorINT([ior]) ==.ior==> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_tf_transmission_bsdf[dielectric_bsdf]
    IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf[mix] --".fg"--> IMPL_gltf_pbr_surfaceshader_base_mix[mix]
    IMPL_gltf_pbr_surfaceshader_iridescenceINT([iridescence]) ==.mix==> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf[mix]
    style IMPL_gltf_pbr_surfaceshader_iridescenceINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_metal_bsdf[generalized_schlick_bsdf] --".bg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf[mix]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.color0==> IMPL_gltf_pbr_surfaceshader_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_metal_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_iridescent_metal_bsdf[layer] --".fg"--> IMPL_gltf_pbr_surfaceshader_mix_iridescent_metal_bsdf[mix]
    IMPL_gltf_pbr_surfaceshader_metal_thinfilm_bsdf[thin_film_bsdf] --".top"--> IMPL_gltf_pbr_surfaceshader_iridescent_metal_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_iridescence_thicknessINT([iridescence_thickness]) ==.thickness==> IMPL_gltf_pbr_surfaceshader_metal_thinfilm_bsdf[thin_film_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iridescence_thicknessINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_iridescence_iorINT([iridescence_ior]) ==.ior==> IMPL_gltf_pbr_surfaceshader_metal_thinfilm_bsdf[thin_film_bsdf]
    style IMPL_gltf_pbr_surfaceshader_iridescence_iorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[generalized_schlick_bsdf] --".base"--> IMPL_gltf_pbr_surfaceshader_iridescent_metal_bsdf[layer]
    IMPL_gltf_pbr_surfaceshader_base_colorINT([base_color]) ==.color0==> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_base_colorINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_normalINT([normal]) ==.normal==> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_normalINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_tangentINT([tangent]) ==.tangent==> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[generalized_schlick_bsdf]
    style IMPL_gltf_pbr_surfaceshader_tangentINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_roughness_uv[roughness_anisotropy] --".roughness"--> IMPL_gltf_pbr_surfaceshader_tf_metal_bsdf[generalized_schlick_bsdf]
    IMPL_gltf_pbr_surfaceshader_emission[uniform_edf] --".edf"--> IMPL_gltf_pbr_surfaceshader_shader_constructor[surface]
    IMPL_gltf_pbr_surfaceshader_emission_color[multiply] --".color"--> IMPL_gltf_pbr_surfaceshader_emission[uniform_edf]
    IMPL_gltf_pbr_surfaceshader_emissiveINT([emissive]) ==.in1==> IMPL_gltf_pbr_surfaceshader_emission_color[multiply]
    style IMPL_gltf_pbr_surfaceshader_emissiveINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_emissive_strengthINT([emissive_strength]) ==.in2==> IMPL_gltf_pbr_surfaceshader_emission_color[multiply]
    style IMPL_gltf_pbr_surfaceshader_emissive_strengthINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_opacity{ifequal} --".opacity"--> IMPL_gltf_pbr_surfaceshader_shader_constructor[surface]
    IMPL_gltf_pbr_surfaceshader_alpha_modeINT([alpha_mode]) ==.value1==> IMPL_gltf_pbr_surfaceshader_opacity[ifequal]
    style IMPL_gltf_pbr_surfaceshader_alpha_modeINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_opacity_mask{ifequal} --".in2"--> IMPL_gltf_pbr_surfaceshader_opacity{ifequal}
    IMPL_gltf_pbr_surfaceshader_alpha_modeINT([alpha_mode]) ==.value1==> IMPL_gltf_pbr_surfaceshader_opacity_mask[ifequal]
    style IMPL_gltf_pbr_surfaceshader_alpha_modeINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_alphaINT([alpha]) ==.in2==> IMPL_gltf_pbr_surfaceshader_opacity_mask[ifequal]
    style IMPL_gltf_pbr_surfaceshader_alphaINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff{ifgreatereq} --".in1"--> IMPL_gltf_pbr_surfaceshader_opacity_mask{ifequal}
    IMPL_gltf_pbr_surfaceshader_alphaINT([alpha]) ==.value1==> IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff[ifgreatereq]
    style IMPL_gltf_pbr_surfaceshader_alphaINT fill:#0bb, color:#111
    IMPL_gltf_pbr_surfaceshader_alpha_cutoffINT([alpha_cutoff]) ==.value2==> IMPL_gltf_pbr_surfaceshader_opacity_mask_cutoff[ifgreatereq]
    style IMPL_gltf_pbr_surfaceshader_alpha_cutoffINT fill:#0bb, color:#111
```
