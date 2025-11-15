import json
import os
import platform
import urllib.request
import zipfile
import tarfile

GITHUB_API = "https://api.github.com/repos/shader-slang/slang/releases/latest"

# ----------------------------------------------------------------------
# Determine which asset to download based on OS / architecture
# ----------------------------------------------------------------------
def choose_asset(assets):
    #print('assets:', assets)
    system = platform.system().lower()
    arch = platform.machine().lower()

    # Map system names to keywords to search for in asset names
    system_keywords = {
        "windows": "windows",
        "linux": "linux",
        "darwin": "macos"  # macOS
    }

    # Map architecture names - keep both normalized and original variants
    arch_variants = []
    if arch in ("x86_64", "amd64"):
        arch_variants = ["x86_64", "x64"]
    elif arch in ("arm64", "aarch64"):
        arch_variants = ["aarch64", "arm64"]
    else:
        arch_variants = [arch]

    # Get the system keyword for this platform
    system_keyword = system_keywords.get(system)
    if not system_keyword:
        raise RuntimeError(f"Unsupported OS: {system}")

    # Find a matching asset by checking for both system and arch keywords
    # Prefer non-debug builds and zip over tar
    candidates = []
    for a in assets:
        name_lower = a["name"].lower()
        # Skip debug-info builds
        if "debug-info" in name_lower:
            continue
        # Check if asset name contains the system keyword and any arch variant
        if system_keyword in name_lower:
            for arch_variant in arch_variants:
                if arch_variant in name_lower:
                    candidates.append(a)
                    break

    # Prefer .zip over .tar.gz
    for candidate in candidates:
        if candidate["name"].lower().endswith(".zip"):
            return candidate
    
    # Fall back to any candidate (likely .tar.gz)
    if candidates:
        return candidates[0]

    raise RuntimeError(f"No suitable Slang binary found for this OS/arch: {arch} on {system}")


# ----------------------------------------------------------------------
# Download a file
# ----------------------------------------------------------------------
def download(url, path):
    print(f"Downloading: {url}")
    urllib.request.urlretrieve(url, path)
    print(f"Saved to: {path}")


# ----------------------------------------------------------------------
# Extract zip or tar.gz
# ----------------------------------------------------------------------
def extract(path, out_dir="slang"):
    print(f"Extracting {path}...")
    if path.endswith(".zip"):
        with zipfile.ZipFile(path, "r") as z:
            z.extractall(out_dir)
    elif path.endswith(".tar.gz"):
        with tarfile.open(path, "r:gz") as t:
            t.extractall(out_dir)
    else:
        raise RuntimeError("Unsupported archive format.")
    print(f"Extracted to: {out_dir}")


# ----------------------------------------------------------------------
# Main logic
# ----------------------------------------------------------------------
def main():
    print("Fetching latest Slang release info...")
    data = urllib.request.urlopen(GITHUB_API).read()
    release = json.loads(data)

    tag = release["tag_name"]
    assets = release["assets"]

    print(f"Latest Slang version: {tag}")

    asset = choose_asset(assets)

    print(f"Selected asset: {asset['name']}")
    url = asset["browser_download_url"]

    filename = asset["name"]
    download(url, filename)
    extract(filename)

    print("\nDone!")
    print("Slang binaries located in ./slang")


if __name__ == "__main__":
    main()
