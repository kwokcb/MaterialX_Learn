```mermaid
graph LR; 
    NG_saturate_color3_N_mix_color3[mix] --> NG_saturate_color3_out([out])
    style NG_saturate_color3_out fill:#1b1, color:#111
    NG_saturate_color3_inINT([in]) ==.fg==> NG_saturate_color3_N_mix_color3[mix]
    style NG_saturate_color3_inINT fill:#0bb, color:#111
    NG_saturate_color3_amountINT([amount]) ==.mix==> NG_saturate_color3_N_mix_color3[mix]
    style NG_saturate_color3_amountINT fill:#0bb, color:#111
    NG_saturate_color3_N_gray_color3[luminance] --".bg"--> NG_saturate_color3_N_mix_color3[mix]
    NG_saturate_color3_inINT([in]) ==.in==> NG_saturate_color3_N_gray_color3[luminance]
    style NG_saturate_color3_inINT fill:#0bb, color:#111
    NG_saturate_color3_lumacoeffsINT([lumacoeffs]) ==.lumacoeffs==> NG_saturate_color3_N_gray_color3[luminance]
    style NG_saturate_color3_lumacoeffsINT fill:#0bb, color:#111
```
