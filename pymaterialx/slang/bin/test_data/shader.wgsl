@binding(0) @group(0) var<storage, read_write> outputBuffer_0 : array<u32>;

@compute
@workgroup_size(8, 8, 1)
fn main(@builtin(global_invocation_id) tid_0 : vec3<u32>)
{
    var index_0 : u32 = tid_0.x + tid_0.y * u32(8);
    outputBuffer_0[index_0] = index_0;
    return;
}

