# Description: A generic script to download a file in parts from a server with a speed limit.
# The script uses the requests library to download the file in parts and time.sleep() to limit the download speed. You can customize the base URL, file details, and speed limit as needed.
# The script will download the file parts sequentially and save them to the output file. The output file will be saved in the same directory as the script.
# You can run this script in your terminal by executing the command python GenericDL.py.

# Python version tested: Python 3.x

import requests # Import the requests library. If in doubt, run "pip install requests" in your terminal.
import time # Import the time library. It is used to limit the download speed.

# Define the base URL and file details
base_url = "[Domain of your site]" # Base URL of the file
file_id = "[file identifier goes here]"  # File identifier
total_parts = "[total number of parts]"   # Total number of parts of the file
output_file = "full_file_name.exts"  # Output file name

# Open the output file in binary write mode. You can optionally comment this line if you want to download the file at the full ISP speed.
def download_with_limit(url, chunk_size=1024, max_speed=4 * 1024 * 1024): # 4 MegaBytes per Second (4MB/s) speed limit. Customise as needed.
    response = requests.get(url, stream=True) # Get the response in stream mode
    response.raise_for_status() # Raise an exception if the response is not successful
    for chunk in response.iter_content(chunk_size=chunk_size): # Iterate over the response content
        yield chunk # Yield the chunk
        time.sleep(chunk_size / max_speed) # Sleep to limit the speed

with open(output_file, "wb") as f: # Open the output file in write binary mode
    for part in range(1, total_parts - 1): # Iterate over the parts of the file
        part_url = f"{base_url}{file_id}.part{part}" # Generate the URL of the part. Ideally, the URL should be in the format: https://example.com/file_id.part[integer]. Example: https://Noobgamer0111iscool.com/990989898089.part1 :)
        print(f"Downloading part {part} from {part_url}") # Print the part being downloaded
        
        # Download the part with speed limit
        for chunk in download_with_limit(part_url): # Iterate over the chunks of the part
            f.write(chunk) # Write the chunk to the output file

print(f"Download complete. File saved as {output_file}") # Print the completion message
# The output of your terminal should look like this: "Downloading part [some integer] from [URL of the part]" and eventually "Download complete. File saved as [output_file]"