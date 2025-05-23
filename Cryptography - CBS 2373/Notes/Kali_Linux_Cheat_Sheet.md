
# Kali Linux Cheat Sheet

## Basic Linux Commands
| Command         | Description                |
|----------------|----------------------------|
| `pwd`           | Show current directory     |
| `ls -la`        | List files with permissions|
| `cd [dir]`      | Change directory           |
| `cp source dest`| Copy file/directory        |
| `mv source dest`| Move/rename file           |
| `rm -rf [target]`| Delete recursively        |
| `ifconfig` / `ip a` | Show network interfaces |
| `ping [host]`   | Ping a host                |

---

## Networking Tools
| Tool                        | Usage                                 |
|-----------------------------|---------------------------------------|
| `nmap -sS -A [IP]`          | Scan ports & detect OS/services       |
| `netstat -tuln`             | Show listening ports                  |
| `tcpdump -i eth0`           | Capture packets on eth0              |
| `wireshark`                 | GUI packet analyzer                   |
| `curl http://example.com`   | Send HTTP request                     |
| `wget [url]`                | Download files                        |

---

## Password Cracking
| Tool                                         | Usage                                 |
|----------------------------------------------|---------------------------------------|
| `john [hashfile]`                            | Crack passwords using John            |
| `hashcat -m [mode] -a 0 hash.txt wordlist.txt` | Crack hashes with Hashcat            |
| `hydra -l user -P passlist.txt [ip] ssh`     | Brute-force login (e.g., SSH)         |

---

## Web Exploitation
| Tool                    | Usage                                     |
|-------------------------|-------------------------------------------|
| `sqlmap -u [url] --dbs` | SQL injection and dump databases          |
| `dirb [url]`            | Directory brute-force                     |
| `nikto -h [host]`       | Web server vulnerability scanner          |
| `burpsuite`             | Web proxy for interception & attack       |

---

## Wireless Attacks
| Tool                                     | Usage                                    |
|------------------------------------------|------------------------------------------|
| `airmon-ng start wlan0`                  | Enable monitor mode                      |
| `airodump-ng wlan0mon`                   | Scan wireless networks                   |
| `aireplay-ng -0 5 -a [BSSID] wlan0mon`   | Deauth attack                            |
| `aircrack-ng capture.cap -w wordlist.txt`| Crack WPA/WPA2 handshake                 |

---

## Privilege Escalation
| Command                      | Description                  |
|------------------------------|------------------------------|
| `sudo -l`                    | List allowed commands        |
| `find / -perm -4000 2>/dev/null` | Find SUID files         |
| `uname -a`                   | Show system info             |
| `cat /etc/passwd`           | Show user accounts           |

---

## Exploitation Frameworks
| Tool           | Usage                          |
|----------------|--------------------------------|
| `msfconsole`   | Start Metasploit Framework     |
| `search exploit` | Find available exploits      |
| `use [path]`   | Use specific exploit module    |
