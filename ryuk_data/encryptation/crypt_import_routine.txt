00000001400028D0 | 48:83EC 38               | sub rsp,38                              |
00000001400028D4 | 833D 61A50200 01         | cmp dword ptr ds:[14002CE3C],1          |
00000001400028DB | 48:8D15 AE200200         | lea rdx,qword ptr ds:[140024990]        | 0000000140024990:L"AES_unique_"
00000001400028E2 | C74424 20 10000000       | mov dword ptr ss:[rsp+20],10            |
00000001400028EA | 48:8D0D 27A50200         | lea rcx,qword ptr ds:[14002CE18]        |
00000001400028F1 | 41:B9 18000000           | mov r9d,18                              |
00000001400028F7 | 0F85 87000000            | jne 140002984                           |
00000001400028FD | 4C:8D05 2C710200         | lea r8,qword ptr ds:[140029A30]         | 0000000140029A30:L"Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype)"
0000000140002904 | FF15 76940200            | call qword ptr ds:[<&CryptAcquireContex |
000000014000290A | 41:B9 18000000           | mov r9d,18                              | DWORD dwProvType = PROV_RSA_AES
0000000140002910 | C74424 20 20000000       | mov dword ptr ss:[rsp+20],20            | DWORD dwFlags = CRYPT_MACHINE_KEYSET
0000000140002918 | 4C:8D05 11710200         | lea r8,qword ptr ds:[140029A30]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype)"
000000014000291F | 48:8D15 6A200200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
0000000140002926 | 48:8D0D EBA40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
000000014000292D | FF15 4D940200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
0000000140002933 | 85C0                     | test eax,eax                            |
0000000140002935 | 0F85 E2000000            | jne 140002A1D                           |
000000014000293B | 44:8D48 18               | lea r9d,qword ptr ds:[rax+18]           | DWORD dwProvType
000000014000293F | C74424 20 28000000       | mov dword ptr ss:[rsp+20],28            | DWORD dwFlags = CRYPT_NEWKEYSET | CRYPT_MACHINE_KEYSET
0000000140002947 | 4C:8D05 E2700200         | lea r8,qword ptr ds:[140029A30]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype)"
000000014000294E | 48:8D15 3B200200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
0000000140002955 | 48:8D0D BCA40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
000000014000295C | FF15 1E940200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
0000000140002962 | 85C0                     | test eax,eax                            |
0000000140002964 | 0F85 B3000000            | jne 140002A1D                           |
000000014000296A | C74424 20 10000000       | mov dword ptr ss:[rsp+20],10            | DWORD dwFlags = CRYPT_DELETEKEYSET
0000000140002972 | 44:8D48 18               | lea r9d,qword ptr ds:[rax+18]           | DWORD dwProvType
0000000140002976 | 48:8D15 13200200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
000000014000297D | 48:8D0D 94A40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
0000000140002984 | 4C:8D05 85200200         | lea r8,qword ptr ds:[140024A10]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider"
000000014000298B | FF15 EF930200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
0000000140002991 | 41:B9 18000000           | mov r9d,18                              | DWORD dwProvType = PROV_RSA_AES
0000000140002997 | C74424 20 20000000       | mov dword ptr ss:[rsp+20],20            | DWORD dwFlags = CRYPT_MACHINE_KEYSET
000000014000299F | 4C:8D05 6A200200         | lea r8,qword ptr ds:[140024A10]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider"
00000001400029A6 | 48:8D15 E31F0200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
00000001400029AD | 48:8D0D 64A40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
00000001400029B4 | FF15 C6930200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
00000001400029BA | 85C0                     | test eax,eax                            |
00000001400029BC | 75 5F                    | jne 140002A1D                           |
00000001400029BE | 44:8D48 18               | lea r9d,qword ptr ds:[rax+18]           | DWORD dwProvType
00000001400029C2 | C74424 20 28000000       | mov dword ptr ss:[rsp+20],28            | DWORD dwFlags = CRYPT_NEWKEYSET | CRYPT_MACHINE_KEYSET
00000001400029CA | 4C:8D05 3F200200         | lea r8,qword ptr ds:[140024A10]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider"
00000001400029D1 | 48:8D15 B81F0200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
00000001400029D8 | 48:8D0D 39A40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
00000001400029DF | FF15 9B930200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
00000001400029E5 | 85C0                     | test eax,eax                            |
00000001400029E7 | 75 34                    | jne 140002A1D                           |
00000001400029E9 | 44:8D48 18               | lea r9d,qword ptr ds:[rax+18]           | DWORD dwProvType
00000001400029ED | C74424 20 08000000       | mov dword ptr ss:[rsp+20],8             | DWORD dwFlags = CRYPT_NEWKEYSET
00000001400029F5 | 4C:8D05 14200200         | lea r8,qword ptr ds:[140024A10]         | LPCTSTR pszProvider = "Microsoft Enhanced RSA and AES Cryptographic Provider"
00000001400029FC | 48:8D15 8D1F0200         | lea rdx,qword ptr ds:[140024990]        | LPCTSTR pszContainer = "C:\\Windows", 0000000140024990:L"AES_unique_"
0000000140002A03 | 48:8D0D 0EA40200         | lea rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV* phProv = "C:\\Windows"
0000000140002A0A | FF15 70930200            | call qword ptr ds:[<&CryptAcquireContex | CryptAcquireContextW
0000000140002A10 | 85C0                     | test eax,eax                            |
0000000140002A12 | 75 09                    | jne 140002A1D                           |
0000000140002A14 | 8D48 01                  | lea ecx,qword ptr ds:[rax+1]            | int ExitCode
0000000140002A17 | FF15 032E3800            | call qword ptr ds:[<&FatalExit>]        | FatalExit
0000000140002A1D | 48:8B0D F4A30200         | mov rcx,qword ptr ds:[14002CE18]        | HCRYPTPROV hProv = "C:\\Windows"
0000000140002A24 | 48:8D05 3D553800         | lea rax,qword ptr ds:[140387F68]        |
0000000140002A2B | 48:894424 28             | mov qword ptr ss:[rsp+28],rax           | HCRYPTKEY* phKey
0000000140002A30 | 48:8D15 99690200         | lea rdx,qword ptr ds:[1400293D0]        | BYTE* pbData = "C:\\Windows"
0000000140002A37 | 45:33C9                  | xor r9d,r9d                             | HCRYPTKEY hPubKey
0000000140002A3A | C74424 20 01000000       | mov dword ptr ss:[rsp+20],1             | DWORD dwFlags = CRYPT_EXPORTABLE
0000000140002A42 | 41:B8 14010000           | mov r8d,114                             | DWORD dwDataLen = 114
0000000140002A48 | FF15 92A60200            | call qword ptr ds:[<&CryptImportKey>]   | CryptImportKey
0000000140002A4E | 85C0                     | test eax,eax                            |
0000000140002A50 | 75 0E                    | jne 140002A60                           |
0000000140002A52 | 8D48 01                  | lea ecx,qword ptr ds:[rax+1]            |
0000000140002A55 | 48:83C4 38               | add rsp,38                              |
0000000140002A59 | 48:FF25 C02D3800         | jmp qword ptr ds:[<&FatalExit>]         |
0000000140002A60 | 48:83C4 38               | add rsp,38                              |
0000000140002A64 | C3                       | ret                                     |