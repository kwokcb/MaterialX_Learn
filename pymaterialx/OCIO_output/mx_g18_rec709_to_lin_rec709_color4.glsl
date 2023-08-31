
// g18_rec709 to lin_rec709 function. Texture count: 0

vec4 mx_g18_rec709_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
  // Add Gamma 'basicPassThruFwd' processing
  
  {
    vec4 gamma = vec4(1.8, 1.8, 1.8, 1.);
    vec4 breakPnt = vec4(0., 0., 0., 0.);
    vec4 isAboveBreak = vec4(greaterThan( outColor, breakPnt));
    vec4 powSeg = pow(max( vec4(0., 0., 0., 0.), outColor ), gamma);
    vec4 res = isAboveBreak * powSeg + ( vec4(1., 1., 1., 1.) - isAboveBreak ) * outColor;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}
