#include <windows.h>
#include <wincrypt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char BYTE;

BYTE *getContentAfterPattern(const char *file_name, const BYTE *pattern, size_t pattern_length) {
    FILE *file = fopen(file_name, "rb");
    if (file == NULL) {
        printf("The file '%s' was not found.\n", file_name);
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    BYTE *content = (BYTE *)malloc(file_size);
    if (content == NULL) {
        fclose(file);
        printf("Memory allocation failed.\n");
        return NULL;
    }

    size_t read_bytes = fread(content, 1, file_size, file);
    fclose(file);

    if (read_bytes != (size_t)file_size) {
        free(content);
        printf("Error reading file.\n");
        return NULL;
    }

    BYTE *found = NULL;
    for (size_t i = 0; i < file_size - pattern_length; i++) {
        if (memcmp(content + i, pattern, pattern_length) == 0) {
            found = content + i;
            break;
        }
    }

    if (found == NULL) {
        printf("Pattern not found in the file.\n");
        free(content);
        return NULL;
    }

    size_t content_length = file_size - (found - content) - pattern_length;
    BYTE *output = (BYTE *)malloc(content_length);
    if (output == NULL) {
        printf("Memory allocation failed.\n");
        free(content);
        return NULL;
    }

    memcpy(output, found + pattern_length, content_length);

    free(content);
    return output;
}

HCRYPTKEY ImportAesKeyUsingRsa(HCRYPTKEY hRsaPublicKey, BYTE *aesKeyData, DWORD aesKeySize, HCRYPTPROV hCryptProv) {
    HCRYPTKEY hAesKey = 0;
    DWORD aesKeySize1 = 0;
    
        if (CryptImportKey(hCryptProv, aesKeyData, aesKeySize, hRsaPublicKey, 0, &hAesKey)) {
            printf("AES key import successful!\n");
        } else {
            printf("AES key import failed. Error: %d\n", GetLastError());
        }
        CryptReleaseContext(hCryptProv, 0);
 
    return hAesKey;
}

unsigned char *readFile(const char *file_name, size_t *out_size) {
    FILE *file = fopen(file_name, "rb");
    if (file == NULL) {
        printf("The file '%s' was not found.\n", file_name);
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    size_t file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    unsigned char *content = (unsigned char *)malloc(file_size);
    if (content == NULL) {
        fclose(file);
        printf("Memory allocation failed.\n");
        return NULL;
    }

    size_t read_bytes = fread(content, 1, file_size, file);
    fclose(file);

    if (read_bytes != file_size) {
        free(content);
        printf("Error reading file.\n");
        return NULL;
    }

    *out_size = file_size;
    return content;
}

unsigned char *findBytesAfterPattern(const unsigned char *bytes, size_t size, size_t *out_size) {
    unsigned char pattern[] = { 0x48, 0x45, 0x52, 0x4D, 0x45, 0x53 };
    size_t pattern_size = sizeof(pattern);

    for (size_t i = 0; i <= size - pattern_size; i++) {
        int match = 1;
        for (size_t j = 0; j < pattern_size; j++) {
            if (bytes[i + j] != pattern[j]) {
                match = 0;
                break;
            }
        }
        if (match) {
            *out_size = size - (i + pattern_size);
            return (unsigned char *)(bytes + i + pattern_size);
        }
    }

    *out_size = 0;
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <file_path>\n", argv[0]);
        return 1;
    }
    //DWORD dwProvType = PROV_RSA_AES;
    //DWORD dwFlags = CRYPT_VERIFYCONTEXT;
    //LPCTSTR pszProvider = MS_ENH_RSA_AES_PROV;
    //LPCTSTR pszContainer = NULL;//TEXT("AES_unique_");
    HCRYPTPROV hProv;

    DWORD dwProvType = PROV_RSA_AES;
DWORD dwFlags = CRYPT_NEWKEYSET | CRYPT_MACHINE_KEYSET;
LPCTSTR pszProvider = TEXT("Microsoft Enhanced RSA and AES Cryptographic Provider");
LPCTSTR pszContainer = TEXT("AES_unique_");
//HCRYPTPROV hProv;

    HCRYPTKEY hKey = 0;
    //RSA1 key obtained in the ryuk_data folder

    // BYTE rsaKey[] = {
    // 0x06, 0x02, 0x00, 0x00, 0x00, 0xA4, 0x00, 0x00, 0x52, 0x53, 0x41, 0x31, 0x00, 0x08, 0x00, 0x00,
    // 0x01, 0x00, 0x01, 0x00, 0x9D, 0x6B, 0xF2, 0xC1, 0x56, 0xC1, 0xBF, 0x3E, 0x00, 0x60, 0x37, 0xDA,
    // 0x02, 0x8B, 0xB3, 0xA6, 0xA9, 0x51, 0xAF, 0xD6, 0x8E, 0x6F, 0xEC, 0x02, 0x97, 0x93, 0x18, 0x24,
    // 0xF4, 0x33, 0x30, 0x63, 0x61, 0x00, 0x4F, 0x82, 0x0D, 0xF0, 0xE6, 0xE0, 0x33, 0xC8, 0x52, 0x9D,
    // 0x14, 0x77, 0xC9, 0xBF, 0xC6, 0xDC, 0xB9, 0x77, 0xB3, 0x76, 0x8E, 0x2A, 0x89, 0x6C, 0x50, 0xB4,
    // 0xE2, 0x36, 0x5F, 0xD0, 0xA6, 0xAD, 0xDC, 0x06, 0x89, 0x5E, 0x73, 0x1E, 0x65, 0xF5, 0xCF, 0x01,
    // 0x0C, 0xC9, 0x29, 0x7B, 0x4C, 0x41, 0xF9, 0xCB, 0x2F, 0x9F, 0xD9, 0x40, 0xE5, 0xF8, 0x29, 0xE0,
    // 0xC5, 0x27};
BYTE rsaKey[] = {
    0x06, 0x02, 0x00, 0x00, 0x00, 0xA4, 0x00, 0x00, 0x52, 0x53, 0x41, 0x31, 0x00, 0x08, 0x00, 0x00,
    0x01, 0x00, 0x01, 0x00, 0x9D, 0x6B, 0xF2, 0xC1, 0x56, 0xC1, 0xBF, 0x3E, 0x00, 0x60, 0x37, 0xDA,
    0x02, 0x8B, 0xB3, 0xA6, 0xA9, 0x51, 0xAF, 0xD6, 0x8E, 0x6F, 0xEC, 0x02, 0x97, 0x93, 0x18, 0x24,
    0xF4, 0x33, 0x30, 0x63, 0x61, 0x00, 0x4F, 0x82, 0x0D, 0xF0, 0xE6, 0xE0, 0x33, 0xC8, 0x52, 0x9D,
    0x14, 0x77, 0xC9, 0xBF, 0xC6, 0xDC, 0xB9, 0x77, 0xB3, 0x76, 0x8E, 0x2A, 0x89, 0x6C, 0x50, 0xB4,
    0xE2, 0x36, 0x5F, 0xD0, 0xA6, 0xAD, 0xDC, 0x06, 0x89, 0x5E, 0x73, 0x1E, 0x65, 0xF5, 0xCF, 0x01,
    0x0C, 0xC9, 0x29, 0x7B, 0x4C, 0x41, 0xF9, 0xCB, 0x2F, 0x9F, 0xD9, 0x40, 0xE5, 0xF8, 0x29, 0xE0,
    0xC5, 0x27, 0xEC, 0xDF, 0x9D, 0xF9, 0x43, 0x11, 0xC2, 0x98, 0xB9, 0x00, 0x11, 0x5F, 0x13, 0x1B,
    0x25, 0x55, 0x81, 0x5E, 0xEE, 0xEF, 0x6A, 0x04, 0x5D, 0xFB, 0xC4, 0xC1, 0x26, 0x3F, 0xFA, 0x2F,
    0x91, 0x6C, 0x15, 0x6C, 0x00, 0xF4, 0xA4, 0x6B, 0xE5, 0xB9, 0x4B, 0x92, 0x04, 0x47, 0x75, 0xFA,
    0xA4, 0x2E, 0x11, 0x9A, 0x58, 0xEA, 0x93, 0x49, 0x41, 0x7D, 0x6E, 0xD7, 0x16, 0x77, 0x23, 0xA0,
    0xD9, 0x67, 0xB9, 0x83, 0x90, 0x72, 0xA3, 0x13, 0xCA, 0xB6, 0x8A, 0x8E, 0xF4, 0xD8, 0xCE, 0x6F,
    0xFC, 0x22, 0xB6, 0x78, 0xFE, 0x4E, 0x91, 0x87, 0x79, 0xA8, 0x73, 0xC2, 0x91, 0xF3, 0xC4, 0x0B,
    0x0E, 0x12, 0x2B, 0x16, 0x62, 0x77, 0x91, 0xDD, 0x19, 0x21, 0x4A, 0xF3, 0x61, 0xFD, 0x0B, 0x3C,
    0x3A, 0x25, 0x70, 0x88, 0x71, 0x45, 0x78, 0x17, 0x51, 0x25, 0x19, 0x04, 0x0B, 0xA5, 0x2D, 0x95,
    0x38, 0xFB, 0xA1, 0xB2, 0xE2, 0xE7, 0x96, 0x3B, 0x9B, 0x3B, 0x49, 0xC0, 0xC2, 0x38, 0x4D, 0xB7,
    0x67, 0x31, 0x17, 0x86, 0x88, 0xC4, 0x65, 0x18, 0x7B, 0x87, 0x37, 0xD6, 0x8A, 0x2A, 0x14, 0x2C,
    0xB0, 0xC1, 0x4A, 0xA4
};

    if(!CryptAcquireContext(&hProv, pszContainer, pszProvider, dwProvType, dwFlags)){
    //if (!CryptAcquireContext(&hProv, NULL, NULL, PROV_RSA_AES, CRYPT_VERIFYCONTEXT)) {
        printf("Error acquiring cryptographic context\n");
        return 1;
    }

    if (!CryptImportKey(hProv, rsaKey, sizeof(rsaKey), 0, CRYPT_EXPORTABLE, &hKey)) {
        printf("CryptImportKey failed with error %d\n", GetLastError());
        CryptReleaseContext(hProv, 0);
        return 1;
    }

    printf("RSA key imported successfully\n");

    BYTE pattern[] = { 0x48, 0x45, 0x52, 0x4D, 0x45, 0x53 }; // "HERMES" in bytes
    BYTE *selected_bytes = getContentAfterPattern(argv[1], pattern, sizeof(pattern));

    size_t file_size;
    unsigned char *content = readFile(argv[1], &file_size);
    

    if (content != NULL) {
        size_t content_size;
        unsigned char *content_after_pattern = findBytesAfterPattern(content, file_size, &content_size);
        printf("Size of %d",content_size);
        if (content_after_pattern != NULL) {
            for (size_t i = 0; i < content_size; i++) {
                printf("%02X ", content_after_pattern[i]);
            }
        } else {
            printf("Pattern not found in the content.\n");
        }

        DWORD aesKeySize = sizeof(content_after_pattern);

        HCRYPTKEY hAesKey = ImportAesKeyUsingRsa(hKey, content_after_pattern, aesKeySize,hProv);
        if (hAesKey) {
                CryptDestroyKey(hAesKey);
            }

        free(selected_bytes);
    }
    
    CryptDestroyKey(hKey);
    CryptReleaseContext(hProv, 0);
    return 0;
}
