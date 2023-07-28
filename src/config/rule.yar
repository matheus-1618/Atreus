import "pe"

rule ryuk_dropper{
   meta:
      description = "Aim to detect Ryuk dropper"
   strings:
      $s1 = "REG ADD" wide
      $s2 = "\"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\"" wide
      $s3 = "/v \"svchos\"" wide
      $s4 = "/t REG_SZ" wide
      $s5 = "/d \"" wide
      $s6 = "No system is safe" ascii wide
      $s7 = "vssadmin resize shadowstorage" ascii wide
      $s8 = "UNIQUE_ID_DO_NOT_REMOVE" ascii wide
   condition:
      pe.is_pe and
      all of them and
      pe.is_32bit() and
      pe.imports("Kernel32.dll", "IsDebuggerPresent") and
      pe.imports("Shell32.dll", "ShellExecuteW") 
}

rule ryuk_exe{
   meta:
      description = "Aim to detect Ryuk executable"
   strings:
      $s1 = "REG ADD" wide
      $s2 = "\"HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\"" wide
      $s3 = "/v \"svchos\"" wide
      $s4 = "/t REG_SZ" wide
      $s5 = "/d \"" wide
      $s6 = "RyukReadMe.txt" wide 
      $s7 = "SeDebugPrivilege" wide 
      $s8 = "stop Antivirus /y" wide ascii
      $s9 = "RSA1" wide ascii

   condition:
      pe.is_pe and
      all of them and
      pe.imports("Kernel32.dll", "CreateRemoteThread") and
      pe.imports("Kernel32.dll", "WriteProcessMemory") and
      pe.imports("Kernel32.dll", "GetProcAddress") and 
      pe.imports("Kernel32.dll", "LoadLibraryA")
}