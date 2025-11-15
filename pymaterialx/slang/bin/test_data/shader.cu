#include "D:/Work/materialx/MaterialX_Learn/pymaterialx/slang/include/slang-cuda-prelude.h"


#line 14 "shader.slang"
struct GlobalParams_0
{
    RWStructuredBuffer<uint> outputBuffer_0;
};


#line 14
extern "C" __constant__ GlobalParams_0 SLANG_globalParams;
#define globalParams_0 (&SLANG_globalParams)

#line 10
extern "C" __global__ void main_0()
{

#line 10
    uint3  _S1 = blockIdx * blockDim + threadIdx;


    uint index_0 = _S1.x + _S1.y * 8U;
    *(&(globalParams_0->outputBuffer_0)[index_0]) = index_0;
    return;
}

