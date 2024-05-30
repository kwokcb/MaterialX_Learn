```mermaid
graph LR
    subgraph nodegraph1
    nodegraph1/sides([sides:10])
    style nodegraph1/sides  fill:#09D, color:#111
    nodegraph1/width([width:1])
    style nodegraph1/width  fill:#09D, color:#111
    nodegraph1/height([height:1])
    style nodegraph1/height  fill:#09D, color:#111
    nodegraph1/output_float([output_float])
    style nodegraph1/output_float   fill:#0C0, color:#111
    nodegraph1/PI([PI:3.141592653589793238462643])
    style nodegraph1/PI  fill:#500, color:#111
    nodegraph1/cos_float[cos_float]
    nodegraph1/aWidth[aWidth]
    nodegraph1/aHeight[aHeight]
    nodegraph1/texcoord_vector2[texcoord_vector2]
    nodegraph1/times_2[times_2]
    nodegraph1/minus_1[minus_1]
    nodegraph1/width_height_vec[width_height_vec]
    nodegraph1/uv[uv]
    nodegraph1/convert_float_surfaceshader[convert_float_surfaceshader:0]
    nodegraph1/multiply_vector2[multiply_vector2]
    nodegraph1/pCoord[pCoord]
    nodegraph1/convert_vector2_surfaceshader[convert_vector2_surfaceshader:0, 0]
    nodegraph1/unity_note[unity_note:https://docs.unity3d.com/Packages/com.unity.shadergraph@6.9/manual/Polygon-Node.html]
    nodegraph1/extract_x[extract_x]
    nodegraph1/extract_y[extract_y]
    nodegraph1/pi_div_sides[pi_div_sides]
    nodegraph1/r[r]
    nodegraph1/pCoord_plus_half[pCoord_plus_half]
    nodegraph1/divide_r[divide_r]
    nodegraph1/floor_float[floor_float]
    nodegraph1/multiply_r[multiply_r]
    nodegraph1/subtract_pCoord[subtract_pCoord]
    nodegraph1/cos_float2[cos_float2]
    nodegraph1/distance[distance]
    nodegraph1/length_texcoord[length_texcoord]
    nodegraph1/clamp_float[clamp_float]
    nodegraph1/one_min_distance[one_min_distance]
    nodegraph1/divide_float3[divide_float3]
    end
    nodegraph1/pi_div_sides --"in"--> nodegraph1/cos_float
    nodegraph1/width --"in2"--> nodegraph1/aWidth
    nodegraph1/cos_float --"in1"--> nodegraph1/aWidth
    nodegraph1/height --"in2"--> nodegraph1/aHeight
    nodegraph1/cos_float --"in1"--> nodegraph1/aHeight
    nodegraph1/texcoord_vector2 --"in1"--> nodegraph1/times_2
    nodegraph1/times_2 --"in1"--> nodegraph1/minus_1
    nodegraph1/aWidth --"in1"--> nodegraph1/width_height_vec
    nodegraph1/aHeight --"in2"--> nodegraph1/width_height_vec
    nodegraph1/width_height_vec --"in2"--> nodegraph1/uv
    nodegraph1/minus_1 --"in1"--> nodegraph1/uv
    nodegraph1/uv --"in1"--> nodegraph1/multiply_vector2
    nodegraph1/extract_x --"inx"--> nodegraph1/pCoord
    nodegraph1/extract_y --"iny"--> nodegraph1/pCoord
    nodegraph1/multiply_vector2 --"in"--> nodegraph1/extract_x
    nodegraph1/multiply_vector2 --"in"--> nodegraph1/extract_y
    nodegraph1/PI --"in1"--> nodegraph1/pi_div_sides
    nodegraph1/sides --"in2"--> nodegraph1/pi_div_sides
    nodegraph1/pi_div_sides --"in1"--> nodegraph1/r
    nodegraph1/pCoord --"in1"--> nodegraph1/pCoord_plus_half
    nodegraph1/r --"in2"--> nodegraph1/divide_r
    nodegraph1/pCoord_plus_half --"in1"--> nodegraph1/divide_r
    nodegraph1/divide_r --"in"--> nodegraph1/floor_float
    nodegraph1/r --"in2"--> nodegraph1/multiply_r
    nodegraph1/floor_float --"in1"--> nodegraph1/multiply_r
    nodegraph1/multiply_r --"in1"--> nodegraph1/subtract_pCoord
    nodegraph1/pCoord --"in2"--> nodegraph1/subtract_pCoord
    nodegraph1/subtract_pCoord --"in"--> nodegraph1/cos_float2
    nodegraph1/cos_float2 --"in1"--> nodegraph1/distance
    nodegraph1/length_texcoord --"in2"--> nodegraph1/distance
    nodegraph1/multiply_vector2 --"in"--> nodegraph1/length_texcoord
    nodegraph1/divide_float3 --"in"--> nodegraph1/clamp_float
    nodegraph1/distance --"in2"--> nodegraph1/one_min_distance
    nodegraph1/one_min_distance --"in1"--> nodegraph1/divide_float3
    nodegraph1/clamp_float --> nodegraph1/output_float
```