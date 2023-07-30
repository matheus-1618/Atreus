#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <fstream>
#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <Windows.h>

int64_t SetLastError = 0x7ffe5bfe5cb0;

int64_t OpenProcess = 0x7ffe5bfeade0;

int64_t GetModuleHandleA = 0x7ffe5bfef0b0;

struct s0 {
    int8_t[60] pad60;
    int32_t f60;
};

int64_t VirtualAllocEx = 0x7ffe5c00ba50;

int64_t WriteProcessMemory = 0x7ffe5c00bcb0;

int64_t CreateRemoteThread = 0x7ffe5c009b50;

int64_t GetLastError = 0x7ffe5bfe5bf0;

int64_t CloseHandle = 0x7ffe5bff48e0;

int64_t VirtualFreeEx = 0x7ffe5c00ba70;

void fun_14000a9cc(int64_t rcx, void* rdx, int64_t r8, int64_t r9);

void fun_140007410();

void fun_140002590(int32_t ecx) {
    int64_t rax2;
    struct s0* rax3;
    int64_t rax4;
    int32_t ebx5;
    int64_t r8_6;
    int64_t rbp7;
    int64_t rax8;
    int32_t eax9;
    int64_t rax10;
    int32_t eax11;
    int64_t rcx12;
    int64_t r8_13;
    void* rdx14;

    SetLastError();
    //Open Process
    rax2 = (int64_t)OpenProcess(0x1fffff);
    if (rax2) {
        rax3 = (struct s0*)GetModuleHandleA();
        if (rax3) {
            rax4 = rax3->f60;
            ebx5 = *reinterpret_cast<int32_t*>(rax4 + (int64_t)rax3 + 80);
            SetLastError();
            *(int32_t*)&r8_6 = ebx5;
            *(int32_t*)((int64_t)&r8_6 + 4) = 0;
            *(int32_t*)&rbp7 = ebx5;
            *(int32_t*)((int64_t)&rbp7 + 4) = 0;
            //Allocate memory in the target process
            rax8 = (int64_t)VirtualAllocEx(rax2, rax3, r8_6, 0x3000);
            if (rax8) {
                //Write in the portion reserved of memory the code to inject
                eax9 = (int32_t)WriteProcessMemory(rax2, rax8, rax3, rbp7);
                if (eax9) {
                    //Execute remotely the code injected in a new thread
                    rax10 = (int64_t)CreateRemoteThread(rax2);
                    if (!rax10) {
                        GetLastError(rax2);
                        CloseHandle(rax2);
                        VirtualFreeEx(rax2, rax3);
                    }
                } else {
                    CloseHandle(rax2, rax8, rax3, rbp7);
                    VirtualFreeEx(rax2, rax3);
                }
            } else {
                eax11 = (int32_t)GetLastError(rax2, rax3, r8_6, 0x3000);
                *(int32_t*)&rcx12 = eax11;
                *(int32_t*)((int64_t)&rcx12 + 4) = 0;
                *(int32_t*)&r8_13 = static_cast<int32_t>(rax8 + 10);
                *(int32_t*)((int64_t)&r8_13 + 4) = 0;
                rdx14 = (void*)((int64_t)__zero_stack_offset() - 8 - 96 - 8 + 8 - 8 + 8 - 8 + 8 - 8 + 8 - 8 + 8 - 8 + 8 + 72);
                fun_14000a9cc(rcx12, rdx14, r8_13, 0x3000);
                CloseHandle(rax2, rdx14, r8_13, 0x3000);
            }
        }
    }
    fun_140007410();
    return;
}
