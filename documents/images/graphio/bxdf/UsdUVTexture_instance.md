```mermaid
graph LR; 
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_r([r])
    style IMP_UsdUVTexture_22_r fill:#1b1, color:#111
    IMP_UsdUVTexture_22_biasINT([bias]) ==.in2==> IMP_UsdUVTexture_22_image_bias[add]
    style IMP_UsdUVTexture_22_biasINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_image_scale[multiply] --".in1"--> IMP_UsdUVTexture_22_image_bias[add]
    IMP_UsdUVTexture_22_scaleINT([scale]) ==.in2==> IMP_UsdUVTexture_22_image_scale[multiply]
    style IMP_UsdUVTexture_22_scaleINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_image_reader[image] --".in1"--> IMP_UsdUVTexture_22_image_scale[multiply]
    IMP_UsdUVTexture_22_fileINT([file]) ==.file==> IMP_UsdUVTexture_22_image_reader[image]
    style IMP_UsdUVTexture_22_fileINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_fallbackINT([fallback]) ==.default==> IMP_UsdUVTexture_22_image_reader[image]
    style IMP_UsdUVTexture_22_fallbackINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_stINT([st]) ==.texcoord==> IMP_UsdUVTexture_22_image_reader[image]
    style IMP_UsdUVTexture_22_stINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_wrapSINT([wrapS]) ==.uaddressmode==> IMP_UsdUVTexture_22_image_reader[image]
    style IMP_UsdUVTexture_22_wrapSINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_wrapTINT([wrapT]) ==.vaddressmode==> IMP_UsdUVTexture_22_image_reader[image]
    style IMP_UsdUVTexture_22_wrapTINT fill:#0bb, color:#111
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_g([g])
    style IMP_UsdUVTexture_22_g fill:#1b1, color:#111
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_b([b])
    style IMP_UsdUVTexture_22_b fill:#1b1, color:#111
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_a([a])
    style IMP_UsdUVTexture_22_a fill:#1b1, color:#111
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_rgb([rgb])
    style IMP_UsdUVTexture_22_rgb fill:#1b1, color:#111
    IMP_UsdUVTexture_22_image_bias[add] --> IMP_UsdUVTexture_22_rgba([rgba])
    style IMP_UsdUVTexture_22_rgba fill:#1b1, color:#111
```
