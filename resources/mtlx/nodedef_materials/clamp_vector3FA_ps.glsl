#version 400

struct BSDF { vec3 response; vec3 throughput; float thickness; float ior; };
#define EDF vec3
struct surfaceshader { vec3 color; vec3 transparency; };
struct volumeshader { vec3 color; vec3 transparency; };
struct displacementshader { vec3 offset; float scale; };
struct lightshader { vec3 intensity; vec3 direction; };
#define material surfaceshader

// Uniform block: PrivateUniforms
uniform sampler2D u_shadowMap;
uniform mat4 u_shadowMatrix = mat4(1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000);
uniform mat4 u_envMatrix = mat4(-1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 0.000000, -1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000);
uniform sampler2D u_envRadiance;
uniform int u_envRadianceMips = 1;
uniform int u_envRadianceSamples = 16;
uniform sampler2D u_envIrradiance;
uniform bool u_refractionEnv = false;
uniform vec3 u_refractionColor = vec3(0.0);
uniform int u_numActiveLightSources = 0;

// Uniform block: PublicUniforms
uniform displacementshader displacementshader1;
uniform vec3 clamp_vector3FA_in = vec3(0.000000, 0.000000, 0.000000);
uniform float clamp_vector3FA_low = 0.000000;
uniform float clamp_vector3FA_high = 1.000000;

// Pixel shader outputs
out vec4 out1;

#define M_FLOAT_EPS 1e-8

float mx_square(float x)
{
    return x*x;
}

vec2 mx_square(vec2 x)
{
    return x*x;
}

vec3 mx_square(vec3 x)
{
    return x*x;
}

#define DIRECTIONAL_ALBEDO_METHOD 0

#define MAX_LIGHT_SOURCES 3
#define M_PI 3.1415926535897932
#define M_PI_INV (1.0 / M_PI)

float mx_pow5(float x)
{
    return mx_square(mx_square(x)) * x;
}

// Standard Schlick Fresnel
float mx_fresnel_schlick(float cosTheta, float F0)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    float x5 = mx_pow5(x);
    return F0 + (1.0 - F0) * x5;
}
vec3 mx_fresnel_schlick(float cosTheta, vec3 F0)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    float x5 = mx_pow5(x);
    return F0 + (1.0 - F0) * x5;
}

// Generalized Schlick Fresnel
float mx_fresnel_schlick(float cosTheta, float F0, float F90)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    float x5 = mx_pow5(x);
    return mix(F0, F90, x5);
}
vec3 mx_fresnel_schlick(float cosTheta, vec3 F0, vec3 F90)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    float x5 = mx_pow5(x);
    return mix(F0, F90, x5);
}

// Generalized Schlick Fresnel with a variable exponent
float mx_fresnel_schlick(float cosTheta, float F0, float F90, float exponent)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    return mix(F0, F90, pow(x, exponent));
}
vec3 mx_fresnel_schlick(float cosTheta, vec3 F0, vec3 F90, float exponent)
{
    float x = clamp(1.0 - cosTheta, 0.0, 1.0);
    return mix(F0, F90, pow(x, exponent));
}

// Enforce that the given normal is forward-facing from the specified view direction.
vec3 mx_forward_facing_normal(vec3 N, vec3 V)
{
    return (dot(N, V) < 0.0) ? -N : N;
}

// https://www.graphics.rwth-aachen.de/publication/2/jgt.pdf
float mx_golden_ratio_sequence(int i)
{
    const float GOLDEN_RATIO = 1.6180339887498948;
    return fract((float(i) + 1.0) * GOLDEN_RATIO);
}

// https://people.irisa.fr/Ricardo.Marques/articles/2013/SF_CGF.pdf
vec2 mx_spherical_fibonacci(int i, int numSamples)
{
    return vec2((float(i) + 0.5) / float(numSamples), mx_golden_ratio_sequence(i));
}

// Generate a uniform-weighted sample in the unit hemisphere.
vec3 mx_uniform_sample_hemisphere(vec2 Xi)
{
    float phi = 2.0 * M_PI * Xi.x;
    float cosTheta = 1.0 - Xi.y;
    float sinTheta = sqrt(1.0 - mx_square(cosTheta));
    return vec3(cos(phi) * sinTheta,
                sin(phi) * sinTheta,
                cosTheta);
}

// Fresnel model options.
const int FRESNEL_MODEL_DIELECTRIC = 0;
const int FRESNEL_MODEL_CONDUCTOR = 1;
const int FRESNEL_MODEL_SCHLICK = 2;
const int FRESNEL_MODEL_AIRY = 3;
const int FRESNEL_MODEL_SCHLICK_AIRY = 4;

// XYZ to CIE 1931 RGB color space (using neutral E illuminant)
const mat3 XYZ_TO_RGB = mat3(2.3706743, -0.5138850, 0.0052982, -0.9000405, 1.4253036, -0.0146949, -0.4706338, 0.0885814, 1.0093968);

// Parameters for Fresnel calculations.
struct FresnelData
{
    int model;

    // Physical Fresnel
    vec3 ior;
    vec3 extinction;

    // Generalized Schlick Fresnel
    vec3 F0;
    vec3 F90;
    float exponent;

    // Thin film
    float tf_thickness;
    float tf_ior;

    // Refraction
    bool refraction;
};

// https://media.disneyanimation.com/uploads/production/publication_asset/48/asset/s2012_pbs_disney_brdf_notes_v3.pdf
// Appendix B.2 Equation 13
float mx_ggx_NDF(vec3 H, vec2 alpha)
{
    vec2 He = H.xy / alpha;
    float denom = dot(He, He) + mx_square(H.z);
    return 1.0 / (M_PI * alpha.x * alpha.y * mx_square(denom));
}

// https://media.disneyanimation.com/uploads/production/publication_asset/48/asset/s2012_pbs_disney_brdf_notes_v3.pdf
// Appendix B.1 Equation 3
float mx_ggx_PDF(vec3 H, float LdotH, vec2 alpha)
{
    float NdotH = H.z;
    return mx_ggx_NDF(H, alpha) * NdotH / (4.0 * LdotH);
}

// https://media.disneyanimation.com/uploads/production/publication_asset/48/asset/s2012_pbs_disney_brdf_notes_v3.pdf
// Appendix B.2 Equation 15
vec3 mx_ggx_importance_sample_NDF(vec2 Xi, vec2 alpha)
{
    float phi = 2.0 * M_PI * Xi.x;
    float tanTheta = sqrt(Xi.y / (1.0 - Xi.y));
    vec3 H = vec3(tanTheta * alpha.x * cos(phi),
                  tanTheta * alpha.y * sin(phi),
                  1.0);
    return normalize(H);
}

// http://jcgt.org/published/0007/04/01/paper.pdf
// Appendix A Listing 1
vec3 mx_ggx_importance_sample_VNDF(vec2 Xi, vec3 V, vec2 alpha)
{
    // Transform the view direction to the hemisphere configuration.
    V = normalize(vec3(V.xy * alpha, V.z));

    // Construct an orthonormal basis from the view direction.
    float len = length(V.xy);
    vec3 T1 = (len > 0.0) ? vec3(-V.y, V.x, 0.0) / len : vec3(1.0, 0.0, 0.0);
    vec3 T2 = cross(V, T1);

    // Parameterization of the projected area.
    float r = sqrt(Xi.y);
    float phi = 2.0 * M_PI * Xi.x;
    float t1 = r * cos(phi);
    float t2 = r * sin(phi);
    float s = 0.5 * (1.0 + V.z);
    t2 = (1.0 - s) * sqrt(1.0 - mx_square(t1)) + s * t2;

    // Reprojection onto hemisphere.
    vec3 H = t1 * T1 + t2 * T2 + sqrt(max(0.0, 1.0 - mx_square(t1) - mx_square(t2))) * V;

    // Transform the microfacet normal back to the ellipsoid configuration.
    H = normalize(vec3(H.xy * alpha, max(H.z, 0.0)));

    return H;
}

// https://www.cs.cornell.edu/~srm/publications/EGSR07-btdf.pdf
// Equation 34
float mx_ggx_smith_G1(float cosTheta, float alpha)
{
    float cosTheta2 = mx_square(cosTheta);
    float tanTheta2 = (1.0 - cosTheta2) / cosTheta2;
    return 2.0 / (1.0 + sqrt(1.0 + mx_square(alpha) * tanTheta2));
}

// Height-correlated Smith masking-shadowing
// http://jcgt.org/published/0003/02/03/paper.pdf
// Equations 72 and 99
float mx_ggx_smith_G2(float NdotL, float NdotV, float alpha)
{
    float alpha2 = mx_square(alpha);
    float lambdaL = sqrt(alpha2 + (1.0 - alpha2) * mx_square(NdotL));
    float lambdaV = sqrt(alpha2 + (1.0 - alpha2) * mx_square(NdotV));
    return 2.0 / (lambdaL / NdotL + lambdaV / NdotV);
}

// Rational quadratic fit to Monte Carlo data for GGX directional albedo.
vec3 mx_ggx_dir_albedo_analytic(float NdotV, float alpha, vec3 F0, vec3 F90)
{
    float x = NdotV;
    float y = alpha;
    float x2 = mx_square(x);
    float y2 = mx_square(y);
    vec4 r = vec4(0.1003, 0.9345, 1.0, 1.0) +
             vec4(-0.6303, -2.323, -1.765, 0.2281) * x +
             vec4(9.748, 2.229, 8.263, 15.94) * y +
             vec4(-2.038, -3.748, 11.53, -55.83) * x * y +
             vec4(29.34, 1.424, 28.96, 13.08) * x2 +
             vec4(-8.245, -0.7684, -7.507, 41.26) * y2 +
             vec4(-26.44, 1.436, -36.11, 54.9) * x2 * y +
             vec4(19.99, 0.2913, 15.86, 300.2) * x * y2 +
             vec4(-5.448, 0.6286, 33.37, -285.1) * x2 * y2;
    vec2 AB = clamp(r.xy / r.zw, 0.0, 1.0);
    return F0 * AB.x + F90 * AB.y;
}

vec3 mx_ggx_dir_albedo_table_lookup(float NdotV, float alpha, vec3 F0, vec3 F90)
{
#if DIRECTIONAL_ALBEDO_METHOD == 1
    if (textureSize(u_albedoTable, 0).x > 1)
    {
        vec2 AB = texture(u_albedoTable, vec2(NdotV, alpha)).rg;
        return F0 * AB.x + F90 * AB.y;
    }
#endif
    return vec3(0.0);
}

// https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf
vec3 mx_ggx_dir_albedo_monte_carlo(float NdotV, float alpha, vec3 F0, vec3 F90)
{
    NdotV = clamp(NdotV, M_FLOAT_EPS, 1.0);
    vec3 V = vec3(sqrt(1.0 - mx_square(NdotV)), 0, NdotV);

    vec2 AB = vec2(0.0);
    const int SAMPLE_COUNT = 64;
    for (int i = 0; i < SAMPLE_COUNT; i++)
    {
        vec2 Xi = mx_spherical_fibonacci(i, SAMPLE_COUNT);

        // Compute the half vector and incoming light direction.
        vec3 H = mx_ggx_importance_sample_VNDF(Xi, V, vec2(alpha));
        vec3 L = -reflect(V, H);
        
        // Compute dot products for this sample.
        float NdotL = clamp(L.z, M_FLOAT_EPS, 1.0);
        float VdotH = clamp(dot(V, H), M_FLOAT_EPS, 1.0);

        // Compute the Fresnel term.
        float Fc = mx_fresnel_schlick(VdotH, 0.0, 1.0);

        // Compute the per-sample geometric term.
        // https://hal.inria.fr/hal-00996995v2/document, Algorithm 2
        float G2 = mx_ggx_smith_G2(NdotL, NdotV, alpha);
        
        // Add the contribution of this sample.
        AB += vec2(G2 * (1.0 - Fc), G2 * Fc);
    }

    // Apply the global component of the geometric term and normalize.
    AB /= mx_ggx_smith_G1(NdotV, alpha) * float(SAMPLE_COUNT);

    // Return the final directional albedo.
    return F0 * AB.x + F90 * AB.y;
}

vec3 mx_ggx_dir_albedo(float NdotV, float alpha, vec3 F0, vec3 F90)
{
#if DIRECTIONAL_ALBEDO_METHOD == 0
    return mx_ggx_dir_albedo_analytic(NdotV, alpha, F0, F90);
#elif DIRECTIONAL_ALBEDO_METHOD == 1
    return mx_ggx_dir_albedo_table_lookup(NdotV, alpha, F0, F90);
#else
    return mx_ggx_dir_albedo_monte_carlo(NdotV, alpha, F0, F90);
#endif
}

float mx_ggx_dir_albedo(float NdotV, float alpha, float F0, float F90)
{
    return mx_ggx_dir_albedo(NdotV, alpha, vec3(F0), vec3(F90)).x;
}

// https://blog.selfshadow.com/publications/turquin/ms_comp_final.pdf
// Equations 14 and 16
vec3 mx_ggx_energy_compensation(float NdotV, float alpha, vec3 Fss)
{
    float Ess = mx_ggx_dir_albedo(NdotV, alpha, 1.0, 1.0);
    return 1.0 + Fss * (1.0 - Ess) / Ess;
}

float mx_ggx_energy_compensation(float NdotV, float alpha, float Fss)
{
    return mx_ggx_energy_compensation(NdotV, alpha, vec3(Fss)).x;
}

// Compute the average of an anisotropic alpha pair.
float mx_average_alpha(vec2 alpha)
{
    return sqrt(alpha.x * alpha.y);
}

// Convert a real-valued index of refraction to normal-incidence reflectivity.
float mx_ior_to_f0(float ior)
{
    return mx_square((ior - 1.0) / (ior + 1.0));
}

// Convert normal-incidence reflectivity to real-valued index of refraction.
float mx_f0_to_ior(float F0)
{
    float sqrtF0 = sqrt(clamp(F0, 0.01, 0.99));
    return (1.0 + sqrtF0) / (1.0 - sqrtF0);
}

vec3 mx_f0_to_ior_colored(vec3 F0)
{
    vec3 sqrtF0 = sqrt(clamp(F0, 0.01, 0.99));
    return (vec3(1.0) + sqrtF0) / (vec3(1.0) - sqrtF0);
}

// https://seblagarde.wordpress.com/2013/04/29/memo-on-fresnel-equations/
float mx_fresnel_dielectric(float cosTheta, float ior)
{
    if (cosTheta < 0.0)
        return 1.0;

    float g =  ior*ior + cosTheta*cosTheta - 1.0;
    // Check for total internal reflection
    if (g < 0.0)
        return 1.0;

    g = sqrt(g);
    float gmc = g - cosTheta;
    float gpc = g + cosTheta;
    float x = gmc / gpc;
    float y = (gpc * cosTheta - 1.0) / (gmc * cosTheta + 1.0);
    return 0.5 * x * x * (1.0 + y * y);
}

void mx_fresnel_dielectric_polarized(float cosTheta, float n, out float Rp, out float Rs)
{
    if (cosTheta < 0.0) {
        Rp = 1.0;
        Rs = 1.0;
        return;
    }

    float cosTheta2 = cosTheta * cosTheta;
    float sinTheta2 = 1.0 - cosTheta2;
    float n2 = n * n;

    float t0 = n2 - sinTheta2;
    float a2plusb2 = sqrt(t0 * t0);
    float t1 = a2plusb2 + cosTheta2;
    float a = sqrt(max(0.5 * (a2plusb2 + t0), 0.0));
    float t2 = 2.0 * a * cosTheta;
    Rs = (t1 - t2) / (t1 + t2);

    float t3 = cosTheta2 * a2plusb2 + sinTheta2 * sinTheta2;
    float t4 = t2 * sinTheta2;
    Rp = Rs * (t3 - t4) / (t3 + t4);
}

void mx_fresnel_dielectric_polarized(float cosTheta, float eta1, float eta2, out float Rp, out float Rs)
{
    float n = eta2 / eta1;
    mx_fresnel_dielectric_polarized(cosTheta, n, Rp, Rs);
}

void mx_fresnel_conductor_polarized(float cosTheta, vec3 n, vec3 k, out vec3 Rp, out vec3 Rs)
{
    cosTheta = clamp(cosTheta, 0.0, 1.0);
    float cosTheta2 = cosTheta * cosTheta;
    float sinTheta2 = 1.0 - cosTheta2;
    vec3 n2 = n * n;
    vec3 k2 = k * k;

    vec3 t0 = n2 - k2 - vec3(sinTheta2);
    vec3 a2plusb2 = sqrt(t0 * t0 + 4.0 * n2 * k2);
    vec3 t1 = a2plusb2 + vec3(cosTheta2);
    vec3 a = sqrt(max(0.5 * (a2plusb2 + t0), 0.0));
    vec3 t2 = 2.0 * a * cosTheta;
    Rs = (t1 - t2) / (t1 + t2);

    vec3 t3 = cosTheta2 * a2plusb2 + vec3(sinTheta2 * sinTheta2);
    vec3 t4 = t2 * sinTheta2;
    Rp = Rs * (t3 - t4) / (t3 + t4);
}

void mx_fresnel_conductor_polarized(float cosTheta, float eta1, vec3 eta2, vec3 kappa2, out vec3 Rp, out vec3 Rs)
{
    vec3 n = eta2 / eta1;
    vec3 k = kappa2 / eta1;
    mx_fresnel_conductor_polarized(cosTheta, n, k, Rp, Rs);
}

vec3 mx_fresnel_conductor(float cosTheta, vec3 n, vec3 k)
{
    vec3 Rp, Rs;
    mx_fresnel_conductor_polarized(cosTheta, n, k, Rp, Rs);
    return 0.5 * (Rp  + Rs);
}

// Phase shift due to a dielectric material
void mx_fresnel_dielectric_phase_polarized(float cosTheta, float eta1, float eta2, out float phiP, out float phiS)
{
    float cosB = cos(atan(eta2 / eta1));    // Brewster's angle
    if (eta2 > eta1) {
        phiP = cosTheta < cosB ? M_PI : 0.0f;
        phiS = 0.0f;
    } else {
        phiP = cosTheta < cosB ? 0.0f : M_PI;
        phiS = M_PI;
    }
}

// Phase shift due to a conducting material
void mx_fresnel_conductor_phase_polarized(float cosTheta, float eta1, vec3 eta2, vec3 kappa2, out vec3 phiP, out vec3 phiS)
{
    if (kappa2 == vec3(0, 0, 0) && eta2.x == eta2.y && eta2.y == eta2.z) {
        // Use dielectric formula to increase performance
        mx_fresnel_dielectric_phase_polarized(cosTheta, eta1, eta2.x, phiP.x, phiS.x);
        phiP = phiP.xxx;
        phiS = phiS.xxx;
        return;
    }
    vec3 k2 = kappa2 / eta2;
    vec3 sinThetaSqr = vec3(1.0) - cosTheta * cosTheta;
    vec3 A = eta2*eta2*(vec3(1.0)-k2*k2) - eta1*eta1*sinThetaSqr;
    vec3 B = sqrt(A*A + mx_square(2.0*eta2*eta2*k2));
    vec3 U = sqrt((A+B)/2.0);
    vec3 V = max(vec3(0.0), sqrt((B-A)/2.0));

    phiS = atan(2.0*eta1*V*cosTheta, U*U + V*V - mx_square(eta1*cosTheta));
    phiP = atan(2.0*eta1*eta2*eta2*cosTheta * (2.0*k2*U - (vec3(1.0)-k2*k2) * V),
                mx_square(eta2*eta2*(vec3(1.0)+k2*k2)*cosTheta) - eta1*eta1*(U*U+V*V));
}

// Evaluation XYZ sensitivity curves in Fourier space
vec3 mx_eval_sensitivity(float opd, vec3 shift)
{
    // Use Gaussian fits, given by 3 parameters: val, pos and var
    float phase = 2.0*M_PI * opd;
    vec3 val = vec3(5.4856e-13, 4.4201e-13, 5.2481e-13);
    vec3 pos = vec3(1.6810e+06, 1.7953e+06, 2.2084e+06);
    vec3 var = vec3(4.3278e+09, 9.3046e+09, 6.6121e+09);
    vec3 xyz = val * sqrt(2.0*M_PI * var) * cos(pos * phase + shift) * exp(- var * phase*phase);
    xyz.x   += 9.7470e-14 * sqrt(2.0*M_PI * 4.5282e+09) * cos(2.2399e+06 * phase + shift[0]) * exp(- 4.5282e+09 * phase*phase);
    return xyz / 1.0685e-7;
}

// A Practical Extension to Microfacet Theory for the Modeling of Varying Iridescence
// https://belcour.github.io/blog/research/publication/2017/05/01/brdf-thin-film.html
vec3 mx_fresnel_airy(float cosTheta, vec3 ior, vec3 extinction, float tf_thickness, float tf_ior,
                                     vec3 f0, vec3 f90, float exponent, bool use_schlick)
{
    // Convert nm -> m
    float d = tf_thickness * 1.0e-9;

    // Assume vacuum on the outside
    float eta1 = 1.0;
    float eta2 = max(tf_ior, eta1);
    vec3 eta3   = use_schlick ? mx_f0_to_ior_colored(f0) : ior;
    vec3 kappa3 = use_schlick ? vec3(0.0)                : extinction;

    // Compute the Spectral versions of the Fresnel reflectance and
    // transmitance for each interface.
    float R12p, T121p, R12s, T121s;
    vec3 R23p, R23s;
    
    // Reflected and transmitted parts in the thin film
    mx_fresnel_dielectric_polarized(cosTheta, eta1, eta2, R12p, R12s);

    // Reflected part by the base
    float scale = eta1 / eta2;
    float cosThetaTSqr = 1.0 - (1.0-cosTheta*cosTheta) * scale*scale;
    float cosTheta2 = sqrt(cosThetaTSqr);
    if (use_schlick)
    {
        vec3 f = mx_fresnel_schlick(cosTheta2, f0, f90, exponent);
        R23p = 0.5 * f;
        R23s = 0.5 * f;
    }
    else
    {
        mx_fresnel_conductor_polarized(cosTheta2, eta2, eta3, kappa3, R23p, R23s);
    }

    // Check for total internal reflection
    if (cosThetaTSqr <= 0.0f)
    {
        R12s = 1.0;
        R12p = 1.0;
    }

    // Compute the transmission coefficients
    T121p = 1.0 - R12p;
    T121s = 1.0 - R12s;

    // Optical path difference
    float D = 2.0 * eta2 * d * cosTheta2;
    vec3 Dphi = 2.0 * M_PI * D / vec3(580.0, 550.0, 450.0);

    float phi21p, phi21s;
    vec3 phi23p, phi23s, r123s, r123p;

    // Evaluate the phase shift
    mx_fresnel_dielectric_phase_polarized(cosTheta, eta1, eta2, phi21p, phi21s);
    if (use_schlick)
    {
        phi23p = vec3(
            (eta3[0] < eta2) ? M_PI : 0.0,
            (eta3[1] < eta2) ? M_PI : 0.0,
            (eta3[2] < eta2) ? M_PI : 0.0);
        phi23s = phi23p;
    }
    else
    {
        mx_fresnel_conductor_phase_polarized(cosTheta2, eta2, eta3, kappa3, phi23p, phi23s);
    }

    phi21p = M_PI - phi21p;
    phi21s = M_PI - phi21s;

    r123p = max(vec3(0.0), sqrt(R12p*R23p));
    r123s = max(vec3(0.0), sqrt(R12s*R23s));

    // Evaluate iridescence term
    vec3 I = vec3(0.0);
    vec3 C0, Cm, Sm;

    // Iridescence term using spectral antialiasing for Parallel polarization

    vec3 S0 = vec3(1.0);

    // Reflectance term for m=0 (DC term amplitude)
    vec3 Rs = (T121p*T121p*R23p) / (vec3(1.0) - R12p*R23p);
    C0 = R12p + Rs;
    I += C0 * S0;

    // Reflectance term for m>0 (pairs of diracs)
    Cm = Rs - T121p;
    for (int m=1; m<=2; ++m)
    {
        Cm *= r123p;
        Sm  = 2.0 * mx_eval_sensitivity(float(m)*D, float(m)*(phi23p+vec3(phi21p)));
        I  += Cm*Sm;
    }

    // Iridescence term using spectral antialiasing for Perpendicular polarization

    // Reflectance term for m=0 (DC term amplitude)
    vec3 Rp = (T121s*T121s*R23s) / (vec3(1.0) - R12s*R23s);
    C0 = R12s + Rp;
    I += C0 * S0;

    // Reflectance term for m>0 (pairs of diracs)
    Cm = Rp - T121s ;
    for (int m=1; m<=2; ++m)
    {
        Cm *= r123s;
        Sm  = 2.0 * mx_eval_sensitivity(float(m)*D, float(m)*(phi23s+vec3(phi21s)));
        I  += Cm*Sm;
    }

    // Average parallel and perpendicular polarization
    I *= 0.5;

    // Convert back to RGB reflectance
    I = clamp(XYZ_TO_RGB * I, vec3(0.0), vec3(1.0));

    return I;
}

FresnelData mx_init_fresnel_data(int model)
{
    return FresnelData(model, vec3(0.0), vec3(0.0), vec3(0.0), vec3(0.0), 0.0, 0.0, 0.0, false);
}

FresnelData mx_init_fresnel_dielectric(float ior)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_DIELECTRIC);
    fd.ior = vec3(ior);
    return fd;
}

FresnelData mx_init_fresnel_conductor(vec3 ior, vec3 extinction)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_CONDUCTOR);
    fd.ior = ior;
    fd.extinction = extinction;
    return fd;
}

FresnelData mx_init_fresnel_schlick(vec3 F0)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_SCHLICK);
    fd.F0 = F0;
    fd.F90 = vec3(1.0);
    fd.exponent = 5.0f;
    return fd;
}

FresnelData mx_init_fresnel_schlick(vec3 F0, vec3 F90, float exponent)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_SCHLICK);
    fd.F0 = F0;
    fd.F90 = F90;
    fd.exponent = exponent;
    return fd;
}

FresnelData mx_init_fresnel_schlick_airy(vec3 F0, vec3 F90, float exponent, float tf_thickness, float tf_ior)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_SCHLICK_AIRY);
    fd.F0 = F0;
    fd.F90 = F90;
    fd.exponent = exponent;
    fd.tf_thickness = tf_thickness;
    fd.tf_ior = tf_ior;
    return fd;
}

FresnelData mx_init_fresnel_dielectric_airy(float ior, float tf_thickness, float tf_ior)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_AIRY);
    fd.ior = vec3(ior);
    fd.tf_thickness = tf_thickness;
    fd.tf_ior = tf_ior;
    return fd;
}

FresnelData mx_init_fresnel_conductor_airy(vec3 ior, vec3 extinction, float tf_thickness, float tf_ior)
{
    FresnelData fd = mx_init_fresnel_data(FRESNEL_MODEL_AIRY);
    fd.ior = ior;
    fd.extinction = extinction;
    fd.tf_thickness = tf_thickness;
    fd.tf_ior = tf_ior;
    return fd;
}

vec3 mx_compute_fresnel(float cosTheta, FresnelData fd)
{
    if (fd.model == FRESNEL_MODEL_DIELECTRIC)
    {
        return vec3(mx_fresnel_dielectric(cosTheta, fd.ior.x));
    }
    else if (fd.model == FRESNEL_MODEL_CONDUCTOR)
    {
        return mx_fresnel_conductor(cosTheta, fd.ior, fd.extinction);
    }
    else if (fd.model == FRESNEL_MODEL_SCHLICK)
    {
        return mx_fresnel_schlick(cosTheta, fd.F0, fd.F90, fd.exponent);
    }
    else
    {
        return mx_fresnel_airy(cosTheta, fd.ior, fd.extinction, fd.tf_thickness, fd.tf_ior,
                                         fd.F0, fd.F90, fd.exponent,
                                         fd.model == FRESNEL_MODEL_SCHLICK_AIRY);
    }
}

// Compute the refraction of a ray through a solid sphere.
vec3 mx_refraction_solid_sphere(vec3 R, vec3 N, float ior)
{
    R = refract(R, N, 1.0 / ior);
    vec3 N1 = normalize(R * dot(R, N) - N * 0.5);
    return refract(R, N1, ior);
}

vec2 mx_latlong_projection(vec3 dir)
{
    float latitude = -asin(dir.y) * M_PI_INV + 0.5;
    float longitude = atan(dir.x, -dir.z) * M_PI_INV * 0.5 + 0.5;
    return vec2(longitude, latitude);
}

vec3 mx_latlong_map_lookup(vec3 dir, mat4 transform, float lod, sampler2D envSampler)
{
    vec3 envDir = normalize((transform * vec4(dir,0.0)).xyz);
    vec2 uv = mx_latlong_projection(envDir);
    return textureLod(envSampler, uv, lod).rgb;
}

// https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch20.html
// Section 20.4 Equation 13
float mx_latlong_compute_lod(vec3 dir, float pdf, float maxMipLevel, int envSamples)
{
    const float MIP_LEVEL_OFFSET = 1.5;
    float effectiveMaxMipLevel = maxMipLevel - MIP_LEVEL_OFFSET;
    float distortion = sqrt(1.0 - mx_square(dir.y));
    return max(effectiveMaxMipLevel - 0.5 * log2(float(envSamples) * pdf * distortion), 0.0);
}

vec3 mx_environment_radiance(vec3 N, vec3 V, vec3 X, vec2 alpha, int distribution, FresnelData fd)
{
    // Generate tangent frame.
    X = normalize(X - dot(X, N) * N);
    vec3 Y = cross(N, X);
    mat3 tangentToWorld = mat3(X, Y, N);

    // Transform the view vector to tangent space.
    V = vec3(dot(V, X), dot(V, Y), dot(V, N));

    // Compute derived properties.
    float NdotV = clamp(V.z, M_FLOAT_EPS, 1.0);
    float avgAlpha = mx_average_alpha(alpha);
    
    // Integrate outgoing radiance using filtered importance sampling.
    // http://cgg.mff.cuni.cz/~jaroslav/papers/2008-egsr-fis/2008-egsr-fis-final-embedded.pdf
    vec3 radiance = vec3(0.0);
    int envRadianceSamples = u_envRadianceSamples;
    for (int i = 0; i < envRadianceSamples; i++)
    {
        vec2 Xi = mx_spherical_fibonacci(i, envRadianceSamples);

        // Compute the half vector and incoming light direction.
        vec3 H = mx_ggx_importance_sample_NDF(Xi, alpha);
        vec3 L = fd.refraction ? mx_refraction_solid_sphere(-V, H, fd.ior.x) : -reflect(V, H);
        
        // Compute dot products for this sample.
        float NdotH = clamp(H.z, M_FLOAT_EPS, 1.0);
        float NdotL = clamp(L.z, M_FLOAT_EPS, 1.0);
        float VdotH = clamp(dot(V, H), M_FLOAT_EPS, 1.0);
        float LdotH = VdotH;

        // Sample the environment light from the given direction.
        vec3 Lw = tangentToWorld * L;
        float pdf = mx_ggx_PDF(H, LdotH, alpha);
        float lod = mx_latlong_compute_lod(Lw, pdf, float(u_envRadianceMips - 1), envRadianceSamples);
        vec3 sampleColor = mx_latlong_map_lookup(Lw, u_envMatrix, lod, u_envRadiance);

        // Compute the Fresnel term.
        vec3 F = mx_compute_fresnel(VdotH, fd);

        // Compute the geometric term.
        float G = mx_ggx_smith_G2(NdotL, NdotV, avgAlpha);

        // Compute the combined FG term, which is inverted for refraction.
        vec3 FG = fd.refraction ? vec3(1.0) - (F * G) : F * G;

        // Add the radiance contribution of this sample.
        // From https://cdn2.unrealengine.com/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf
        //   incidentLight = sampleColor * NdotL
        //   microfacetSpecular = D * F * G / (4 * NdotL * NdotV)
        //   pdf = D * NdotH / (4 * VdotH)
        //   radiance = incidentLight * microfacetSpecular / pdf
        radiance += sampleColor * FG * VdotH / (NdotV * NdotH);
    }

    // Normalize and return the final radiance.
    radiance /= float(envRadianceSamples);
    return radiance;
}

vec3 mx_environment_irradiance(vec3 N)
{
    return mx_latlong_map_lookup(N, u_envMatrix, 0.0, u_envIrradiance);
}


vec3 mx_surface_transmission(vec3 N, vec3 V, vec3 X, vec2 alpha, int distribution, FresnelData fd)
{
    vec3 transmission;
    if (u_refractionEnv)
    {
        // Approximate the appearance of surface transmission as glossy
        // environment map refraction, ignoring any scene geometry that might
        // be visible through the surface.
        fd.refraction = true;
        transmission = mx_environment_radiance(N, V, X, alpha, distribution, fd);
    }
    else
    {
        transmission = u_refractionColor;
    }

    return transmission;
}

struct LightData
{
    int type;
    vec3 direction;
    vec3 color;
    float intensity;
};

uniform LightData u_lightData[MAX_LIGHT_SOURCES];

// https://developer.nvidia.com/gpugems/gpugems3/part-ii-light-and-shadows/chapter-8-summed-area-variance-shadow-maps
float mx_variance_shadow_occlusion(vec2 moments, float fragmentDepth)
{
    const float MIN_VARIANCE = 0.00001;

    // One-tailed inequality valid if fragmentDepth > moments.x.
    float p = (fragmentDepth <= moments.x) ? 1.0 : 0.0;

    // Compute variance.
    float variance = moments.y - mx_square(moments.x);
    variance = max(variance, MIN_VARIANCE);

    // Compute probabilistic upper bound.
    float d = fragmentDepth - moments.x;
    float pMax = variance / (variance + mx_square(d));
    return max(p, pMax);
}

vec2 mx_compute_depth_moments()
{
    float depth = gl_FragCoord.z;
    return vec2(depth, mx_square(depth));
}
void mx_directional_light(LightData light, vec3 position, out lightshader result)
{
    result.direction = -light.direction;
    result.intensity = light.color * light.intensity;
}

int numActiveLightSources()
{
    return min(u_numActiveLightSources, MAX_LIGHT_SOURCES) ;
}

void sampleLightSource(LightData light, vec3 position, out lightshader result)
{
    result.intensity = vec3(0.0);
    result.direction = vec3(0.0);
    if (light.type == 1)
    {
        mx_directional_light(light, position, result);
    }
}

void NG_convert_vector3_shader(vec3 in1, out surfaceshader out1)
{
    vec3 vec3_to_color3_out = vec3(in1.x, in1.y, in1.z);
    surfaceshader surface_out = surfaceshader(vec3(0.0),vec3(0.0));
    surface_out.color = 1.000000 * vec3_to_color3_out;
    surface_out.transparency = 0.000000 * vec3(1.000000, 1.000000, 1.000000);
    surface_out.color *= 1.000000;
    surface_out.transparency = mix(vec3(1.0), surface_out.transparency, 1.000000);
    out1 = surface_out;
}

void main()
{
    vec3 clamp_vector3FA_out = clamp(clamp_vector3FA_in, clamp_vector3FA_low, clamp_vector3FA_high);
    surfaceshader shader_clamp_vector3FA_out_out = surfaceshader(vec3(0.0),vec3(0.0));
    NG_convert_vector3_shader(clamp_vector3FA_out, shader_clamp_vector3FA_out_out);
    material material_clamp_vector3FA_out_out = shader_clamp_vector3FA_out_out;
    out1 = vec4(material_clamp_vector3FA_out_out.color, 1.0);
}

