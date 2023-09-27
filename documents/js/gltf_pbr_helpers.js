
// Convert UI color to RGBA for rendering
function hexToRgbArray(hex) {
    // Remove the '#' if it's present
    hex = hex.replace(/^#/, '');

    // Parse the hex values for red, green, and blue
    const r = parseInt(hex.substring(0, 2), 16);
    const g = parseInt(hex.substring(2, 4), 16);
    const b = parseInt(hex.substring(4, 6), 16);

    // Create and return an array [r, g, b]
    return [r / 255.0, g / 255.0, b / 255.0, 1];
}

// Convert UI sRGB to linear RGB
function sRGBToLinearRGB(rgbArray) {
    const linearRGB = [];

    for (let i = 0; i < 3; i++) {
        const channelValue = rgbArray[i];
        linearRGB[i] = Math.pow(channelValue, 2.2);
    }

    return linearRGB;
}

function updateMaterial(id, value, type)
{
  const modelViewerParameters = document.querySelector("model-viewer#materialviewer");
  if (modelViewerParameters.model && modelViewerParameters.model.materials) 
  {
    let material = modelViewerParameters.model.materials[0];

    //console.log('update material', id, value, type);

    orgvalue = value;
    if (type == 'color3')
    {
      //value = sRGBToLinearRGB(hexToRgbArray(value));
      value = hexToRgbArray(value);
    }
    if (id == 'ND_gltf_pbr_surfaceshader_base_color')
    {
      material.pbrMetallicRoughness.setBaseColorFactor(value);
      rgba = hexToRgbArray(orgvalue);
      r = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_0')
      r.value = rgba[0];        
      g = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_1')
      g.value = rgba[1];        
      b = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_2')
      b.value = rgba[2];        
    }
    else if (id == 'ND_gltf_pbr_surfaceshader_metallic')
    {
        material.pbrMetallicRoughness.setMetallicFactor(value);
    }
    else if (id == 'ND_gltf_pbr_surfaceshader_roughness')
    {
        material.pbrMetallicRoughness.setRoughnessFactor(value);
    }
    else if (id == 'ND_gltf_pbr_surfaceshader_transmission')
    {
      material.setTransmissionFactor(value);
    }
    else if (id == 'ND_gltf_pbr_surfaceshader_specular')
    {
        material.setSpecularFactor(value);
    }
    else if (id == 'ND_gltf_pbr_surfaceshader_specular_color')
    {
        material.setSpecularColorFactor(value);
        rgba = hexToRgbArray(orgvalue);
        r = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_0')
        r.value = rgba[0];        
        g = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_1')
        g.value = rgba[1];        
        b = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_2')
        b.value = rgba[2];        
  
    }
  }
}

function addMaterialEventListeners()
{
    nd = 'ND_gltf_pbr_surfaceshader'
    inputs = ['_base_color', '_roughness', '_metallic', '_transmission', '_specular', '_specular_color'];
    for (input in inputs) {
        widget = document.getElementById(nd + inputs[input])
        if (widget) {
            widget.addEventListener('input',
                function (event) {
                    const id = event.target.id;
                    const value = event.target.value;
                    const type = event.target.type;
                    updateMaterial(id, value, type)
                }, false);
            widget.addEventListener('change',
                function (event) {
                    const id = event.target.id;
                    const value = event.target.value;
                    const type = event.target.type;
                    updateMaterial(id, value, type)
                }, false);
        }
    }

    const modelViewerParameters = document.querySelector("model-viewer#materialviewer");
    if (modelViewerParameters)
    {
        modelViewerParameters.addEventListener("load", (ev) => {
            for (input in inputs) {
                widget = document.getElementById(nd + inputs[input])
                if (widget)
                {
                    updateMaterial(nd + inputs[input], widget.value, widget.type);
                }
            }
        });
    }
}

addMaterialEventListeners();
