import psutil
import subprocess
import concurrent.futures

# Function to get DLLs for a process
def get_dlls(pid):
    try:
        cmd = f"ListDlls.exe -accepteula {pid}"
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        dlls = [line.strip().split()[-1].split("\\")[-1] for line in output.splitlines() if line.startswith("0x")][1:]
        return pid, dlls
    except Exception as e:
        return None

# Get the list of all process IDs
processes = psutil.process_iter()
pids = [process.pid for process in processes]

# Dictionary to store DLLs for each process
dlls_by_process = {}

# Execute get_dlls function in parallel using threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_dlls, pid) for pid in pids]

    # Process the results as they become available
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            pid, dlls = result
            dlls_by_process[pid] = dlls

# Print the DLLs for each process
for pid, dlls in dlls_by_process.items():
    print(f"DLLs for PID {pid}:")
    print(dlls)
#    for dll in dlls:
#        print(dll.split("\\")[-1])
    print()
