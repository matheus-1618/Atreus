from controller import Controller
import ctypes
import os
import psutil
import sys
from time import sleep
import concurrent.futures
from prettytable import PrettyTable
import tkinter as tk
import tkinter.messagebox as tkmb

controller = Controller()
if not os.path.exists('logs'):
    os.mkdir('logs')

def write_to_file(filename, content):
    try:
        # Open the file in append mode
        with open(filename, "a") as file:
            file.write(content)
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the content
        with open(filename, "w") as file:
            file.write(content)
            
def list_to_string_with_newlines(input_list):
    return '\n'.join(str(item) for item in input_list)

def hide_console_window():
    console_window = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(console_window, 0)

def high_privileges():
    process = psutil.Process(os.getpid())
    process.nice(psutil.HIGH_PRIORITY_CLASS)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False
    
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
    if not is_admin():
        print("This script requires administrator privileges to run.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    hide_console_window()
    high_privileges()
    while True:
        processes = controller.trace_create_remote_thread_call()
        if len(processes) > 0:
            terminate_suspect_process(processes[0]["SourcePID"])
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(terminate_suspect_process, event["TargetPID"]) for event in processes]
                concurrent.futures.wait(futures)
            # Show the popup message after the finish of files
            sleep(15)
            show_popup_message()
        sleep(1)
if __name__ == "__main__":
    main()