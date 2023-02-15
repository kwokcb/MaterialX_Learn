```mermaid
graph LR; 
    NG_ramp4_vector4_N_mix_vector4[mix] --> NG_ramp4_vector4_out([out])
    style NG_ramp4_vector4_out fill:#1b1, color:#111
    NG_ramp4_vector4_N_mixtop_vector4[mix] --".bg"--> NG_ramp4_vector4_N_mix_vector4[mix]
    NG_ramp4_vector4_valuetlINT([valuetl]) ==.bg==> NG_ramp4_vector4_N_mixtop_vector4[mix]
    style NG_ramp4_vector4_valuetlINT fill:#0bb, color:#111
    NG_ramp4_vector4_valuetrINT([valuetr]) ==.fg==> NG_ramp4_vector4_N_mixtop_vector4[mix]
    style NG_ramp4_vector4_valuetrINT fill:#0bb, color:#111
    NG_ramp4_vector4_N_s_vector4[extract] --".mix"--> NG_ramp4_vector4_N_mixtop_vector4[mix]
    NG_ramp4_vector4_N_txclamp_vector4[clamp] --".in"--> NG_ramp4_vector4_N_s_vector4[extract]
    NG_ramp4_vector4_texcoordINT([texcoord]) ==.in==> NG_ramp4_vector4_N_txclamp_vector4[clamp]
    style NG_ramp4_vector4_texcoordINT fill:#0bb, color:#111
    NG_ramp4_vector4_N_mixbot_vector4[mix] --".fg"--> NG_ramp4_vector4_N_mix_vector4[mix]
    NG_ramp4_vector4_valueblINT([valuebl]) ==.bg==> NG_ramp4_vector4_N_mixbot_vector4[mix]
    style NG_ramp4_vector4_valueblINT fill:#0bb, color:#111
    NG_ramp4_vector4_valuebrINT([valuebr]) ==.fg==> NG_ramp4_vector4_N_mixbot_vector4[mix]
    style NG_ramp4_vector4_valuebrINT fill:#0bb, color:#111
    NG_ramp4_vector4_N_s_vector4[extract] --".mix"--> NG_ramp4_vector4_N_mixbot_vector4[mix]
    NG_ramp4_vector4_N_t_vector4[extract] --".mix"--> NG_ramp4_vector4_N_mix_vector4[mix]
    NG_ramp4_vector4_N_txclamp_vector4[clamp] --".in"--> NG_ramp4_vector4_N_t_vector4[extract]
```
