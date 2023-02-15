```mermaid
graph LR; 
    NG_convert_color4_shader_surface[surface_unlit] --> NG_convert_color4_shader_out([out])
    style NG_convert_color4_shader_out fill:#1b1, color:#111
    NG_convert_color4_shader_convert[convert] --".emission_color"--> NG_convert_color4_shader_surface[surface_unlit]
    NG_convert_color4_shader_inINT([in]) ==.in==> NG_convert_color4_shader_convert[convert]
    style NG_convert_color4_shader_inINT fill:#0bb, color:#111
    NG_convert_color4_shader_extract[extract] --".opacity"--> NG_convert_color4_shader_surface[surface_unlit]
    NG_convert_color4_shader_inINT([in]) ==.in==> NG_convert_color4_shader_extract[extract]
    style NG_convert_color4_shader_inINT fill:#0bb, color:#111
```
