```mermaid
graph LR; 
    NG_convert_boolean_material_surfacematerial[surfacematerial] --> NG_convert_boolean_material_out([out])
    style NG_convert_boolean_material_out fill:#1b1, color:#111
    NG_convert_boolean_material_surface_unlit[surface_unlit] --".surfaceshader"--> NG_convert_boolean_material_surfacematerial[surfacematerial]
    NG_convert_boolean_material_float_to_color3[convert] --".emission_color"--> NG_convert_boolean_material_surface_unlit[surface_unlit]
    NG_convert_boolean_material_bool_to_float[convert] --".in"--> NG_convert_boolean_material_float_to_color3[convert]
    NG_convert_boolean_material_inINT([in]) ==.in==> NG_convert_boolean_material_bool_to_float[convert]
    style NG_convert_boolean_material_inINT fill:#0bb, color:#111
```
