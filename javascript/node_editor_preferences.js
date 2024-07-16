/**
 * @class MxNodeEditorPreferences
 * @description Class to store preferences for the node editor
 * - preferences - Object containing preferences for the node editor
 * - preferences.icon_map - Object containing mapping of file extensions to icons
 * - preferences.examples - Object containing example materials
 * Note that all material and icon file references are relative to the root of the deployment folder.
 * while geometry is referenced by name only.
 */
export class MxNodeEditorPreferences {

    constructor() {
        this._preferences = {};

        this._preferences.default_material_file = "Materials/Examples/Custom/marbley.mtlx";
        this._preferences.default_geometry_file = "sphere";

        this._preferences.icon_map = {
            "gltf": "./Icons/gltf_logo.webp",
            "usd": "./Icons/openusd_logo.webp",
            "open_pbr": "./Icons/openpbr_logo.svg", // TODO: Use official logo when available.
            "houdini": "./Icons/houdini_icon.webp",
            "maya": "./Icons/maya_surfaces.webp",
        };

        this._preferences.examples = {
            "Default Materials": {
                "Unlit": "Materials/Examples/Custom/default_unlit.mtlx",
                "OpenPBR": "Materials/Examples/OpenPBR/open_pbr_default.mtlx",
                "glTF PBR": "Materials/Examples/GltfPbr/gltf_pbr_default.mtlx",
                "Standard Surface": "Materials/Examples/StandardSurface/standard_surface_default.mtlx",
                "Usd Preview Surface": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_default.mtlx",            
            },
            "Sample Graphs": {
                "Patterns": {
                    "Gooch": "Materials/Examples/Custom/gooch_shade.mtlx",
                    "Simple Checkerboard": "Materials/Examples/Custom/simple_checkerboard_graph.mtlx",
                    "Hatch": "Materials/Examples/Custom/pseudo_hatching_publish.mtlx",
                    "Patterned Shaders": "Materials/Examples/Custom/compound_graph_example.mtlx",
                },
                "Materials": {
                    "glTF Boombox": "Materials/Examples/Custom/gltf_boombox_graph.mtlx",
                    "OpenPBR Pattern": "Materials/Examples/Custom/marbley.mtlx",
                    "Custom Shader Definition": "Materials/Examples/Custom/MayaLambert_embedded_def.mtlx",
                },
                "Images": {
                    "File Lookup": "Materials/Examples/Custom/simple_file_texture.mtlx",
                },
            },
            "Preset Materials": {
                "glTF": {
                    "Car Paint": "Materials/Examples/GltfPbr/gltf_pbr_carpaint.mtlx",
                    "Glass": "Materials/Examples/GltfPbr/gltf_pbr_glass.mtlx",
                    "Gold": "Materials/Examples/GltfPbr/gltf_pbr_gold.mtlx",
                    "Plastic": "Materials/Examples/GltfPbr/gltf_pbr_plastic.mtlx"
                },
                "OpenPBR": {
                    "Aluminum": "Materials/Examples/OpenPBR/open_pbr_aluminum_brushed.mtlx",
                    "Car Paint": "Materials/Examples/OpenPBR/open_pbr_carpaint.mtlx",
                    "Glass": "Materials/Examples/OpenPBR/open_pbr_glass.mtlx",
                    "Honey": "Materials/Examples/OpenPBR/open_pbr_honey.mtlx",
                    "Ketchup": "Materials/Examples/OpenPBR/open_pbr_ketchup.mtlx",
                    "Light Bulb": "Materials/Examples/OpenPBR/open_pbr_lightbulb.mtlx",
                    "Pearl": "Materials/Examples/OpenPBR/open_pbr_pearl.mtlx",
                    "Soap Bubble": "Materials/Examples/OpenPBR/open_pbr_soapbubble.mtlx",
                    "Velvet": "Materials/Examples/OpenPBR/open_pbr_velvet.mtlx"
                },
                "Standard Surface": {
                    "Brass": "Materials/Examples/StandardSurface/standard_surface_brass_tiled.mtlx",
                    "Brick": "Materials/Examples/StandardSurface/standard_surface_brick_procedural.mtlx",
                    "Car Paint": "Materials/Examples/StandardSurface/standard_surface_carpaint.mtlx",
                    "Chess Set": "Materials/Examples/StandardSurface/standard_surface_chess_set.mtlx",
                    "Chrome": "Materials/Examples/standard_surface_chrome.mtlx",
                    "Copper": "Materials/Examples/StandardSurface/standard_surface_copper.mtlx",
                    "Glass": "Materials/Examples/StandardSurface/standard_surface_glass.mtlx",
                    "Tinted Glass": "Materials/Examples/StandardSurface/standard_surface_glass_tinted.mtlx",
                    "Gold": "Materials/Examples/StandardSurface/standard_surface_gold.mtlx",
                    "Grey": "Materials/Examples/StandardSurface/standard_surface_greysphere.mtlx",
                    "Calibration": "Materials/Examples/StandardSurface/standard_surface_greysphere_calibration.mtlx",
                    "Jade": "Materials/Examples/StandardSurface/standard_surface_jade.mtlx",
                    "Marble": "Materials/Examples/StandardSurface/standard_surface_marble_solid.mtlx",
                    "Brushed Metal": "Materials/Examples/StandardSurface/standard_surface_metal_brushed.mtlx",
                    "Plastic": "Materials/Examples/StandardSurface/standard_surface_plastic.mtlx",
                    "Thin Film": "Materials/Examples/StandardSurface/standard_surface_thin_film.mtlx",
                    "Velvet": "Materials/Examples/StandardSurface/standard_surface_velvet.mtlx",
                    "Tiled Wood": "Materials/Examples/StandardSurface/standard_surface_wood_tiled.mtlx",
                },
                "UsdPreviewSurface": {
                    "Brass": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_brass_tiled.mtlx",
                    "Car Paint": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_carpaint.mtlx",
                    "Glass": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_glass.mtlx",
                    "Gold": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_gold.mtlx",
                    "Plastic": "Materials/Examples/UsdPreviewSurface/usd_preview_surface_plastic.mtlx",
                },
                "GPUOpen": {
                    "Motley Patchwork Rug": "Materials/Examples/Custom/AMD/Motley_Patchwork_Rug.mtlx",
                    "Black Upholstery": "Materials/Examples/Custom/AMD/Black_Upholstery.mtlx",
                    "Old Copper": "Materials/Examples/Custom/AMD/Copper_Old.mtlx"
                }
            }
        }
    }


    /**
     * @description Method to return the default geometry file
     * @returns {String} - Default geometry file path
     */
    getDefaultGeometryFile() {
        return this._preferences.default_geometry_file;
    }

    /**
     * @description Method to return the default material file
     * @returns {String} - Default material file path
     */
    getDefaultMaterialFile() {
        return this._preferences.default_material_file;
    }

    /**
     * @description Method to return the preferences object
     * @returns {Object} - Object containing preferences for the node editor
     */
    getPreferences() {
        return this._preferences;
    }

    /**
     * @description Return material examples structure
     * @returns {Object} - Object containing example materials
     */
    getExamples() {
        return this._preferences.examples;
    }

    /**
     * @description Return icon map structure
     * @returns {Object} - Object containing mapping of semantic categories to icons
     */
    getIconMap() {
        return this._preferences.icon_map;
    }
}

