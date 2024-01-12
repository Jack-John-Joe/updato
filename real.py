import time
import requests
import os

# Print "Updating.." for 10 seconds
print("Updating..", end="")
for i in range(10):
    time.sleep(1)
    print(".", end="")

# Download the latest update .py file from the given URL
url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/latest.py"
response = requests.get(url)
if response.status_code == 200:
    # Save the file to the current directory
    filename = "latest.py"
    with open(filename, "w") as f:
        f.write(response.text)
    # Run the file using os.system
    os.system(f"python {filename}")
else:
    # Handle the error
    print(f"\nError: Failed to download the file from {url}")
