from controller import Controller
import ctypes
import os
import sys
from time import sleep
import concurrent.futures
from prettytable import PrettyTable
import tkinter as tk
import tkinter.messagebox as tkmb
from utils import is_admin, hide_console_window, high_privileges, list_to_string_with_newlines, write_to_file, are_lists_equal

controller = Controller()
if not os.path.exists('logs'):
    os.mkdir('logs')
    
def show_popup_message():
    icon_path = os.path.abspath("assets\\atreus.ico")
    window = tk.Tk()
    # change title bar icon
    window.iconbitmap(icon_path)
    window.withdraw()
    # same icon is also set for the message box
    tkmb.showwarning(title='Atreus',
                      message="Ryuk threat hunted, logs and dumps available in Atreus root folder")

def terminate_suspect_process(pid):
    try:
        #Suspend process
        controller.suspend_process(pid)
        #Write details in log file
        processes = controller.detail_process(pid)
        tab = PrettyTable(list(processes.keys()))
        tab.add_row(list(processes.values()))
        write_to_file(f"logs\\process_details_{pid}.txt", "FILE DETAILS:\n"+tab.get_string())
        #Write dlls imported in log file
        dlls = controller.dlls_from_process(pid)
        write_to_file(f"logs\\process_details_{pid}.txt", "\n\nDLLS IMPORTED:\n\n"+list_to_string_with_newlines(dlls))
        #Write files opened by process
        files = controller.files_opened_from_process(pid)
        write_to_file(f"logs\\process_details_{pid}.txt", "\n\nFILES OPENED BY PROCESS:\n\n"+list_to_string_with_newlines(files))
        #Dump process
        controller.dump_process(pid)
        #Kill process
        controller.kill_process(pid)
        return True
    except Exception as e:
        print(f"Error for PID {pid}: {e}")
        return False

def main():
    processes_handled = []
    if not is_admin():
        print("This script requires administrator privileges to run.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    hide_console_window()
    high_privileges()
    while True:
        suspect_processes = []
        processes = controller.trace_create_remote_thread_call()
        if not are_lists_equal(processes, processes_handled):
            suspect_processes = [process for process in processes if process not in processes_handled]
            processes_handled = processes.copy()
        else:
            suspect_processes = []
        if len(suspect_processes) > 0:
            terminate_suspect_process(suspect_processes[0]["SourcePID"])
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(terminate_suspect_process, event["TargetPID"]) for event in suspect_processes]
                concurrent.futures.wait(futures)
            # Show the popup message after the finish of files
            show_popup_message()
        sleep(.1)
if __name__ == "__main__":
    main()