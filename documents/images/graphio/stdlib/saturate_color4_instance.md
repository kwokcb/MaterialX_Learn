```mermaid
graph LR; 
    NG_saturate_color4_N_mix_color4[mix] --> NG_saturate_color4_out([out])
    style NG_saturate_color4_out fill:#1b1, color:#111
    NG_saturate_color4_inINT([in]) ==.fg==> NG_saturate_color4_N_mix_color4[mix]
    style NG_saturate_color4_inINT fill:#0bb, color:#111
    NG_saturate_color4_amountINT([amount]) ==.mix==> NG_saturate_color4_N_mix_color4[mix]
    style NG_saturate_color4_amountINT fill:#0bb, color:#111
    NG_saturate_color4_N_gray_color4[luminance] --".bg"--> NG_saturate_color4_N_mix_color4[mix]
    NG_saturate_color4_inINT([in]) ==.in==> NG_saturate_color4_N_gray_color4[luminance]
    style NG_saturate_color4_inINT fill:#0bb, color:#111
    NG_saturate_color4_lumacoeffsINT([lumacoeffs]) ==.lumacoeffs==> NG_saturate_color4_N_gray_color4[luminance]
    style NG_saturate_color4_lumacoeffsINT fill:#0bb, color:#111
```
