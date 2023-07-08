import psutil
import urllib.request
import zipfile
import os
import subprocess


# Download and extract ListDlls utility
url = 'https://download.sysinternals.com/files/ListDlls.zip'
file_name = 'ListDlls.zip'

try:
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(file_name)
except Exception as e:
    print(f"Error downloading and extracting ListDlls utility: {e}")
    exit()

# Get the list of all process IDs
processes = psutil.process_iter()
pids = [process.pid for process in processes]

# Execute ListDlls for each process and print DLLs
for pid in pids:
    try:
        cmd = f"ListDlls.exe -accepteula {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        print(f"DLLs for PID {pid}:\n{output}")
    except Exception as e:
        print(f"Error executing ListDlls for PID {pid}: {e}")
