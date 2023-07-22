import psutil
import subprocess
import concurrent.futures
class MonitorDlls:
    def __init__(self) -> None:
        self.process_dlls = {}

    def __get_dlls(self,pid):
        try:
            cmd = f"bin\\ListDlls.exe -accepteula {pid}"
            output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
            dlls = [line.strip().split()[-1].split("\\")[-1] for line in output.splitlines() if line.startswith("0x")][1:]
            self.process_dlls[pid] = dlls
        except Exception as e:
            return f"Error executing ListDlls for PID {pid}: {e}"

    def get_all_process_dlls(self):
        return self.process_dlls
    
    def get_dlls_from_process(self,pid):
        self.__get_dlls(pid)
        return self.process_dlls[pid]
    
    def get_details_from_all_processes(self):
        processes = psutil.process_iter()
        pids = [process.pid for process in processes]
        # Execute pslist in parallel using threads
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit the tasks
            futures = [executor.submit(self.__get_dlls, pid) for pid in pids]
            # Process the results as they become available
            for future in concurrent.futures.as_completed(futures):
                pass

