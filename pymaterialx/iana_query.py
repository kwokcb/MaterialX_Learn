import requests

def fetch_iana_uri_schemes():
    # URL of the IANA URI schemes registry
    url = "https://www.iana.org/assignments/uri-schemes/uri-schemes-1.csv"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the CSV content
        lines = response.text.splitlines()
        # Skip the header and extract the scheme names
        schemes = [line.split(",")[0].strip('"') for line in lines[1:]]
        return schemes
    else:
        raise Exception("Failed to fetch URI schemes from IANA")

# Example usage
try:
    uri_schemes = fetch_iana_uri_schemes()
    print("Fetched URI schemes:", uri_schemes)
except Exception as e:
    print(e)