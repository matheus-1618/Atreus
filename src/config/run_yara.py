import yara
import os

def scan_exe_yara(directories):
    files = {}
    rules = yara.compile(r"config\rule.yar")
    for target_directory in directories:
        for file_name in os.listdir(target_directory):
            file_path = os.path.join(target_directory, file_name)
            if os.path.isfile(file_path):
                matches = rules.match(file_path)
                if matches:
                    files[os.path.join(target_directory, file_name)] = str(matches[0])
    return files