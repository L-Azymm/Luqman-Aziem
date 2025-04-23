# 🔍 Finding Info in Files

## 🛠 Using `grep` with Help Commands

- `-A<n>` → Show **n** lines **After** the matched **keyword**
- `-B<n>` → Show **n** lines **Before** the matched **keyword**
- `-C<n>` → Show **n** lines **Before and After** the matched **keyword***

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
