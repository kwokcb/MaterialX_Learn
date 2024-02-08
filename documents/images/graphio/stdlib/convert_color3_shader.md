```mermaid
graph LR; 
    NG_convert_color3_shader_surface[surface_unlit] --> NG_convert_color3_shader_out([out])
    style NG_convert_color3_shader_out fill:#1b1, color:#111
    NG_convert_color3_shader_inINT([in]) ==.emission_color==> NG_convert_color3_shader_surface[surface_unlit]
    style NG_convert_color3_shader_inINT fill:#0bb, color:#111
```
