```mermaid
graph LR; 
    IMP_UsdPrimvarReader_vector3_primvar[geompropvalue] --> IMP_UsdPrimvarReader_vector3_out([out])
    style IMP_UsdPrimvarReader_vector3_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_vector3_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_vector3_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector3_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_vector3_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_vector3_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector3_fallbackINT fill:#0bb, color:#111
```
