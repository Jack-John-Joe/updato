# Import the requests, subprocess, sys and configparser modules
import requests
import subprocess
import sys
import configparser

# Define the URLs of the update scripts
latest_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/latest.py"
windows11_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/11.py"
custom_url = "https://raw.githubusercontent.com/Jack-John-Joe/updato/main/updates/custom.py"

# Create a ConfigParser object and read the config.ini file if it exists
config = configparser.ConfigParser()
config.read("config.ini")

# Get the section name and option name for the user's choice
section = "Preferences"
option = "Update"

# Ask the user to choose between the latest update, windows 11, custom update, or last used option
choice = input("Do you want to download the latest update, windows 11, custom update, or last used option? (L/W/C/U) ")

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
elif choice.upper() == "U":
    # Check if the config.ini file has the user's preference
    if config.has_option(section, option):
        # Get the user's preference from the config.ini file
        preference = config.get(section, option)
        # Download and run the corresponding script based on the user's preference
        if preference.upper() == "L":
            # Download the latest update script as a binary file
            response = requests.get(latest_url)
            filename = "latest.py"
            with open(filename, "wb") as file:
                file.write(response.content)
            # Run the latest update script using subprocess
            subprocess.run([sys.executable, filename])
        elif preference.upper() == "W":
            # Download the windows 11 script as a binary file
            response = requests.get(windows11_url)
            filename = "11.py"
            with open(filename, "wb") as file:
                file.write(response.content)
            # Run the windows 11 script using subprocess
            subprocess.run([sys.executable, filename])
        elif preference.upper() == "C":
            # Download the custom update script as a binary file
            response = requests.get(custom_url)
            filename = "custom.py"
            with open(filename, "wb") as file:
                file.write(response.content)
            # Run the custom update script using subprocess
            subprocess.run([sys.executable, filename])
        else:
            # Print an error message if the user's preference is invalid
            print("Invalid preference. Please enter L, W, or C.")
    else:
        # Print an error message if the config.ini file does not have the user's preference
        print("No preference found. Please enter L, W, or C.")
else:
    # Print an error message if the user's choice is invalid
    print("Invalid choice. Please enter L, W, C, or U.")

# Set the option value to the user's choice in the ConfigParser object
config.set(section, option, choice)

# Write the ConfigParser object to the config.ini file
with open("config.ini", "w") as file:
    config.write(file)
