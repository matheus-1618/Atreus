import os
import psutil
import urllib.request
import zipfile
import subprocess

# Download and extract PSTools utility
url = 'https://download.sysinternals.com/files/PSTools.zip'
file_name = 'PSTools.zip'
extract_folder = 'PSTools'

try:
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    os.remove(file_name)
except Exception as e:
    print(f"Error downloading and extracting PSTools utility: {e}")
    exit()

# Get the list of all process IDs
processes = psutil.process_iter()
pids = [process.pid for process in processes]

# Execute pslist -x pid for each process using subprocess
for pid in pids:
    try:
        cmd = f"PSTools\pslist.exe -accepteula {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(f"Output for PID {pid}:\n{output}")        
    except Exception as e:
        print(f"Error executing pslist for PID {pid}: {e}")
