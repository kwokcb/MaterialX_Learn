def reduce_bit_depth(img, bits=4):
    """
    @brief Reduce bit depth per channel for an image.
    @param img Input image (uint8).
    @param bits Number of bits to keep (1-8).
    @return Image with reduced bit depth per channel.
    """
    shift = 8 - bits
    return ((img >> shift) << shift).astype(np.uint8)

import os
import cv2
import numpy as np
import argparse

## @file optimize_images.py
#  @brief Batch optimize PNG images by resizing and/or reducing color precision using OpenCV.
#
#  This script allows batch processing of PNG images in a folder, supporting resizing by percentage 
#  and color quantization. 

def quantize_image(img, k):
    """
    @brief Reduce the number of colors in an image using k-means clustering.
    @param img Input image as a NumPy array.
    @param k Number of colors (clusters) to quantize to.
    @return Quantized image as a NumPy array.
    """
    pixels = img.reshape((-1, 3))
    pixels = np.float32(pixels)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    return quantized.reshape(img.shape)


def process_image(path, out_dir, resize_pct, quantize_k, do_resize, do_quantize, do_bitdepth, bitdepth, to_webp, webp_quality, setsize):
    """
    @brief Process a single image: resize, quantize colors, reduce bit depth, and/or convert to WebP, then save to output directory.
    @param path Path to the input image file.
    @param out_dir Output directory to save the processed image.
    @param resize_pct Resize percentage (int).
    @param quantize_k Number of colors for quantization (int).
    @param do_resize Whether to resize the image (bool).
    @param do_quantize Whether to quantize the image (bool).
    @param do_bitdepth Whether to reduce bit depth (bool).
    @param bitdepth Number of bits to keep per channel (int).
    @param to_webp Whether to save as WebP (bool).
    @param setsize Set absoute size.
    @param webp_quality WebP quality (int, 0-100).
    """
    img = cv2.imread(path)
    if img is None:
        print(f"Failed to read {path}")
        return
    if setsize and max(img.shape[0], img.shape[1]) > setsize:
        scale = setsize / max(img.shape[0], img.shape[1])
        width = int(img.shape[1] * scale)
        height = int(img.shape[0] * scale)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    if do_resize and resize_pct != 100:
        width = int(img.shape[1] * resize_pct / 100)
        height = int(img.shape[0] * resize_pct / 100)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    if do_bitdepth:
        img = reduce_bit_depth(img, bitdepth)
    if do_quantize:
        img = quantize_image(img, quantize_k)
    if to_webp:
        base = os.path.splitext(os.path.basename(path))[0]
        out_path = os.path.join(out_dir, base + ".webp")
        cv2.imwrite(out_path, img, [int(cv2.IMWRITE_WEBP_QUALITY), webp_quality])
    else:
        out_path = os.path.join(out_dir, os.path.basename(path))
        cv2.imwrite(out_path, img)
    print(f"Saved: {out_path}")


def main():
    """
    @brief Main entry point for the script. Parses arguments and processes all PNG images in the input folder.
    """
    parser = argparse.ArgumentParser(description="Batch optimize PNG images: resize, reduce bit depth, reduce precision, and/or convert to WebP.")
    parser.add_argument("input_folder", help="Folder containing PNG images")
    parser.add_argument("-o", "--output_folder", default=None, help="Output folder (default: input_folder/optimized)")
    parser.add_argument("-r", "--resize", type=int, default=100, help="Resize percentage (default: 50)")
    parser.add_argument("-p", "--pixelsize", type=int, default=0, help="Set size (in pixels)")
    parser.add_argument("-q", "--quantize", type=int, default=None, help="Reduce precision to K colors (e.g., 256)")
    parser.add_argument("-b", "--bitdepth", type=int, default=None, help="Reduce bit depth per channel (1-8, e.g., 4)")
    parser.add_argument("--webp", action="store_true", help="Save output images as WebP format")
    parser.add_argument("--webp_quality", type=int, default=80, help="WebP quality (0-100, default: 80)")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder or os.path.join(input_folder, "optimized")
    os.makedirs(output_folder, exist_ok=True)

    do_resize = args.resize is not None
    do_quantize = args.quantize is not None
    do_bitdepth = args.bitdepth is not None
    to_webp = args.webp
    webp_quality = args.webp_quality
    resize_pct = args.resize if do_resize else 100
    quantize_k = args.quantize if do_quantize else 256
    bitdepth = args.bitdepth if do_bitdepth else 8
    pixelsize = args.pixelsize if args.pixelsize is not None else -1    
    if pixelsize > 0:
        do_resize = False

    print(f'Processing folder: {input_folder}')
    processed_count = 0
    for fname in os.listdir(input_folder):
        if fname.lower().endswith(".png"):
            print(f"Processing: {fname}")
            in_path = os.path.join(input_folder, fname)
            process_image(in_path, output_folder, resize_pct, quantize_k, do_resize, do_quantize, do_bitdepth, bitdepth, to_webp, webp_quality, pixelsize)
            processed_count += 1
    print(f"Processed {processed_count} images.")
if __name__ == "__main__":
    main()
