#include <metal_stdlib>
#include <metal_math>
#include <metal_texture>
using namespace metal;

#line 10 "test_data/shader.slang"
[[kernel]] void main_0(uint3 tid_0 [[thread_position_in_grid]], uint device* outputBuffer_0 [[buffer(0)]])
{

    uint index_0 = tid_0.x + tid_0.y * 8U;
    *(outputBuffer_0+index_0) = index_0;
    return;
}

