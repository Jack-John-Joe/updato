import requests
import subprocess
import os

# Get the latest update from the Microsoft Update Catalog
url = "https://www.catalog.update.microsoft.com/Search.aspx?q=latest"
response = requests.get(url)
if response.status_code == 200:
    # Parse the response to find the download link and the filename
    # This is a simplified example, the actual parsing may be more complex
    download_link = response.text.split("downloadInformation")[1].split('"')[2]
    filename = download_link.split("/")[-1]
    # Download the update file to the current directory
    response = requests.get(download_link)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        # Install the update silently using subprocess
        subprocess.run([filename, "/quiet", "/norestart"], check=True)
        # Print the message
        print("Installed latest update.")
    else:
        # Handle the error
        print(f"Error: Failed to download the update from {download_link}")
else:
    # Handle the error
    print(f"Error: Failed to get the latest update from {url}")

# End the script without closing the window
os.system("pause")
