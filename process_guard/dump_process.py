import urllib.request
import zipfile
import os
import subprocess
import psutil

# Download and extract Procdump
url = 'https://download.sysinternals.com/files/Procdump.zip'
file_name = 'Procdump.zip'

try:
    urllib.request.urlretrieve(url, file_name)
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(file_name)
except Exception as e:
    print(f"Error downloading and extracting Procdump: {e}")
    exit()

# Get the list of running processes
processes = list(psutil.process_iter())

# Create memory dumps for the processes
for process in processes:
    pid = process.pid
    dump_file = f"Process_{pid}.dmp"
    command = f"procdump -ma -accepteula {pid} {dump_file}"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Memory dump created for process with PID {pid}")
    except subprocess.CalledProcessError as e:
        pass
        #print(f"Error creating memory dump for process with PID {pid}: {e}")
