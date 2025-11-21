import cv2
import sys
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_all_methods(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    if img1 is None or img2 is None:
        raise ValueError("Could not load one or both images")
    
    # Resize to same dimensions if different
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    results = {}
    
    # SSIM (Structural Similarity)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    results['SSIM'] = ssim(gray1, gray2)
    
    # OpenCV Hashes
    hashes = {
        'PHash': cv2.img_hash.PHash_create(),
        'ColorMomentHash': cv2.img_hash.ColorMomentHash_create(),
        'AverageHash': cv2.img_hash.AverageHash_create(),
        'MarrHildrethHash': cv2.img_hash.MarrHildrethHash_create()
    }
    
    for name, hash_func in hashes.items():
        hash1 = hash_func.compute(img1)
        hash2 = hash_func.compute(img2)
        print('Hashes for method:', name)
        print('hash1:', hash1)
        print('hash2:', hash2)
        results[name] = hash_func.compare(hash1, hash2)
    
    # RMS (Root Mean Square) Difference
    diff = img1.astype(np.float32) - img2.astype(np.float32)
    rms = np.sqrt(np.mean(np.square(diff)))
    results['RMS'] = rms
    
    return results

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_rendered.py <image1> <image2>")
        sys.exit(1)
    
    img1_path, img2_path = sys.argv[1], sys.argv[2]
    
    try:
        results = compare_all_methods(img1_path, img2_path)
        
        print("Comparison Results:")
        print("==================")
        for method, score in results.items():
            if method == 'SSIM':
                print(f"{method}: {score:.4f} (1.0 = identical)")
            elif method == 'RMS':
                print(f"{method}: {score:.4f} (0 = identical)")
            else:
                print(f"{method}: {score} (0 = identical)")
                
    except Exception as e:
        print(f"Error: {e}")
