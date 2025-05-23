### Node Group: pbr
* [absorption_vdf](#node-absorption_vdf) [add](#node-add) [anisotropic_vdf](#node-anisotropic_vdf) [artistic_ior](#node-artistic_ior) [blackbody](#node-blackbody) [burley_diffuse_bsdf](#node-burley_diffuse_bsdf) [chiang_hair_absorption_from_color](#node-chiang_hair_absorption_from_color) [chiang_hair_bsdf](#node-chiang_hair_bsdf) [chiang_hair_roughness](#node-chiang_hair_roughness) [conductor_bsdf](#node-conductor_bsdf) [conical_edf](#node-conical_edf) [deon_hair_absorption_from_melanin](#node-deon_hair_absorption_from_melanin) [dielectric_bsdf](#node-dielectric_bsdf) [displacement](#node-displacement) [generalized_schlick_bsdf](#node-generalized_schlick_bsdf) [generalized_schlick_edf](#node-generalized_schlick_edf) [glossiness_anisotropy](#node-glossiness_anisotropy) [layer](#node-layer) [light](#node-light) [measured_edf](#node-measured_edf) [mix](#node-mix) [multiply](#node-multiply) [oren_nayar_diffuse_bsdf](#node-oren_nayar_diffuse_bsdf) [roughness_anisotropy](#node-roughness_anisotropy) [roughness_dual](#node-roughness_dual) [sheen_bsdf](#node-sheen_bsdf) [subsurface_bsdf](#node-subsurface_bsdf) [surface](#node-surface) [translucent_bsdf](#node-translucent_bsdf) [uniform_edf](#node-uniform_edf) [volume](#node-volume) 
---------
 
### Category: *oren_nayar_diffuse_bsdf*
<details open><summary>ND_oren_nayar_diffuse_bsdf</summary>
<p>
 
* *Nodedef*: ND_oren_nayar_diffuse_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A BSDF node for diffuse reflections.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color** | color3 | 0.18, 0.18, 0.18 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **energy_compensation** | boolean | False |  |  |  |  |  |  |  |  |  | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *burley_diffuse_bsdf*
<details open><summary>ND_burley_diffuse_bsdf</summary>
<p>
 
* *Nodedef*: ND_burley_diffuse_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A BSDF node for Burley diffuse reflections.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color** | color3 | 0.18, 0.18, 0.18 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *translucent_bsdf*
<details open><summary>ND_translucent_bsdf</summary>
<p>
 
* *Nodedef*: ND_translucent_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A BSDF node for pure diffuse transmission.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *dielectric_bsdf*
<details open><summary>ND_dielectric_bsdf</summary>
<p>
 
* *Nodedef*: ND_dielectric_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A reflection/transmission BSDF node based on a microfacet model and a Fresnel curve for dielectrics.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **tint** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **ior** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | vector2 | 0.05, 0.05 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_thickness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_ior** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **tangent** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **distribution** | string | ggx |  |  |  |  |  |  |  |  |  | true |
| **scatter_mode** | string | R |  |  |  |  |  |  |  |  |  | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *conductor_bsdf*
<details open><summary>ND_conductor_bsdf</summary>
<p>
 
* *Nodedef*: ND_conductor_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A reflection BSDF node based on a microfacet model and a Fresnel curve for conductors/metals.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **ior** | color3 | 0.183, 0.421, 1.373 |  |  |  |  |  |  |  |  |  |  |
| **extinction** | color3 | 3.424, 2.346, 1.77 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | vector2 | 0.05, 0.05 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_thickness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_ior** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **tangent** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **distribution** | string | ggx |  |  |  |  |  |  |  |  |  | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *generalized_schlick_bsdf*
<details open><summary>ND_generalized_schlick_bsdf</summary>
<p>
 
* *Nodedef*: ND_generalized_schlick_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A reflection/transmission BSDF node based on a microfacet model and a generalized Schlick Fresnel curve.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color0** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **color82** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **color90** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **exponent** | float | 5.0 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | vector2 | 0.05, 0.05 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_thickness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **thinfilm_ior** | float | 1.5 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **tangent** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **distribution** | string | ggx |  |  |  |  |  |  |  |  |  | true |
| **scatter_mode** | string | R |  |  |  |  |  |  |  |  |  | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *subsurface_bsdf*
<details open><summary>ND_subsurface_bsdf</summary>
<p>
 
* *Nodedef*: ND_subsurface_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A subsurface scattering BSDF for true subsurface scattering.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color** | color3 | 0.18, 0.18, 0.18 |  |  |  |  |  |  |  |  |  |  |
| **radius** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **anisotropy** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *sheen_bsdf*
<details open><summary>ND_sheen_bsdf</summary>
<p>
 
* *Nodedef*: ND_sheen_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A microfacet BSDF for the back-scattering properties of cloth-like materials.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **weight** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **roughness** | float | 0.3 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **mode** | string | conty_kulla |  |  |  |  |  |  |  |  |  | true |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *chiang_hair_bsdf*
<details open><summary>ND_chiang_hair_bsdf</summary>
<p>
 
* *Nodedef*: ND_chiang_hair_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A BSDF node for Chiang hair shading model.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **tint_R** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **tint_TT** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **tint_TRT** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **ior** | float | 1.55 |  |  |  |  |  |  |  |  |  |  |
| **roughness_R** | vector2 | 0.1, 0.1 |  |  |  |  |  |  |  |  |  |  |
| **roughness_TT** | vector2 | 0.05, 0.05 |  |  |  |  |  |  |  |  |  |  |
| **roughness_TRT** | vector2 | 0.2, 0.2 |  |  |  |  |  |  |  |  |  |  |
| **cuticle_angle** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **absorption_coefficient** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **curve_direction** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *uniform_edf*
<details open><summary>ND_uniform_edf</summary>
<p>
 
* *Nodedef*: ND_uniform_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: An EDF node for uniform emission.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *conical_edf*
<details open><summary>ND_conical_edf</summary>
<p>
 
* *Nodedef*: ND_conical_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Constructs an EDF emitting light inside a cone around the normal direction.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **inner_angle** | float | 60.0 |  |  |  |  |  |  |  |  |  |  |
| **outer_angle** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *measured_edf*
<details open><summary>ND_measured_edf</summary>
<p>
 
* *Nodedef*: ND_measured_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Constructs an EDF emitting light according to a measured IES light profile.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **normal** | vector3 | None |  |  |  |  |  |  |  |  |  |  |
| **file** | filename |  |  |  |  |  |  |  |  |  |  | true |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *generalized_schlick_edf*
<details open><summary>ND_generalized_schlick_edf</summary>
<p>
 
* *Nodedef*: ND_generalized_schlick_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Modifies an EDF with a directional factor.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color0** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **color90** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **exponent** | float | 5.0 |  |  |  |  |  |  |  |  |  |  |
| **base** | EDF |  |  |  |  |  |  |  |  |  |  |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *absorption_vdf*
<details open><summary>ND_absorption_vdf</summary>
<p>
 
* *Nodedef*: ND_absorption_vdf
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Constructs a VDF for pure light absorption.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **absorption** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *anisotropic_vdf*
<details open><summary>ND_anisotropic_vdf</summary>
<p>
 
* *Nodedef*: ND_anisotropic_vdf
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Constructs a VDF scattering light for a participating medium, based on the Henyey-Greenstein phase function.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **absorption** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **scattering** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  |  |  |
| **anisotropy** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *surface*
<details open><summary>ND_surface</summary>
<p>
 
* *Nodedef*: ND_surface
* *Type*: surfaceshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A constructor node for the surfaceshader type.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **bsdf** | BSDF |  |  |  |  |  |  |  |  |  | Distribution function for surface scattering. |  |
| **edf** | EDF |  |  |  |  |  |  |  |  |  | Distribution function for surface emission. |  |
| **opacity** | float | 1.0 |  |  |  |  |  |  |  |  | Surface cutout opacity |  |
| **thin_walled** | boolean | False |  |  |  |  |  |  |  |  | Option to make the surface thin-walled. | true |
| *out* | surfaceshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *volume*
<details open><summary>ND_volume</summary>
<p>
 
* *Nodedef*: ND_volume
* *Type*: volumeshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A constructor node for the volumeshader type.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **vdf** | VDF |  |  |  |  |  |  |  |  |  | Volume distribution function for the medium. |  |
| **edf** | EDF |  |  |  |  |  |  |  |  |  | Emission distribution function for the medium. |  |
| *out* | volumeshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *light*
<details open><summary>ND_light</summary>
<p>
 
* *Nodedef*: ND_light
* *Type*: lightshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A constructor node for the lightshader type.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **edf** | EDF |  |  |  |  |  |  |  |  |  | Distribution function for light emission. |  |
| **intensity** | float | 1.0 |  |  |  |  |  |  |  |  | Multiplier for the light intensity |  |
| **exposure** | float | 0.0 |  |  |  |  |  |  |  |  | Exposure control for the light intensity |  |
| *out* | lightshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *displacement*
<details open><summary>ND_displacement_float</summary>
<p>
 
* *Nodedef*: ND_displacement_float
* *Type*: displacementshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A constructor node for the displacementshader type.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **displacement** | float | 0.0 |  |  |  |  |  |  |  |  | Scalar displacement amount along the surface normal direction. |  |
| **scale** | float | 1.0 |  |  |  |  |  |  |  |  | Scale factor for the displacement vector |  |
| *out* | displacementshader | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_displacement_vector3</summary>
<p>
 
* *Nodedef*: ND_displacement_vector3
* *Type*: displacementshader
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A constructor node for the displacementshader type.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **displacement** | vector3 | 0, 0, 0 |  |  |  |  |  |  |  |  | Vector displacement in (dPdu, dPdv, N) tangent/normal space. |  |
| **scale** | float | 1.0 |  |  |  |  |  |  |  |  | Scale factor for the displacement vector |  |
| *out* | displacementshader | None |  |  |  |  |  |  |  |  |  |  |
### Category: *layer*
<details open><summary>ND_layer_bsdf</summary>
<p>
 
* *Nodedef*: ND_layer_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Layer two BSDF's with vertical layering.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **top** | BSDF |  |  |  |  |  |  |  |  |  |  |  |
| **base** | BSDF |  |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_layer_vdf</summary>
<p>
 
* *Nodedef*: ND_layer_vdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Layer a BSDF over a VDF describing the interior media.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **top** | BSDF |  |  |  |  |  |  |  |  |  |  |  |
| **base** | VDF |  |  |  |  |  |  |  |  |  |  |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *mix*
<details open><summary>ND_mix_bsdf</summary>
<p>
 
* *Nodedef*: ND_mix_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Mix two BSDF's according to an input mix amount.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **fg** | BSDF |  |  |  |  |  |  |  |  |  |  |  |
| **bg** | BSDF |  |  |  |  |  |  |  |  |  |  |  |
| **mix** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  | Mixing weight, range [0, 1]. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_mix_edf</summary>
<p>
 
* *Nodedef*: ND_mix_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Mix two EDF's according to an input mix amount.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **fg** | EDF |  |  |  |  |  |  |  |  |  |  |  |
| **bg** | EDF |  |  |  |  |  |  |  |  |  |  |  |
| **mix** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  | Mixing weight, range [0, 1]. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_mix_vdf</summary>
<p>
 
* *Nodedef*: ND_mix_vdf
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Mix two VDF's according to an input mix amount.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **fg** | VDF |  |  |  |  |  |  |  |  |  |  |  |
| **bg** | VDF |  |  |  |  |  |  |  |  |  |  |  |
| **mix** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  | Mixing weight, range [0, 1]. |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *add*
<details open><summary>ND_add_bsdf</summary>
<p>
 
* *Nodedef*: ND_add_bsdf
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for additive blending of BSDF's.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | BSDF |  |  |  |  |  |  |  |  |  | First BSDF. |  |
| **in2** | BSDF |  |  |  |  |  |  |  |  |  | Second BSDF. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_add_edf</summary>
<p>
 
* *Nodedef*: ND_add_edf
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for additive blending of EDF's.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | EDF |  |  |  |  |  |  |  |  |  | First EDF. |  |
| **in2** | EDF |  |  |  |  |  |  |  |  |  | Second EDF. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_add_vdf</summary>
<p>
 
* *Nodedef*: ND_add_vdf
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for additive blending of VDF's.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | VDF |  |  |  |  |  |  |  |  |  | First VDF. |  |
| **in2** | VDF |  |  |  |  |  |  |  |  |  | Second VDF. |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *multiply*
<details open><summary>ND_multiply_bsdfC</summary>
<p>
 
* *Nodedef*: ND_multiply_bsdfC
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of a BSDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | BSDF |  |  |  |  |  |  |  |  |  | The BSDF to scale. |  |
| **in2** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_multiply_bsdfF</summary>
<p>
 
* *Nodedef*: ND_multiply_bsdfF
* *Type*: BSDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of a BSDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | BSDF |  |  |  |  |  |  |  |  |  | The BSDF to scale. |  |
| **in2** | float | 1.0 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | BSDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_multiply_edfC</summary>
<p>
 
* *Nodedef*: ND_multiply_edfC
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of an EDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | EDF |  |  |  |  |  |  |  |  |  | The EDF to scale. |  |
| **in2** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_multiply_edfF</summary>
<p>
 
* *Nodedef*: ND_multiply_edfF
* *Type*: EDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of an EDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | EDF |  |  |  |  |  |  |  |  |  | The EDF to scale. |  |
| **in2** | float | 1.0 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | EDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_multiply_vdfC</summary>
<p>
 
* *Nodedef*: ND_multiply_vdfC
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of an VDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | VDF |  |  |  |  |  |  |  |  |  | The VDF to scale. |  |
| **in2** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
<details open><summary>ND_multiply_vdfF</summary>
<p>
 
* *Nodedef*: ND_multiply_vdfF
* *Type*: VDF
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: A node for adjusting the contribution of an VDF with a weight.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **in1** | VDF |  |  |  |  |  |  |  |  |  | The VDF to scale. |  |
| **in2** | float | 1.0 |  |  |  |  |  |  |  |  | Scaling weight. |  |
| *out* | VDF | None |  |  |  |  |  |  |  |  |  |  |
### Category: *roughness_anisotropy*
<details open><summary>ND_roughness_anisotropy</summary>
<p>
 
* *Nodedef*: ND_roughness_anisotropy
* *Type*: vector2
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates anisotropic surface roughness from a scalar roughness/anisotropy parameterization.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **roughness** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| **anisotropy** | float | 0.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *roughness_dual*
<details open><summary>ND_roughness_dual</summary>
<p>
 
* *Nodedef*: ND_roughness_dual
* *Type*: vector2
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates anisotropic surface roughness from a dual surface roughness parameterization.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **roughness** | vector2 | 0, 0 |  |  |  |  |  |  |  |  |  |  |
| *out* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *glossiness_anisotropy*
<details open><summary>ND_glossiness_anisotropy</summary>
<p>
 
* *Nodedef*: ND_glossiness_anisotropy
* *Type*: vector2
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates anisotropic surface roughness from a scalar glossiness/anisotropy parameterization.
* *Nodegraph*: IMP_glossiness_anisotropy


```mermaid
graph TB
    subgraph IMP_glossiness_anisotropy
    IMP_glossiness_anisotropy_invert1[invert1]
    IMP_glossiness_anisotropy_roughness1[roughness1]
    style IMP_glossiness_anisotropy_out  fill:#0C0, color:#FFF
    IMP_glossiness_anisotropy_out([out])
    style IMP_glossiness_anisotropy_glossiness  fill:#09D, color:#FFF
    IMP_glossiness_anisotropy_glossiness([glossiness])
    style IMP_glossiness_anisotropy_anisotropy  fill:#09D, color:#FFF
    IMP_glossiness_anisotropy_anisotropy([anisotropy])
    end
    IMP_glossiness_anisotropy_glossiness --"in"--> IMP_glossiness_anisotropy_invert1
    IMP_glossiness_anisotropy_invert1 --"roughness"--> IMP_glossiness_anisotropy_roughness1
    IMP_glossiness_anisotropy_anisotropy --"anisotropy"--> IMP_glossiness_anisotropy_roughness1
    IMP_glossiness_anisotropy_roughness1 --> IMP_glossiness_anisotropy_out
```
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **glossiness** | float | 1.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| **anisotropy** | float | 0.0 |  | 0.0 | 1.0 |  |  |  |  |  |  |  |
| *out* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *blackbody*
<details open><summary>ND_blackbody</summary>
<p>
 
* *Nodedef*: ND_blackbody
* *Type*: color3
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Returns the radiant emittance of a blackbody radiator with the given temperature.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **temperature** | float | 5000.0 |  |  |  |  |  |  |  |  |  |  |
| *out* | color3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *artistic_ior*
<details open><summary>ND_artistic_ior</summary>
<p>
 
* *Nodedef*: ND_artistic_ior
* *Type*: multioutput
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Converts the artistic parameterization reflectivity and edge_color to  complex IOR values.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **reflectivity** | color3 | 0.944, 0.776, 0.373 |  |  |  |  |  |  |  |  |  |  |
| **edge_color** | color3 | 0.998, 0.981, 0.751 |  |  |  |  |  |  |  |  |  |  |
| *ior* | color3 | None |  |  |  |  |  |  |  |  |  |  |
| *extinction* | color3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *deon_hair_absorption_from_melanin*
<details open><summary>ND_deon_hair_absorption_from_melanin</summary>
<p>
 
* *Nodedef*: ND_deon_hair_absorption_from_melanin
* *Type*: vector3
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates hair absorption from melanin parameters.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **melanin_concentration** | float | 0.25 |  |  |  |  |  |  |  |  |  |  |
| **melanin_redness** | float | 0.5 |  |  |  |  |  |  |  |  |  |  |
| **eumelanin_color** | color3 | 0.657704, 0.498077, 0.254107 |  |  |  |  |  |  |  | true | constant from d'Eon et al. 2011, converted to color via exp(-c) |  |
| **pheomelanin_color** | color3 | 0.829444, 0.67032, 0.349938 |  |  |  |  |  |  |  | true | constant from d'Eon et al. 2011, converted to color via exp(-c) |  |
| *absorption* | vector3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *chiang_hair_absorption_from_color*
<details open><summary>ND_chiang_hair_absorption_from_color</summary>
<p>
 
* *Nodedef*: ND_chiang_hair_absorption_from_color
* *Type*: vector3
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates hair absorption from a color.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **color** | color3 | 1, 1, 1 |  |  |  |  |  |  |  |  |  |  |
| **azimuthal_roughness** | float | 0.2 |  |  |  |  |  |  |  |  |  |  |
| *absorption* | vector3 | None |  |  |  |  |  |  |  |  |  |  |
### Category: *chiang_hair_roughness*
<details open><summary>ND_chiang_hair_roughness</summary>
<p>
 
* *Nodedef*: ND_chiang_hair_roughness
* *Type*: multioutput
* *Group*: pbr
* *Version*: 1.0. Is default: False
* *Doc*: Calculates hair roughness for R, TT and TRT component.
* *Implementation*: Non-graph
 

| Name | Type | Default Value | UI name | UI min | UI max | UI Soft Min | UI Soft Max | UI step | UI group | UI Advanced | Doc | Uniform |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **longitudinal** | float | 0.1 |  |  |  |  |  |  |  |  |  |  |
| **azimuthal** | float | 0.2 |  |  |  |  |  |  |  |  |  |  |
| **scale_TT** | float | 0.5 |  |  |  |  |  |  |  | true |  |  |
| **scale_TRT** | float | 2.0 |  |  |  |  |  |  |  | true |  |  |
| *roughness_R* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| *roughness_TT* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
| *roughness_TRT* | vector2 | None |  |  |  |  |  |  |  |  |  |  |
</p></details>
 
