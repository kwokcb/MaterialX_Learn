```mermaid
graph LR; 
    NG_tiledimage_vector3_N_img_vector3[image] --> NG_tiledimage_vector3_out([out])
    style NG_tiledimage_vector3_out fill:#1b1, color:#111
    NG_tiledimage_vector3_fileINT([file]) ==.file==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_fileINT fill:#0bb, color:#111
    NG_tiledimage_vector3_dfaultINT([default]) ==.default==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_dfaultINT fill:#0bb, color:#111
    NG_tiledimage_vector3_filtertypeINT([filtertype]) ==.filtertype==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_filtertypeINT fill:#0bb, color:#111
    NG_tiledimage_vector3_framerangeINT([framerange]) ==.framerange==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_framerangeINT fill:#0bb, color:#111
    NG_tiledimage_vector3_frameoffsetINT([frameoffset]) ==.frameoffset==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_frameoffsetINT fill:#0bb, color:#111
    NG_tiledimage_vector3_frameendactionINT([frameendaction]) ==.frameendaction==> NG_tiledimage_vector3_N_img_vector3[image]
    style NG_tiledimage_vector3_frameendactionINT fill:#0bb, color:#111
    NG_tiledimage_vector3_N_multtilesize_vector3[multiply] --".texcoord"--> NG_tiledimage_vector3_N_img_vector3[image]
    NG_tiledimage_vector3_realworldtilesizeINT([realworldtilesize]) ==.in2==> NG_tiledimage_vector3_N_multtilesize_vector3[multiply]
    style NG_tiledimage_vector3_realworldtilesizeINT fill:#0bb, color:#111
    NG_tiledimage_vector3_N_divtilesize_vector3[divide] --".in1"--> NG_tiledimage_vector3_N_multtilesize_vector3[multiply]
    NG_tiledimage_vector3_realworldimagesizeINT([realworldimagesize]) ==.in2==> NG_tiledimage_vector3_N_divtilesize_vector3[divide]
    style NG_tiledimage_vector3_realworldimagesizeINT fill:#0bb, color:#111
    NG_tiledimage_vector3_N_sub_vector3[subtract] --".in1"--> NG_tiledimage_vector3_N_divtilesize_vector3[divide]
    NG_tiledimage_vector3_uvoffsetINT([uvoffset]) ==.in2==> NG_tiledimage_vector3_N_sub_vector3[subtract]
    style NG_tiledimage_vector3_uvoffsetINT fill:#0bb, color:#111
    NG_tiledimage_vector3_N_mult_vector3[multiply] --".in1"--> NG_tiledimage_vector3_N_sub_vector3[subtract]
    NG_tiledimage_vector3_texcoordINT([texcoord]) ==.in1==> NG_tiledimage_vector3_N_mult_vector3[multiply]
    style NG_tiledimage_vector3_texcoordINT fill:#0bb, color:#111
    NG_tiledimage_vector3_uvtilingINT([uvtiling]) ==.in2==> NG_tiledimage_vector3_N_mult_vector3[multiply]
    style NG_tiledimage_vector3_uvtilingINT fill:#0bb, color:#111
```
