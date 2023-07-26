import winreg
from config.monitor_registry import check_registry
import tkinter as tk
import tkinter.messagebox as tkmb
import ctypes
import psutil
import os
import time
import sys
from utils import is_admin, hide_console_window, high_privileges

def show_popup_message():
    icon_path = os.path.abspath("assets\\atreus.ico")
    window = tk.Tk()
    # change title bar icon
    window.iconbitmap(icon_path)
    window.withdraw()
    # same icon is also set for the message box
    tkmb.showinfo(title='Atreus',
                      message="Ryuk registry of persistence removed")


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
        
