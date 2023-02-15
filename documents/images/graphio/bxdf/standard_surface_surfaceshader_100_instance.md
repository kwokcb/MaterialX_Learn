```mermaid
graph LR; 
    NG_standard_surface_surfaceshader_100_shader_constructor[surface] --> NG_standard_surface_surfaceshader_100_out([out])
    style NG_standard_surface_surfaceshader_100_out fill:#1b1, color:#111
    NG_standard_surface_surfaceshader_100_coat_layer[layer] --".bsdf"--> NG_standard_surface_surfaceshader_100_shader_constructor[surface]
    NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf] --".top"--> NG_standard_surface_surfaceshader_100_coat_layer[layer]
    NG_standard_surface_surfaceshader_100_coatINT([coat]) ==.weight==> NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_coatINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_IORINT([coat_IOR]) ==.ior==> NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_coat_IORINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_normalINT([coat_normal]) ==.normal==> NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_coat_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_roughness_vector[roughness_anisotropy] --".roughness"--> NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_coat_roughnessINT([coat_roughness]) ==.roughness==> NG_standard_surface_surfaceshader_100_coat_roughness_vector[roughness_anisotropy]
    style NG_standard_surface_surfaceshader_100_coat_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_anisotropyINT([coat_anisotropy]) ==.anisotropy==> NG_standard_surface_surfaceshader_100_coat_roughness_vector[roughness_anisotropy]
    style NG_standard_surface_surfaceshader_100_coat_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_tangent{ifgreater} --".tangent"--> NG_standard_surface_surfaceshader_100_coat_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_coat_anisotropyINT([coat_anisotropy]) ==.value1==> NG_standard_surface_surfaceshader_100_coat_tangent[ifgreater]
    style NG_standard_surface_surfaceshader_100_coat_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_tangentINT([tangent]) ==.in2==> NG_standard_surface_surfaceshader_100_coat_tangent[ifgreater]
    style NG_standard_surface_surfaceshader_100_tangentINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize[normalize] --".in1"--> NG_standard_surface_surfaceshader_100_coat_tangent{ifgreater}
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate[rotate3d] --".in"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_normalize[normalize]
    NG_standard_surface_surfaceshader_100_tangentINT([tangent]) ==.in==> NG_standard_surface_surfaceshader_100_coat_tangent_rotate[rotate3d]
    style NG_standard_surface_surfaceshader_100_tangentINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_normalINT([coat_normal]) ==.axis==> NG_standard_surface_surfaceshader_100_coat_tangent_rotate[rotate3d]
    style NG_standard_surface_surfaceshader_100_coat_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree[multiply] --".amount"--> NG_standard_surface_surfaceshader_100_coat_tangent_rotate[rotate3d]
    NG_standard_surface_surfaceshader_100_coat_rotationINT([coat_rotation]) ==.in1==> NG_standard_surface_surfaceshader_100_coat_tangent_rotate_degree[multiply]
    style NG_standard_surface_surfaceshader_100_coat_rotationINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated[multiply] --".base"--> NG_standard_surface_surfaceshader_100_coat_layer[layer]
    NG_standard_surface_surfaceshader_100_thin_film_layer[layer] --".in1"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated[multiply]
    NG_standard_surface_surfaceshader_100_thin_film_bsdf[thin_film_bsdf] --".top"--> NG_standard_surface_surfaceshader_100_thin_film_layer[layer]
    NG_standard_surface_surfaceshader_100_thin_film_thicknessINT([thin_film_thickness]) ==.thickness==> NG_standard_surface_surfaceshader_100_thin_film_bsdf[thin_film_bsdf]
    style NG_standard_surface_surfaceshader_100_thin_film_thicknessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_thin_film_IORINT([thin_film_IOR]) ==.ior==> NG_standard_surface_surfaceshader_100_thin_film_bsdf[thin_film_bsdf]
    style NG_standard_surface_surfaceshader_100_thin_film_IORINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_metalness_mix[mix] --".base"--> NG_standard_surface_surfaceshader_100_thin_film_layer[layer]
    NG_standard_surface_surfaceshader_100_metalnessINT([metalness]) ==.mix==> NG_standard_surface_surfaceshader_100_metalness_mix[mix]
    style NG_standard_surface_surfaceshader_100_metalnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf] --".fg"--> NG_standard_surface_surfaceshader_100_metalness_mix[mix]
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior] --> NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorior([ior])
    style NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorior fill:#1b1, color:#111
    NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorior --".ior"--> NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf]
    NG_standard_surface_surfaceshader_100_metal_reflectivity[multiply] --".reflectivity"--> NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior]
    NG_standard_surface_surfaceshader_100_base_colorINT([base_color]) ==.in1==> NG_standard_surface_surfaceshader_100_metal_reflectivity[multiply]
    style NG_standard_surface_surfaceshader_100_base_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_baseINT([base]) ==.in2==> NG_standard_surface_surfaceshader_100_metal_reflectivity[multiply]
    style NG_standard_surface_surfaceshader_100_baseINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_metal_edgecolor[multiply] --".edge_color"--> NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior]
    NG_standard_surface_surfaceshader_100_specular_colorINT([specular_color]) ==.in1==> NG_standard_surface_surfaceshader_100_metal_edgecolor[multiply]
    style NG_standard_surface_surfaceshader_100_specular_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_specularINT([specular]) ==.in2==> NG_standard_surface_surfaceshader_100_metal_edgecolor[multiply]
    style NG_standard_surface_surfaceshader_100_specularINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_artistic_ior[artistic_ior] --> NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorextinction([extinction])
    style NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorextinction fill:#1b1, color:#111
    NG_standard_surface_surfaceshader_100_NG_standard_surface_surfaceshader_100_artistic_iorextinction --".extinction"--> NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf]
    NG_standard_surface_surfaceshader_100_main_roughness[roughness_anisotropy] --".roughness"--> NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf]
    NG_standard_surface_surfaceshader_100_specular_anisotropyINT([specular_anisotropy]) ==.anisotropy==> NG_standard_surface_surfaceshader_100_main_roughness[roughness_anisotropy]
    style NG_standard_surface_surfaceshader_100_specular_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affected_roughness[mix] --".roughness"--> NG_standard_surface_surfaceshader_100_main_roughness[roughness_anisotropy]
    NG_standard_surface_surfaceshader_100_specular_roughnessINT([specular_roughness]) ==.bg==> NG_standard_surface_surfaceshader_100_coat_affected_roughness[mix]
    style NG_standard_surface_surfaceshader_100_specular_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[multiply] --".mix"--> NG_standard_surface_surfaceshader_100_coat_affected_roughness[mix]
    NG_standard_surface_surfaceshader_100_coat_roughnessINT([coat_roughness]) ==.in2==> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[multiply]
    style NG_standard_surface_surfaceshader_100_coat_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1[multiply] --".in1"--> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[multiply]
    NG_standard_surface_surfaceshader_100_coat_affect_roughnessINT([coat_affect_roughness]) ==.in1==> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1[multiply]
    style NG_standard_surface_surfaceshader_100_coat_affect_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coatINT([coat]) ==.in2==> NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply1[multiply]
    style NG_standard_surface_surfaceshader_100_coatINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_main_tangent{ifgreater} --".tangent"--> NG_standard_surface_surfaceshader_100_metal_bsdf[conductor_bsdf]
    NG_standard_surface_surfaceshader_100_specular_anisotropyINT([specular_anisotropy]) ==.value1==> NG_standard_surface_surfaceshader_100_main_tangent[ifgreater]
    style NG_standard_surface_surfaceshader_100_specular_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_tangentINT([tangent]) ==.in2==> NG_standard_surface_surfaceshader_100_main_tangent[ifgreater]
    style NG_standard_surface_surfaceshader_100_tangentINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_tangent_rotate_normalize[normalize] --".in1"--> NG_standard_surface_surfaceshader_100_main_tangent{ifgreater}
    NG_standard_surface_surfaceshader_100_tangent_rotate[rotate3d] --".in"--> NG_standard_surface_surfaceshader_100_tangent_rotate_normalize[normalize]
    NG_standard_surface_surfaceshader_100_tangentINT([tangent]) ==.in==> NG_standard_surface_surfaceshader_100_tangent_rotate[rotate3d]
    style NG_standard_surface_surfaceshader_100_tangentINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.axis==> NG_standard_surface_surfaceshader_100_tangent_rotate[rotate3d]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_tangent_rotate_degree[multiply] --".amount"--> NG_standard_surface_surfaceshader_100_tangent_rotate[rotate3d]
    NG_standard_surface_surfaceshader_100_specular_rotationINT([specular_rotation]) ==.in1==> NG_standard_surface_surfaceshader_100_tangent_rotate_degree[multiply]
    style NG_standard_surface_surfaceshader_100_specular_rotationINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_specular_layer[layer] --".bg"--> NG_standard_surface_surfaceshader_100_metalness_mix[mix]
    NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf] --".top"--> NG_standard_surface_surfaceshader_100_specular_layer[layer]
    NG_standard_surface_surfaceshader_100_specularINT([specular]) ==.weight==> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_specularINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_specular_colorINT([specular_color]) ==.tint==> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_specular_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_specular_IORINT([specular_IOR]) ==.ior==> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_specular_IORINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_main_roughness[roughness_anisotropy] --".roughness"--> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_main_tangent{ifgreater} --".tangent"--> NG_standard_surface_surfaceshader_100_specular_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_transmission_mix[mix] --".base"--> NG_standard_surface_surfaceshader_100_specular_layer[layer]
    NG_standard_surface_surfaceshader_100_transmissionINT([transmission]) ==.mix==> NG_standard_surface_surfaceshader_100_transmission_mix[mix]
    style NG_standard_surface_surfaceshader_100_transmissionINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf] --".fg"--> NG_standard_surface_surfaceshader_100_transmission_mix[mix]
    NG_standard_surface_surfaceshader_100_transmission_colorINT([transmission_color]) ==.tint==> NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_transmission_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_specular_IORINT([specular_IOR]) ==.ior==> NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_specular_IORINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_transmission_roughness[roughness_anisotropy] --".roughness"--> NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_specular_anisotropyINT([specular_anisotropy]) ==.anisotropy==> NG_standard_surface_surfaceshader_100_transmission_roughness[roughness_anisotropy]
    style NG_standard_surface_surfaceshader_100_specular_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness[mix] --".roughness"--> NG_standard_surface_surfaceshader_100_transmission_roughness[roughness_anisotropy]
    NG_standard_surface_surfaceshader_100_transmission_roughness_clamped[clamp] --".bg"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness[mix]
    NG_standard_surface_surfaceshader_100_transmission_roughness_add[add] --".in"--> NG_standard_surface_surfaceshader_100_transmission_roughness_clamped[clamp]
    NG_standard_surface_surfaceshader_100_specular_roughnessINT([specular_roughness]) ==.in1==> NG_standard_surface_surfaceshader_100_transmission_roughness_add[add]
    style NG_standard_surface_surfaceshader_100_specular_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_transmission_extra_roughnessINT([transmission_extra_roughness]) ==.in2==> NG_standard_surface_surfaceshader_100_transmission_roughness_add[add]
    style NG_standard_surface_surfaceshader_100_transmission_extra_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affect_roughness_multiply2[multiply] --".mix"--> NG_standard_surface_surfaceshader_100_coat_affected_transmission_roughness[mix]
    NG_standard_surface_surfaceshader_100_main_tangent{ifgreater} --".tangent"--> NG_standard_surface_surfaceshader_100_transmission_bsdf[dielectric_bsdf]
    NG_standard_surface_surfaceshader_100_sheen_layer[layer] --".bg"--> NG_standard_surface_surfaceshader_100_transmission_mix[mix]
    NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf] --".top"--> NG_standard_surface_surfaceshader_100_sheen_layer[layer]
    NG_standard_surface_surfaceshader_100_sheenINT([sheen]) ==.weight==> NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    style NG_standard_surface_surfaceshader_100_sheenINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_sheen_colorINT([sheen_color]) ==.color==> NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    style NG_standard_surface_surfaceshader_100_sheen_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_sheen_roughnessINT([sheen_roughness]) ==.roughness==> NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    style NG_standard_surface_surfaceshader_100_sheen_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_sheen_bsdf[sheen_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_subsurface_mix[mix] --".base"--> NG_standard_surface_surfaceshader_100_sheen_layer[layer]
    NG_standard_surface_surfaceshader_100_subsurfaceINT([subsurface]) ==.mix==> NG_standard_surface_surfaceshader_100_subsurface_mix[mix]
    style NG_standard_surface_surfaceshader_100_subsurfaceINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[mix] --".fg"--> NG_standard_surface_surfaceshader_100_subsurface_mix[mix]
    NG_standard_surface_surfaceshader_100_translucent_bsdf[translucent_bsdf] --".fg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[mix]
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_translucent_bsdf[translucent_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[power] --".color"--> NG_standard_surface_surfaceshader_100_translucent_bsdf[translucent_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative[max] --".in1"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[power]
    NG_standard_surface_surfaceshader_100_subsurface_colorINT([subsurface_color]) ==.in1==> NG_standard_surface_surfaceshader_100_subsurface_color_nonnegative[max]
    style NG_standard_surface_surfaceshader_100_subsurface_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_gamma[add] --".in2"--> NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[power]
    NG_standard_surface_surfaceshader_100_coat_gamma_multiply[multiply] --".in1"--> NG_standard_surface_surfaceshader_100_coat_gamma[add]
    NG_standard_surface_surfaceshader_100_coat_affect_colorINT([coat_affect_color]) ==.in2==> NG_standard_surface_surfaceshader_100_coat_gamma_multiply[multiply]
    style NG_standard_surface_surfaceshader_100_coat_affect_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_clamped[clamp] --".in1"--> NG_standard_surface_surfaceshader_100_coat_gamma_multiply[multiply]
    NG_standard_surface_surfaceshader_100_coatINT([coat]) ==.in==> NG_standard_surface_surfaceshader_100_coat_clamped[clamp]
    style NG_standard_surface_surfaceshader_100_coatINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf] --".bg"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[mix]
    NG_standard_surface_surfaceshader_100_subsurface_anisotropyINT([subsurface_anisotropy]) ==.anisotropy==> NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    style NG_standard_surface_surfaceshader_100_subsurface_anisotropyINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affected_subsurface_color[power] --".color"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_radius_scaled[multiply] --".radius"--> NG_standard_surface_surfaceshader_100_subsurface_bsdf[subsurface_bsdf]
    NG_standard_surface_surfaceshader_100_subsurface_scaleINT([subsurface_scale]) ==.in2==> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled[multiply]
    style NG_standard_surface_surfaceshader_100_subsurface_scaleINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_subsurface_radius_vector[convert] --".in1"--> NG_standard_surface_surfaceshader_100_subsurface_radius_scaled[multiply]
    NG_standard_surface_surfaceshader_100_subsurface_radiusINT([subsurface_radius]) ==.in==> NG_standard_surface_surfaceshader_100_subsurface_radius_vector[convert]
    style NG_standard_surface_surfaceshader_100_subsurface_radiusINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_subsurface_selector[convert] --".mix"--> NG_standard_surface_surfaceshader_100_selected_subsurface_bsdf[mix]
    NG_standard_surface_surfaceshader_100_thin_walledINT([thin_walled]) ==.in==> NG_standard_surface_surfaceshader_100_subsurface_selector[convert]
    style NG_standard_surface_surfaceshader_100_thin_walledINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_diffuse_bsdf[oren_nayar_diffuse_bsdf] --".bg"--> NG_standard_surface_surfaceshader_100_subsurface_mix[mix]
    NG_standard_surface_surfaceshader_100_baseINT([base]) ==.weight==> NG_standard_surface_surfaceshader_100_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style NG_standard_surface_surfaceshader_100_baseINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_diffuse_roughnessINT([diffuse_roughness]) ==.roughness==> NG_standard_surface_surfaceshader_100_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style NG_standard_surface_surfaceshader_100_diffuse_roughnessINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_normalINT([normal]) ==.normal==> NG_standard_surface_surfaceshader_100_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    style NG_standard_surface_surfaceshader_100_normalINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color[power] --".color"--> NG_standard_surface_surfaceshader_100_diffuse_bsdf[oren_nayar_diffuse_bsdf]
    NG_standard_surface_surfaceshader_100_base_color_nonnegative[max] --".in1"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color[power]
    NG_standard_surface_surfaceshader_100_base_colorINT([base_color]) ==.in1==> NG_standard_surface_surfaceshader_100_base_color_nonnegative[max]
    style NG_standard_surface_surfaceshader_100_base_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_gamma[add] --".in2"--> NG_standard_surface_surfaceshader_100_coat_affected_diffuse_color[power]
    NG_standard_surface_surfaceshader_100_coat_attenuation[mix] --".in2"--> NG_standard_surface_surfaceshader_100_thin_film_layer_attenuated[multiply]
    NG_standard_surface_surfaceshader_100_coat_colorINT([coat_color]) ==.fg==> NG_standard_surface_surfaceshader_100_coat_attenuation[mix]
    style NG_standard_surface_surfaceshader_100_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coatINT([coat]) ==.mix==> NG_standard_surface_surfaceshader_100_coat_attenuation[mix]
    style NG_standard_surface_surfaceshader_100_coatINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_emission_edf[uniform_edf] --".edf"--> NG_standard_surface_surfaceshader_100_shader_constructor[surface]
    NG_standard_surface_surfaceshader_100_emission_weight_attenuated[multiply] --".color"--> NG_standard_surface_surfaceshader_100_emission_edf[uniform_edf]
    NG_standard_surface_surfaceshader_100_emission_weight[multiply] --".in1"--> NG_standard_surface_surfaceshader_100_emission_weight_attenuated[multiply]
    NG_standard_surface_surfaceshader_100_emission_colorINT([emission_color]) ==.in1==> NG_standard_surface_surfaceshader_100_emission_weight[multiply]
    style NG_standard_surface_surfaceshader_100_emission_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_emissionINT([emission]) ==.in2==> NG_standard_surface_surfaceshader_100_emission_weight[multiply]
    style NG_standard_surface_surfaceshader_100_emissionINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coat_emission_attenuation[mix] --".in2"--> NG_standard_surface_surfaceshader_100_emission_weight_attenuated[multiply]
    NG_standard_surface_surfaceshader_100_coat_colorINT([coat_color]) ==.fg==> NG_standard_surface_surfaceshader_100_coat_emission_attenuation[mix]
    style NG_standard_surface_surfaceshader_100_coat_colorINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_coatINT([coat]) ==.mix==> NG_standard_surface_surfaceshader_100_coat_emission_attenuation[mix]
    style NG_standard_surface_surfaceshader_100_coatINT fill:#0bb, color:#111
    NG_standard_surface_surfaceshader_100_opacity_luminance[luminance] --".r -> .opacity"--> NG_standard_surface_surfaceshader_100_shader_constructor[surface]
    NG_standard_surface_surfaceshader_100_opacityINT([opacity]) ==.in==> NG_standard_surface_surfaceshader_100_opacity_luminance[luminance]
    style NG_standard_surface_surfaceshader_100_opacityINT fill:#0bb, color:#111
```
