
// acescct_ap1 to lin_rec709 function. Texture count: 0

vec4 mx_acescct_ap1_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
  // Add Log 'Camera Log to Lin' processing
  
  {
    vec3 log_break = vec3(0.155251175, 0.155251175, 0.155251175);
    vec3 linear_segment_offset = vec3(0.0729055703, 0.0729055703, 0.0729055703);
    vec3 linear_segment_slopeinv = vec3(0.0948745236, 0.0948745236, 0.0948745236);
    vec3 lin_slopeinv = vec3(1., 1., 1.);
    vec3 lin_offset = vec3(0., 0., 0.);
    vec3 log_slopeinv = vec3(17.5200005, 17.5200005, 17.5200005);
    vec3 log_base = vec3(2., 2., 2.);
    vec3 log_offset = vec3(0.5547945205479452, 0.5547945205479452, 0.5547945205479452);
    vec3 isAboveBreak = vec3(greaterThan( outColor.rgb, log_break));
    vec3 linSeg = ( outColor.rgb - linear_segment_offset ) * linear_segment_slopeinv;
    vec3 logSeg = (outColor.rgb - log_offset) * log_slopeinv;
    logSeg = pow(log_base, logSeg);
    logSeg = lin_slopeinv * (logSeg - lin_offset);
    outColor.rgb = isAboveBreak * logSeg + ( vec3(1., 1., 1.) - isAboveBreak ) * linSeg;
  }
  
  // Add Matrix processing
  
  {
    vec4 res = vec4(outColor.rgb.r, outColor.rgb.g, outColor.rgb.b, outColor.a);
    vec4 tmp = res;
    res = mat4(1.7050509926579815, -0.1302564175070435, -0.024003356804618042, 0., -0.62179212065700562, 1.1408047365754048, -0.1289689760649709, 0., -0.0832588720009797, -0.010548319068357653, 1.1529723328695858, 0., 0., 0., 0., 1.) * tmp;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}
