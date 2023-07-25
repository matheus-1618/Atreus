import winreg
from config.monitor_registry import check_registry
import tkinter as tk
import tkinter.messagebox as tkmb
import ctypes
import psutil
import os
import time
import sys

def show_popup_message():
    icon_path = os.path.abspath("assets\\atreus.ico")
    window = tk.Tk()
    # change title bar icon
    window.iconbitmap(icon_path)
    window.withdraw()
    # same icon is also set for the message box
    tkmb.showinfo(title='Atreus',
                      message="Ryuk registry of persistence removed")
    
def hide_console_window():
    console_window = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(console_window, 0)

def high_privileges():
    process = psutil.Process(os.getpid())
    process.nice(psutil.HIGH_PRIORITY_CLASS)

def delete_registry_value():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    value_name = "svchos"
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(registry_key, value_name)
        print(f"The value '{value_name}' has been deleted from the registry key '{key_path}'.")
        show_popup_message()
    except FileNotFoundError:
        print(f"The registry key '{key_path}' does not exist.")
    except PermissionError:
        print(f"Access denied. You may need administrator privileges to delete the registry value.")
    except Exception as e:
        print(f"An error occurred while deleting the registry value: {e}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False
    
if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges to run.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    hide_console_window()
    high_privileges()
    while True:
        if check_registry():
            delete_registry_value()
        time.sleep(5)
        
