import urllib.request
import zipfile
import os
import subprocess

# Download and extract Sigcheck utility
url = 'https://download.sysinternals.com/files/Sigcheck.zip'
file_name = 'Sigcheck.zip'
extract_folder = 'Sigcheck'

try:
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    os.remove(file_name)
except Exception as e:
    print(f"Error downloading and extracting Sigcheck utility: {e}")
    exit()

# Define the command to execute Sigcheck
command = ["Sigcheck\\sigcheck64.exe", "-v", "-accepteula", "C:\\Users\\Public"]

try:
    # Execute the command and capture the output
    output = subprocess.check_output(command,input="y", stderr=subprocess.STDOUT, universal_newlines=True)
    #print(f"Sigcheck output:\n{output}")
    print(output.split("\n"))
except subprocess.CalledProcessError as e:
    print(f"Error executing Sigcheck (Exit code {e.returncode}):")
    for i in e.output.split(r"c:\users\public"):
        for m in i.split("\n"):
            if "detection" in m or ".exe" in m:
                print(m)
        #print(i)
