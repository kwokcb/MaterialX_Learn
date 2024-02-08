```mermaid
graph LR; 
    NG_range_vector2FA_N_switch_vector2FA{ifequal} --> NG_range_vector2FA_out([out])
    style NG_range_vector2FA_out fill:#1b1, color:#111
    NG_range_vector2FA_doclampINT([doclamp]) ==.value1==> NG_range_vector2FA_N_switch_vector2FA[ifequal]
    style NG_range_vector2FA_doclampINT fill:#0bb, color:#111
    NG_range_vector2FA_N_clamp_vector2FA[clamp] --".in1"--> NG_range_vector2FA_N_switch_vector2FA{ifequal}
    NG_range_vector2FA_outlowINT([outlow]) ==.low==> NG_range_vector2FA_N_clamp_vector2FA[clamp]
    style NG_range_vector2FA_outlowINT fill:#0bb, color:#111
    NG_range_vector2FA_outhighINT([outhigh]) ==.high==> NG_range_vector2FA_N_clamp_vector2FA[clamp]
    style NG_range_vector2FA_outhighINT fill:#0bb, color:#111
    NG_range_vector2FA_N_remap2_vector2FA[remap] --".in"--> NG_range_vector2FA_N_clamp_vector2FA[clamp]
    NG_range_vector2FA_outlowINT([outlow]) ==.outlow==> NG_range_vector2FA_N_remap2_vector2FA[remap]
    style NG_range_vector2FA_outlowINT fill:#0bb, color:#111
    NG_range_vector2FA_outhighINT([outhigh]) ==.outhigh==> NG_range_vector2FA_N_remap2_vector2FA[remap]
    style NG_range_vector2FA_outhighINT fill:#0bb, color:#111
    NG_range_vector2FA_N_gamma_vector2FA[multiply] --".in"--> NG_range_vector2FA_N_remap2_vector2FA[remap]
    NG_range_vector2FA_N_pow_vector2FA[power] --".in1"--> NG_range_vector2FA_N_gamma_vector2FA[multiply]
    NG_range_vector2FA_N_abs_vector2FA[absval] --".in1"--> NG_range_vector2FA_N_pow_vector2FA[power]
    NG_range_vector2FA_N_remap1_vector2FA[remap] --".in"--> NG_range_vector2FA_N_abs_vector2FA[absval]
    NG_range_vector2FA_inINT([in]) ==.in==> NG_range_vector2FA_N_remap1_vector2FA[remap]
    style NG_range_vector2FA_inINT fill:#0bb, color:#111
    NG_range_vector2FA_inlowINT([inlow]) ==.inlow==> NG_range_vector2FA_N_remap1_vector2FA[remap]
    style NG_range_vector2FA_inlowINT fill:#0bb, color:#111
    NG_range_vector2FA_inhighINT([inhigh]) ==.inhigh==> NG_range_vector2FA_N_remap1_vector2FA[remap]
    style NG_range_vector2FA_inhighINT fill:#0bb, color:#111
    NG_range_vector2FA_N_recip_vector2FA[divide] --".in2"--> NG_range_vector2FA_N_pow_vector2FA[power]
    NG_range_vector2FA_gammaINT([gamma]) ==.in2==> NG_range_vector2FA_N_recip_vector2FA[divide]
    style NG_range_vector2FA_gammaINT fill:#0bb, color:#111
    NG_range_vector2FA_N_sign_vector2FA[sign] --".in2"--> NG_range_vector2FA_N_gamma_vector2FA[multiply]
    NG_range_vector2FA_N_remap1_vector2FA[remap] --".in"--> NG_range_vector2FA_N_sign_vector2FA[sign]
    NG_range_vector2FA_N_remap2_vector2FA[remap] --".in2"--> NG_range_vector2FA_N_switch_vector2FA{ifequal}
```
