import urllib.request
import zipfile
import os
import subprocess
import concurrent.futures

def get_sigcheck():
    if not os.path.exists('Sigcheck'):
        # Download and extract Sigcheck utility
        url = 'https://download.sysinternals.com/files/Sigcheck.zip'
        file_name = 'Sigcheck.zip'
        extract_folder = 'Sigcheck'
        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            os.remove(file_name)
        except Exception as e:
            print(f"Error downloading and extracting Sigcheck utility: {e}")
            exit()
        finally:
            return True
    return False

# Check if Sigcheck utility is available or download it
if get_sigcheck():
    print("Sigcheck utility downloaded successfully.")
else:
    print("Sigcheck utility already exists.")

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

   
