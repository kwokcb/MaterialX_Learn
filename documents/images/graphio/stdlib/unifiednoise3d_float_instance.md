```mermaid
graph LR; 
    NG_unifiednoise3d_float_N_range[range] --> NG_unifiednoise3d_float_out([out])
    style NG_unifiednoise3d_float_out fill:#1b1, color:#111
    NG_unifiednoise3d_float_outminINT([outmin]) ==.outlow==> NG_unifiednoise3d_float_N_range[range]
    style NG_unifiednoise3d_float_outminINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_outmaxINT([outmax]) ==.outhigh==> NG_unifiednoise3d_float_N_range[range]
    style NG_unifiednoise3d_float_outmaxINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_clampoutputINT([clampoutput]) ==.doclamp==> NG_unifiednoise3d_float_N_range[range]
    style NG_unifiednoise3d_float_clampoutputINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_switch_type{switch} --".in"--> NG_unifiednoise3d_float_N_range[range]
    NG_unifiednoise3d_float_typeINT([type]) ==.which==> NG_unifiednoise3d_float_N_switch_type[switch]
    style NG_unifiednoise3d_float_typeINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_perlin_noise3d[noise3d] --".in1"--> NG_unifiednoise3d_float_N_switch_type{switch}
    NG_unifiednoise3d_float_N_apply_cell_jitter[rotate3d] --".position"--> NG_unifiednoise3d_float_N_perlin_noise3d[noise3d]
    NG_unifiednoise3d_float_N_apply_offset[add] --".in"--> NG_unifiednoise3d_float_N_apply_cell_jitter[rotate3d]
    NG_unifiednoise3d_float_offsetINT([offset]) ==.in2==> NG_unifiednoise3d_float_N_apply_offset[add]
    style NG_unifiednoise3d_float_offsetINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_apply_freq[multiply] --".in1"--> NG_unifiednoise3d_float_N_apply_offset[add]
    NG_unifiednoise3d_float_positionINT([position]) ==.in1==> NG_unifiednoise3d_float_N_apply_freq[multiply]
    style NG_unifiednoise3d_float_positionINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_freqINT([freq]) ==.in2==> NG_unifiednoise3d_float_N_apply_freq[multiply]
    style NG_unifiednoise3d_float_freqINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_cell_jitter_mult[multiply] --".amount"--> NG_unifiednoise3d_float_N_apply_cell_jitter[rotate3d]
    NG_unifiednoise3d_float_N_jitter_minus_one[subtract] --".in1"--> NG_unifiednoise3d_float_N_cell_jitter_mult[multiply]
    NG_unifiednoise3d_float_jitterINT([jitter]) ==.in1==> NG_unifiednoise3d_float_N_jitter_minus_one[subtract]
    style NG_unifiednoise3d_float_jitterINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_cellnoise3d[cellnoise3d] --".in2"--> NG_unifiednoise3d_float_N_switch_type{switch}
    NG_unifiednoise3d_float_N_apply_cell_jitter[rotate3d] --".position"--> NG_unifiednoise3d_float_N_cellnoise3d[cellnoise3d]
    NG_unifiednoise3d_float_N_worleynoise3d[worleynoise3d] --".in3"--> NG_unifiednoise3d_float_N_switch_type{switch}
    NG_unifiednoise3d_float_jitterINT([jitter]) ==.jitter==> NG_unifiednoise3d_float_N_worleynoise3d[worleynoise3d]
    style NG_unifiednoise3d_float_jitterINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_apply_offset[add] --".position"--> NG_unifiednoise3d_float_N_worleynoise3d[worleynoise3d]
    NG_unifiednoise3d_float_N_fractal3d[fractal3d] --".in4"--> NG_unifiednoise3d_float_N_switch_type{switch}
    NG_unifiednoise3d_float_octavesINT([octaves]) ==.octaves==> NG_unifiednoise3d_float_N_fractal3d[fractal3d]
    style NG_unifiednoise3d_float_octavesINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_lacunarityINT([lacunarity]) ==.lacunarity==> NG_unifiednoise3d_float_N_fractal3d[fractal3d]
    style NG_unifiednoise3d_float_lacunarityINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_diminishINT([diminish]) ==.diminish==> NG_unifiednoise3d_float_N_fractal3d[fractal3d]
    style NG_unifiednoise3d_float_diminishINT fill:#0bb, color:#111
    NG_unifiednoise3d_float_N_apply_cell_jitter[rotate3d] --".position"--> NG_unifiednoise3d_float_N_fractal3d[fractal3d]
```
