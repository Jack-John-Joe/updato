# Define a log file path
$Logfile = "C:\PS\Logs\python_install.log"

# Define a function to write to the log file with timestamp
function WriteLog {
    Param ([string]$LogString)
    $Stamp = (Get-Date).toString("yyyy/MM/dd HH:mm:ss")
    $LogMessage = "$Stamp $LogString"
    Add-content $LogFile -value $LogMessage
}

# Write a message to the log file indicating the start of the script
WriteLog "The script is started"

# Check if python is in the system PATH
if ($env:Path -like '*python*') {
    # Write a message to the log file indicating that python is already installed
    WriteLog "Python is already installed"
} else {
    # Write a message to the log file indicating that python is not installed
    WriteLog "Python is not installed"

    # Download python installer from the official website
    $url = "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe"
    $filename = "python-installer.exe"
    Invoke-WebRequest -Uri $url -OutFile $filename

    # Write a message to the log file indicating that the python installer is downloaded
    WriteLog "The python installer is downloaded"

    # Install python silently with default options
    Start-Process -FilePath $filename -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Write a message to the log file indicating that the python installation is completed
    WriteLog "The python installation is completed"
}

# Run real.py using python
python real.py

# Write a message to the log file indicating that the script is finished
WriteLog "The script is finished"
