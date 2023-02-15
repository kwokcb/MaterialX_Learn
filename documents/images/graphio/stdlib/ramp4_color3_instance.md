```mermaid
graph LR; 
    NG_ramp4_color3_N_mix_color3[mix] --> NG_ramp4_color3_out([out])
    style NG_ramp4_color3_out fill:#1b1, color:#111
    NG_ramp4_color3_N_mixtop_color3[mix] --".bg"--> NG_ramp4_color3_N_mix_color3[mix]
    NG_ramp4_color3_valuetlINT([valuetl]) ==.bg==> NG_ramp4_color3_N_mixtop_color3[mix]
    style NG_ramp4_color3_valuetlINT fill:#0bb, color:#111
    NG_ramp4_color3_valuetrINT([valuetr]) ==.fg==> NG_ramp4_color3_N_mixtop_color3[mix]
    style NG_ramp4_color3_valuetrINT fill:#0bb, color:#111
    NG_ramp4_color3_N_s_color3[extract] --".mix"--> NG_ramp4_color3_N_mixtop_color3[mix]
    NG_ramp4_color3_N_txclamp_color3[clamp] --".in"--> NG_ramp4_color3_N_s_color3[extract]
    NG_ramp4_color3_texcoordINT([texcoord]) ==.in==> NG_ramp4_color3_N_txclamp_color3[clamp]
    style NG_ramp4_color3_texcoordINT fill:#0bb, color:#111
    NG_ramp4_color3_N_mixbot_color3[mix] --".fg"--> NG_ramp4_color3_N_mix_color3[mix]
    NG_ramp4_color3_valueblINT([valuebl]) ==.bg==> NG_ramp4_color3_N_mixbot_color3[mix]
    style NG_ramp4_color3_valueblINT fill:#0bb, color:#111
    NG_ramp4_color3_valuebrINT([valuebr]) ==.fg==> NG_ramp4_color3_N_mixbot_color3[mix]
    style NG_ramp4_color3_valuebrINT fill:#0bb, color:#111
    NG_ramp4_color3_N_s_color3[extract] --".mix"--> NG_ramp4_color3_N_mixbot_color3[mix]
    NG_ramp4_color3_N_t_color3[extract] --".mix"--> NG_ramp4_color3_N_mix_color3[mix]
    NG_ramp4_color3_N_txclamp_color3[clamp] --".in"--> NG_ramp4_color3_N_t_color3[extract]
```
