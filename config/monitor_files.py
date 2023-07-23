import psutil
import subprocess
import concurrent.futures

class MonitorFiles:
    def __init__(self) -> None:
        self.files_by_process = {}

    # Function to get open files for a process
    def __get_open_files(self,pid):
        try:
            cmd = f"config\\Handle64.exe -accepteula -p {pid}"
            output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
            files = [line.strip().split(':', 1)[1].strip().split(" ")[-1].split("\\")[-1] for line in output.splitlines() if ':' in line]
            return pid, files
        except Exception as e:
            return None,None

    def __set_files_by_process(self,pid,files):
        if pid in self.files_by_process:
            self.files_by_process[pid].extend(files)
            self.files_by_process[pid] = list(set(self.files_by_process[pid]))
        else:
            self.files_by_process[pid] = files

    def get_opened_files(self,pid):
        return self.files_by_process[pid]
    
    def get_all_opened_files(self):
        self.__scan_processes_handles()
        return self.files_by_process
    
    def __scan_processes_handles(self):
        # Get the list of all running processes
        processes = psutil.process_iter()

        # Execute get_open_files function in parallel using threads
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.__get_open_files, process.pid) for process in processes]

            # Process the results as they become available
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result and result[0]!=None:
                    pid, files = result
                    self.__set_files_by_process(pid,files)


