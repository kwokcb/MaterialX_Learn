
// Declaration of class wrapper

struct mx_acescg_to_lin_rec709_color4mx_acescg_to_lin_rec709_color4
{
mx_acescg_to_lin_rec709_color4mx_acescg_to_lin_rec709_color4(
)
{
}


// Declaration of the OCIO shader function

float4 mx_acescg_to_lin_rec709_color4(float4 inPixel)
{
  float4 outColor = inPixel;
  
  // Add Matrix processing
  
  {
    float4 res = float4(outColor.rgb.r, outColor.rgb.g, outColor.rgb.b, outColor.a);
    float4 tmp = res;
    res = float4x4(1.7050509926579815, -0.1302564175070435, -0.024003356804618042, 0., -0.62179212065700562, 1.1408047365754048, -0.1289689760649709, 0., -0.0832588720009797, -0.010548319068357653, 1.1529723328695858, 0., 0., 0., 0., 1.) * tmp;
    outColor.rgb = float3(res.x, res.y, res.z);
    outColor.a = res.w;
  }

  return outColor;
}

// Close class wrapper


};
float4 mx_acescg_to_lin_rec709_color4(
  float4 inPixel)
{
  return mx_acescg_to_lin_rec709_color4mx_acescg_to_lin_rec709_color4(
  ).mx_acescg_to_lin_rec709_color4(inPixel);
}
