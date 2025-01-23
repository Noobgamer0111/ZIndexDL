import requests
import time

# Define the base URL and file details
base_url = "https://cdn-161.storage.zindex.eu.org/"
file_id = "2dc1703f0440d7270de275823b8b4a11b0fa30028a50239ebee88eabc1bcba93"
total_parts = 269
output_file = "output.mkv"

# Open the output file in binary write mode
def download_with_limit(url, chunk_size=1024, max_speed=4 * 1024 * 1024):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for chunk in response.iter_content(chunk_size=chunk_size):
        yield chunk
        time.sleep(chunk_size / max_speed)

with open(output_file, "wb") as f:
    for part in range(1, total_parts - 1):
        part_url = f"{base_url}{file_id}.part{part}"
        print(f"Downloading part {part} from {part_url}")
        
        # Download the part with speed limit
        for chunk in download_with_limit(part_url):
            f.write(chunk)

print(f"Download complete. File saved as {output_file}")
