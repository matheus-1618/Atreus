import psutil
import urllib.request
import zipfile
import os
import subprocess
import concurrent.futures

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

# Function to get open files for a process
def get_open_files(process):
    try:
        pid = process.pid
        name = process.name()
        cmd = f"Handle.exe -accepteula -p {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        files = [line.strip().split(':', 1)[1].strip().split(" ")[-1] for line in output.splitlines() if ':' in line]
        return name, files
    except Exception as e:
        return None

# Get the list of all running processes
processes = psutil.process_iter()

# Dictionary to store files open by each process
files_by_process = {}

# Execute get_open_files function in parallel using threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_open_files, process) for process in processes]

    # Process the results as they become available
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            name, files = result
            files_by_process[name] = files

# Print the files open by each process
for process, files in files_by_process.items():
    print(f"Files open by {process}:")
    print(files)
    # for file in files:
    #     print(file)
    print()
