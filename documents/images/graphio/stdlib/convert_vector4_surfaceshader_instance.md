```mermaid
graph LR; 
    NG_convert_vector4_surfaceshader_surface[surface_unlit] --> NG_convert_vector4_surfaceshader_out([out])
    style NG_convert_vector4_surfaceshader_out fill:#1b1, color:#111
    NG_convert_vector4_surfaceshader_color4_to_color3[convert] --".emission_color"--> NG_convert_vector4_surfaceshader_surface[surface_unlit]
    NG_convert_vector4_surfaceshader_vec4_to_color4[convert] --".in"--> NG_convert_vector4_surfaceshader_color4_to_color3[convert]
    NG_convert_vector4_surfaceshader_inINT([in]) ==.in==> NG_convert_vector4_surfaceshader_vec4_to_color4[convert]
    style NG_convert_vector4_surfaceshader_inINT fill:#0bb, color:#111
    NG_convert_vector4_surfaceshader_color4_to_float[extract] --".opacity"--> NG_convert_vector4_surfaceshader_surface[surface_unlit]
    NG_convert_vector4_surfaceshader_vec4_to_color4[convert] --".in"--> NG_convert_vector4_surfaceshader_color4_to_float[extract]
```
