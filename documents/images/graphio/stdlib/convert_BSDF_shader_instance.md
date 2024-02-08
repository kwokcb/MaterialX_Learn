```mermaid
graph LR; 
    NG_convert_BSDF_shader_surface[surface] --> NG_convert_BSDF_shader_out([out])
    style NG_convert_BSDF_shader_out fill:#1b1, color:#111
    NG_convert_BSDF_shader_inINT([in]) ==.bsdf==> NG_convert_BSDF_shader_surface[surface]
    style NG_convert_BSDF_shader_inINT fill:#0bb, color:#111
```
