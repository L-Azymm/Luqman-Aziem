- [1. Test Esok @ 10, datang kul 9](#1-test-esok--10-datang-kul-9)
- [2. Steps](#2-steps)
  - [2.1. Identify the binary](#21-identify-the-binary)
    - [2.1.1. DIE](#211-die)
  - [2.2. Find pyinstaller Decompiler](#22-find-pyinstaller-decompiler)
  - [2.3. Install pyinstxtractor-ng](#23-install-pyinstxtractor-ng)
  - [2.4. Decompile](#24-decompile)
    - [2.4.1. Convert .exe to .pyc](#241-convert-exe-to-pyc)
    - [2.4.2. Find .pyc decompiler](#242-find-pyc-decompiler)
    - [2.4.3. uncompyle6](#243-uncompyle6)
    - [2.4.4. Convert .pyc to .py](#244-convert-pyc-to-py)
- [3. Tools](#3-tools)
  - [3.1. Good to have](#31-good-to-have)

Simulated Ransomware
Decrypt the ransomware to get the actual file

# 1. Test Esok @ 10, datang kul 9

single binary file **gmi.exe** âœ…

# 2. Steps

## 2.1. Identify the binary

- hash âœ…
- Identify the programming language; die âœ…

### 2.1.1. DIE

https://github.com/horsicq/DIE-engine/releases

- Python, pyinstaller

## 2.2. Find pyinstaller Decompiler

https://www.google.com/search?q=pyinstaller+Decompiler

## 2.3. Install pyinstxtractor-ng

https://github.com/pyinstxtractor/pyinstxtractor-ng
https://github.com/pyinstxtractor/pyinstxtractor-ng/releases/download/2025.01.05/pyinstxtractor-ng.exe

## 2.4. Decompile

### 2.4.1. Convert .exe to .pyc 

```powershell
.\pyinstxtractor-ng.exe <filename>
.\pyinstxtractor-ng.exe gmi.exe
```

```python
PS C:\Tools\DECOMPILE_ME> pyinstxtractor-ng.exe .\gmi2025.exe
[+] Processing .\gmi2025.exe
[+] Pyinstaller version: 2.1+
[+] Python version: 3.8
[+] Length of package: 4644943 bytes
[+] Found 19 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: gmi2025.pyc
[+] Found 74 files in PYZ archive
[+] Successfully extracted pyinstaller archive: .\gmi2025.exe

You can now use a python decompiler on the pyc files within the extracted directory
PS C:\Tools\DECOMPILE_ME>

PS C:\Tools\DECOMPILE_ME> cd .\gmi2025.exe_extracted\
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted> ls gmi*


    Directory: C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         23/5/2025   6:30 AM            668 gmi2025.pyc

PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted>
```

- .pyc non readable

```powershell
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted> Get-Content gmi2025.pyc
U

Ã£â˜»@s"ddâ˜ºlZdâ˜»dâ™¥â€žZâ˜ºeâ˜»dâ™¦kâ˜»râ–²eâ˜ºÆ’â˜ºdâ˜ºS)â™£Ã©Ncâ™ 
Cspdâ˜º}tjâ˜º|dâ˜»dâ™¥Ââ˜»â˜ºdâ™¦dâ™£dâ™ dÅ“â™¥}â˜º|â˜ºÂ â˜»Â¡D]6\â˜»}â˜»}â™¥tjâ™¥Â â™¦||â˜»Â¡â˜»}â™¦tâ™£|â™¦Æ’â˜»Ââ–º}â™£|â™£Â â™ |â™¥Â¡â˜ºâ˜ºW5QRXq&td      |â€ºÂâ˜»Æ’â˜ºâ˜ºdS)
NGMITest2T)â˜ºexist_okzâ–²This is the content of file 1.z$Another file with different content.zâ–²Final file written by the EXE.)â™¥z   file1.txtz     file2.txtz      file3.txtÃšâ˜ºwzâ—„Files written to Ãšâ˜»osmakedirsÃšâ™£itemsÃšâ™¦pathÃšâ™¦joinÃšâ™¦openÃšâ™£writeÃšâ™£print)â™ Ãš
target_dirÃšâ™£filesfilenameÃšcontentfilepathÃšâ˜ºfÂ©râ€¼Ãº
gmi2025.pyÃšâ™‚write_filesâ™¥sâ–¬â˜ºâ™¦â˜ºâ™«â™¥â˜»â˜ºâ˜»â˜ºâ˜»Ã½â™ â™ â–ºâ˜ºâ™«â˜ºâ™€â˜ºâ–¬â˜ºrÂ§__main__)â™¥râ™£rÂ§__name__râ€¼râ€¼râ€¼rÂ¶<module>â˜ºsâ˜º
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted>
```

### 2.4.2. Find .pyc decompiler

https://www.google.com/search?q=decompile+.pyc

https://stackoverflow.com/questions/5287253/is-it-possible-to-decompile-a-compiled-pyc-file-into-a-py-file

### 2.4.3. uncompyle6

```powershell
pip install uncompyle6
```

https://pypi.org/project/uncompyle6/

```ps
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted> C:\venv38\Scripts\uncompyle6.exe --help
Usage: uncompyle6 [OPTIONS] FILES...

  Cross Python bytecode decompiler for Python bytecode up to Python 3.8.

Options:
  -A, --asm++ / --no-asm++      show xdis assembler and tokenized assembler
  -a, --asm / --no-asm
  -g, --grammar / --no-grammar
  -t, --tree / --no-tree
  -T, --tree++ / --no-tree++    show parse tree and Abstract Syntax Tree
  --linemaps / --no-linemaps    show line number correspondencies between
                                byte-code and generated source output
  --verify [run|syntax]
  -r, --recurse / --no-recurse
  -o, --output PATH
  --version                     Show the version and exit.
  --start-offset INTEGER        start decomplation at offset; default is 0 or
                                the starting offset.
  --version                     Show the version and exit.
  --stop-offset INTEGER         stop decomplation when seeing an offset
                                greater or equal to this; default is -1 which
                                indicates no stopping point.
  --help                        Show this message and exit.
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted>
```

```powershell
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted> C:\venv38\Scripts\uncompyle6.exe -o . .\gmi2025.pyc
.\gmi2025.pyc --
# Successfully decompiled file
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted>
```

```powershell
PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted> ls gmi*


    Directory: C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         23/5/2025   6:36 AM            772 gmi2025.py
-a----         23/5/2025   6:30 AM            668 gmi2025.pyc


PS C:\Tools\DECOMPILE_ME\gmi2025.exe_extracted>
```

### 2.4.4. Convert .pyc to .py

```powershell
uncompyle6.exe -o C:\Tools\decompile .\gmi2025.pyc
```

# 3. Tools

1. Python 3.8

## 3.1. Good to have

Everything
7z
Git
https://www.zabkat.com/x2lite.htm