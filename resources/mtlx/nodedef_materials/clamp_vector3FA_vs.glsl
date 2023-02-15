#version 400

// Uniform block: PrivateUniforms
uniform mat4 u_worldMatrix = mat4(1.0);
uniform mat4 u_viewProjectionMatrix = mat4(1.0);

// Inputs block: VertexInputs
in vec3 i_position;

void main()
{
    vec4 hPositionWorld = u_worldMatrix * vec4(i_position, 1.0);
    gl_Position = u_viewProjectionMatrix * hPositionWorld;
}

