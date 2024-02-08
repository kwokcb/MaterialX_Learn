```mermaid
graph LR; 
    NG_range_color4FA_N_switch_color4FA{ifequal} --> NG_range_color4FA_out([out])
    style NG_range_color4FA_out fill:#1b1, color:#111
    NG_range_color4FA_doclampINT([doclamp]) ==.value1==> NG_range_color4FA_N_switch_color4FA[ifequal]
    style NG_range_color4FA_doclampINT fill:#0bb, color:#111
    NG_range_color4FA_N_clamp_color4FA[clamp] --".in1"--> NG_range_color4FA_N_switch_color4FA{ifequal}
    NG_range_color4FA_outlowINT([outlow]) ==.low==> NG_range_color4FA_N_clamp_color4FA[clamp]
    style NG_range_color4FA_outlowINT fill:#0bb, color:#111
    NG_range_color4FA_outhighINT([outhigh]) ==.high==> NG_range_color4FA_N_clamp_color4FA[clamp]
    style NG_range_color4FA_outhighINT fill:#0bb, color:#111
    NG_range_color4FA_N_remap2_color4FA[remap] --".in"--> NG_range_color4FA_N_clamp_color4FA[clamp]
    NG_range_color4FA_outlowINT([outlow]) ==.outlow==> NG_range_color4FA_N_remap2_color4FA[remap]
    style NG_range_color4FA_outlowINT fill:#0bb, color:#111
    NG_range_color4FA_outhighINT([outhigh]) ==.outhigh==> NG_range_color4FA_N_remap2_color4FA[remap]
    style NG_range_color4FA_outhighINT fill:#0bb, color:#111
    NG_range_color4FA_N_gamma_color4FA[multiply] --".in"--> NG_range_color4FA_N_remap2_color4FA[remap]
    NG_range_color4FA_N_pow_color4FA[power] --".in1"--> NG_range_color4FA_N_gamma_color4FA[multiply]
    NG_range_color4FA_N_abs_color4FA[absval] --".in1"--> NG_range_color4FA_N_pow_color4FA[power]
    NG_range_color4FA_N_remap1_color4FA[remap] --".in"--> NG_range_color4FA_N_abs_color4FA[absval]
    NG_range_color4FA_inINT([in]) ==.in==> NG_range_color4FA_N_remap1_color4FA[remap]
    style NG_range_color4FA_inINT fill:#0bb, color:#111
    NG_range_color4FA_inlowINT([inlow]) ==.inlow==> NG_range_color4FA_N_remap1_color4FA[remap]
    style NG_range_color4FA_inlowINT fill:#0bb, color:#111
    NG_range_color4FA_inhighINT([inhigh]) ==.inhigh==> NG_range_color4FA_N_remap1_color4FA[remap]
    style NG_range_color4FA_inhighINT fill:#0bb, color:#111
    NG_range_color4FA_N_recip_color4FA[divide] --".in2"--> NG_range_color4FA_N_pow_color4FA[power]
    NG_range_color4FA_gammaINT([gamma]) ==.in2==> NG_range_color4FA_N_recip_color4FA[divide]
    style NG_range_color4FA_gammaINT fill:#0bb, color:#111
    NG_range_color4FA_N_sign_color4FA[sign] --".in2"--> NG_range_color4FA_N_gamma_color4FA[multiply]
    NG_range_color4FA_N_remap1_color4FA[remap] --".in"--> NG_range_color4FA_N_sign_color4FA[sign]
    NG_range_color4FA_N_remap2_color4FA[remap] --".in2"--> NG_range_color4FA_N_switch_color4FA{ifequal}
```
