
// lin_ap1 to lin_rec709 function. Texture count: 0

vec4 mx_lin_ap1_to_lin_rec709_color4(vec4 inPixel)
{
  vec4 outColor = inPixel;
  
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
