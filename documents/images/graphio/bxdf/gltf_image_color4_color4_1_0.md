```mermaid
graph LR; 
    NG_gltf_image_color4_color4_1_0_scale_image[multiply] --> NG_gltf_image_color4_color4_1_0_out([out])
    style NG_gltf_image_color4_color4_1_0_out fill:#1b1, color:#111
    NG_gltf_image_color4_color4_1_0_factorINT([factor]) ==.in1==> NG_gltf_image_color4_color4_1_0_scale_image[multiply]
    style NG_gltf_image_color4_color4_1_0_factorINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_image[image] --".in2"--> NG_gltf_image_color4_color4_1_0_scale_image[multiply]
    NG_gltf_image_color4_color4_1_0_fileINT([file]) ==.file==> NG_gltf_image_color4_color4_1_0_image[image]
    style NG_gltf_image_color4_color4_1_0_fileINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_dfaultINT([default]) ==.default==> NG_gltf_image_color4_color4_1_0_image[image]
    style NG_gltf_image_color4_color4_1_0_dfaultINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_uaddressmodeINT([uaddressmode]) ==.uaddressmode==> NG_gltf_image_color4_color4_1_0_image[image]
    style NG_gltf_image_color4_color4_1_0_uaddressmodeINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_vaddressmodeINT([vaddressmode]) ==.vaddressmode==> NG_gltf_image_color4_color4_1_0_image[image]
    style NG_gltf_image_color4_color4_1_0_vaddressmodeINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_filtertypeINT([filtertype]) ==.filtertype==> NG_gltf_image_color4_color4_1_0_image[image]
    style NG_gltf_image_color4_color4_1_0_filtertypeINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_place2d[place2d] --".texcoord"--> NG_gltf_image_color4_color4_1_0_image[image]
    NG_gltf_image_color4_color4_1_0_pivotINT([pivot]) ==.pivot==> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    style NG_gltf_image_color4_color4_1_0_pivotINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_operationorderINT([operationorder]) ==.operationorder==> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    style NG_gltf_image_color4_color4_1_0_operationorderINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_texcoord1[texcoord] --".texcoord"--> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    NG_gltf_image_color4_color4_1_0_uvindexINT([uvindex]) ==.index==> NG_gltf_image_color4_color4_1_0_texcoord1[texcoord]
    style NG_gltf_image_color4_color4_1_0_uvindexINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_invert_scale[divide] --".scale"--> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    NG_gltf_image_color4_color4_1_0_scaleINT([scale]) ==.in2==> NG_gltf_image_color4_color4_1_0_invert_scale[divide]
    style NG_gltf_image_color4_color4_1_0_scaleINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_negate_rotate[multiply] --".rotate"--> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    NG_gltf_image_color4_color4_1_0_rotateINT([rotate]) ==.in1==> NG_gltf_image_color4_color4_1_0_negate_rotate[multiply]
    style NG_gltf_image_color4_color4_1_0_rotateINT fill:#0bb, color:#111
    NG_gltf_image_color4_color4_1_0_negate_offset[multiply] --".offset"--> NG_gltf_image_color4_color4_1_0_place2d[place2d]
    NG_gltf_image_color4_color4_1_0_offsetINT([offset]) ==.in1==> NG_gltf_image_color4_color4_1_0_negate_offset[multiply]
    style NG_gltf_image_color4_color4_1_0_offsetINT fill:#0bb, color:#111
```
