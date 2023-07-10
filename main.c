#include <stdio.h>
#include <windows.h>
#include <detours.h>

// Function pointer for the original CreateRemoteThreadEx function
typedef HANDLE(WINAPI* PCreateRemoteThreadEx)(HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD);

// Detoured function for CreateRemoteThreadEx
HANDLE WINAPI MyCreateRemoteThreadEx(HANDLE hProcess, LPSECURITY_ATTRIBUTES lpThreadAttributes,
                                    SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress,
                                    LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId)
{
    printf("CreateRemoteThreadEx called\n");

    // Call the original CreateRemoteThreadEx function
    PCreateRemoteThreadEx pOrigCreateRemoteThreadEx = (PCreateRemoteThreadEx)DetourFunction(
        DetourFindFunction("kernel32.dll", "CreateRemoteThreadEx"), MyCreateRemoteThreadEx);

    if (pOrigCreateRemoteThreadEx)
    {
        // Call the original function
        return pOrigCreateRemoteThreadEx(hProcess, lpThreadAttributes, dwStackSize,
                                         lpStartAddress, lpParameter, dwCreationFlags, lpThreadId);
    }

    return NULL;
}

// Entry point of the program
int main()
{
    // Initialize Detours
    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());
    DetourAttach(&(PVOID&)CreateRemoteThreadEx, MyCreateRemoteThreadEx);
    DetourTransactionCommit();

    // Perform some actions or wait for the hook to trigger

    // Remove the hook before exiting
    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());
    DetourDetach(&(PVOID&)CreateRemoteThreadEx, MyCreateRemoteThreadEx);
    DetourTransactionCommit();

    return 0;
}
