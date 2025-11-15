#version 460
layout(row_major) uniform;
layout(row_major) buffer;

#line 5 0
layout(std430, binding = 0) buffer StructuredBuffer_uint_t_0 {
    uint _data[];
} outputBuffer_0;


layout(local_size_x = 8, local_size_y = 8, local_size_z = 1) in;
void main()
{
    uint index_0 = gl_GlobalInvocationID.x + gl_GlobalInvocationID.y * 8U;
    outputBuffer_0._data[uint(index_0)] = index_0;
    return;
}

