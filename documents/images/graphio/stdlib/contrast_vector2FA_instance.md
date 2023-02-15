```mermaid
graph LR; 
    NG_contrast_vector2FA_N_add_vector2FA[add] --> NG_contrast_vector2FA_out([out])
    style NG_contrast_vector2FA_out fill:#1b1, color:#111
    NG_contrast_vector2FA_pivotINT([pivot]) ==.in2==> NG_contrast_vector2FA_N_add_vector2FA[add]
    style NG_contrast_vector2FA_pivotINT fill:#0bb, color:#111
    NG_contrast_vector2FA_N_mul_vector2FA[multiply] --".in1"--> NG_contrast_vector2FA_N_add_vector2FA[add]
    NG_contrast_vector2FA_amountINT([amount]) ==.in2==> NG_contrast_vector2FA_N_mul_vector2FA[multiply]
    style NG_contrast_vector2FA_amountINT fill:#0bb, color:#111
    NG_contrast_vector2FA_N_sub_vector2FA[subtract] --".in1"--> NG_contrast_vector2FA_N_mul_vector2FA[multiply]
    NG_contrast_vector2FA_inINT([in]) ==.in1==> NG_contrast_vector2FA_N_sub_vector2FA[subtract]
    style NG_contrast_vector2FA_inINT fill:#0bb, color:#111
    NG_contrast_vector2FA_pivotINT([pivot]) ==.in2==> NG_contrast_vector2FA_N_sub_vector2FA[subtract]
    style NG_contrast_vector2FA_pivotINT fill:#0bb, color:#111
```
