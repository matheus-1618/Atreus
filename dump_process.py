import subprocess
import psutil
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
