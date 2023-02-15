```mermaid
graph LR; 
    NG_range_vector3FA_N_switch_vector3FA{ifequal} --> NG_range_vector3FA_out([out])
    style NG_range_vector3FA_out fill:#1b1, color:#111
    NG_range_vector3FA_doclampINT([doclamp]) ==.value1==> NG_range_vector3FA_N_switch_vector3FA[ifequal]
    style NG_range_vector3FA_doclampINT fill:#0bb, color:#111
    NG_range_vector3FA_N_clamp_vector3FA[clamp] --".in1"--> NG_range_vector3FA_N_switch_vector3FA{ifequal}
    NG_range_vector3FA_outlowINT([outlow]) ==.low==> NG_range_vector3FA_N_clamp_vector3FA[clamp]
    style NG_range_vector3FA_outlowINT fill:#0bb, color:#111
    NG_range_vector3FA_outhighINT([outhigh]) ==.high==> NG_range_vector3FA_N_clamp_vector3FA[clamp]
    style NG_range_vector3FA_outhighINT fill:#0bb, color:#111
    NG_range_vector3FA_N_remap2_vector3FA[remap] --".in"--> NG_range_vector3FA_N_clamp_vector3FA[clamp]
    NG_range_vector3FA_outlowINT([outlow]) ==.outlow==> NG_range_vector3FA_N_remap2_vector3FA[remap]
    style NG_range_vector3FA_outlowINT fill:#0bb, color:#111
    NG_range_vector3FA_outhighINT([outhigh]) ==.outhigh==> NG_range_vector3FA_N_remap2_vector3FA[remap]
    style NG_range_vector3FA_outhighINT fill:#0bb, color:#111
    NG_range_vector3FA_N_gamma_vector3FA[multiply] --".in"--> NG_range_vector3FA_N_remap2_vector3FA[remap]
    NG_range_vector3FA_N_pow_vector3FA[power] --".in1"--> NG_range_vector3FA_N_gamma_vector3FA[multiply]
    NG_range_vector3FA_N_abs_vector3FA[absval] --".in1"--> NG_range_vector3FA_N_pow_vector3FA[power]
    NG_range_vector3FA_N_remap1_vector3FA[remap] --".in"--> NG_range_vector3FA_N_abs_vector3FA[absval]
    NG_range_vector3FA_inINT([in]) ==.in==> NG_range_vector3FA_N_remap1_vector3FA[remap]
    style NG_range_vector3FA_inINT fill:#0bb, color:#111
    NG_range_vector3FA_inlowINT([inlow]) ==.inlow==> NG_range_vector3FA_N_remap1_vector3FA[remap]
    style NG_range_vector3FA_inlowINT fill:#0bb, color:#111
    NG_range_vector3FA_inhighINT([inhigh]) ==.inhigh==> NG_range_vector3FA_N_remap1_vector3FA[remap]
    style NG_range_vector3FA_inhighINT fill:#0bb, color:#111
    NG_range_vector3FA_N_recip_vector3FA[divide] --".in2"--> NG_range_vector3FA_N_pow_vector3FA[power]
    NG_range_vector3FA_gammaINT([gamma]) ==.in2==> NG_range_vector3FA_N_recip_vector3FA[divide]
    style NG_range_vector3FA_gammaINT fill:#0bb, color:#111
    NG_range_vector3FA_N_sign_vector3FA[sign] --".in2"--> NG_range_vector3FA_N_gamma_vector3FA[multiply]
    NG_range_vector3FA_N_remap1_vector3FA[remap] --".in"--> NG_range_vector3FA_N_sign_vector3FA[sign]
    NG_range_vector3FA_N_remap2_vector3FA[remap] --".in2"--> NG_range_vector3FA_N_switch_vector3FA{ifequal}
```
