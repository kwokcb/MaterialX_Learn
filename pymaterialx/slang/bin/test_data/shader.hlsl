#pragma pack_matrix(column_major)
#ifdef SLANG_HLSL_ENABLE_NVAPI
#include "nvHLSLExtns.h"
#endif

#ifndef __DXC_VERSION_MAJOR
// warning X3557: loop doesn't seem to do anything, forcing loop to unroll
#pragma warning(disable : 3557)
#endif


#line 5 "shader.slang"
RWStructuredBuffer<uint > outputBuffer_0 : register(u0);




[numthreads(8, 8, 1)]
void main(uint3 tid_0 : SV_DispatchThreadID)
{
    uint index_0 = tid_0.x + tid_0.y * 8U;
    outputBuffer_0[index_0] = index_0;
    return;
}

