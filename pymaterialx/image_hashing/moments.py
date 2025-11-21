import cv2
import numpy as np
import sys

def compute_color_moments(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")
    
    # Convert BGR to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Split into H, S, V channels
    h, s, v = cv2.split(hsv)
    
    # Compute moments for each channel
    channels = [h, s, v]
    feature_vector = []
    
    for channel in channels:
        # Convert to float64 for higher precision
        channel_float = channel.astype(np.float64)
        mean = np.mean(channel_float)
        std = np.std(channel_float)
        # Skewness: third standardized moment
        skew = np.mean((channel_float - mean) ** 3) / (std ** 3) if std != 0 else 0.0
        feature_vector.extend([mean, std, skew])
    
    return np.array(feature_vector)

def main():
    if len(sys.argv) != 3:
        print("Usage: python color_moment_hash.py <image1_path> <image2_path>")
        sys.exit(1)
    
    img1_path, img2_path = sys.argv[1], sys.argv[2]
    
    try:
        # Compute color moments for both images
        moments1 = compute_color_moments(img1_path)
        moments2 = compute_color_moments(img2_path)
        
        # Compute Euclidean distance between the feature vectors
        distance = np.linalg.norm(moments1 - moments2)
        
        print(f"Color Moments for Image 1: {moments1}")
        print(f"Color Moments for Image 2: {moments2}")
        print(f"Euclidean Distance between feature vectors: {distance}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
