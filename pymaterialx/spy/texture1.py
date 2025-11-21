## main.py

import slangpy as spy
import numpy as np
import pathlib
import os
import socket
import time

currentFolder = pathlib.Path().cwd()
# Create a Slang device with the current folder included in the search paths.
device = spy.create_device(include_paths=[str(currentFolder),
])

slang_source = """
// A simple function that adds two numbers together
float add(float a, float b)
{
    return a + b;
}
"""

# A Slang module represents a collection of Slang code that can be compiled and executed on the device. 
#module = spy.Module.load_from_file(device, "example.slang")
module = spy.Module.load_from_source(device, "example.slang", slang_source)

# Create a couple of buffers with 128x128 random floats
a = np.random.rand(128, 128).astype(np.float32)
b = np.random.rand(128, 128).astype(np.float32)

# Call our function and ask for a texture back
result = module.add(a, b, _result='texture')

# Print the first 5x5 values
print(result.to_numpy()[:5, :5])

# Display the result using tev if the viewer is running
def _tev_is_running(host=None, port=None):
    h = host or os.environ.get("TEV_HOST", "127.0.0.1")
    p = int(os.environ.get("TEV_PORT", "14158")) if port is None else int(port)
    try:
        with socket.create_connection((h, p), timeout=0.2):
            return True
    except OSError:
        return False

# Always save PNG when displaying via tev or Matplotlib
ALWAYS_SAVE = True

def _prep_rgb(arr: np.ndarray) -> np.ndarray:
    img = arr
    if img.ndim == 2:
        img = np.repeat(img[..., None], 3, axis=2)
    if img.shape[-1] == 4:
        img = img[..., :3]
    if img.shape[-1] == 1:
        img = np.repeat(img, 3, axis=2)
    return np.clip(img, 0, 1)

def _save_image(arr: np.ndarray, name: str) -> pathlib.Path | None:
    stem = name.replace(' ', '_')
    out_path = pathlib.Path.cwd() / f"{stem}.png"
    img = _prep_rgb(arr)
    # Try Pillow
    try:
        from PIL import Image
        img8 = (img * 255).astype(np.uint8)
        Image.fromarray(img8).save(out_path)
        print(f"[INFO] Saved image to {out_path}")
        return out_path
    except Exception:
        pass
    # Try Matplotlib
    try:
        import matplotlib.pyplot as plt
        plt.imsave(out_path, img)
        print(f"[INFO] Saved image to {out_path}")
        return out_path
    except Exception:
        pass
    # Last resort: save numpy array
    npy_path = pathlib.Path.cwd() / f"{stem}.npy"
    np.save(npy_path, arr)
    print(f"[INFO] Could not save PNG; saved array to {npy_path}. Install pillow or matplotlib to save images.")
    return None

if _tev_is_running():
    spy.tev.show(result, name='add random')
    if ALWAYS_SAVE:
        _ = _save_image(result.to_numpy(), 'add_random')
else:
    print("[INFO] tev viewer not running; falling back to local display.")

    def _display_fallback(tex, name='image'):
        arr = tex.to_numpy()
        # Try Matplotlib first
        try:
            import matplotlib.pyplot as plt
            img = arr
            if img.ndim == 2:
                plt.imshow(img, cmap='gray')
            else:
                if img.shape[-1] == 4:
                    img = img[..., :3]
                if img.shape[-1] == 1:
                    img = img[..., 0]
                    plt.imshow(img, cmap='gray')
                else:
                    plt.imshow(np.clip(img, 0, 1))
            if ALWAYS_SAVE:
                _ = _save_image(arr, name)
            plt.title(name)
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            return
        except Exception:
            pass

        # Fallback to Pillow: save PNG and open
        try:
            from PIL import Image
            img = arr
            if img.ndim == 2:
                img = np.repeat(img[..., None], 3, axis=2)
            if img.shape[-1] == 4:
                img = img[..., :3]
            if img.shape[-1] == 1:
                img = np.repeat(img, 3, axis=2)
            img8 = (np.clip(img, 0, 1) * 255).astype(np.uint8)
            out_path = pathlib.Path.cwd() / f"{name.replace(' ', '_')}.png"
            Image.fromarray(img8).save(out_path)
            try:
                import webbrowser
                webbrowser.open(str(out_path.resolve()))
            except Exception:
                pass
            print(f"[INFO] Saved image to {out_path}")
            return
        except Exception:
            pass

        # Last resort: save numpy array
        npy_path = pathlib.Path.cwd() / f"{name.replace(' ', '_')}.npy"
        np.save(npy_path, arr)
        print(f"[INFO] Could not display image; saved array to {npy_path}. Install matplotlib or pillow for visualization.")

    _display_fallback(result, name='add_random')