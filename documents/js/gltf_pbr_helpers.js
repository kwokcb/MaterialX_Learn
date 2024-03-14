
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

function updateMaterial(id, value, type) {
    const modelViewerParameters = document.querySelector("model-viewer#materialviewer");
    if (modelViewerParameters.model && modelViewerParameters.model.materials) {
        let material = modelViewerParameters.model.materials[0];

        //console.log('update material', id, value, type);

        orgvalue = value;
        if (type == 'color3') {
            //value = sRGBToLinearRGB(hexToRgbArray(value));
            value = hexToRgbArray(value);
        }
        if (id == 'ND_gltf_pbr_surfaceshader_base_color') {
            material.pbrMetallicRoughness.setBaseColorFactor(value);
            rgba = hexToRgbArray(orgvalue);
            r = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_0')
            r.value = rgba[0];
            g = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_1')
            g.value = rgba[1];
            b = document.getElementById('ND_gltf_pbr_surfaceshader_base_color_2')
            b.value = rgba[2];
        }
        else if (id == 'ND_gltf_pbr_surfaceshader_metallic') {
            material.pbrMetallicRoughness.setMetallicFactor(value);
        }
        else if (id == 'ND_gltf_pbr_surfaceshader_roughness') {
            material.pbrMetallicRoughness.setRoughnessFactor(value);
        }
        else if (id == 'ND_gltf_pbr_surfaceshader_transmission') {
            material.setTransmissionFactor(value);
        }
        else if (id == 'ND_gltf_pbr_surfaceshader_specular') {
            material.setSpecularFactor(value);
        }
        else if (id == 'ND_gltf_pbr_surfaceshader_specular_color') {
            material.setSpecularColorFactor(value);
            rgba = hexToRgbArray(orgvalue);
            r = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_0')
            r.value = rgba[0];
            g = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_1')
            g.value = rgba[1];
            b = document.getElementById('ND_gltf_pbr_surfaceshader_specular_color_2')
            b.value = rgba[2];

        }
        else if (id == 'ND_gltf_pbr_surfaceshader_iridescence') {
            //console.log('setIridescenceFactor', value)
            material.setIridescenceFactor(value);
        }

        /*slider = document.getElementById(id + '_slider')
        if (slider)
        {
            slider.textContent = value
        }*/
    }
}


/*
dd watcher for:  ND_gltf_pbr_surfaceshader_metallic
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_roughness
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_occlusion
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_transmission
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_specular
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_ior
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_alpha
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_alpha_cutoff
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_iridescence
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_iridescence_ior
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_iridescence_thickness
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_sheen_roughness
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_clearcoat
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_clearcoat_roughness
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_emissive_strength
gltf_pbr_helpers.js:110 Add watcher for:  ND_gltf_pbr_surfaceshader_thickness
*/
function addMaterialEventListeners() {
    nd = 'ND_gltf_pbr_surfaceshader'
    inputs = ['_base_color', '_roughness', '_metallic', '_transmission', '_specular', '_specular_color', '_iridescence'];
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

    // Find all elements of type range
    sliders = document.getElementsByClassName('form-range')
    for (let slider of sliders) {
        id = slider.id
        slider = document.getElementById(id)
        //console.log('Add watcher for: ', slider.id)
        slider.addEventListener('input',
            function (event) {
                slider_text_id = event.target.id + "_slider"
                slider_text = document.getElementById(slider_text_id)
                //console.log('update: ', slider_text, ' value: ', event.target.value)
                if (slider_text) {
                    slider_text.value = event.target.value;
                }
            }, false);
        slider.addEventListener('change',
            function (event) {
                slider_text_id = event.target.id + "_slider"
                slider_text = document.getElementById(slider_text_id)
                //console.log('update: ', slider_text, ' value: ', event.target.value)
                if (slider_text) {
                    slider_text.value = event.target.value;
                }
            }, false);

        slider_text_id = document.getElementById(id + "_slider")
        slider_text_id.addEventListener('change',
            function (event) {
                // Remove '_slider from event.target.id
                slider = document.getElementById(event.target.id.replace('_slider', ''))
                console.log('update: ', slider.id, ' value: ', event.target.value)
                if (slider) {
                    slider.value = event.target.value;
                }
                updateMaterial(slider.id, event.target.value, slider.type)
            }, false);
            
    }

    const modelViewerParameters = document.querySelector("model-viewer#materialviewer");
    if (modelViewerParameters) {
        modelViewerParameters.addEventListener("load", (ev) => {
            for (input in inputs) {
                widget = document.getElementById(nd + inputs[input])
                if (widget) {
                    updateMaterial(nd + inputs[input], widget.value, widget.type);
                }
            }
        });
    }
}

addMaterialEventListeners();
