import psutil
import subprocess
import concurrent.futures

# Get the list of all process IDs


class MonitorProcess:
    def __init__(self) -> None:
        self.process_details = {}

    # Function to execute pslist and capture the output
    def __execute_pslist(self,pid):
        try:
            cmd = f"PSTools\\pslist.exe -accepteula {pid}"
            output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
            keys,values = output.split("\n")[7:][0].split(),output.split("\n")[7:][1].split()
            details = {key: value for key, value in zip(keys, values)}
            self.process_details[pid] = details
        except Exception as e:
            return f"Error executing pslist for PID {pid}: {e}"

    def get_all_process_details(self):
        self.__get_details_from_all_processes()
        return self.process_details
    
    def get_details_from_process(self,pid):
        self.__execute_pslist(pid)
        return self.process_details[pid]
    
    def __get_details_from_all_processes(self):
        processes = psutil.process_iter()
        pids = [process.pid for process in processes]
        # Execute pslist in parallel using threads
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the tasks
            futures = [executor.submit(self.__execute_pslist, pid) for pid in pids]
            # Process the results as they become available
            for future in concurrent.futures.as_completed(futures):
                pass
