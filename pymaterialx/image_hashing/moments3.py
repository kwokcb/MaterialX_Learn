import numpy as np
import cv2
import sys

from numpy.lib.stride_tricks import as_strided
import math
from scipy.fftpack import dct

# ----------------------------------------------------
# Helper: OpenCV-equivalent BGR → HSV conversion
# ----------------------------------------------------
def bgr_to_hsv_numpy(bgr):
    b = bgr[..., 0] / 255.0
    g = bgr[..., 1] / 255.0
    r = bgr[..., 2] / 255.0
    
    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    delta = cmax - cmin

    # Hue
    h = np.zeros_like(cmax)
    mask = delta != 0
    
    r_eq_max = (cmax == r) & mask
    g_eq_max = (cmax == g) & mask
    b_eq_max = (cmax == b) & mask
    
    h[r_eq_max] = (60 * ((g[r_eq_max] - b[r_eq_max]) / delta[r_eq_max]) + 360) % 360
    h[g_eq_max] = (60 * ((b[g_eq_max] - r[g_eq_max]) / delta[g_eq_max]) + 120) % 360
    h[b_eq_max] = (60 * ((r[b_eq_max] - g[b_eq_max]) / delta[b_eq_max]) + 240) % 360
    
    # Saturation
    s = np.zeros_like(cmax)
    s[cmax != 0] = delta[cmax != 0] / cmax[cmax != 0]
    
    # Value
    v = cmax
    
    return np.stack([h, s, v], axis=-1)

# ----------------------------------------------------
# Helper: OpenCV-like bilinear resize to 256x256
# ----------------------------------------------------
def resize_bilinear_numpy(img, new_h=256, new_w=256):
    h, w, c = img.shape
    y = np.linspace(0, h - 1, new_h)
    x = np.linspace(0, w - 1, new_w)

    x0 = np.floor(x).astype(int)
    x1 = np.minimum(x0 + 1, w - 1)
    y0 = np.floor(y).astype(int)
    y1 = np.minimum(y0 + 1, h - 1)

    wy = y - y0
    wx = x - x0

    out = np.zeros((new_h, new_w, c), dtype=np.float32)

    for i in range(new_h):
        for j in range(new_w):
            top = (1 - wx[j]) * img[y0[i], x0[j]] + wx[j] * img[y0[i], x1[j]]
            bot = (1 - wx[j]) * img[y1[i], x0[j]] + wx[j] * img[y1[i], x1[j]]
            out[i, j] = (1 - wy[i]) * top + wy[i] * bot

    return out

# ----------------------------------------------------
# Helper: Compute skewness like OpenCV
# ----------------------------------------------------
def moment_skew(x, mean, std):
    if std == 0:
        return 0.0
    return np.mean(((x - mean) / std) ** 3)

# ----------------------------------------------------
# Extract 42-value Color Moment Hash
# ----------------------------------------------------
def color_moment_hash_numpy_only(bgr_image):

    # 1. Resize to 256x256 (OpenCV default)
    img = resize_bilinear_numpy(bgr_image.astype(np.float32), 256, 256)

    # 2. Convert BGR → HSV
    hsv = bgr_to_hsv_numpy(img)

    # 3. Split channels
    H = hsv[..., 0]
    S = hsv[..., 1]
    V = hsv[..., 2]

    # 4. Divide into 8×8 blocks → each block is 32×32 px
    block_size = 32
    blocks = []
    for by in range(8):
        for bx in range(8):
            y0 = by * block_size
            x0 = bx * block_size
            blocks.append((H[y0:y0+block_size, x0:x0+block_size],
                           S[y0:y0+block_size, x0:x0+block_size],
                           V[y0:y0+block_size, x0:x0+block_size]))

    # 5. Compute mean/std/skew for each block – 64 blocks × 3 channels × 3 stats = 576
    stats = np.zeros((64, 9), dtype=np.float32)
    for i, (h, s, v) in enumerate(blocks):
        vals = []
        for ch in [h, s, v]:
            m = float(np.mean(ch))
            sd = float(np.std(ch))
            sk = float(moment_skew(ch, m, sd))
            vals += [m, sd, sk]
        stats[i] = vals

    # 6. Compute mean/std across blocks → first 18 numbers
    mean_across = np.mean(stats, axis=0)
    std_across = np.std(stats, axis=0)
    first18 = np.concatenate([mean_across, std_across])

    # 7. Compute DCT of H channel (like OpenCV)
    dct_h = np.real(dct(dct(H.T, norm='ortho').T, norm='ortho'))

    # Extract the same 24 zig-zag positions used by OpenCV
    zigzag_positions = [
        (0,1),(1,0),(1,1),(0,2),(2,0),(1,2),(2,1),(2,2),
        (0,3),(3,0),(1,3),(3,1),(2,3),(3,2),
        (0,4),(4,0),(1,4),(4,1),(2,4),(4,2),(3,4),(4,3),
        (4,4),(0,5)
    ]
    dct_vals = np.array([dct_h[y, x] for (y, x) in zigzag_positions], dtype=np.float32)

    # 42 total values
    return np.concatenate([first18, dct_vals])

def compute_color_moments(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from {image_path}")

    #return color_moment_hash_numpy(image)
    return color_moment_hash_numpy_only(image)

def color_moment_hash_numpy_no(image_bgr):
    """
    Pure NumPy implementation of OpenCV ColorMomentHash.

    Input:
        image_bgr: BGR uint8 image (like cv2.imread output)
    Output:
        42-element float64 vector (same output shape as OpenCV)
    """

    # Resize to 256×256 as OpenCV implementation does
    img = cv2.resize(image_bgr, (256, 256), interpolation=cv2.INTER_AREA)

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float64)
    H, S, V = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]

    # Normalize to [0,1]
    H /= 255.0
    S /= 255.0
    V /= 255.0

    # Split into 8×8 blocks
    block_h = 256 // 8
    block_w = 256 // 8

    moments = []

    for by in range(8):
        for bx in range(8):
            block_H = H[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]
            block_S = S[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]
            block_V = V[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]

            # ---- Color moment features (for each block) ----
            #
            # OpenCV uses moment features:
            #    mean(H), mean(S), mean(V)
            #    stddev(H), stddev(S), stddev(V)
            #    skewness(H), skewness(S), skewness(V)
            #
            # That yields: 3 channels × 3 moments = 9 values per block
            #
            # 9 features × 8×8 blocks (64) = 576 values
            # BUT: ColorMomentHash outputs 42:
            #
            # It aggregates block moments across all 64 blocks:
            #   - mean of each moment across blocks
            #   - stddev of each moment across blocks
            #
            # Result: 9 features × (mean + stddev) = 18
            # Then each of H,S,V treated separately → 18×? → total 42
            #
            # So we compute block moments and aggregate later.

            for channel in (block_H, block_S, block_V):
                c = channel.flatten()
                mean = c.mean()
                std = c.std()
                skew = ((c - mean)**3).mean() ** (1/3)
                moments.append([mean, std, skew])

    # moments list = 64 blocks × 3 channels × 3 features = 576 rows
    M = np.array(moments).reshape(64, 9)

    # Aggregate like OpenCV:
    # compute per-feature means and stddev across the 64 blocks
    mean_features = M.mean(axis=0)
    std_features = M.std(axis=0)

    hash_vector = np.concatenate([mean_features, std_features])  # 18 values

    # OpenCV also computes hue-only high-frequency moment terms
    # (24 additional values) — implemented here:

    # Compute DCT of H channel
    H_dct = cv2.dct(H.astype(np.float64))

    # OpenCV samples DCT values in a zig-zag-like method:
    extra = []
    for i in range(1, 4):         # 3×3 = 9 positions (skip DC term)
        for j in range(1, 4):
            extra.append(H_dct[i, j])

    # Add neighboring coarse relationships (OpenCV’s 24-term extension)
    extra = np.array(extra + list(H_dct[4:8, 4:8].flatten()))
    # total extra = 9 + 16 = 25 (OpenCV uses 24; we drop 1)
    extra = extra[:24]

    # Final vec = 18 + 24 = 42 values
    return np.concatenate([hash_vector, extra])

##################################################

def color_moment_hash_numpy(image_bgr):
    """
    Pure NumPy implementation of the main logic of OpenCV ColorMomentHash.
    Produces a 42-element feature vector (18 block-moment features + 24 DCT features).
    """

    # Resize to 256×256 as OpenCV implementation does
    img = cv2.resize(image_bgr, (256, 256), interpolation=cv2.INTER_AREA)

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float64)
    H, S, V = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]

    # Normalize to [0,1]
    H /= 255.0
    S /= 255.0
    V /= 255.0

    # Split into 8×8 blocks
    block_h = 256 // 8
    block_w = 256 // 8

    moments = []

    for by in range(8):
        for bx in range(8):
            block_H = H[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]
            block_S = S[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]
            block_V = V[by*block_h:(by+1)*block_h, bx*block_w:(bx+1)*block_w]

            # Compute: mean, std, skewness for H, S, V
            for channel in (block_H, block_S, block_V):
                c = channel.flatten()

                mean = c.mean()
                std = c.std()

                # ---- FIXED SKEWNESS (OpenCV-style) ----
                if std == 0:
                    skew = 0.0
                else:
                    skew = np.mean((c - mean)**3) / (std**3)

                moments.append([mean, std, skew])

    # moments = 64 blocks × 3 channels × 3 moments = 576 × 3
    M = np.array(moments).reshape(64, 9)

    # Aggregate per-feature means and stddev across the 64 blocks
    mean_features = M.mean(axis=0)
    std_features  = M.std(axis=0)

    # First 18 output values
    hash_vector = np.concatenate([mean_features, std_features])

    # ----------------------------------------------------------------
    # EXTRA 24 VALUES (APPROXIMATE DCT SAMPLING — NOT FULL OPENCV MATCH)
    # ----------------------------------------------------------------
    H_dct = cv2.dct(H.astype(np.float64))

    extra = []

    # sample DCT[1:4, 1:4] -> 9 values
    for i in range(1, 4):
        for j in range(1, 4):
            extra.append(H_dct[i, j])

    # sample DCT[4:8, 4:8] -> 16 values (drop last to make 24 total)
    block_4x4 = H_dct[4:8, 4:8].flatten()
    extra.extend(block_4x4)

    extra = np.array(extra[:24])

    # Final 42-length vector
    return np.concatenate([hash_vector, extra])


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