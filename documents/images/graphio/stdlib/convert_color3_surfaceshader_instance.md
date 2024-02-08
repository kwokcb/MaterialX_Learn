```mermaid
graph LR; 
    NG_convert_color3_surfaceshader_surface[surface_unlit] --> NG_convert_color3_surfaceshader_out([out])
    style NG_convert_color3_surfaceshader_out fill:#1b1, color:#111
    NG_convert_color3_surfaceshader_inINT([in]) ==.emission_color==> NG_convert_color3_surfaceshader_surface[surface_unlit]
    style NG_convert_color3_surfaceshader_inINT fill:#0bb, color:#111
```
