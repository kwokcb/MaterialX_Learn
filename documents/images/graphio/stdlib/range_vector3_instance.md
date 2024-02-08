```mermaid
graph LR; 
    NG_range_vector3_N_switch_vector3{ifequal} --> NG_range_vector3_out([out])
    style NG_range_vector3_out fill:#1b1, color:#111
    NG_range_vector3_doclampINT([doclamp]) ==.value1==> NG_range_vector3_N_switch_vector3[ifequal]
    style NG_range_vector3_doclampINT fill:#0bb, color:#111
    NG_range_vector3_N_clamp_vector3[clamp] --".in1"--> NG_range_vector3_N_switch_vector3{ifequal}
    NG_range_vector3_outlowINT([outlow]) ==.low==> NG_range_vector3_N_clamp_vector3[clamp]
    style NG_range_vector3_outlowINT fill:#0bb, color:#111
    NG_range_vector3_outhighINT([outhigh]) ==.high==> NG_range_vector3_N_clamp_vector3[clamp]
    style NG_range_vector3_outhighINT fill:#0bb, color:#111
    NG_range_vector3_N_remap2_vector3[remap] --".in"--> NG_range_vector3_N_clamp_vector3[clamp]
    NG_range_vector3_outlowINT([outlow]) ==.outlow==> NG_range_vector3_N_remap2_vector3[remap]
    style NG_range_vector3_outlowINT fill:#0bb, color:#111
    NG_range_vector3_outhighINT([outhigh]) ==.outhigh==> NG_range_vector3_N_remap2_vector3[remap]
    style NG_range_vector3_outhighINT fill:#0bb, color:#111
    NG_range_vector3_N_gamma_vector3[multiply] --".in"--> NG_range_vector3_N_remap2_vector3[remap]
    NG_range_vector3_N_pow_vector3[power] --".in1"--> NG_range_vector3_N_gamma_vector3[multiply]
    NG_range_vector3_N_abs_vector3[absval] --".in1"--> NG_range_vector3_N_pow_vector3[power]
    NG_range_vector3_N_remap1_vector3[remap] --".in"--> NG_range_vector3_N_abs_vector3[absval]
    NG_range_vector3_inINT([in]) ==.in==> NG_range_vector3_N_remap1_vector3[remap]
    style NG_range_vector3_inINT fill:#0bb, color:#111
    NG_range_vector3_inlowINT([inlow]) ==.inlow==> NG_range_vector3_N_remap1_vector3[remap]
    style NG_range_vector3_inlowINT fill:#0bb, color:#111
    NG_range_vector3_inhighINT([inhigh]) ==.inhigh==> NG_range_vector3_N_remap1_vector3[remap]
    style NG_range_vector3_inhighINT fill:#0bb, color:#111
    NG_range_vector3_N_recip_vector3[divide] --".in2"--> NG_range_vector3_N_pow_vector3[power]
    NG_range_vector3_gammaINT([gamma]) ==.in2==> NG_range_vector3_N_recip_vector3[divide]
    style NG_range_vector3_gammaINT fill:#0bb, color:#111
    NG_range_vector3_N_sign_vector3[sign] --".in2"--> NG_range_vector3_N_gamma_vector3[multiply]
    NG_range_vector3_N_remap1_vector3[remap] --".in"--> NG_range_vector3_N_sign_vector3[sign]
    NG_range_vector3_N_remap2_vector3[remap] --".in2"--> NG_range_vector3_N_switch_vector3{ifequal}
```
