import ctypes
from ctypes import wintypes
import psutil

# Load kernel32.dll
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Constants
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
PROCESS_CREATE_THREAD = 0x0002

# Define the CreateRemoteThread function signature
CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.restype = wintypes.HANDLE
CreateRemoteThread.argtypes = [
    wintypes.HANDLE,  # hProcess
    wintypes.LPVOID,  # lpThreadAttributes
    wintypes.SIZE,  # dwStackSize
    wintypes.LPVOID,  # lpStartAddress
    wintypes.LPVOID,  # lpParameter
    wintypes.DWORD,   # dwCreationFlags
    wintypes.LPDWORD  # lpThreadId
]

# Function to check if CreateRemoteThread is available in a process
def is_create_remote_thread_available(process_id):
    # Open the process with required access rights
    hProcess = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ | PROCESS_CREATE_THREAD, False, process_id)
    if not hProcess:
        return False

    # Check if CreateRemoteThread function is available
    create_remote_thread_address = kernel32.GetProcAddress(kernel32.GetModuleHandleA(b'kernel32'), b'CreateRemoteThread')
    is_available = create_remote_thread_address is not None

    # Close the process handle
    kernel32.CloseHandle(hProcess)

    return is_available

# Get the list of running process IDs using psutil
process_ids = [proc.pid for proc in psutil.process_iter()]

# Iterate over all running processes
for process_id in process_ids:
    if is_create_remote_thread_available(process_id):
        print(f"CreateRemoteThread is available in process with ID: {process_id}")
