import subprocess
import os

# Create memory dumps for the processes
def dump_process(pid)->str:
    if not os.path.exists('dump'):
        os.mkdir('dump')

    dump_file = f"dump\\Process_{pid}.dmp"
    command = f"config\\procdump -ma -accepteula {pid} {dump_file}"
    try:
        subprocess.run(command, shell=True, check=True)
        return f"Memory dump created for process with PID {pid}"
    except subprocess.CalledProcessError as e:
        return f"Error creating memory dump for process with PID {pid}: {e}"
