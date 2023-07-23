from controller import Controller
import ctypes
import os
import psutil
import sys
from time import sleep

controller = Controller()
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
            for event in processes:
                controller.kill_process(event["SourcePID"])
                controller.kill_process(event["TargetPID"])
        sleep(1)
if __name__ == "__main__":
    main()