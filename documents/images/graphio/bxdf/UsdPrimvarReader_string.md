```mermaid
graph LR; 
    IMP_UsdPrimvarReader_string_primvar[geompropvalue] --> IMP_UsdPrimvarReader_string_out([out])
    style IMP_UsdPrimvarReader_string_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_string_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_string_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_string_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_string_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_string_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_string_fallbackINT fill:#0bb, color:#111
```
