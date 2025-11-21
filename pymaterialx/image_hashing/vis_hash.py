import cv2
import numpy as np
import matplotlib.pyplot as plt
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
    
    # Compute all hashes upfront
    hash_results = {}
    for name, hash_func in hash_methods.items():
        hash1 = hash_func.compute(img1)
        hash2 = hash_func.compute(img2)
        similarity = hash_func.compare(hash1, hash2)
        hash_results[name] = {
            'hash1': hash1,
            'hash2': hash2,
            'similarity': similarity,
            'func': hash_func
        }
    
    # Create figure - now with more rows for hash visualizations
    n_methods = len(hash_methods)
    fig = plt.figure(figsize=(18, 6 * (n_methods + 2)))
    
    # Create grid layout
    gs = plt.GridSpec(n_methods + 2, 6, figure=fig)
    
    # Row 0: Original images and difference
    ax1 = fig.add_subplot(gs[0, :2])
    ax2 = fig.add_subplot(gs[0, 2:4])
    ax3 = fig.add_subplot(gs[0, 4:6])
    
    # Row 1: RMS analysis
    ax4 = fig.add_subplot(gs[1, :2])
    ax5 = fig.add_subplot(gs[1, 2:4])
    ax6 = fig.add_subplot(gs[1, 4:6])
    
    # Original images
    ax1.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    ax1.set_title('Image 1')
    ax1.axis('off')
    
    ax2.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    ax2.set_title('Image 2')
    ax2.axis('off')
    
    # Absolute difference
    ax3.imshow(cv2.cvtColor(diff_abs, cv2.COLOR_BGR2RGB))
    ax3.set_title('Absolute Difference\n(Bright areas = more difference)')
    ax3.axis('off')
    
    # RMS Difference visualization
    rms_normalized = np.sqrt(np.mean(diff_squared, axis=2))
    im = ax4.imshow(rms_normalized, cmap='hot')
    ax4.set_title('RMS Difference Heatmap\n(Hot = more difference)')
    ax4.axis('off')
    plt.colorbar(im, ax=ax4)
    
    # RMS statistics
    ax5.axis('off')
    rms_text = f'RMS Difference Statistics:\n\n'
    rms_text += f'Overall RMS: {rms_overall:.2f}\n'
    rms_text += f'Red Channel RMS: {rms_r:.2f}\n'
    rms_text += f'Green Channel RMS: {rms_g:.2f}\n'
    rms_text += f'Blue Channel RMS: {rms_b:.2f}\n\n'
    rms_text += f'Max Possible: 255.0'
    
    ax5.text(0.5, 0.5, rms_text, ha='center', va='center', fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    ax5.set_title('RMS Difference Values')
    
    # Difference histogram
    diff_flat = diff_abs.flatten()
    ax6.hist(diff_flat, bins=50, color='red', alpha=0.7)
    ax6.set_title('Pixel Difference Distribution')
    ax6.set_xlabel('Absolute Difference')
    ax6.set_ylabel('Frequency')
    ax6.grid(True, alpha=0.3)
    
    # Hash results - one row per method with 3 columns each
    for idx, (name, result) in enumerate(hash_results.items(), 2):
        # Create subplots for this hash method
        ax_hash1 = fig.add_subplot(gs[idx, 0:2])  # Hash 1 visualization
        ax_hash2 = fig.add_subplot(gs[idx, 2:4])  # Hash 2 visualization  
        ax_sim = fig.add_subplot(gs[idx, 4:6])    # Similarity result
        
        hash1 = result['hash1']
        hash2 = result['hash2']
        similarity = result['similarity']
        
        # Visualize hashes based on type
        if name in ['AverageHash', 'PHash', 'MarrHildrethHash']:
            # Bit-based hashes - show as binary images
            hash1_bits = np.unpackbits(hash1)
            hash2_bits = np.unpackbits(hash2)
            
            # Determine optimal grid size
            hash_len = len(hash1_bits)
            # Find factors for grid
            factors = []
            for i in range(1, int(np.sqrt(hash_len)) + 1):
                if hash_len % i == 0:
                    factors.append((i, hash_len // i))
            
            if factors:
                rows, cols = factors[-1]  # Use most square aspect ratio
            else:
                rows, cols = 8, hash_len // 8  # Fallback
                
            try:
                hash1_img = hash1_bits.reshape(rows, cols)
                hash2_img = hash2_bits.reshape(rows, cols)
                
                ax_hash1.imshow(hash1_img, cmap='binary', interpolation='nearest')
                ax_hash2.imshow(hash2_img, cmap='binary', interpolation='nearest')
                
            except:
                # If reshaping fails, plot as 1D array
                ax_hash1.stem(range(len(hash1_bits)), hash1_bits, basefmt=" ")
                ax_hash2.stem(range(len(hash2_bits)), hash2_bits, basefmt=" ")
                
        else:
            # Non-bit hashes (like ColorMomentHash) - plot as bar charts
            x = range(len(hash1))
            ax_hash1.bar(x, hash1.flatten(), alpha=0.7, color='blue')
            ax_hash2.bar(x, hash2.flatten(), alpha=0.7, color='blue')
            
            # Set similar y-axis limits for comparison
            all_vals = np.concatenate([hash1.flatten(), hash2.flatten()])
            y_min, y_max = np.min(all_vals), np.max(all_vals)
            padding = (y_max - y_min) * 0.1
            ax_hash1.set_ylim(y_min - padding, y_max + padding)
            ax_hash2.set_ylim(y_min - padding, y_max + padding)
            
            ax_hash1.grid(True, alpha=0.3)
            ax_hash2.grid(True, alpha=0.3)
        
        # Set titles for hash visualizations
        hash1_title = f'{name}\nImage 1 Hash\nLength: {len(hash1)}'
        hash2_title = f'{name}\nImage 2 Hash\nLength: {len(hash2)}'
        
        ax_hash1.set_title(hash1_title, fontsize=10)
        ax_hash2.set_title(hash2_title, fontsize=10)
        
        # Similarity result with color coding
        if name in ['AverageHash', 'PHash', 'MarrHildrethHash']:
            # For bit-based hashes, 0 = identical
            color = "lightgreen" if similarity == 0 else "lightcoral"
            perfect_score = 0
        else:
            # For distance-based hashes, lower = more similar
            # Use a threshold - you might need to adjust this
            threshold = 100  # Adjust based on the hash method
            color = "lightgreen" if similarity < threshold else "lightcoral"
            perfect_score = 0
        
        similarity_text = f'Similarity Score: {similarity:.2f}'
        if similarity == perfect_score:
            similarity_text += '\n(Perfect Match!)'
        
        ax_sim.text(0.5, 0.5, similarity_text, 
                   ha='center', va='center', fontsize=14,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=color))
        ax_sim.set_title(f'{name} Comparison Result', fontsize=12)
        ax_sim.axis('off')
        
        # Add hash values as text for small hashes
        if len(hash1) <= 16:  # Only show for reasonably small hashes
            hash1_str = ' '.join(f'{int(x):02x}' for x in hash1.flatten())
            hash2_str = ' '.join(f'{int(x):02x}' for x in hash2.flatten())
            
            ax_hash1.text(0.02, 0.98, f'Hex: {hash1_str}', 
                         transform=ax_hash1.transAxes, fontsize=8, 
                         verticalalignment='top', bbox=dict(boxstyle="round,pad=0.1", facecolor="white", alpha=0.7))
            ax_hash2.text(0.02, 0.98, f'Hex: {hash2_str}', 
                         transform=ax_hash2.transAxes, fontsize=8, 
                         verticalalignment='top', bbox=dict(boxstyle="round,pad=0.1", facecolor="white", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('hash_comparison_visualization.png')
    
    return {
        'rms_overall': rms_overall,
        'rms_channels': (rms_b, rms_g, rms_r),
        'hash_results': hash_results
    }

# Usage example
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python hash_comparison.py <image1> <image2>")
        sys.exit(1)
    
    img1_path, img2_path = sys.argv[1], sys.argv[2]
    results = comprehensive_hash_visualization(img1_path, img2_path)
    
    # Print summary
    print("\n=== SUMMARY ===")
    print(f"RMS Overall: {results['rms_overall']:.2f}")
    print("\nHash Similarities:")
    for name, result in results['hash_results'].items():
        print(f"{name}: {result['similarity']}")
