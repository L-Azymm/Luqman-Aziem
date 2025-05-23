# 🔐 Cryptography - Malware Analysis

Hello and Assalamualaikum!

👾*Zymm*👾 is Back,

And for this new project:

The goal was to reverse a binary file (simulated ransomware) to recover its encrypted contents using decompilation and analysis techniques.

Imma provide ya fellas with the things you need and steps by steps for easir walkthrough but, before that, we need to do some prequisite

Well we need to be ready to create a masterpiece, am i right?

⚠️ WARNING ⚠️

PLEASE REMEMBER AND TAKE NOTE THAT THIS PROJECT WAS RUN AND DID INSIDE A SAFE SPACE OF VIRTUAL MACHINE

DO NOT ATTEMPT ON YOUR HOST DEVICE WHEN HADNDLING MALICIOUS FILES AND MALWARES

---

## 🧪 Objective

Ok so the main target for us is to decrypt the file of the malware and retrieve the original file contents, this gonna involve some analysis and understanding its behavior, sounds hard? dont worry, it is 🤣

---

## 🧰 Pre requisite / Tools Used

Here are some of the utensils that we gonna use to eat this malware up

- [DIE (Detect It Easy)](https://github.com/horsicq/DIE-engine/releases) – we gonna use this to analyze the file
  
- [pyinstxtractor-ng](https://github.com/pyinstxtractor/pyinstxtractor-ng) – we gonna reverse it from executable(`.exe`) to .pyc etc.

- [uncompyle6](https://pypi.org/project/uncompyle6/) – to decompile `.pyc` to `.py` This is where the fun starts, or hell some might say 😈

Wanna install? Use this:

```powershell
pip install uncompyle6
```

- `Python 3.8` - Why py 3.8? yeah because higher than this wont support the `uncompyle6` the we're gonna use
  
- PowerShell / Terminal
  
- (Optional) 7-Zip, Git, file explorer tools - Why optional? well its up to you if you wanna use this, but its gonna be **A LOT** and i mean **A WHOLE LOT** easier having this with ya

## Additional Steps For Setting Up Your Tools

This is an optional step that you can chosse either you want to do it or not, but i insist doing this because it will make your usage of the tool easier, so whats the harm i doing so right? C'mon lets do it

Ok so first off this is only for the `umcompyle6` and `PyInstxtractor-ng` (i hate this name, its hard to remember and say🤣)

after installing both of em using this command

```powershell
pip install uncompyle6

pip install pyinstxtractor-ng
```

Use this command to see where was it installed files is, this will *Show You The Way*, exacly, the path

```powershell
pip show uncompyle6

pip show pyinstxtractor-ng
```

And you will see an output like this or maybe close to this, this is mine, so dont worry if its slightly different

- `uncompyle6`

```powershell
PS C:\Users\zymm> pip show uncompyle6
Name: uncompyle6
Version: 3.9.2
Summary: Python cross-version byte-code library and disassembler
Home-page: None
Author: None
Author-email: Rocky Bernstein <rb@dustyfeet.com>
License: GPL
Location: c:\users\zymm\appdata\local\programs\python\python38\lib\site-packages
Requires: spark-parser, click, xdis
Required-by:
PS C:\Users\zymm>
```

And this

- `pyinstxtractor-ng`

```powershell
PS C:\Users\zymm> pip show pyinstxtractor-ng
Name: pyinstxtractor-ng
Version: 2025.1.6
Summary: PyInstaller Extractor Next Generation
Home-page: None
Author: extremecoders-re
Author-email: None
License: GPL-3.0-only
Location: c:\users\zymm\appdata\local\programs\python\python38\lib\site-packages
Requires: xdis, pycryptodome
Required-by:
PS C:\Users\zymm>
```

You can see **A WHOLE LOT** of information about the tools, this will come in handy for other purposes

---

Next open up you search bar, and search `Environment Variables` and open it

After that, try finding `User Variable` find `Path` and click Edit, click new to add a new path, and paste the path for the `uncompyle6` and `PyInstxtractor-ng`, and finally click `OK` to save,

This will allow you to run both of em from anywhere premenatly, just be sure to get the path right, because we want *Jalan yang Lurus dan Benar* 🤣

So heres quick n' easy to follow (with some pic for easier navigation):

- Search Enviroment Variable

![path](Assets/path/enviro.png)

- Select Enviroment Variable

![path](Assets/path/enviro2.png)

- Select User Variable

![path](Assets/path/user_enviro.png)

- Paste path

![path](Assets/path/add_path.png)

- OK to save

So after you're done with the paths, you will be able to run the executeables (`.exe`) from anywhere in your terminal,

SEE! EASIER! no need for path, but im not saying paths is not important, well you do you

---

## 📁 Given File

This is the main star of our project, (Drum Rolls please)

The malicious file that we gonna be Reverse engineer of

- `example.exe` – suspected ransomware executable

⚠️ WARNING ⚠️

MAKE SURE TO CREATE A SNAPSHOT OF YOUR VIRTUAL MACHINE BEFOR RUNNING THE MALWARE, SO WE CAN REVERT AFTER BEING INFECTED

---

## 🧭 いくぞ Blasting Off With Step-by-Step

## 1. 🕵️ Identify the Binary

Ok so first off, we're gonna be using DIE, not death, `DIE (Detect It Easy)`, a bit exssive for a name eh? my thoughts too actually

This will show you a brief info on the files or malware that you will be investigating

- You can choose the file
- Drag n' Drop

![DIE]()

You gonna see things like what language it use, what was it packed with etc. for Example: `Python based` and `PyInstaller`

---

## 2. 📦 Extract Contents from EXE

### Run pyinstxtractor-ng

Ok now we gonna use `pyinstxtractor` to reverese it packaging.

Why? because after finding out the language it used, we're gonna need to find the pure coding file for reverse engineering

```powershell
pyinstxtractor-ng.exe <filename>
```

After running this command in your terminal, you can find that from the extension of `.exe.` you gonna find another with the extension of `.pyc`

or even  a new folder like example.exe_extracted/ with some .pyc files inside. Well anywhich ones works fine 😉

Now we're gonna focus on the `.pyc` file from now on

Let's view what you can see from the file first by using `Get-Content`

```powershell
Get-Content <filename>
```

![output]()

Here you gonna see an alien language or we say the binary data or a garbled text

Easy to say a non readable

---

### Time to play with `uncompyle6`

Here we are, one more step to get what we need, lets proceed to use `uncompyle6` to decomplile the previous `.pyc` file into a `.py` file

Here's the command we're gonna use

```powershell
uncompyle6.exe -o . .\gmi2025.pyc
```

But for more info on `uncompyle6` You can use help

```powershell
uncompyle6.exe --help
```

now lets see the files that has been decompiled with `ls`

![list]()

---

### FBI OPEN UP

Now that we're able to obtain the pure `.py` code, lets open it up

![py content]()

---

### NOW THE REAL GAME BEGINS

Now that we have the file and its content, lets see if we can find some info by analyzing the content,

Lets lookout for thing like

- Keys (Public,Private)
- The codes
- Links
- Files
- Names
- Hash / Encryption Format
- Functions

![Code]()

After gaining some info on our hands, its like obtaining the stones 🔴🔵🟢🟡🟣 for our [Infinity Gauntlet](https://en.wikipedia.org/wiki/The_Infinity_Gauntlet)

Thats how powerful information is,

*The Pen is mightier than The Sword* - Edward Bulwer-Lytton

But please dont bring a pen to a swordfight, theres a reason why is an `expression`

---

### Figuring Out the Key

Seems like the files is encrypted, so lets see if we can crack it and steal its pearl (plaintext)
