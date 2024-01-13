# Import the requests and subprocess modules
import requests
import subprocess

# Define the URL of the Windows 11 Media Creation Tool
url = "https://www.microsoft.com/en-us/software-download/windows11/"

# Download the tool as a binary file
response = requests.get(url)
filename = "MediaCreationTool.exe"
with open(filename, "wb") as file:
    file.write(response.content)

# Run the tool using subprocess with the /auto upgrade argument
subprocess.run([filename, "/auto", "upgrade"])

