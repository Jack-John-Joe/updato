# Download python installer from the official website
$url = "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe"
$filename = "python-installer.exe"
Invoke-WebRequest -Uri $url -OutFile $filename

# Install python silently with default options
Start-Process -FilePath $filename -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Run real.py using python
python real.py
