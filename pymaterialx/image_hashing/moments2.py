import cv2
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python color_moment_hash_opencv.py <image1_path> <image2_path>")
        sys.exit(1)

    img1_path, img2_path = sys.argv[1], sys.argv[2]

    # Load images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print("Error: Could not load one or both images")
        sys.exit(1)

    # Create Color Moment Hash object
    cm_hash = cv2.img_hash.ColorMomentHash_create()

    # Compute the hash
    hash1 = cm_hash.compute(img1)
    hash2 = cm_hash.compute(img2)

    # Compare the hashes
    similarity = cm_hash.compare(hash1, hash2)

    print(f"Color Moment Hash similarity: {similarity}")
    # Note: The compare function returns a value that represents the similarity.
    # Lower values mean more similar.

if __name__ == "__main__":
    main()
