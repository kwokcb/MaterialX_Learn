import os
import requests
import zipfile

GITHUB_TOKEN = None
REPO_OWNER = "AcademySoftwareFoundation" 
REPO_NAME = "MaterialX"
N = 15  # Number of latest releases to download
DOWNLOAD_DIR = "releases"  # Directory to save downloaded files
TARGET_FILE_NAMES = ["Windows"]
GET_FIRST = True
CHUNK_SIZE = (65536*65536*16) # 16 MB chunk size for downloading  

# GitHub API URL for releases
RELEASES_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases"

# Create download directory if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_file(url, dest_path, download_chunk_size=CHUNK_SIZE):
    """Download a file from a given URL to the specified destination."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    with open(dest_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=download_chunk_size):
            #print(f"...Downloading {len(chunk)} bytes")
            print('*', end='', flush=True)  # Print a dot for each chunk downloaded
            file.write(chunk)

def download_releases():
    """Download the assets of the latest N releases."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(RELEASES_API_URL, headers=headers)
    response.raise_for_status()

    releases = response.json()
    for release in releases[:N]:
        release_name = release["name"]
        asset_urls = []
        asset_names = []
        tag_names = []
        print(f"Checking assets for release: {release_name}. Tag: {release['tag_name']}")
        for asset in release["assets"]:
            asset_name = asset["name"]
            # Check if the asset name contains any of the target file names
            if any(target in asset_name for target in TARGET_FILE_NAMES):
                print("- Found asset:", asset_name)
                tag_names.append(release["tag_name"].replace(" ", "_").replace(".", "_"))
                #asset_names.append(asset_name)
                asset_url = asset["browser_download_url"]
                asset_urls.append(asset_url)

        # Sort asset_urls and tag_names by value of tag_names 
        asset_urls, tag_names = zip(*sorted(zip(asset_urls, tag_names), key=lambda x: x[1], reverse=True))
        #print(f"Sorted asset URLs and tag names: {asset_urls}\n, {tag_names}")
        for asset_url, tag_name in zip(asset_urls, tag_names):
            print(f"- Downloading {asset_name} from {asset_url}")
            dest_path = os.path.join(DOWNLOAD_DIR, tag_name + ".zip")
            download_file(asset_url, dest_path)
            print(f"Saved to {dest_path}")
            #if GET_FIRST:
            #    break
        print(f"Finished checking assets for release: {release_name}")

def download_libraries():
    """Download the 'Source code (zip)' for the latest N releases and 
    extract the standard 'libraries' folder
    """
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(RELEASES_API_URL, headers=headers)
    response.raise_for_status()

    releases = response.json()
    for release in releases[:N]:
        tag_name = release["tag_name"]
        release_name = release["name"]
        print(f"Downloading 'Source code (zip)' for release: {release_name} (tag: {tag_name})")

        source_zip_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/archive/refs/tags/{tag_name}.zip"
        dest_path = os.path.join(DOWNLOAD_DIR, f"{tag_name}.zip")
        download_file(source_zip_url, dest_path)
        print(f"Saved to {dest_path}")

        # Extract out the "libraries" folder from the zip file
        with zipfile.ZipFile(dest_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if "libraries" in file and "resources" not in file:
                    zip_ref.extract(file, os.path.join(DOWNLOAD_DIR, tag_name))
                    print(f"Extracted {file} to {os.path.join(DOWNLOAD_DIR, tag_name)}")
        # Optionally, remove the zip file after extraction
        os.remove(dest_path)
        print(f"Removed zip file: {dest_path}") 


def main():
    # TODO: Ad arguments...
    #download_releases()
    download_libraries()

if __name__ == "__main__":
    main()
