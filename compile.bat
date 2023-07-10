cd "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\" 
vcvarsall.bat x86_amd64
cl /EHsc /I"C:\Users\Matheus\Downloads\Detours-4.0.1\src" main.c /link /LIBPATH:"C:\Users\Matheus\Downloads\Detours-4.0.1\lib.X64" detours.lib