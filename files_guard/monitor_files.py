import psutil
import urllib.request
import zipfile
import os
import subprocess

# Download and extract Handle utility
url = 'https://download.sysinternals.com/files/Handle.zip'
file_name = 'Handle.zip'

try:
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(file_name)
except Exception as e:
    print(f"Error downloading and extracting Handle utility: {e}")
    exit()

# Get the list of all running processes
processes = psutil.process_iter()

# Iterate over processes and list open files using Handle
for process in processes:
    try:
        pid = process.pid
        cmd = f"Handle.exe -accepteula -p {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(f"Files open by PID {pid}:\n{output}")
    except Exception as e:
        pass
        #print(f"Error listing open files for PID {pid}: {e}")
