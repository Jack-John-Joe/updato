import requests
import subprocess
import os

# Get the latest updates from the Microsoft Update Catalog
url = "https://www.catalog.update.microsoft.com/Search.aspx?q=latest"
response = requests.get(url)
if response.status_code == 200:
    # Parse the response to find the download links and the filenames
    # This is a simplified example, the actual parsing may be more complex
    download_links = response.text.split("downloadInformation")[1:6]
    for i in range(5):
        download_link = download_links[i].split('"')[2]
        filename = download_link.split("/")[-1]
        # Download the update file to the current directory
        response = requests.get(download_link)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            # Install the update silently using subprocess
            subprocess.run([filename, "/quiet", "/norestart"], check=True)
            # Print the message
            print(f"Installed update {i+1}.")
        else:
            # Handle the error
            print(f"Error: Failed to download update {i+1} from {download_link}")
else:
    # Handle the error
    print(f"Error: Failed to get the latest updates from {url}")

# End the script without closing the window
os.system("pause")
