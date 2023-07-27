rule Ryuk_Dropper{
   meta:
      description = "Detects Ryuk dropper binary"
      author = "Colin Cowie"
   strings:
      $s1 = "\\users\\Public\\window.bat" ascii wide
      $s2 = "Main Invoked" ascii wide
      $s3 = "somedll.dll" ascii wide
      $s4 = "vssadmin resize shadowstorage" ascii wide
      $s5 = "InvokeMainViaCRT" ascii wide
   condition:
      3 of them
}

rule Ryuk_Payload{
   meta:
      description = "Detects Ryuk payload binary"
      author = "Colin Cowie"
   strings:
      $s1 = "UNIQUE_ID_DO_NOT_REMOVE" ascii wide
      $s2 = ".RYK" ascii wide
      $s3 = "RyukReadMe.txt" ascii wide
      $s4 = "fg4tgf4f3.dll" ascii wide
      $s5 = "2 files we unlock for free"
      $s6 = "Backups were either encrypted"
      $s7 = "HERMES"
      $s8 = "AhnLab"
   condition:
      4 of them
}