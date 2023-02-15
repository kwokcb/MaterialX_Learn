```mermaid
graph LR; 
    IMP_UsdPrimvarReader_integer_primvar[geompropvalue] --> IMP_UsdPrimvarReader_integer_out([out])
    style IMP_UsdPrimvarReader_integer_out fill:#1b1, color:#111
    IMP_UsdPrimvarReader_integer_varnameINT([varname]) ==.geomprop==> IMP_UsdPrimvarReader_integer_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_integer_varnameINT fill:#0bb, color:#111
    IMP_UsdPrimvarReader_integer_fallbackINT([fallback]) ==.default==> IMP_UsdPrimvarReader_integer_primvar[geompropvalue]
    style IMP_UsdPrimvarReader_integer_fallbackINT fill:#0bb, color:#111
```
