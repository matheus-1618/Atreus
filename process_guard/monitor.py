import ctypes
from ctypes import wintypes

# Constants
TH32CS_SNAPPROCESS = 0x00000002
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize', wintypes.DWORD),
        ('cntUsage', wintypes.DWORD),
        ('th32ProcessID', wintypes.DWORD),
        ('th32DefaultHeapID', ctypes.POINTER(ctypes.c_uint)),
        ('th32ModuleID', wintypes.DWORD),
        ('cntThreads', wintypes.DWORD),
        ('th32ParentProcessID', wintypes.DWORD),
        ('pcPriClassBase', wintypes.LONG),
        ('dwFlags', wintypes.DWORD),
        ('szExeFile', ctypes.c_char * 260),
        ('szProcessPath', ctypes.c_char * 260),
        ('dwNumThreads', wintypes.DWORD),
        ('dwNumHandles', wintypes.DWORD)
    ]

def monitor_processes():
    # Get the process snapshot
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel32.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    kernel32.CreateToolhelp32Snapshot.argtypes = [wintypes.DWORD, wintypes.DWORD]
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)

    # Check for errors
    if snapshot == INVALID_HANDLE_VALUE:
        error_code = ctypes.get_last_error()
        raise ctypes.WinError(error_code)

    # Initialize PROCESSENTRY32 structure
    pe32 = PROCESSENTRY32()
    pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)

    # Get the first process entry
    success = kernel32.Process32First(snapshot, ctypes.byref(pe32))

    # Iterate over processes
    while success:
        process_name = pe32.szExeFile.decode()
        process_path = pe32.szProcessPath.decode()
        process_id = pe32.th32ProcessID
        parent_process_id = pe32.th32ParentProcessID
        num_threads = pe32.cntThreads
        num_handles = pe32.cntUsage

        print("Process Name:", process_name)
        print("Process ID:", process_id)
        print("Parent Process ID:", parent_process_id)
        print("Process Path:", process_path)
        print("Number of Threads:", num_threads)
        print("Number of Handles:", num_handles)
        print("-----------------------------")

        success = kernel32.Process32Next(snapshot, ctypes.byref(pe32))

    # Close the snapshot handle
    kernel32.CloseHandle(snapshot)

# Call the function to monitor processes
monitor_processes()
