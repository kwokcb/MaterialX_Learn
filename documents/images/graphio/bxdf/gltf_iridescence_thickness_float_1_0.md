```mermaid
graph LR; 
    NG_gltf_iridescence_thickness_float_1_0_mixThickness[mix] --> NG_gltf_iridescence_thickness_float_1_0_out([out])
    style NG_gltf_iridescence_thickness_float_1_0_out fill:#1b1, color:#111
    NG_gltf_iridescence_thickness_float_1_0_thicknessMinINT([thicknessMin]) ==.fg==> NG_gltf_iridescence_thickness_float_1_0_mixThickness[mix]
    style NG_gltf_iridescence_thickness_float_1_0_thicknessMinINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_thicknessMaxINT([thicknessMax]) ==.bg==> NG_gltf_iridescence_thickness_float_1_0_mixThickness[mix]
    style NG_gltf_iridescence_thickness_float_1_0_thicknessMaxINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_extract[extract] --".mix"--> NG_gltf_iridescence_thickness_float_1_0_mixThickness[mix]
    NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image] --".in"--> NG_gltf_iridescence_thickness_float_1_0_extract[extract]
    NG_gltf_iridescence_thickness_float_1_0_fileINT([file]) ==.file==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_fileINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_dfaultINT([default]) ==.default==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_dfaultINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_uvindexINT([uvindex]) ==.uvindex==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_uvindexINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_pivotINT([pivot]) ==.pivot==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_pivotINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_scaleINT([scale]) ==.scale==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_scaleINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_rotateINT([rotate]) ==.rotate==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_rotateINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_offsetINT([offset]) ==.offset==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_offsetINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_uaddressmodeINT([uaddressmode]) ==.uaddressmode==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_uaddressmodeINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_vaddressmodeINT([vaddressmode]) ==.vaddressmode==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_vaddressmodeINT fill:#0bb, color:#111
    NG_gltf_iridescence_thickness_float_1_0_filtertypeINT([filtertype]) ==.filtertype==> NG_gltf_iridescence_thickness_float_1_0_thickness_image[gltf_image]
    style NG_gltf_iridescence_thickness_float_1_0_filtertypeINT fill:#0bb, color:#111
```
