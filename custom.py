# Import the requests, subprocess and sys modules
import requests
import subprocess
import sys

# Ask the user to enter the microsoft update catalog link
link = input("Please enter the microsoft update catalog link: ")

# Download the update file as a binary file
response = requests.get(link)
filename = link.split("/")[-1] # Extract the file name from the link
with open(filename, "wb") as file:
    file.write(response.content)

# Install the update silently using subprocess
subprocess.run([filename, "/quiet", "/norestart"])
