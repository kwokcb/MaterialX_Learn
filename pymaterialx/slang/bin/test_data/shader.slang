// shader.slang
// Minimal Slang 2025 compute shader

// Declare a global RW buffer with binding
RWStructuredBuffer<uint> outputBuffer; // global, no :register

// Compute entry point
[shader("compute")]
[numthreads(8, 8, 1)]
void main(uint3 tid : SV_DispatchThreadID)
{
    // Simple computation
    uint index = tid.x + tid.y * 8;
    outputBuffer[index] = index;
}
