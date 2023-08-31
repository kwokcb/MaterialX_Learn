
// srgb_texture to lin_rec709 function. Texture count: 0

vec4 mx_srgb_texture_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
  // Add Gamma 'monCurveFwd' processing
  
  {
    vec4 breakPnt = vec4(0.0392857157, 0.0392857157, 0.0392857157, 1.);
    vec4 slope = vec4(0.077380158, 0.077380158, 0.077380158, 1.);
    vec4 scale = vec4(0.947867274, 0.947867274, 0.947867274, 0.999998987);
    vec4 offset = vec4(0.0521326996, 0.0521326996, 0.0521326996, 9.99998974e-07);
    vec4 gamma = vec4(2.4000001, 2.4000001, 2.4000001, 1.00000095);
    vec4 isAboveBreak = vec4(greaterThan( outColor, breakPnt));
    vec4 linSeg = outColor * slope;
    vec4 powSeg = pow( max( vec4(0., 0., 0., 0.), scale * outColor + offset), gamma);
    vec4 res = isAboveBreak * powSeg + ( vec4(1., 1., 1., 1.) - isAboveBreak ) * linSeg;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}
