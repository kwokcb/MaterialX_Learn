```mermaid
graph LR; 
    NG_NG_gltf_image_color3_color3_1_0_scale_image[multiply] --> NG_NG_gltf_image_color3_color3_1_0_out([out])
    style NG_NG_gltf_image_color3_color3_1_0_out fill:#1b1, color:#111
    NG_NG_gltf_image_color3_color3_1_0_factorINT([factor]) ==.in1==> NG_NG_gltf_image_color3_color3_1_0_scale_image[multiply]
    style NG_NG_gltf_image_color3_color3_1_0_factorINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_image[image] --".in2"--> NG_NG_gltf_image_color3_color3_1_0_scale_image[multiply]
    NG_NG_gltf_image_color3_color3_1_0_fileINT([file]) ==.file==> NG_NG_gltf_image_color3_color3_1_0_image[image]
    style NG_NG_gltf_image_color3_color3_1_0_fileINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_dfaultINT([default]) ==.default==> NG_NG_gltf_image_color3_color3_1_0_image[image]
    style NG_NG_gltf_image_color3_color3_1_0_dfaultINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_uaddressmodeINT([uaddressmode]) ==.uaddressmode==> NG_NG_gltf_image_color3_color3_1_0_image[image]
    style NG_NG_gltf_image_color3_color3_1_0_uaddressmodeINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_vaddressmodeINT([vaddressmode]) ==.vaddressmode==> NG_NG_gltf_image_color3_color3_1_0_image[image]
    style NG_NG_gltf_image_color3_color3_1_0_vaddressmodeINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_filtertypeINT([filtertype]) ==.filtertype==> NG_NG_gltf_image_color3_color3_1_0_image[image]
    style NG_NG_gltf_image_color3_color3_1_0_filtertypeINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_place2d[place2d] --".texcoord"--> NG_NG_gltf_image_color3_color3_1_0_image[image]
    NG_NG_gltf_image_color3_color3_1_0_pivotINT([pivot]) ==.pivot==> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    style NG_NG_gltf_image_color3_color3_1_0_pivotINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_operationorderINT([operationorder]) ==.operationorder==> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    style NG_NG_gltf_image_color3_color3_1_0_operationorderINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_texcoord1[texcoord] --".texcoord"--> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    NG_NG_gltf_image_color3_color3_1_0_uvindexINT([uvindex]) ==.index==> NG_NG_gltf_image_color3_color3_1_0_texcoord1[texcoord]
    style NG_NG_gltf_image_color3_color3_1_0_uvindexINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_invert_scale[divide] --".scale"--> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    NG_NG_gltf_image_color3_color3_1_0_scaleINT([scale]) ==.in2==> NG_NG_gltf_image_color3_color3_1_0_invert_scale[divide]
    style NG_NG_gltf_image_color3_color3_1_0_scaleINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_negate_rotate[multiply] --".rotate"--> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    NG_NG_gltf_image_color3_color3_1_0_rotateINT([rotate]) ==.in1==> NG_NG_gltf_image_color3_color3_1_0_negate_rotate[multiply]
    style NG_NG_gltf_image_color3_color3_1_0_rotateINT fill:#0bb, color:#111
    NG_NG_gltf_image_color3_color3_1_0_negate_offset[multiply] --".offset"--> NG_NG_gltf_image_color3_color3_1_0_place2d[place2d]
    NG_NG_gltf_image_color3_color3_1_0_offsetINT([offset]) ==.in1==> NG_NG_gltf_image_color3_color3_1_0_negate_offset[multiply]
    style NG_NG_gltf_image_color3_color3_1_0_offsetINT fill:#0bb, color:#111
```
