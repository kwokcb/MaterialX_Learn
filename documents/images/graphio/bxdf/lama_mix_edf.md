```mermaid
graph LR; 
    NG_lama_mix_edf_mix[mix] --> NG_lama_mix_edf_out([out])
    style NG_lama_mix_edf_out fill:#1b1, color:#111
    NG_lama_mix_edf_material2INT([material2]) ==.fg==> NG_lama_mix_edf_mix[mix]
    style NG_lama_mix_edf_material2INT fill:#0bb, color:#111
    NG_lama_mix_edf_material1INT([material1]) ==.bg==> NG_lama_mix_edf_mix[mix]
    style NG_lama_mix_edf_material1INT fill:#0bb, color:#111
    NG_lama_mix_edf_mixINT([mix]) ==.mix==> NG_lama_mix_edf_mix[mix]
    style NG_lama_mix_edf_mixINT fill:#0bb, color:#111
```
