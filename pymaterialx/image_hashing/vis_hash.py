# @file vis_hash.py
# @brief Comprehensive image hash comparison and visualization tool.
# Install dependeices with: pip install -r requirements.txt
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import time
import argparse

class ImageHashVisualizer:
    """
    Comprehensive image hash comparison and visualization tool.

    Hash method summary:
    - AverageHash (aHash): Computes a simple mean value of image pixels. Produces a binary hash by comparing each pixel to the average. Sensitive to overall brightness, robust to minor changes.
    - PHash (Perceptual Hash): Uses Discrete Cosine Transform (DCT) to capture image structure. More robust to small changes, compression, and scaling. Focuses on image features rather than pixel values.
    - ColorMomentHash: Uses color moments (mean, standard deviation, skewness) of image channels. Captures color distribution and statistics. Good for distinguishing images with different color schemes.
    - MarrHildrethHash: Based on Marr-Hildreth edge detection (Laplacian of Gaussian). Encodes edge information and image structure. Robust to lighting changes, focuses on shapes and edges.
    - RadialVarianceHash: Analyzes variance along radial lines from the image center in polar coordinates. Robust to rotation and circular patterns. Focuses on structural distribution radiating outward.

    Visualizations:
    - Absolute difference image
    - RMS difference heatmap
    - Histograms of per-pixel differences
    - Hash visualizations and similarity scores
    """
    def __init__(self, img1_path, img2_path):
        self.img1_path = img1_path
        self.img2_path = img2_path
        self.img1 = None
        self.img2 = None
        self.hash_methods = {
            'AverageHash': cv2.img_hash.AverageHash_create(),
            'PHash': cv2.img_hash.PHash_create(),
            'ColorMomentHash': cv2.img_hash.ColorMomentHash_create(),
            'MarrHildrethHash': cv2.img_hash.MarrHildrethHash_create(),
            #'RadialVarianceHash': cv2.img_hash.RadialVarianceHash_create()
        }
        self.timings = {}
        self.diff_abs = None
        self.diff_squared = None
        self.rms_overall = 0.0
        self.hash_results = {}
        self.visualize = False
        self.plot_differences = False
        self.save_figures = True
        self.visualize = False
        self.plot_differences = False

    def set_visualize(self, visualize): 
        self.visualize = visualize

    def set_plot_differences(self, plot):
        self.plot_differences = plot

    def set_image_paths(self, img1_path, img2_path):
        self.img1_path = img1_path
        self.img2_path = img2_path

    def get_hash_methods(self):
        return self.hash_methods

    def get_timings(self):
        return self.timings
    
    def clear_timings(self):
        self.timings = {}

    def draw(self):

        n_methods = len(self.hash_methods)
        t_plot = time.time()
        fig = plt.figure(figsize=(18, 6 * (n_methods + 2)))
        gs = plt.GridSpec(n_methods + 2, 6, figure=fig)

        # Row 0: Original images and difference
        ax1 = fig.add_subplot(gs[0, :2])
        ax2 = fig.add_subplot(gs[0, 2:4])
        ax3 = fig.add_subplot(gs[0, 4:6])

        # Row 1: RMS analysis
        ax4 = fig.add_subplot(gs[1, :2])
        ax5 = fig.add_subplot(gs[1, 2:4])
        ax6 = fig.add_subplot(gs[1, 4:6])

        # Timers for difference displays
        diff_plot_timings = {}

        # Original images
        t_img1 = time.time()
        ax1.imshow(cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB))
        ax1.set_title('Image 1')
        ax1.axis('off')
        diff_plot_timings['img1'] = time.time() - t_img1

        t_img2 = time.time()
        ax2.imshow(cv2.cvtColor(self.img2, cv2.COLOR_BGR2RGB))
        ax2.set_title('Image 2')
        ax2.axis('off')
        diff_plot_timings['img2'] = time.time() - t_img2

        t_absdiff = time.time()
        ax3.imshow(cv2.cvtColor(self.diff_abs, cv2.COLOR_BGR2RGB))
        ax3.set_title('Absolute Difference\n(Bright areas = more difference)')
        ax3.axis('off')
        diff_plot_timings['absolute_diff'] = time.time() - t_absdiff

        t_rms_heatmap = time.time()
        rms_normalized = np.sqrt(np.mean(self.diff_squared, axis=2))
        im = ax4.imshow(rms_normalized, cmap='hot')
        ax4.set_title(f'RMS Difference Heatmap\n(RMS: {self.rms_overall:.2f})')
        ax4.axis('off')
        plt.colorbar(im, ax=ax4)
        diff_plot_timings['rms_heatmap'] = time.time() - t_rms_heatmap

        t_rms_hist = time.time()
        if self.plot_differences:
            rms_flat = rms_normalized.flatten()
            ax5.hist(rms_flat, bins=50, color='gray', alpha=0.7)
            ax5.set_title('Per-Pixel RMS Difference Distribution')
            ax5.set_xlabel('RMS Difference')
            ax5.set_ylabel('Frequency')
            ax5.grid(True, alpha=0.3)
            rms_nonzero = rms_flat[rms_flat > 0]
            if len(rms_nonzero) > 0:
                rms_max_actual = np.max(rms_nonzero)
            else:
                rms_max_actual = 1.0
            ax5.set_xlim(0, float(rms_max_actual))
            rms_text = f'RMS Statistics:\nOverall: {self.rms_overall:.2f}\nMax: 255.0'
            ax5.text(0.98, 0.98, rms_text, ha='right', va='top', fontsize=10,
                    transform=ax5.transAxes,
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="lightyellow", alpha=0.8))
            diff_plot_timings['rms_histogram'] = time.time() - t_rms_hist

            t_abs_hist = time.time()
            diff_flat = self.diff_abs.flatten()
            ax6.hist(diff_flat, bins=50, color='red', alpha=0.7)
            ax6.set_title('Pixel Difference Distribution')
            ax6.set_xlabel('Absolute Difference')
            ax6.set_ylabel('Frequency')
            ax6.grid(True, alpha=0.3)
            diff_nonzero = diff_flat[diff_flat > 0]
            if len(diff_nonzero) > 0:
                diff_max_actual = np.max(diff_nonzero)
            else:
                diff_max_actual = 1.0
            ax6.set_xlim(0, float(diff_max_actual))
            diff_plot_timings['absolute_histogram'] = time.time() - t_abs_hist
        else:
            ax5.axis('off')
            ax6.axis('off')
        
        # Hash results - one row per method with 3 columns each
        plot_timings = {}
        for idx, (name, result) in enumerate(self.hash_results.items(), 2):
            t_plot_hash = time.time()
            # ...existing code...
            ax_hash1 = fig.add_subplot(gs[idx, 0:2])  # Hash 1 visualization
            ax_hash2 = fig.add_subplot(gs[idx, 2:4])  # Hash 2 visualization  
            ax_sim = fig.add_subplot(gs[idx, 4:6])    # Similarity result
            hash1 = result['hash1']
            hash2 = result['hash2']
            similarity = result['similarity']
            # ...existing code for visualization...
            if name in ['AverageHash', 'PHash', 'MarrHildrethHash']:
                hash1_bits = np.unpackbits(hash1)
                hash2_bits = np.unpackbits(hash2)
                hash_len = len(hash1_bits)
                factors = []
                for i in range(1, int(np.sqrt(hash_len)) + 1):
                    if hash_len % i == 0:
                        factors.append((i, hash_len // i))
                if factors:
                    rows, cols = factors[-1]
                else:
                    rows, cols = 8, hash_len // 8
                try:
                    hash1_img = hash1_bits.reshape(rows, cols)
                    hash2_img = hash2_bits.reshape(rows, cols)
                    ax_hash1.imshow(hash1_img, cmap='binary', interpolation='nearest')
                    ax_hash2.imshow(hash2_img, cmap='binary', interpolation='nearest')
                except:
                    ax_hash1.stem(range(len(hash1_bits)), hash1_bits, basefmt=" ")
                    ax_hash2.stem(range(len(hash2_bits)), hash2_bits, basefmt=" ")
            else:
                x = range(len(hash1))
                ax_hash1.bar(x, hash1.flatten(), alpha=0.7, color='blue')
                ax_hash2.bar(x, hash2.flatten(), alpha=0.7, color='blue')
                all_vals = np.concatenate([hash1.flatten(), hash2.flatten()])
                y_min, y_max = np.min(all_vals), np.max(all_vals)
                padding = (y_max - y_min) * 0.1
                ax_hash1.set_ylim(y_min - padding, y_max + padding)
                ax_hash2.set_ylim(y_min - padding, y_max + padding)
                ax_hash1.grid(True, alpha=0.3)
                ax_hash2.grid(True, alpha=0.3)
            hash1_title = f'{name}\nImage 1 Hash\nLength: {len(hash1)}'
            hash2_title = f'{name}\nImage 2 Hash\nLength: {len(hash2)}'
            ax_hash1.set_title(hash1_title, fontsize=10)
            ax_hash2.set_title(hash2_title, fontsize=10)
            if name in ['AverageHash', 'PHash', 'MarrHildrethHash']:
                color = "lightgreen" if similarity == 0 else "lightcoral"
                perfect_score = 0
            else:
                threshold = 100
                color = "lightgreen" if similarity < threshold else "lightcoral"
                perfect_score = 0
            similarity_text = f'Similarity Score: {similarity:.2f}'
            if similarity == perfect_score:
                similarity_text += '\n(Perfect Match!)'
            hex_text = ""
            if len(hash1) <= 16:
                import textwrap
                hash1_str = ' '.join(f'{int(x):02x}' for x in hash1.flatten())
                hash2_str = ' '.join(f'{int(x):02x}' for x in hash2.flatten())
                wrap_width = 32
                hash1_str_wrapped = '\n'.join(textwrap.wrap(hash1_str, wrap_width))
                hash2_str_wrapped = '\n'.join(textwrap.wrap(hash2_str, wrap_width))
                hex_text = f'\nImage 1 Hex:\n{hash1_str_wrapped}\nImage 2 Hex:\n{hash2_str_wrapped}'
            ax_sim.text(0.5, 0.5, similarity_text + hex_text,
                        ha='center', va='center', fontsize=12,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor=color))
            ax_sim.set_title(f'{name} Comparison Result', fontsize=12)
            ax_sim.axis('off')
            plot_timings[name] = time.time() - t_plot_hash
        
        #plt.tight_layout()

        self.timings['plotting'] = time.time() - t_plot
        self.timings['difference_display'] = diff_plot_timings
        t_save = time.time()
        if self.save_figures:
            plt.savefig('hash_comparison_visualization.png')
            self.timings['saving'] = time.time() - t_save

    def compare(self):
        self.clear_timings()
        t_start = time.time()
        t_load = time.time()
        self.img1 = cv2.imread(self.img1_path)
        self.img2 = cv2.imread(self.img2_path)
        self.timings['image_load'] = time.time() - t_load
        
        if self.img1 is None or self.img2 is None:
            raise ValueError("Could not load one or both images")
        
        # Resize to same dimensions
        if self.img1.shape != self.img2.shape:
            img2 = cv2.resize(self.img2, (self.img1.shape[1], self.img1.shape[0]))
                
        # Compute image differences with RMS
        t_rms = time.time()
        self.diff_abs = cv2.absdiff(self.img1, self.img2)
        self.diff_squared = (self.img1.astype(np.float32) - self.img2.astype(np.float32)) ** 2
        rms_b = sqrt(np.mean(self.diff_squared[:,:,0]))
        rms_g = sqrt(np.mean(self.diff_squared[:,:,1]))
        rms_r = sqrt(np.mean(self.diff_squared[:,:,2]))
        self.rms_overall = sqrt(np.mean(self.diff_squared))
        self.timings['rms_calc'] = time.time() - t_rms
        
        # Compute all hashes upfront
        t_hash = time.time()
        self.hash_results = {}
        hash_timings = {}
        for name, hash_func in self.hash_methods.items():
            t_hash_type = time.time()
            hash1 = hash_func.compute(self.img1)
            hash2 = hash_func.compute(self.img2)
            similarity = hash_func.compare(hash1, hash2)
            self.hash_results[name] = {
                'hash1': hash1,
                'hash2': hash2,
                'similarity': similarity,
                'func': hash_func
            }
            hash_timings[name] = time.time() - t_hash_type
        self.timings['hash_calc'] = time.time() - t_hash
        self.timings['hash_calc_types'] = hash_timings
        
        if self.visualize:
            self.draw()

        self.timings['total'] = time.time() - t_start

        return {
            'rms_overall': self.rms_overall,
            'rms_channels': (rms_b, rms_g, rms_r),
            'hash_results': self.hash_results
        }

def main():
    parser = argparse.ArgumentParser(description="Comprehensive Image Hash Comparison and Visualization Tool")
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    parser.add_argument("-v", "--visualize", action="store_true", help="Enable visualization of results")
    parser.add_argument("-pd", "--plot-differences", action="store_true", help="Plot image histograms")
    args = parser.parse_args()
    
    visualizer = ImageHashVisualizer(args.image1, args.image2)
    visualizer.set_plot_differences(args.plot_differences)
    visualizer.set_visualize(args.visualize)
    results = visualizer.compare()
    
    # Print summary
    print("### Image Hash Comparison Results\n")
    print(f"- RMS Overall: {results['rms_overall']}")

    print("##### Hash Similarities\n")
    print("| Hash Method | Hash Image 1 | Hash Image 2 | Similarity |")
    print("| :-------------: |:-------------: | :-----------: |:-----------: |")
    for name, result in results['hash_results'].items():
        hash1 = result['hash1']
        hash2 = result['hash2']
        # Format hash values for display
        if hasattr(hash1, 'flatten'):
            hash1_str = ' '.join(f'{int(x):02x}' for x in hash1.flatten())
        else:
            hash1_str = str(hash1)
        if hasattr(hash2, 'flatten'):
            hash2_str = ' '.join(f'{int(x):02x}' for x in hash2.flatten())
        else:
            hash2_str = str(hash2)
        #hash_display = f": {hash1_str}. 2: {hash2_str}"
        print(f"| {name} | {hash1_str} | { hash2_str} | {result['similarity']} |")

    timings = visualizer.get_timings()
    print("\n##### Timings (seconds)\n")
    print("| Step | Time (s) |")
    print("|------|----------|")
    for k, v in timings.items():
        if isinstance(v, dict):
            print(f"| **{k}** | |")
            for subk, subv in v.items():
                print(f"| - {subk} | {subv:.3f} |")
        else:
            print(f"| {k} | {v:.3f} |")

if __name__ == "__main__":
    main()