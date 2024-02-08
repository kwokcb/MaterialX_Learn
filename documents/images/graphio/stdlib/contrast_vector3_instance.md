```mermaid
graph LR; 
    NG_contrast_vector3_N_add_vector3[add] --> NG_contrast_vector3_out([out])
    style NG_contrast_vector3_out fill:#1b1, color:#111
    NG_contrast_vector3_pivotINT([pivot]) ==.in2==> NG_contrast_vector3_N_add_vector3[add]
    style NG_contrast_vector3_pivotINT fill:#0bb, color:#111
    NG_contrast_vector3_N_mul_vector3[multiply] --".in1"--> NG_contrast_vector3_N_add_vector3[add]
    NG_contrast_vector3_amountINT([amount]) ==.in2==> NG_contrast_vector3_N_mul_vector3[multiply]
    style NG_contrast_vector3_amountINT fill:#0bb, color:#111
    NG_contrast_vector3_N_sub_vector3[subtract] --".in1"--> NG_contrast_vector3_N_mul_vector3[multiply]
    NG_contrast_vector3_inINT([in]) ==.in1==> NG_contrast_vector3_N_sub_vector3[subtract]
    style NG_contrast_vector3_inINT fill:#0bb, color:#111
    NG_contrast_vector3_pivotINT([pivot]) ==.in2==> NG_contrast_vector3_N_sub_vector3[subtract]
    style NG_contrast_vector3_pivotINT fill:#0bb, color:#111
```
