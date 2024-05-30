```mermaid
graph LR
    subgraph nodegraph1
    style nodegraph1_sides  fill:#09D, color:#FFF
    nodegraph1_sides([sides:10])
    style nodegraph1_width  fill:#09D, color:#FFF
    nodegraph1_width([width:1])
    style nodegraph1_height  fill:#09D, color:#FFF
    nodegraph1_height([height:1])
    style nodegraph1_output_float  fill:#0C0, color:#FFF
    nodegraph1_output_float([output_float])
    style nodegraph1_PI  fill:#500, color:#FFF
    nodegraph1_PI([PI:3.141592653589793238462643])
    nodegraph1_cos_float[cos_float]
    nodegraph1_aWidth[aWidth]
    nodegraph1_aHeight[aHeight]
    nodegraph1_texcoord_vector2[texcoord_vector2]
    nodegraph1_times_2[times_2]
    nodegraph1_minus_1[minus_1]
    nodegraph1_width_height_vec[width_height_vec]
    nodegraph1_uv[uv]
    nodegraph1_convert_float_surfaceshader[convert_float_surfaceshader:0]
    nodegraph1_multiply_vector2[multiply_vector2]
    nodegraph1_pCoord[pCoord]
    nodegraph1_convert_vector2_surfaceshader[convert_vector2_surfaceshader:0, 0]
    nodegraph1_unity_note[unity_note:https://docs.unity3d.com/Packages/com.unity.shadergraph@6.9/manual/Polygon-Node.html]
    nodegraph1_extract_x[extract_x]
    nodegraph1_extract_y[extract_y]
    nodegraph1_pi_div_sides[pi_div_sides]
    nodegraph1_r[r]
    nodegraph1_pCoord_plus_half[pCoord_plus_half]
    nodegraph1_divide_r[divide_r]
    nodegraph1_floor_float[floor_float]
    nodegraph1_multiply_r[multiply_r]
    nodegraph1_subtract_pCoord[subtract_pCoord]
    nodegraph1_cos_float2[cos_float2]
    nodegraph1_distance[distance]
    nodegraph1_length_texcoord[length_texcoord]
    nodegraph1_clamp_float[clamp_float]
    nodegraph1_one_min_distance[one_min_distance]
    nodegraph1_divide_float3[divide_float3]
    end
    nodegraph1_pi_div_sides --"in"--> nodegraph1_cos_float
    nodegraph1_width --"in2"--> nodegraph1_aWidth
    nodegraph1_cos_float --"in1"--> nodegraph1_aWidth
    nodegraph1_height --"in2"--> nodegraph1_aHeight
    nodegraph1_cos_float --"in1"--> nodegraph1_aHeight
    nodegraph1_texcoord_vector2 --"in1"--> nodegraph1_times_2
    nodegraph1_times_2 --"in1"--> nodegraph1_minus_1
    nodegraph1_aWidth --"in1"--> nodegraph1_width_height_vec
    nodegraph1_aHeight --"in2"--> nodegraph1_width_height_vec
    nodegraph1_width_height_vec --"in2"--> nodegraph1_uv
    nodegraph1_minus_1 --"in1"--> nodegraph1_uv
    nodegraph1_uv --"in1"--> nodegraph1_multiply_vector2
    nodegraph1_extract_x --"inx"--> nodegraph1_pCoord
    nodegraph1_extract_y --"iny"--> nodegraph1_pCoord
    nodegraph1_multiply_vector2 --"in"--> nodegraph1_extract_x
    nodegraph1_multiply_vector2 --"in"--> nodegraph1_extract_y
    nodegraph1_PI --"in1"--> nodegraph1_pi_div_sides
    nodegraph1_sides --"in2"--> nodegraph1_pi_div_sides
    nodegraph1_pi_div_sides --"in1"--> nodegraph1_r
    nodegraph1_pCoord --"in1"--> nodegraph1_pCoord_plus_half
    nodegraph1_r --"in2"--> nodegraph1_divide_r
    nodegraph1_pCoord_plus_half --"in1"--> nodegraph1_divide_r
    nodegraph1_divide_r --"in"--> nodegraph1_floor_float
    nodegraph1_r --"in2"--> nodegraph1_multiply_r
    nodegraph1_floor_float --"in1"--> nodegraph1_multiply_r
    nodegraph1_multiply_r --"in1"--> nodegraph1_subtract_pCoord
    nodegraph1_pCoord --"in2"--> nodegraph1_subtract_pCoord
    nodegraph1_subtract_pCoord --"in"--> nodegraph1_cos_float2
    nodegraph1_cos_float2 --"in1"--> nodegraph1_distance
    nodegraph1_length_texcoord --"in2"--> nodegraph1_distance
    nodegraph1_multiply_vector2 --"in"--> nodegraph1_length_texcoord
    nodegraph1_divide_float3 --"in"--> nodegraph1_clamp_float
    nodegraph1_distance --"in2"--> nodegraph1_one_min_distance
    nodegraph1_one_min_distance --"in1"--> nodegraph1_divide_float3
    nodegraph1_clamp_float --> nodegraph1_output_float
```