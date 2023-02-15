```mermaid
graph LR; 
    IMP_UsdPrimvarReader_float_primvar[geompropvalue] --> IMP_UsdPrimvarReader_float_out([out])
    style IMP_UsdPrimvarReader_float_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_float_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_float_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_float_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_float_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_float_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_float_fallbackINT fill:#0bb, color:#111
```
