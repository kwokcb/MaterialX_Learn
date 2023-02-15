```mermaid
graph LR; 
    IMP_UsdPrimvarReader_vector2_primvar[geompropvalue] --> IMP_UsdPrimvarReader_vector2_out([out])
    style IMP_UsdPrimvarReader_vector2_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_vector2_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_vector2_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector2_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_vector2_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_vector2_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector2_fallbackINT fill:#0bb, color:#111
```
