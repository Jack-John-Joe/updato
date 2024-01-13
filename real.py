# Import the requests, subprocess and sys modules
import requests
import subprocess
import sys

# Define the URLs of the update scripts
latest_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/latest.py"
windows11_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/11.py"
custom_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/custom.py"

# Ask the user to choose between the latest update, windows 11, or custom update
choice = input("Do you want to download the latest update, windows 11, or custom update? (L/W/C) ")

# Download and run the corresponding script based on the user's choice
if choice.upper() == "L":
    # Download the latest update script as a binary file
    response = requests.get(latest_url)
    filename = "latest.py"
    with open(filename, "wb") as file:
        file.write(response.content)
    # Run the latest update script using subprocess
    subprocess.run([sys.executable, filename])
elif choice.upper() == "W":
    # Download the windows 11 script as a binary file
    response = requests.get(windows11_url)
    filename = "11.py"
    with open(filename, "wb") as file:
        file.write(response.content)
    # Run the windows 11 script using subprocess
    subprocess.run([sys.executable, filename])
elif choice.upper() == "C":
    # Download the custom update script as a binary file
    response = requests.get(custom_url)
    filename = "custom.py"
    with open(filename, "wb") as file:
        file.write(response.content)
    # Run the custom update script using subprocess
    subprocess.run([sys.executable, filename])
else:
    # Print an error message if the user's choice is invalid
    print("Invalid choice. Please enter L, W, or C.")
