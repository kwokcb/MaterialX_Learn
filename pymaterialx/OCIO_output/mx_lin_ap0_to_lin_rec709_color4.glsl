
// lin_ap0 to lin_rec709 function. Texture count: 0

vec4 mx_lin_ap0_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
  // Add Matrix processing
  
  {
    vec4 res = vec4(outColor.rgb.r, outColor.rgb.g, outColor.rgb.b, outColor.a);
    vec4 tmp = res;
    res = mat4(2.5216861867438798, -0.27647991422992202, -0.015378064966034201, 0., -1.1341309882397199, 1.37271908766826, -0.152975335867399, 0., -0.38755519850416398, -0.096239173438334005, 1.16835340083343, 0., 0., 0., 0., 1.) * tmp;
    outColor.rgb = vec3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}
