# 🔐 Cryptography - Malware Analysis

Hello and Assalamualaikum!

The goal was to reverse a binary file (simulated ransomware) to recover its encrypted contents using decompilation and analysis techniques.

Imma provide ya fellas with the things you need and steps by steps for easir walkthrough but, before that, we need to do some prequisite

---

## 📁 Given File

This is the main star of our project, (Drum Rolls please)

The malicious file that we gonna be Reverse engineer of

- `gmi2025.exe` – suspected ransomware executable

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

---

## 🧭 Step-by-Step Walkthrough

## 1. 🕵️ Identify the Binary

Ok so first off, we're gonna be using DIE, not death, `DIE (Detect It Easy)`, a bit exssive for e name eh? my thoughts too actually

This will show you a brief info on the files or malware that you will be investigating

- You can choose the file
- Drag n' Drop

![DIE]()

You gonna see things like what language it use, what was it packed with etc. for Example: `Python based` and `PyInstaller`

## 2. 📦 Extract Contents from EXE

### Run pyinstxtractor-ng

Ok now we gonna use `pyinstxtractor` to reverese it packaging. 

Why? because after finding out the language it used, we're gonna need to find the pure coding file for reverse engineering

```powershell
pyinstxtractor-ng.exe <filename>
```

After running this command in your terminal, you can find that from the extension of `.exe.` you gonna find another with the extension of `.pyc`

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

![Code]()

After gaining some info on our hands, its like obtaining the stones 🔴🔵🟢🟡🟣 for our [Infinity Gauntlet](https://en.wikipedia.org/wiki/The_Infinity_Gauntlet)

Thats how powerful information is,

*The Pen is mightier than The Sword* - Edward Bulwer-Lytton

But please dont bring a pen to a swordfight, theres a reason why is an `expression`

---

### Figuring Out the Key

Seems like the files is encrypted, so lets see if we can crack it and steal its pearl (plaintext)
