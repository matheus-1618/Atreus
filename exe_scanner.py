import subprocess
import concurrent.futures

# Define the command to execute Sigcheck
command = ["Sigcheck\\sigcheck64.exe", "-v", "-accepteula","-s", "C:\\Users\\Public"]

try:
    # Execute the command and capture the output
    output = subprocess.check_output(command, input="y", stderr=subprocess.STDOUT, universal_newlines=True)
    #print(f"Sigcheck output:\n{output}")
    print(output.split("\n"))
except subprocess.CalledProcessError as e:
    #print(f"Error executing Sigcheck (Exit code {e.returncode}):")
    #print(e.output)
    lines = e.output.strip().split('\n')

    file_dict = {}

    file_info = {}
    file_path = ""

    for line in lines:
        if line.startswith('c:'):
            if file_info:
                file_dict[file_path] = file_info
            file_info = {}
            file_path = line.rstrip(':')
        else:
            key_value = line.split(':', 1)
            if len(key_value) == 2:
                key, value = key_value
                file_info[key.strip()] = value.strip()

    # Add the last file info
    if file_info:
        file_dict[file_path] = file_info

    print(file_dict)

# Function to execute Sigcheck and capture the output
def execute_sigcheck(command):
    try:
        output = subprocess.check_output(command, input="y", stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

# Execute Sigcheck in parallel using threads
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the tasks
    futures = [executor.submit(execute_sigcheck, command) for _ in range(5)]  # Submit 5 tasks as an example

   
