import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

#import cv2
#import numpy as np
#import matplotlib.pyplot as plt
from math import sqrt

def comprehensive_hash_visualization(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    if img1 is None or img2 is None:
        raise ValueError("Could not load one or both images")
    
    # Resize to same dimensions
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    hash_methods = {
        'AverageHash': cv2.img_hash.AverageHash_create(),
        'PHash': cv2.img_hash.PHash_create(),
        'ColorMomentHash': cv2.img_hash.ColorMomentHash_create(),
        'MarrHildrethHash': cv2.img_hash.MarrHildrethHash_create()
    }
    
    # Compute image differences with RMS
    diff_abs = cv2.absdiff(img1, img2)
    diff_squared = (img1.astype(np.float32) - img2.astype(np.float32)) ** 2
    
    # Calculate RMS for each channel and overall
    rms_b = sqrt(np.mean(diff_squared[:,:,0]))
    rms_g = sqrt(np.mean(diff_squared[:,:,1]))
    rms_r = sqrt(np.mean(diff_squared[:,:,2]))
    rms_overall = sqrt(np.mean(diff_squared))
    
    # Create figure
    n_methods = len(hash_methods)
    fig, axes = plt.subplots(n_methods + 2, 3, figsize=(15, 5 * (n_methods + 2)))
    
    # Original images
    axes[0,0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('Image 1')
    axes[0,0].axis('off')
    
    axes[0,1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title('Image 2')
    axes[0,1].axis('off')
    
    # Absolute difference
    axes[0,2].imshow(cv2.cvtColor(diff_abs, cv2.COLOR_BGR2RGB))
    axes[0,2].set_title('Absolute Difference\n(Bright areas = more difference)')
    axes[0,2].axis('off')
    
    # RMS Difference visualization
    rms_normalized = np.sqrt(np.mean(diff_squared, axis=2))
    im = axes[1,0].imshow(rms_normalized, cmap='hot')
    axes[1,0].set_title('RMS Difference Heatmap\n(Hot = more difference)')
    axes[1,0].axis('off')
    plt.colorbar(im, ax=axes[1,0])
    
    # RMS statistics
    axes[1,1].axis('off')
    rms_text = f'RMS Difference Statistics:\n\n'
    rms_text += f'Overall RMS: {rms_overall:.2f}\n'
    rms_text += f'Red Channel RMS: {rms_r:.2f}\n'
    rms_text += f'Green Channel RMS: {rms_g:.2f}\n'
    rms_text += f'Blue Channel RMS: {rms_b:.2f}\n\n'
    rms_text += f'Max Possible: 255.0'
    
    axes[1,1].text(0.5, 0.5, rms_text, ha='center', va='center', fontsize=12,
                  bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    axes[1,1].set_title('RMS Difference Values')
    
    # Difference histogram
    diff_flat = diff_abs.flatten()
    axes[1,2].hist(diff_flat, bins=50, color='red', alpha=0.7)
    axes[1,2].set_title('Pixel Difference Distribution')
    axes[1,2].set_xlabel('Absolute Difference')
    axes[1,2].set_ylabel('Frequency')
    axes[1,2].grid(True, alpha=0.3)
    
    # Hash results
    for idx, (name, hash_func) in enumerate(hash_methods.items(), 2):
        hash1 = hash_func.compute(img1)
        hash2 = hash_func.compute(img2)
        similarity = hash_func.compare(hash1, hash2)
        
        # For bit-based hashes, show visual representation
        if name in ['AverageHash', 'PHash']:
            hash1_bits = np.unpackbits(hash1)
            hash2_bits = np.unpackbits(hash2)
            hash_size = int(np.sqrt(len(hash1_bits)))
            
            hash1_img = hash1_bits.reshape(hash_size, hash_size)
            hash2_img = hash2_bits.reshape(hash_size, hash_size)
            
            axes[idx,0].imshow(hash1_img, cmap='binary', interpolation='nearest')
            axes[idx,0].set_title(f'{name}\nHash 1')
            axes[idx,0].axis('off')
            
            axes[idx,1].imshow(hash2_img, cmap='binary', interpolation='nearest')
            axes[idx,1].set_title(f'{name}\nHash 2')
            axes[idx,1].axis('off')
        else:
            # For non-bit hashes, just show the values
            axes[idx,0].text(0.5, 0.6, f'{name}\nHash 1', ha='center', va='center', fontsize=10)
            axes[idx,0].text(0.5, 0.4, f'Length: {len(hash1)}', ha='center', va='center', fontsize=8)
            axes[idx,0].axis('off')
            
            axes[idx,1].text(0.5, 0.6, f'{name}\nHash 2', ha='center', va='center', fontsize=10)
            axes[idx,1].text(0.5, 0.4, f'Length: {len(hash2)}', ha='center', va='center', fontsize=8)
            axes[idx,1].axis('off')
        
        # Similarity result with color coding
        color = "lightgreen" if similarity == 0 else "lightcoral"
        axes[idx,2].text(0.5, 0.5, f'Similarity: {similarity}', 
                        ha='center', va='center', fontsize=12,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor=color))
        axes[idx,2].set_title('Comparison Result')
        axes[idx,2].axis('off')
    
    plt.tight_layout()
    plt.savefig("vis_rms.png")
    #plt.show()
    
    return {
        'rms_overall': rms_overall,
        'rms_channels': (rms_b, rms_g, rms_r),
        'hash_results': {name: hash_func.compare(hash_func.compute(img1), hash_func.compute(img2)) 
                        for name, hash_func in hash_methods.items()}
    }

def visualize_bit_hash(image_path, hash_method_name):
    img = cv2.imread(image_path)
    
    if hash_method_name == "AverageHash":
        hash_func = cv2.img_hash.AverageHash_create()
    elif hash_method_name == "PHash":
        hash_func = cv2.img_hash.PHash_create()
    else:
        raise ValueError("Unsupported hash method")
    
    hash_value = hash_func.compute(img)
    
    # Convert hash to binary image (typically 8x8 for AverageHash)
    hash_size = int(np.sqrt(len(hash_value) * 8))
    hash_bits = np.unpackbits(hash_value).reshape(hash_size, hash_size)
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Original image
    ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    ax1.set_title(f'Original Image')
    ax1.axis('off')
    
    # Hash visualization
    ax2.imshow(hash_bits, cmap='binary', interpolation='nearest')
    ax2.set_title(f'{hash_method_name} Visualization\n{hash_size}x{hash_size} bits')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    return hash_bits

def visualize_hash_comparison(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    # Resize to same dimensions
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    # Initialize hash methods
    hash_methods = {
        'AverageHash': cv2.img_hash.AverageHash_create(),
        'PHash': cv2.img_hash.PHash_create(),
        'ColorMomentHash': cv2.img_hash.ColorMomentHash_create()
    }
    
    results = {}
    
    # Compute hashes and differences
    for name, hash_func in hash_methods.items():
        hash1 = hash_func.compute(img1)
        hash2 = hash_func.compute(img2)
        similarity = hash_func.compare(hash1, hash2)
        results[name] = {
            'hash1': hash1,
            'hash2': hash2, 
            'similarity': similarity
        }
    
    # Create visualization
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    
    # Original images
    axes[0,0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('Image 1')
    axes[0,0].axis('off')
    
    axes[0,1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title('Image 2')
    axes[0,1].axis('off')
    
    # Pixel difference
    diff = cv2.absdiff(img1, img2)
    axes[0,2].imshow(cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
    axes[0,2].set_title('Pixel Difference')
    axes[0,2].axis('off')
    
    # Hash visualizations
    col = 0
    for name, result in results.items():
        if name in ['AverageHash', 'PHash']:
            # Visualize bit-based hashes
            hash1_bits = np.unpackbits(result['hash1'])
            hash2_bits = np.unpackbits(result['hash2'])
            hash_size = int(np.sqrt(len(hash1_bits)))
            
            hash1_img = hash1_bits.reshape(hash_size, hash_size)
            hash2_img = hash2_bits.reshape(hash_size, hash_size)
            
            axes[1,col].imshow(hash1_img, cmap='binary', interpolation='nearest')
            axes[1,col].set_title(f'{name}\nHash 1\nSimilarity: {result["similarity"]}')
            axes[1,col].axis('off')
            
            axes[1,col+1].imshow(hash2_img, cmap='binary', interpolation='nearest')
            axes[1,col+1].set_title(f'{name}\nHash 2')
            axes[1,col+1].axis('off')
            
            col += 2
    
    plt.tight_layout()
    plt.show()
    
    return results

def visualize_hash_differences(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    #hash_func = cv2.img_hash.ColorMomentHash_create()
    hash_func = cv2.img_hash.PHash_create()
    hash1 = hash_func.compute(img1)
    hash2 = hash_func.compute(img2)
    
    # Convert hashes to binary arrays
    hash1_bits = np.unpackbits(hash1)
    hash2_bits = np.unpackbits(hash2)
    
    # Create difference map (1 = different, 0 = same)
    diff_bits = hash1_bits != hash2_bits
    hash_size = int(np.sqrt(len(diff_bits)))
    diff_map = diff_bits.reshape(hash_size, hash_size)
    
    # Visualization
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    # Original images
    axes[0,0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('Image 1')
    axes[0,0].axis('off')
    
    axes[0,1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title('Image 2')
    axes[0,1].axis('off')
    
    # Hash visualizations
    hash1_img = hash1_bits.reshape(hash_size, hash_size)
    hash2_img = hash2_bits.reshape(hash_size, hash_size)
    
    axes[0,2].imshow(hash1_img, cmap='binary', interpolation='nearest')
    axes[0,2].set_title('Hash 1 (Image 1)')
    axes[0,2].axis('off')
    
    axes[1,0].imshow(hash2_img, cmap='binary', interpolation='nearest')
    axes[1,0].set_title('Hash 2 (Image 2)')
    axes[1,0].axis('off')
    
    # Difference heatmap
    im = axes[1,1].imshow(diff_map, cmap='Reds', interpolation='nearest')
    axes[1,1].set_title(f'Hash Differences\n{np.sum(diff_bits)} differing bits')
    axes[1,1].axis('off')
    plt.colorbar(im, ax=axes[1,1])
    
    # Similarity score
    similarity = hash_func.compare(hash1, hash2)
    axes[1,2].text(0.5, 0.5, f'Similarity Score:\n{similarity}', 
                   ha='center', va='center', fontsize=15)
    axes[1,2].set_title('Comparison Result')
    axes[1,2].axis('off')
    
    plt.tight_layout()
    plt.savefig("vis.png")
    plt.show()

def comprehensive_hash_visualization_v1(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    
    hash_methods = {
        'AverageHash': cv2.img_hash.AverageHash_create(),
        'PHash': cv2.img_hash.PHash_create(),
        'ColorMomentHash': cv2.img_hash.ColorMomentHash_create(),
        'MarrHildrethHash': cv2.img_hash.MarrHildrethHash_create()
    }
    
    # Create figure
    n_methods = len(hash_methods)
    fig, axes = plt.subplots(n_methods + 1, 3, figsize=(12, 4 * (n_methods + 1)))
    
    # Original images
    axes[0,0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0,0].set_title('Image 1')
    axes[0,0].axis('off')
    
    axes[0,1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[0,1].set_title('Image 2')
    axes[0,1].axis('off')
    
    diff = cv2.absdiff(img1, img2)
    axes[0,2].imshow(cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
    axes[0,2].set_title('Pixel Difference')
    axes[0,2].axis('off')
    
    # Hash results
    for idx, (name, hash_func) in enumerate(hash_methods.items(), 1):
        hash1 = hash_func.compute(img1)
        hash2 = hash_func.compute(img2)
        similarity = hash_func.compare(hash1, hash2)
        
        axes[idx,0].text(0.5, 0.6, f'{name}\nHash 1', ha='center', va='center', fontsize=12)
        axes[idx,0].text(0.5, 0.4, f'Length: {len(hash1)}', ha='center', va='center', fontsize=10)
        axes[idx,0].axis('off')
        
        axes[idx,1].text(0.5, 0.6, f'{name}\nHash 2', ha='center', va='center', fontsize=12)
        axes[idx,1].text(0.5, 0.4, f'Length: {len(hash2)}', ha='center', va='center', fontsize=10)
        axes[idx,1].axis('off')
        
        axes[idx,2].text(0.5, 0.5, f'Similarity: {similarity}', 
                        ha='center', va='center', fontsize=14,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
        axes[idx,2].set_title('Comparison Result')
        axes[idx,2].axis('off')
    
    plt.tight_layout()
    plt.savefig("vis_c.png")
    #plt.show()

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_rendered.py <image1> <image2>")
        sys.exit(1)
    
    img1_path, img2_path = sys.argv[1], sys.argv[2]
    
    #try:
    #    results = compare_all_methods(img1_path, img2_path)
    #    
    #    print("Comparison Results:")
    #    print("==================")
    #    for method, score in results.items():
    #        if method == 'SSIM':
    #            print(f"{method}: {score:.4f} (1.0 = identical)")
    #        elif method == 'RMS':
    #            print(f"{method}: {score:.4f} (0 = identical)")
    #        else:
    #            print(f"{method}: {score} (0 = identical)")
    #            
    #except Exception as e:
    #    print(f"Error: {e}")

    #img1_path, img2_path = "image1.png", "image2.png"
    
    # Choose one visualization method:
    # visualize_bit_hash(img1_path, "PHash")
    # visualize_hash_comparison(img1_path, img2_path)
    #visualize_hash_differences(img1_path, img2_path)
    comprehensive_hash_visualization(img1_path, img2_path)
