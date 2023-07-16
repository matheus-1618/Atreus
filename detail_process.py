import os
import psutil
import urllib.request
import zipfile
import subprocess
import concurrent.futures

# Get the list of all process IDs
processes = psutil.process_iter()
pids = [process.pid for process in processes]

# Function to execute pslist and capture the output
def execute_pslist(pid):
    try:
        cmd = f"PSTools\\pslist.exe -accepteula {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        keys,values = output.split("\n")[7:][0].split(),output.split("\n")[7:][1].split()
        result_dict = {key: value for key, value in zip(keys, values)}
        return result_dict
    except Exception as e:
        return f"Error executing pslist for PID {pid}: {e}"

# Execute pslist in parallel using threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the tasks
    futures = [executor.submit(execute_pslist, pid) for pid in pids]

    # Process the results as they become available
    for future in concurrent.futures.as_completed(futures):
        output = future.result()
        print(output)
