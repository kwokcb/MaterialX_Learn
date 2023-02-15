```mermaid
graph LR; 
    NG_lama_mix_bsdf_mix[mix] --> NG_lama_mix_bsdf_out([out])
    style NG_lama_mix_bsdf_out fill:#1b1, color:#111
    NG_lama_mix_bsdf_material2INT([material2]) ==.fg==> NG_lama_mix_bsdf_mix[mix]
    style NG_lama_mix_bsdf_material2INT fill:#0bb, color:#111
    NG_lama_mix_bsdf_material1INT([material1]) ==.bg==> NG_lama_mix_bsdf_mix[mix]
    style NG_lama_mix_bsdf_material1INT fill:#0bb, color:#111
    NG_lama_mix_bsdf_mixINT([mix]) ==.mix==> NG_lama_mix_bsdf_mix[mix]
    style NG_lama_mix_bsdf_mixINT fill:#0bb, color:#111
```
