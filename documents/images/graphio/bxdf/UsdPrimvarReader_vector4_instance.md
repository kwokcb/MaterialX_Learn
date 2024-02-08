```mermaid
graph LR; 
    IMP_UsdPrimvarReader_vector4_primvar[geompropvalue] --> IMP_UsdPrimvarReader_vector4_out([out])
    style IMP_UsdPrimvarReader_vector4_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_vector4_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_vector4_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector4_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_vector4_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_vector4_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_vector4_fallbackINT fill:#0bb, color:#111
```
