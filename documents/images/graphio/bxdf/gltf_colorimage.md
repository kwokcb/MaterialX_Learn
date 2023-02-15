```mermaid
graph LR; 
    NG_gltf_colorimage_combine_color[combine3] --> NG_gltf_colorimage_outcolor([outcolor])
    style NG_gltf_colorimage_outcolor fill:#1b1, color:#111
    NG_gltf_colorimage_separate_color[separate4] --> NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutr([outr])
    style NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutr fill:#1b1, color:#111
    NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutr --".in1"--> NG_gltf_colorimage_combine_color[combine3]
    NG_gltf_colorimage_modulate_geomcolor[multiply] --".in"--> NG_gltf_colorimage_separate_color[separate4]
    NG_gltf_colorimage_geomcolorINT([geomcolor]) ==.in2==> NG_gltf_colorimage_modulate_geomcolor[multiply]
    style NG_gltf_colorimage_geomcolorINT fill:#0bb, color:#111
    NG_gltf_colorimage_modulate_color[multiply] --".in1"--> NG_gltf_colorimage_modulate_geomcolor[multiply]
    NG_gltf_colorimage_colorINT([color]) ==.in1==> NG_gltf_colorimage_modulate_color[multiply]
    style NG_gltf_colorimage_colorINT fill:#0bb, color:#111
    NG_gltf_colorimage_image[gltf_image] --".in2"--> NG_gltf_colorimage_modulate_color[multiply]
    NG_gltf_colorimage_fileINT([file]) ==.file==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_fileINT fill:#0bb, color:#111
    NG_gltf_colorimage_dfaultINT([default]) ==.default==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_dfaultINT fill:#0bb, color:#111
    NG_gltf_colorimage_uvindexINT([uvindex]) ==.uvindex==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_uvindexINT fill:#0bb, color:#111
    NG_gltf_colorimage_pivotINT([pivot]) ==.pivot==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_pivotINT fill:#0bb, color:#111
    NG_gltf_colorimage_scaleINT([scale]) ==.scale==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_scaleINT fill:#0bb, color:#111
    NG_gltf_colorimage_rotateINT([rotate]) ==.rotate==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_rotateINT fill:#0bb, color:#111
    NG_gltf_colorimage_offsetINT([offset]) ==.offset==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_offsetINT fill:#0bb, color:#111
    NG_gltf_colorimage_filtertypeINT([filtertype]) ==.filtertype==> NG_gltf_colorimage_image[gltf_image]
    style NG_gltf_colorimage_filtertypeINT fill:#0bb, color:#111
    NG_gltf_colorimage_separate_color[separate4] --> NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutg([outg])
    style NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutg fill:#1b1, color:#111
    NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutg --".in2"--> NG_gltf_colorimage_combine_color[combine3]
    NG_gltf_colorimage_separate_color[separate4] --> NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutb([outb])
    style NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutb fill:#1b1, color:#111
    NG_gltf_colorimage_NG_gltf_colorimage_separate_coloroutb --".in3"--> NG_gltf_colorimage_combine_color[combine3]
    NG_gltf_colorimage_separate_alpha[dot] --> NG_gltf_colorimage_outa([outa])
    style NG_gltf_colorimage_outa fill:#1b1, color:#111
    NG_gltf_colorimage_separate_color[separate4] --> NG_gltf_colorimage_NG_gltf_colorimage_separate_colorouta([outa])
    style NG_gltf_colorimage_NG_gltf_colorimage_separate_colorouta fill:#1b1, color:#111
    NG_gltf_colorimage_NG_gltf_colorimage_separate_colorouta --".in"--> NG_gltf_colorimage_separate_alpha[dot]
```
