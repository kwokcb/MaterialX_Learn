```mermaid
graph LR; 
    NG_tiledimage_vector4_N_img_vector4[image] --> NG_tiledimage_vector4_out([out])
    style NG_tiledimage_vector4_out fill:#1b1, color:#111
    NG_tiledimage_vector4_fileINT([file]) ==.file==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_fileINT fill:#0bb, color:#111
    NG_tiledimage_vector4_dfaultINT([default]) ==.default==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_dfaultINT fill:#0bb, color:#111
    NG_tiledimage_vector4_filtertypeINT([filtertype]) ==.filtertype==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_filtertypeINT fill:#0bb, color:#111
    NG_tiledimage_vector4_framerangeINT([framerange]) ==.framerange==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_framerangeINT fill:#0bb, color:#111
    NG_tiledimage_vector4_frameoffsetINT([frameoffset]) ==.frameoffset==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_frameoffsetINT fill:#0bb, color:#111
    NG_tiledimage_vector4_frameendactionINT([frameendaction]) ==.frameendaction==> NG_tiledimage_vector4_N_img_vector4[image]
    style NG_tiledimage_vector4_frameendactionINT fill:#0bb, color:#111
    NG_tiledimage_vector4_N_multtilesize_vector4[multiply] --".texcoord"--> NG_tiledimage_vector4_N_img_vector4[image]
    NG_tiledimage_vector4_realworldtilesizeINT([realworldtilesize]) ==.in2==> NG_tiledimage_vector4_N_multtilesize_vector4[multiply]
    style NG_tiledimage_vector4_realworldtilesizeINT fill:#0bb, color:#111
    NG_tiledimage_vector4_N_divtilesize_vector4[divide] --".in1"--> NG_tiledimage_vector4_N_multtilesize_vector4[multiply]
    NG_tiledimage_vector4_realworldimagesizeINT([realworldimagesize]) ==.in2==> NG_tiledimage_vector4_N_divtilesize_vector4[divide]
    style NG_tiledimage_vector4_realworldimagesizeINT fill:#0bb, color:#111
    NG_tiledimage_vector4_N_sub_vector4[subtract] --".in1"--> NG_tiledimage_vector4_N_divtilesize_vector4[divide]
    NG_tiledimage_vector4_uvoffsetINT([uvoffset]) ==.in2==> NG_tiledimage_vector4_N_sub_vector4[subtract]
    style NG_tiledimage_vector4_uvoffsetINT fill:#0bb, color:#111
    NG_tiledimage_vector4_N_mult_vector4[multiply] --".in1"--> NG_tiledimage_vector4_N_sub_vector4[subtract]
    NG_tiledimage_vector4_texcoordINT([texcoord]) ==.in1==> NG_tiledimage_vector4_N_mult_vector4[multiply]
    style NG_tiledimage_vector4_texcoordINT fill:#0bb, color:#111
    NG_tiledimage_vector4_uvtilingINT([uvtiling]) ==.in2==> NG_tiledimage_vector4_N_mult_vector4[multiply]
    style NG_tiledimage_vector4_uvtilingINT fill:#0bb, color:#111
```
