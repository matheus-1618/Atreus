import os
import subprocess
import concurrent.futures
import json

# Define the command to execute Sigcheck
command = ["src\\config\\Sigcheck\\sigcheck64.exe", "-v", "-accepteula"]

def fill_dict(output, file_dict):
    lines = output.strip().split('\n')
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
    return file_dict

def filter_dict(mapping):
    filter_dict = {}
    for key in mapping:
        try:
            detected, total = mapping[key]["VT detection"].split("/")
            detected, total = int(detected), int(total)
            if detected / total > 0.3:
                filter_dict[key] = mapping[key]
        except:
            pass
    return filter_dict

def execute_sigcheck(file_path):
    try:
        output = subprocess.check_output(command + [file_path], input="y", stderr=subprocess.STDOUT, universal_newlines=True)
        return fill_dict(output, {})
    except subprocess.CalledProcessError as e:
        return fill_dict(e.output, {})

def process_directory(directories):
    file_dict = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for directory in directories:
            files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
            for file in files:
                file_path = os.path.join(directory, file)
                file_dict.update(executor.submit(execute_sigcheck, file_path).result())
    return file_dict

if __name__ == "__main__":

    # Specify the starting directory
    directories =  ["C:\\Users\\Public",os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop"),os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")]

    # Call the function to process the directory
    result_dict = process_directory(directories)

    # Filter the resulting dictionary
    filtered_dict = filter_dict(result_dict)
    json_file_path = "excluded_files.json"

    # Write the filtered_dict to the JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(filtered_dict, json_file)
