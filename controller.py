
from config.monitor_dlls import *
from config.monitor_files import *
from config.monitor_sysmon import *
from config.monitor_registry import check_registry
from config.exe_scanner import *
from config.dump_process import *
from config.detail_process import *
from config.process_manager import *
from psutil import Process

class Controller:
    def __init__(self) -> None:
        self.process_manager = ProcessManager()
        self.monitor_dlls = MonitorDlls()
        self.monitor_files = MonitorFiles()
        self.monitor_sysmon = MonitorSysmon()
        self.monitor_process = MonitorProcess()

    def dump_process(self,pid)->None:
        response = dump_process(pid)
        print(response)
    
    def detail_process(self,pid)->dict:
        if self.process_manager.is_process_running(pid):
            return self.monitor_process.get_details_from_process(pid)
        return None
    
    def detail_all_process(self)->dict:
        return self.monitor_process.get_all_process_details()
    
    def dlls_from_process(self,pid)->list:
        return self.monitor_dlls.get_dlls_from_process(pid)
    
    def dlls_from_all_processes(self)->dict:
        return self.monitor_dlls.get_all_process_dlls()
    
    def scan_registry(self)->bool:
        return check_registry()

    def scan_files(self)->None:
        directories =  ["C:\\Users\\Public",
                        os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop"),
                        os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")]
        result_dict = process_directory(directories)
        filtered_dict = filter_dict(result_dict)
        json_file_path = "suspected_files.json"
        with open(json_file_path, "w") as json_file:
            json.dump(filtered_dict, json_file)
    
    def monitor_files_created(self,count=100)->list:
        return self.monitor_sysmon.monitor_files_created(count)
    
    def trace_create_remote_thread_call(self)->list:
        return self.monitor_sysmon.monitor_create_remote_thread()
    
    def get_process(self,pid) -> Process:
        if self.process_manager.is_process_running(pid):
            return self.process_manager.get_process_by_pid(pid)
        return None
    
    def suspend_process(self,pid)->bool:
        if self.process_manager.is_process_running(pid):
            return self.process_manager.suspend_process(pid)
        
    def resume_process(self,pid)->bool:
        if self.process_manager.is_process_running(pid):
            return self.process_manager.resume_process(pid)
        
    def kill_process(self,pid)->bool:
        if self.process_manager.is_process_running(pid):
            return self.process_manager.kill_process(pid)
    
