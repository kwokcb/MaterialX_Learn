
// g22_ap1 to lin_rec709 function. Texture count: 0

vec4 mx_g22_ap1_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
  // Add Gamma 'basicPassThruFwd' processing
  
  {
    vec4 gamma = vec4(2.2000000000000002, 2.2000000000000002, 2.2000000000000002, 1.);
    vec4 breakPnt = vec4(0., 0., 0., 0.);
    vec4 isAboveBreak = vec4(greaterThan( outColor, breakPnt));
    vec4 powSeg = pow(max( vec4(0., 0., 0., 0.), outColor ), gamma);
    vec4 res = isAboveBreak * powSeg + ( vec4(1., 1., 1., 1.) - isAboveBreak ) * outColor;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }
  
  // Add Matrix processing
  
  {
    vec4 res = vec4(outColor.rgb.r, outColor.rgb.g, outColor.rgb.b, outColor.a);
    vec4 tmp = res;
    res = mat4(1.7050509926579756, -0.13025641750704287, -0.02400335680461799, 0., -0.62179212065700873, 1.1408047365754079, -0.12896897606497126, 0., -0.083258872000981698, -0.010548319068357195, 1.152972332869586, 0., 0., 0., 0., 1.) * tmp;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}
