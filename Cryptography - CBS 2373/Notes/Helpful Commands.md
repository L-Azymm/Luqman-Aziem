# 🔍 Finding Info in Files

## 🛠 Using `grep` with Help Commands

- `-A<n>` → Show **<n> lines After** the match <Keyword>
- `-B<n>` → Show **<n> lines Before** the match <Keyword>
- `-C<n>` → Show **<n> lines Before and After** the match <Keyword>

---

## 📌 Command Format

```sh
<tool> -h or --help | grep <keyword> -A<n>
```

## Example

- Nmap 

```sh
nmap -h | grep OUTPUT -A10
```

- MySQL

```sh
mysql --help | grep OUTPUT -A10
```
