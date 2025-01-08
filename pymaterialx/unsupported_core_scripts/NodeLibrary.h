/// @class ND_disney_brdf_2012_surface
///   Type: surfaceshader
///   Node Group: pbr
class ND_disney_brdf_2012_surface
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  baseColor
    /// value:  0.16, 0.16, 0.16
    color3 baseColor();
 
    /// Input  metallic
    float metallic();
 
    /// Input  subsurface
    float subsurface();
 
    /// Input  specular
    /// value:  0.5
    float specular();
 
    /// Input  roughness
    /// value:  0.5
    float roughness();
 
    /// Input  specularTint
    float specularTint();
 
    /// Input  anisotropic
    float anisotropic();
 
    /// Input  sheen
    float sheen();
 
    /// Input  sheenTint
    /// value:  0.5
    float sheenTint();
 
    /// Input  clearcoat
    float clearcoat();
 
    /// Input  clearcoatGloss
    /// value:  1.0
    float clearcoatGloss();
    /// @}
    /// @name Outputs
    /// value:  1.0
    /// @{
 
    /// Output:  out
    surfaceshader out();
    /// @}
};
 
/// @class ND_disney_bsdf_2015_surface
///   Type: surfaceshader
///   Node Group: pbr
class ND_disney_bsdf_2015_surface
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  baseColor
    /// value:  0.16, 0.16, 0.16
    color3 baseColor();
 
    /// Input  metallic
    float metallic();
 
    /// Input  roughness
    /// value:  0.5
    float roughness();
 
    /// Input  anisotropic
    float anisotropic();
 
    /// Input  specularTint
    float specularTint();
 
    /// Input  sheen
    float sheen();
 
    /// Input  sheenTint
    /// value:  0.5
    float sheenTint();
 
    /// Input  clearcoat
    float clearcoat();
 
    /// Input  clearcoatGloss
    /// value:  1.0
    float clearcoatGloss();
 
    /// Input  specTrans
    float specTrans();
 
    /// Input  ior
    /// value:  1.5
    float ior();
 
    /// Input  scatterDistance
    /// value:  0, 0, 0
    vector3 scatterDistance();
 
    /// Input  flatness
    float flatness();
 
    /// Input  diffTrans
    float diffTrans();
 
    /// Input  thin
    boolean thin();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    surfaceshader out();
    /// @}
};
 
/// @class ND_gltf_pbr_surfaceshader
///   Type: surfaceshader
///   Node Group: pbr
///   Version: 2.0.1. Is default: True
///   Description: glTF PBR
class ND_gltf_pbr_surfaceshader
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  base_color
    /// value:  1, 1, 1
    /// uiname: Base Color
    /// uimin: 0, 0, 0
    /// uimax: 1, 1, 1
    /// uifolder: Base
    color3 base_color();
 
    /// Input  metallic
    /// value:  1.0
    /// uiname: Metallic
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Base
    float metallic();
 
    /// Input  roughness
    /// value:  1.0
    /// uiname: Roughness
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Base
    float roughness();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  occlusion
    /// value:  1.0
    /// uiname: Occlusion
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Base
    float occlusion();
 
    /// Input  transmission
    float transmission();
 
    /// Input  specular
    /// value:  1.0
    /// uiname: Specular
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Base
    float specular();
 
    /// Input  specular_color
    /// value:  1, 1, 1
    /// uiname: Specular Color
    /// uimin: 0, 0, 0
    /// uisoftmax: 1, 1, 1
    /// uifolder: Base
    color3 specular_color();
 
    /// Input  ior
    /// value:  1.5
    /// uiname: Index of Refraction
    /// uimin: 1
    /// uisoftmax: 3
    /// uifolder: Base
    /// uniform: true
    float ior();
 
    /// Input  alpha
    /// value:  1.0
    /// uiname: Alpha
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Alpha
    float alpha();
 
    /// Input  alpha_mode
    integer alpha_mode();
 
    /// Input  alpha_cutoff
    /// value:  0.5
    /// uiname: Alpha Cutoff
    /// uimin: 0
    /// uimax: 1
    /// uifolder: Alpha
    /// uniform: true
    float alpha_cutoff();
 
    /// Input  iridescence
    float iridescence();
 
    /// Input  iridescence_ior
    /// value:  1.3
    /// uiname: Iridescence Index of Refraction
    /// uimin: 1
    /// uisoftmax: 3
    /// uifolder: Iridescence
    /// uniform: true
    float iridescence_ior();
 
    /// Input  iridescence_thickness
    /// value:  100.0
    /// uiname: Iridescence Thickness
    /// uimin: 0
    /// uisoftmin: 100
    /// uisoftmax: 400
    /// uifolder: Iridescence
    float iridescence_thickness();
 
    /// Input  sheen_color
    /// value:  0, 0, 0
    /// uiname: Sheen Color
    /// uimin: 0, 0, 0
    /// uimax: 1, 1, 1
    /// uifolder: Sheen
    color3 sheen_color();
 
    /// Input  sheen_roughness
    float sheen_roughness();
 
    /// Input  clearcoat
    float clearcoat();
 
    /// Input  clearcoat_roughness
    float clearcoat_roughness();
 
    /// Input  clearcoat_normal
    vector3 clearcoat_normal();
 
    /// Input  emissive
    /// value:  0, 0, 0
    /// uiname: Emissive
    /// uimin: 0, 0, 0
    /// uimax: 1, 1, 1
    /// uifolder: Emission
    color3 emissive();
 
    /// Input  emissive_strength
    /// value:  1.0
    /// uiname: Emissive Strength
    /// uimin: 0
    /// uifolder: Emission
    /// uniform: true
    float emissive_strength();
 
    /// Input  thickness
    float thickness();
 
    /// Input  attenuation_distance
    float attenuation_distance();
 
    /// Input  attenuation_color
    /// value:  1, 1, 1
    /// uiname: Attenuation Color
    /// uimin: 0, 0, 0
    /// uimax: 1, 1, 1
    /// uifolder: Volume
    /// uniform: true
    color3 attenuation_color();
    /// @}
    /// @name Outputs
    /// value:  1, 1, 1
    /// @{
 
    /// Output:  out
    surfaceshader out();
    /// @}
};
 
/// @class ND_gltf_colorimage
///   Type: multioutput
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_colorimage
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  default
    /// value:  0, 0, 0, 0
    /// uifolder: Image
    color4 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    /// uifolder: Image
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    /// uifolder: Image
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    /// uifolder: Image
    vector2 offset();
 
    /// Input  operationorder
    /// value:  1
    /// uifolder: Image
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uifolder: Image
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uifolder: Image
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uifolder: Image
    /// uniform: true
    string filtertype();
 
    /// Input  color
    /// value:  1, 1, 1, 1
    /// uifolder: Color
    color4 color();
 
    /// Input  geomcolor
    /// value:  1, 1, 1, 1
    /// uiname: Geometry Color
    /// uifolder: Color
    color4 geomcolor();
    /// @}
    /// @name Outputs
    /// value:  1, 1, 1, 1
    /// @{
 
    /// Output:  outcolor
    color3 outcolor();
 
    /// Output:  outa
    float outa();
    /// @}
};
 
/// @class ND_gltf_image_color3_color3_1_0
///   Type: color3
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_image_color3_color3_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  factor
    /// value:  1, 1, 1
    color3 factor();
 
    /// Input  default
    /// value:  0, 0, 0
    color3 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    vector2 offset();
 
    /// Input  operationorder
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uniform: true
    string filtertype();
    /// @}
    /// @name Outputs
    /// value:  linear
    /// @{
 
    /// Output:  out
    color3 out();
    /// @}
};
 
/// @class ND_gltf_image_color4_color4_1_0
///   Type: color4
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_image_color4_color4_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  factor
    /// value:  1, 1, 1, 1
    color4 factor();
 
    /// Input  default
    /// value:  0, 0, 0, 0
    color4 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    vector2 offset();
 
    /// Input  operationorder
    /// value:  1
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uniform: true
    string filtertype();
    /// @}
    /// @name Outputs
    /// value:  linear
    /// @{
 
    /// Output:  out
    color4 out();
    /// @}
};
 
/// @class ND_gltf_image_float_float_1_0
///   Type: float
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_image_float_float_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  factor
    /// value:  1.0
    float factor();
 
    /// Input  default
    float default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    vector2 offset();
 
    /// Input  operationorder
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uniform: true
    string filtertype();
    /// @}
    /// @name Outputs
    /// value:  linear
    /// @{
 
    /// Output:  out
    float out();
    /// @}
};
 
/// @class ND_gltf_image_vector3_vector3_1_0
///   Type: vector3
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_image_vector3_vector3_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  default
    /// value:  0, 0, 0
    vector3 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    vector2 offset();
 
    /// Input  operationorder
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uniform: true
    string filtertype();
    /// @}
    /// @name Outputs
    /// value:  linear
    /// @{
 
    /// Output:  out
    vector3 out();
    /// @}
};
 
/// @class ND_gltf_normalmap_vector3_1_0
///   Type: vector3
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_normalmap_vector3_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  default
    /// value:  0.5, 0.5, 1
    vector3 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 1
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    vector2 offset();
 
    /// Input  operationorder
    integer operationorder();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uniform: true
    string filtertype();
    /// @}
    /// @name Outputs
    /// value:  linear
    /// @{
 
    /// Output:  out
    vector3 out();
    /// @}
};
 
/// @class ND_gltf_iridescence_thickness_float_1_0
///   Type: float
///   Node Group: texture2d
///   Version: 1.0. Is default: True
class ND_gltf_iridescence_thickness_float_1_0
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  default
    /// value:  0, 0, 0
    /// uifolder: Image
    vector3 default();
 
    /// Input  uvindex
    integer uvindex();
 
    /// Input  pivot
    /// value:  0, 0
    /// uifolder: Image
    vector2 pivot();
 
    /// Input  scale
    /// value:  1, 1
    /// uifolder: Image
    vector2 scale();
 
    /// Input  rotate
    float rotate();
 
    /// Input  offset
    /// value:  0, 0
    /// uifolder: Image
    vector2 offset();
 
    /// Input  uaddressmode
    /// value:  periodic
    /// uifolder: Image
    /// uniform: true
    string uaddressmode();
 
    /// Input  vaddressmode
    /// value:  periodic
    /// uifolder: Image
    /// uniform: true
    string vaddressmode();
 
    /// Input  filtertype
    /// value:  linear
    /// uifolder: Image
    /// uniform: true
    string filtertype();
 
    /// Input  thicknessMin
    /// value:  100.0
    /// uifolder: Thickness
    float thicknessMin();
 
    /// Input  thicknessMax
    /// value:  400.0
    /// uifolder: Thickness
    float thicknessMax();
    /// @}
    /// @name Outputs
    /// value:  400.0
    /// @{
 
    /// Output:  out
    float out();
    /// @}
};
 
/// @class ND_standard_surface_surfaceshader
///   Type: surfaceshader
///   Node Group: pbr
///   Version: 1.0.1. Is default: True
///   Inherits From*: ND_standard_surface_surfaceshader_100
///   Description: Autodesk standard surface shader
class ND_standard_surface_surfaceshader public ND_standard_surface_surfaceshader_100
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  base
    /// value:  1.0
    /// uiname: Base
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Base
    /// doc: Multiplier on the intensity of the diffuse reflection.
    float base();
 
    /// Input  base_color
    /// value:  0.8, 0.8, 0.8
    /// uiname: Base Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Base
    /// doc: Color of the diffuse reflection.
    color3 base_color();
    /// @}
};
 
/// @class ND_standard_surface_surfaceshader_100
///   Type: surfaceshader
///   Node Group: pbr
///   Version: 1.0.0. Is default: False
///   Description: Autodesk standard surface shader
class ND_standard_surface_surfaceshader_100
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  base
    /// value:  0.8
    /// uiname: Base
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Base
    /// doc: Multiplier on the intensity of the diffuse reflection.
    float base();
 
    /// Input  base_color
    /// value:  1, 1, 1
    /// uiname: Base Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Base
    /// doc: Color of the diffuse reflection.
    color3 base_color();
 
    /// Input  diffuse_roughness
    float diffuse_roughness();
 
    /// Input  metalness
    float metalness();
 
    /// Input  specular
    /// value:  1.0
    /// uiname: Specular
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Specular
    /// doc: Multiplier on the intensity of the specular reflection.
    float specular();
 
    /// Input  specular_color
    /// value:  1, 1, 1
    /// uiname: Specular Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Specular
    /// doc: Color tint on the specular reflection.
    color3 specular_color();
 
    /// Input  specular_roughness
    /// value:  0.2
    /// uiname: Specular Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Specular
    /// doc: The roughness of the specular reflection. Lower numbers produce sharper reflections, higher numbers produce blurrier reflections.
    float specular_roughness();
 
    /// Input  specular_IOR
    /// value:  1.5
    /// uiname: Index of Refraction
    /// uimin: 0.0
    /// uisoftmin: 1.0
    /// uisoftmax: 3.0
    /// uifolder: Specular
    /// doc: Index of refraction for specular reflection.
    float specular_IOR();
 
    /// Input  specular_anisotropy
    float specular_anisotropy();
 
    /// Input  specular_rotation
    float specular_rotation();
 
    /// Input  transmission
    float transmission();
 
    /// Input  transmission_color
    /// value:  1, 1, 1
    /// uiname: Transmission Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Transmission
    /// uiadvanced: true
    /// doc: Color tint on the transmitted light.
    color3 transmission_color();
 
    /// Input  transmission_depth
    float transmission_depth();
 
    /// Input  transmission_scatter
    /// value:  0, 0, 0
    /// uiname: Transmission Scatter
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Transmission
    /// uiadvanced: true
    /// doc: Scattering coefficient of the interior medium. Suitable for a large body of liquid or one that is fairly thick, such as an ocean, honey, ice, or frosted glass.
    color3 transmission_scatter();
 
    /// Input  transmission_scatter_anisotropy
    float transmission_scatter_anisotropy();
 
    /// Input  transmission_dispersion
    float transmission_dispersion();
 
    /// Input  transmission_extra_roughness
    float transmission_extra_roughness();
 
    /// Input  subsurface
    float subsurface();
 
    /// Input  subsurface_color
    /// value:  1, 1, 1
    /// uiname: Subsurface Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Subsurface
    /// uiadvanced: true
    /// doc: The color of the subsurface scattering effect.
    color3 subsurface_color();
 
    /// Input  subsurface_radius
    /// value:  1, 1, 1
    /// uiname: Subsurface Radius
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Subsurface
    /// uiadvanced: true
    /// doc: The mean free path. The distance which light can travel before being scattered inside the surface.
    color3 subsurface_radius();
 
    /// Input  subsurface_scale
    /// value:  1.0
    /// uiname: Subsurface Scale
    /// uimin: 0.0
    /// uisoftmax: 10.0
    /// uifolder: Subsurface
    /// uiadvanced: true
    /// doc: Scalar weight for the subsurface radius value.
    float subsurface_scale();
 
    /// Input  subsurface_anisotropy
    float subsurface_anisotropy();
 
    /// Input  sheen
    float sheen();
 
    /// Input  sheen_color
    /// value:  1, 1, 1
    /// uiname: Sheen Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Sheen
    /// uiadvanced: true
    /// doc: The color of the sheen layer.
    color3 sheen_color();
 
    /// Input  sheen_roughness
    /// value:  0.3
    /// uiname: Sheen Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Sheen
    /// uiadvanced: true
    /// doc: The roughness of the sheen layer.
    float sheen_roughness();
 
    /// Input  coat
    float coat();
 
    /// Input  coat_color
    /// value:  1, 1, 1
    /// uiname: Coat Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Coat
    /// doc: The color of the clear-coat layer's transparency.
    color3 coat_color();
 
    /// Input  coat_roughness
    /// value:  0.1
    /// uiname: Coat Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Coat
    /// doc: The roughness of the clear-coat reflections. The lower the value, the sharper the reflection.
    float coat_roughness();
 
    /// Input  coat_anisotropy
    float coat_anisotropy();
 
    /// Input  coat_rotation
    float coat_rotation();
 
    /// Input  coat_IOR
    /// value:  1.5
    /// uiname: Coat Index of Refraction
    /// uimin: 0.0
    /// uisoftmin: 1.0
    /// uisoftmax: 3.0
    /// uifolder: Coat
    /// doc: The index of refraction of the clear-coat layer.
    float coat_IOR();
 
    /// Input  coat_normal
    vector3 coat_normal();
 
    /// Input  coat_affect_color
    float coat_affect_color();
 
    /// Input  coat_affect_roughness
    float coat_affect_roughness();
 
    /// Input  thin_film_thickness
    float thin_film_thickness();
 
    /// Input  thin_film_IOR
    /// value:  1.5
    /// uiname: Thin Film Index of Refraction
    /// uimin: 0.0
    /// uisoftmin: 1.0
    /// uisoftmax: 3.0
    /// uifolder: Thin Film
    /// uiadvanced: true
    /// doc: The index of refraction of the medium surrounding the material.
    float thin_film_IOR();
 
    /// Input  emission
    float emission();
 
    /// Input  emission_color
    /// value:  1, 1, 1
    /// uiname: Emission Color
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Emission
    /// doc: The color of the emitted light.
    color3 emission_color();
 
    /// Input  opacity
    /// value:  1, 1, 1
    /// uiname: Opacity
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    /// uifolder: Geometry
    /// doc: The opacity of the entire material.
    color3 opacity();
 
    /// Input  thin_walled
    boolean thin_walled();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  tangent
    vector3 tangent();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    surfaceshader out();
    /// @}
};
 
/// @class ND_UsdPreviewSurface_surfaceshader
///   Type: surfaceshader
///   Node Group: pbr
///   Version: 2.3. Is default: True
///   Description: USD preview surface shader
class ND_UsdPreviewSurface_surfaceshader
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  diffuseColor
    /// value:  0.18, 0.18, 0.18
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    color3 diffuseColor();
 
    /// Input  emissiveColor
    /// value:  0, 0, 0
    /// uimin: 0,0,0
    /// uisoftmax: 1,1,1
    color3 emissiveColor();
 
    /// Input  useSpecularWorkflow
    integer useSpecularWorkflow();
 
    /// Input  specularColor
    /// value:  0, 0, 0
    /// uimin: 0,0,0
    /// uimax: 1,1,1
    color3 specularColor();
 
    /// Input  metallic
    float metallic();
 
    /// Input  roughness
    /// value:  0.5
    /// uimin: 0.0
    /// uimax: 1.0
    float roughness();
 
    /// Input  clearcoat
    float clearcoat();
 
    /// Input  clearcoatRoughness
    /// value:  0.01
    /// uimin: 0.0
    /// uimax: 1.0
    float clearcoatRoughness();
 
    /// Input  opacity
    /// value:  1.0
    /// uimin: 0.0
    /// uimax: 1.0
    float opacity();
 
    /// Input  opacityThreshold
    float opacityThreshold();
 
    /// Input  ior
    /// value:  1.5
    /// uimin: 0.0
    /// uisoftmin: 1.0
    /// uisoftmax: 3.0
    float ior();
 
    /// Input  normal
    /// value:  0, 0, 1
    vector3 normal();
 
    /// Input  displacement
    float displacement();
 
    /// Input  occlusion
    /// value:  1.0
    /// uimin: 0.0
    /// uimax: 1.0
    float occlusion();
    /// @}
    /// @name Outputs
    /// value:  1.0
    /// @{
 
    /// Output:  out
    surfaceshader out();
    /// @}
};
 
/// @class ND_UsdUVTexture
///   Type: multioutput
///   Node Group: texture2d
///   Version: 2.2. Is default: False
///   Inherits From*: ND_UsdUVTexture_23
class ND_UsdUVTexture public ND_UsdUVTexture_23
{
  public:
    /// @name Outputs
    /// @{
 
    /// Output:  r
    float r();
 
    /// Output:  g
    float g();
 
    /// Output:  b
    float b();
 
    /// Output:  a
    float a();
 
    /// Output:  rgb
    color3 rgb();
 
    /// Output:  rgba
    color4 rgba();
    /// @}
};
 
/// @class ND_UsdUVTexture_23
///   Type: multioutput
///   Node Group: texture2d
///   Version: 2.3. Is default: True
class ND_UsdUVTexture_23
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  file
    filename file();
 
    /// Input  st
    vector2 st();
 
    /// Input  wrapS
    /// value:  periodic
    /// uniform: true
    string wrapS();
 
    /// Input  wrapT
    /// value:  periodic
    /// uniform: true
    string wrapT();
 
    /// Input  fallback
    /// value:  0, 0, 0, 1
    color4 fallback();
 
    /// Input  scale
    /// value:  1, 1, 1, 1
    /// uniform: true
    color4 scale();
 
    /// Input  bias
    /// value:  0, 0, 0, 0
    /// uniform: true
    color4 bias();
    /// @}
    /// @name Outputs
    /// value:  0, 0, 0, 0
    /// @{
 
    /// Output:  r
    float r();
 
    /// Output:  g
    float g();
 
    /// Output:  b
    float b();
 
    /// Output:  a
    float a();
 
    /// Output:  rgb
    color3 rgb();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_integer
///   Type: integer
///   Node Group: geometric
class ND_UsdPrimvarReader_integer
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    integer fallback();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    integer out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_boolean
///   Type: boolean
///   Node Group: geometric
class ND_UsdPrimvarReader_boolean
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    boolean fallback();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    boolean out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_string
///   Type: string
///   Node Group: geometric
class ND_UsdPrimvarReader_string
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    string fallback();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    string out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_float
///   Type: float
///   Node Group: geometric
class ND_UsdPrimvarReader_float
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    float fallback();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    float out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_vector2
///   Type: vector2
///   Node Group: geometric
class ND_UsdPrimvarReader_vector2
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    /// value:  0, 0
    vector2 fallback();
    /// @}
    /// @name Outputs
    /// value:  0, 0
    /// @{
 
    /// Output:  out
    vector2 out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_vector3
///   Type: vector3
///   Node Group: geometric
class ND_UsdPrimvarReader_vector3
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    /// value:  0, 0, 0
    vector3 fallback();
    /// @}
    /// @name Outputs
    /// value:  0, 0, 0
    /// @{
 
    /// Output:  out
    vector3 out();
    /// @}
};
 
/// @class ND_UsdPrimvarReader_vector4
///   Type: vector4
///   Node Group: geometric
class ND_UsdPrimvarReader_vector4
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  varname
    string varname();
 
    /// Input  fallback
    /// value:  0, 0, 0, 0
    vector4 fallback();
    /// @}
    /// @name Outputs
    /// value:  0, 0, 0, 0
    /// @{
 
    /// Output:  out
    vector4 out();
    /// @}
};
 
/// @class ND_UsdTransform2d
///   Type: vector2
///   Node Group: math
class ND_UsdTransform2d
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  in
    vector2 in();
 
    /// Input  rotation
    float rotation();
 
    /// Input  scale
    /// value:  1, 1
    vector2 scale();
 
    /// Input  translation
    /// value:  0, 0
    vector2 translation();
    /// @}
    /// @name Outputs
    /// value:  0, 0
    /// @{
 
    /// Output:  out
    vector2 out();
    /// @}
};
 
/// @class ND_lama_add_bsdf
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_add_bsdf
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  material1
    BSDF material1();
 
    /// Input  material2
    BSDF material2();
 
    /// Input  weight1
    /// value:  1.0
    /// uiname: Weight 1
    /// uimin: 0.0
    /// uimax: 1.0
    /// doc: Weight of the first material.
    float weight1();
 
    /// Input  weight2
    float weight2();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_add_edf
///   Type: EDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_add_edf
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  material1
    EDF material1();
 
    /// Input  material2
    EDF material2();
 
    /// Input  weight1
    /// value:  1.0
    /// uiname: Weight 1
    /// uimin: 0.0
    /// uimax: 1.0
    /// doc: Weight of the first material.
    float weight1();
 
    /// Input  weight2
    float weight2();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    EDF out();
    /// @}
};
 
/// @class ND_lama_conductor
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
///   Description: Lama conductor
class ND_lama_conductor
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  tint
    /// value:  1, 1, 1
    /// uiname: Tint
    /// uifolder: Main
    /// doc: Overall color multiplier. It should be used with parcimony, as a non-white value breaks physicality. The prefered way to define the color of a conductor is through the Fresnel attributes right below.
    color3 tint();
 
    /// Input  fresnelMode
    integer fresnelMode();
 
    /// Input  IOR
    /// value:  0.18, 0.42, 1.37
    /// uiname: IOR
    /// uifolder: Main
    /// doc: Index of refraction (often denoted by eta), defining the color reflected by the surface in the normal direction.
    vector3 IOR();
 
    /// Input  extinction
    /// value:  3.42, 2.35, 1.77
    /// uiname: Extinction
    /// uifolder: Main
    /// doc: Extinction coefficient (often denoted by kappa), influencing how the reflected color curve evolves between its value in the normal direction (or 0 degree), and 1 when reaching 90 degrees. A null value does not deviate the curve at all.
    vector3 extinction();
 
    /// Input  reflectivity
    /// value:  0.945, 0.7772, 0.3737
    /// uiname: Reflectivity
    /// uifolder: Main
    /// doc: Color reflected by the surface in the normal direction.
    color3 reflectivity();
 
    /// Input  edgeColor
    /// value:  0.9979, 0.9813, 0.7523
    /// uiname: Edge Color
    /// uifolder: Main
    /// doc: Indicates how the reflected color curve evolves between its value in the normal direction (or 0 degree), and 1 when reaching 90 degrees. Note that this color is unlikely to be reached, and just bends the curve towards it when reaching grazing angles. A null value does not deviate the curve at all.
    color3 edgeColor();
 
    /// Input  roughness
    /// value:  0.1
    /// uiname: Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Main
    /// doc: Micro-facet distribution roughness.
    float roughness();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  anisotropy
    float anisotropy();
 
    /// Input  anisotropyDirection
    vector3 anisotropyDirection();
 
    /// Input  anisotropyRotation
    float anisotropyRotation();
 
    /// Input  iridescenceThickness
    float iridescenceThickness();
 
    /// Input  iridescenceIOR
    /// value:  1.5
    /// uiname: IOR
    /// uimin: 1.0
    /// uimax: 3.0
    /// uifolder: Iridescence
    /// doc: Thin film index of refraction, driving the iridescent effect.
    float iridescenceIOR();
 
    /// Input  exteriorIOR
    /// value:  1.0
    /// uiname: Exterior IOR
    /// uimin: 1.0
    /// uimax: 3.0
    /// uifolder: Advanced
    /// doc: Defines what the IOR of the exterior medium is (can be either the outside medium, eg. air or water, or in case of a layered material, the top layer medium, like plexiglass or varnish).
    float exteriorIOR();
    /// @}
    /// @name Outputs
    /// value:  1.0
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_dielectric
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
///   Description: Lama dielectric
class ND_lama_dielectric
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  reflectionTint
    /// value:  1, 1, 1
    /// uiname: Reflection Tint
    /// uifolder: Main
    /// doc: Color multiplier for external reflection. It should be used with parcimony, as a non-white value breaks physicality.
    color3 reflectionTint();
 
    /// Input  transmissionTint
    /// value:  1, 1, 1
    /// uiname: Transmission Tint
    /// uifolder: Main
    /// doc: Color multiplier for rays going inside the medium (covers external transmission and internal reflection). It should be used with parcimony, as a non-white value breaks physicality. The prefered way to define the color of a dielectric is through the Interior attributes right below.
    color3 transmissionTint();
 
    /// Input  fresnelMode
    integer fresnelMode();
 
    /// Input  IOR
    /// value:  1.5
    /// uiname: IOR
    /// uimin: 1.0
    /// uimax: 3.0
    /// uifolder: Main
    /// doc: Index of refraction (often denoted by eta), defining the amount reflected by the surface in the normal direction, and how the rays are bent by refraction.
    float IOR();
 
    /// Input  reflectivity
    /// value:  0.04
    /// uiname: Reflectivity
    /// uifolder: Main
    /// doc: Reflectivity
    float reflectivity();
 
    /// Input  roughness
    /// value:  0.1
    /// uiname: Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Main
    /// doc: Micro-facet distribution roughness.
    float roughness();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  anisotropy
    float anisotropy();
 
    /// Input  direction
    vector3 direction();
 
    /// Input  rotation
    float rotation();
 
    /// Input  exteriorIOR
    /// value:  1.0
    /// uiname: Exterior IOR
    /// uimin: 1.0
    /// uimax: 3.0
    /// uifolder: Advanced
    /// doc: Defines what the IOR of the exterior medium is (can be either the outside medium, eg. air or water, or in case of a layered material, the top layer medium, like plexiglass or varnish).
    float exteriorIOR();
 
    /// Input  absorptionColor
    /// value:  1, 1, 1
    /// uiname: Absorption Color
    /// uifolder: Interior
    /// doc: Absorption color
    color3 absorptionColor();
 
    /// Input  absorptionRadius
    /// value:  1.0
    /// uiname: Absorption Radius
    /// uifolder: Interior
    /// doc: Absorption radius
    float absorptionRadius();
 
    /// Input  scatterColor
    /// value:  0, 0, 0
    /// uiname: Scatter Color
    /// uifolder: Interior
    /// doc: Scatter color
    color3 scatterColor();
 
    /// Input  scatterAnisotropy
    float scatterAnisotropy();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_diffuse
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_diffuse
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  color
    /// value:  0.18, 0.18, 0.18
    /// uiname: Color
    /// doc: Diffuse color (aka albedo), defining what ratio of light is reflected for each color channel.
    color3 color();
 
    /// Input  roughness
    float roughness();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  energyCompensation
    /// value:  1.0
    /// uiname: Energy Compensation
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Advanced
    /// doc: Indicates how much energy should be added to compensate for the loss inherent to the Oren-Nayar model, ranging from no compensation at all, to the expected energy from multiple scattering between the micro-facets. This prevents overly dark results when roughness is high.
    /// uniform: true
    float energyCompensation();
 
    /// Input  lobeName
    /// value:  diffuse
    /// uiname: Lobe Name
    /// uifolder: Advanced
    /// doc: Defines the name that can be used in LPE AOVs for this lobe.
    /// uniform: true
    string lobeName();
 
    /// Input  matte
    string matte();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_emission
///   Type: EDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
///   Description: Lama emission
class ND_lama_emission
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  color
    /// value:  1, 1, 1
    /// uiname: Color
    /// uifolder: Main
    /// doc: Color being uniformly emitted in all directions above the surface.
    color3 color();
    /// @}
    /// @name Outputs
    /// value:  1, 1, 1
    /// @{
 
    /// Output:  out
    EDF out();
    /// @}
};
 
/// @class ND_lama_layer_bsdf
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_layer_bsdf
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  materialTop
    BSDF materialTop();
 
    /// Input  materialBase
    BSDF materialBase();
 
    /// Input  topMix
    /// value:  1.0
    /// uiname: Top Mix
    /// uimin: 0.0
    /// uimax: 1.0
    /// doc: Defines how visible the top material is.
    float topMix();
 
    /// Input  topThickness
    float topThickness();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_mix_bsdf
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_mix_bsdf
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  material1
    BSDF material1();
 
    /// Input  material2
    BSDF material2();
 
    /// Input  mix
    float mix();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_mix_edf
///   Type: EDF
class ND_lama_mix_edf
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  material1
    EDF material1();
 
    /// Input  material2
    EDF material2();
 
    /// Input  mix
    float mix();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    EDF out();
    /// @}
};
 
/// @class ND_lama_sheen
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
///   Description: Lama sheen
class ND_lama_sheen
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  color
    /// value:  1, 1, 1
    /// uiname: Color
    /// uifolder: Main
    /// doc: Amount of sheen to add, per channel. When this node is used as top material in a stack, the more sheen is added, the less energy will be transmitted to the base material.
    color3 color();
 
    /// Input  roughness
    /// value:  0.1
    /// uiname: Roughness
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Main
    /// doc: Roughness of the sheen effect. Very rough sheen can be used to create a rough diffuse look (when combined with a diffuse node by a stack or mix).
    float roughness();
 
    /// Input  normal
    vector3 normal();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_sss
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
///   Description: Lama SSS
class ND_lama_sss
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  color
    /// value:  0.18, 0.18, 0.18
    /// uiname: Color
    /// uifolder: Main
    /// doc: Diffuse color (aka albedo), defining what ratio of light is reflected -- or transmitted -- for each color channel.
    color3 color();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  sssRadius
    /// value:  0, 0, 0
    /// uiname: Radius
    /// uifolder: SSS
    /// doc: Diffuse Mean Free Path, expressed for each color channel in mm. Indicates on average how much the light travels under the surface before being scattered. The higher the value, the softer the result will be. If null, the computation simplifies to a Lambertian lobe.
    color3 sssRadius();
 
    /// Input  sssScale
    /// value:  1.0
    /// uiname: Scale
    /// uifolder: SSS
    /// doc: Multiplies the radius, to adjust its scale to the scene at hand. If null, the computation simplifies to a Lambertian lobe.
    float sssScale();
 
    /// Input  sssMode
    integer sssMode();
 
    /// Input  sssIOR
    /// value:  1.0
    /// uiname: IOR
    /// uimin: 1.0
    /// uimax: 2.0
    /// uifolder: SSS
    /// doc: Index of refraction use to trigger cases of total internal reflections, when the paths are reaching the surface after having travelled under it. Can be used to avoid excessive glow in highly curved regions (corners, creases, ...).
    float sssIOR();
 
    /// Input  sssAnisotropy
    float sssAnisotropy();
 
    /// Input  sssBleed
    float sssBleed();
 
    /// Input  sssFollowTopology
    float sssFollowTopology();
 
    /// Input  sssSubset
    string sssSubset();
 
    /// Input  sssContinuationRays
    integer sssContinuationRays();
 
    /// Input  sssUnitLength
    /// value:  0.00328
    /// uiname: Unit Length
    /// uifolder: SSS
    /// doc: Specifies what unit length the scene is using. It is a multiplier on the mean free path or diffuse mean free path which is expressed in mm. The default value of 0.00328 converts between feet and mm.
    float sssUnitLength();
 
    /// Input  mode
    integer mode();
 
    /// Input  albedoInversionMethod
    integer albedoInversionMethod();
 
    /// Input  diffuseLobeName
    /// value:  diffuse
    /// uiname: Diffuse Lobe Name
    /// uifolder: Advanced
    /// doc: Defines the name that can be used in LPE AOVs for the diffuse lobe (when the SSS radius is null).
    /// uniform: true
    string diffuseLobeName();
 
    /// Input  sssEntryLobeName
    /// value:  irradiance
    /// uiname: SSS Entry Lobe Name
    /// uifolder: Advanced
    /// doc: Defines the name that can be used in LPE AOVs for the SSS Entry lobe.
    /// uniform: true
    string sssEntryLobeName();
 
    /// Input  sssExitLobeName
    string sssExitLobeName();
 
    /// Input  sssId
    integer sssId();
 
    /// Input  matte
    string matte();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_lama_translucent
///   Type: BSDF
///   Node Group: pbr
///   Version: 1.0. Is default: True
class ND_lama_translucent
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  color
    /// value:  0.18, 0.18, 0.18
    /// uiname: Color
    /// doc: Translucent color (aka albedo), defining what ratio of light is transmitted for each color channel.
    color3 color();
 
    /// Input  roughness
    float roughness();
 
    /// Input  normal
    vector3 normal();
 
    /// Input  energyCompensation
    /// value:  1.0
    /// uiname: Energy Compensation
    /// uimin: 0.0
    /// uimax: 1.0
    /// uifolder: Advanced
    /// doc: Indicates how much energy should be added to compensate for the loss inherent to the Oren-Nayar model, ranging from no compensation at all, to the expected energy from multiple scattering between the micro-facets. This prevents overly dark results when roughness is high.
    /// uniform: true
    float energyCompensation();
 
    /// Input  lobeName
    /// value:  diffuse
    /// uiname: Lobe Name
    /// uifolder: Advanced
    /// doc: Defines the name that can be used in LPE AOVs for this lobe.
    /// uniform: true
    string lobeName();
 
    /// Input  matte
    string matte();
    /// @}
    /// @name Outputs
    /// @{
 
    /// Output:  out
    BSDF out();
    /// @}
};
 
/// @class ND_standard_surface_to_gltf_pbr
///   Type: multioutput
class ND_standard_surface_to_gltf_pbr
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  base
    /// value:  1.0
    float base();
 
    /// Input  base_color
    /// value:  0.8, 0.8, 0.8
    color3 base_color();
 
    /// Input  metalness
    float metalness();
 
    /// Input  specular_roughness
    /// value:  0.2
    float specular_roughness();
 
    /// Input  transmission
    float transmission();
 
    /// Input  transmission_color
    /// value:  1, 1, 1
    color3 transmission_color();
 
    /// Input  transmission_depth
    float transmission_depth();
 
    /// Input  sheen
    float sheen();
 
    /// Input  sheen_color
    /// value:  1, 1, 1
    color3 sheen_color();
 
    /// Input  sheen_roughness
    /// value:  0.3
    float sheen_roughness();
 
    /// Input  coat
    float coat();
 
    /// Input  coat_color
    /// value:  0, 0, 0
    color3 coat_color();
 
    /// Input  coat_roughness
    /// value:  0.1
    float coat_roughness();
 
    /// Input  emission
    float emission();
 
    /// Input  emission_color
    /// value:  1, 1, 1
    color3 emission_color();
    /// @}
    /// @name Outputs
    /// value:  1, 1, 1
    /// @{
 
    /// Output:  base_color_out
    color3 base_color_out();
 
    /// Output:  metallic_out
    float metallic_out();
 
    /// Output:  roughness_out
    float roughness_out();
 
    /// Output:  transmission_out
    float transmission_out();
 
    /// Output:  thickness_out
    float thickness_out();
 
    /// Output:  attenuation_color_out
    color3 attenuation_color_out();
 
    /// Output:  sheen_color_out
    color3 sheen_color_out();
 
    /// Output:  sheen_roughness_out
    float sheen_roughness_out();
 
    /// Output:  clearcoat_out
    float clearcoat_out();
 
    /// Output:  clearcoat_roughness_out
    float clearcoat_roughness_out();
 
    /// Output:  emissive_out
    color3 emissive_out();
    /// @}
};
 
/// @class ND_standard_surface_to_UsdPreviewSurface
///   Type: multioutput
class ND_standard_surface_to_UsdPreviewSurface
{
  public:
    /// @name Inputs
    /// @{
 
    /// Input  metalness
    float metalness();
 
    /// Input  base
    /// value:  1.0
    float base();
 
    /// Input  base_color
    /// value:  0.8, 0.8, 0.8
    color3 base_color();
 
    /// Input  specular
    /// value:  1.0
    float specular();
 
    /// Input  specular_color
    /// value:  1, 1, 1
    color3 specular_color();
 
    /// Input  specular_IOR
    /// value:  1.5
    float specular_IOR();
 
    /// Input  specular_roughness
    /// value:  0.2
    float specular_roughness();
 
    /// Input  coat
    float coat();
 
    /// Input  coat_color
    /// value:  1, 1, 1
    color3 coat_color();
 
    /// Input  coat_roughness
    /// value:  0.1
    float coat_roughness();
 
    /// Input  emission
    float emission();
 
    /// Input  emission_color
    /// value:  1, 1, 1
    color3 emission_color();
 
    /// Input  opacity
    /// value:  1, 1, 1
    color3 opacity();
 
    /// Input  normal
    /// value:  0.5, 0.5, 1
    vector3 normal();
    /// @}
    /// @name Outputs
    /// value:  0.5, 0.5, 1
    /// @{
 
    /// Output:  diffuseColor_out
    color3 diffuseColor_out();
 
    /// Output:  emissiveColor_out
    color3 emissiveColor_out();
 
    /// Output:  metallic_out
    float metallic_out();
 
    /// Output:  roughness_out
    float roughness_out();
 
    /// Output:  clearcoat_out
    float clearcoat_out();
 
    /// Output:  clearcoatRoughness_out
    float clearcoatRoughness_out();
 
    /// Output:  opacity_out
    float opacity_out();
 
    /// Output:  ior_out
    float ior_out();
 
    /// Output:  normal_out
    vector3 normal_out();
    /// @}
};
 
