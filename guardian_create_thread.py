import ctypes
from ctypes import wintypes
import psutil
import time

# Constants
PROCESS_ALL_ACCESS = 0x1F0FFF

# Load kernel32.dll
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Load user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Function callback type for hook
HOOKPROC = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

# Define the LUID structure
class LUID(ctypes.Structure):
    _fields_ = [
        ("LowPart", ctypes.c_ulong),
        ("HighPart", ctypes.c_long),
    ]

# Define the LUID_AND_ATTRIBUTES structure
class LUID_AND_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("Luid", LUID),
        ("Attributes", wintypes.DWORD),
    ]

# Define the TOKEN_PRIVILEGES structure
class TOKEN_PRIVILEGES(ctypes.Structure):
    _fields_ = [
        ("PrivilegeCount", wintypes.DWORD),
        ("Privileges", LUID_AND_ATTRIBUTES * 1),
    ]

# Global variables
g_hHook = None

# Hook procedure callback
def HookProc(nCode, wParam, lParam):
    if nCode >= 0:
        # Check if CreateRemoteThread is called
        if wParam == 0x11F:  # WM_USER + 1
            process_id = ctypes.windll.kernel32.GetProcessId(ctypes.windll.kernel32.GetCurrentProcess())
            process = psutil.Process(process_id)
            process_name = process.name()
            print(f"CreateRemoteThread called in process: {process_name}")
    return user32.CallNextHookEx(g_hHook, nCode, wParam, lParam)

# Function to set the hook
def set_hook():
    global g_hHook
    g_hHook = user32.SetWindowsHookExA(3, HOOKPROC(HookProc), kernel32.GetModuleHandleA(None), 0)

# Function to remove the hook
def remove_hook():
    user32.UnhookWindowsHookEx(g_hHook)

# Get the list of running process IDs using psutil
process_ids = [proc.pid for proc in psutil.process_iter()]

for process_id in process_ids:
    # Open the process
    hProcess = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)
    if hProcess:
        # Set the hook
        print(f"Observing process {process_id}")
        set_hook()

        # Wait for the hook to trigger (e.g., wait for user input)
        #input("Press Enter to continue...")
        time.sleep(5)
        # Remove the hook
        remove_hook()

        # Close the process handle
        kernel32.CloseHandle(hProcess)
