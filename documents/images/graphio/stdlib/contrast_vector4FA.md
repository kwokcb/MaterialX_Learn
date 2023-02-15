```mermaid
graph LR; 
    NG_contrast_vector4FA_N_add_vector4FA[add] --> NG_contrast_vector4FA_out([out])
    style NG_contrast_vector4FA_out fill:#1b1, color:#111
    NG_contrast_vector4FA_pivotINT([pivot]) ==.in2==> NG_contrast_vector4FA_N_add_vector4FA[add]
    style NG_contrast_vector4FA_pivotINT fill:#0bb, color:#111
    NG_contrast_vector4FA_N_mul_vector4FA[multiply] --".in1"--> NG_contrast_vector4FA_N_add_vector4FA[add]
    NG_contrast_vector4FA_amountINT([amount]) ==.in2==> NG_contrast_vector4FA_N_mul_vector4FA[multiply]
    style NG_contrast_vector4FA_amountINT fill:#0bb, color:#111
    NG_contrast_vector4FA_N_sub_vector4FA[subtract] --".in1"--> NG_contrast_vector4FA_N_mul_vector4FA[multiply]
    NG_contrast_vector4FA_inINT([in]) ==.in1==> NG_contrast_vector4FA_N_sub_vector4FA[subtract]
    style NG_contrast_vector4FA_inINT fill:#0bb, color:#111
    NG_contrast_vector4FA_pivotINT([pivot]) ==.in2==> NG_contrast_vector4FA_N_sub_vector4FA[subtract]
    style NG_contrast_vector4FA_pivotINT fill:#0bb, color:#111
```
