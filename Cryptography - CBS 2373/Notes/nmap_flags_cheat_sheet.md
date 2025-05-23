
# Nmap Command Flags Cheat Sheet

## 1. Target Specification
| Flag | Description |
|------|-------------|
| `-iL <inputfile>` | Scan targets from a file |
| `-iR <num>` | Scan <num> random hosts |
| `--exclude <host1,host2>` | Exclude specific hosts |
| `--excludefile <file>` | Exclude targets from a file |

## 2. Scan Techniques
| Flag | Description |
|------|-------------|
| `-sS` | TCP SYN (stealth) scan |
| `-sT` | TCP connect scan |
| `-sU` | UDP scan |
| `-sA` | ACK scan |
| `-sN` | Null scan (no flags set) |
| `-sF` | FIN scan |
| `-sX` | Xmas scan (FIN, PSH, URG flags) |
| `-sW` | Window scan |
| `-sM` | Maimon scan |

## 3. Port Specification
| Flag | Description |
|------|-------------|
| `-p <ports>` | Specify ports to scan (e.g., `-p 22,80,443` or `-p 1-1000`) |
| `--top-ports <num>` | Scan most common <num> ports |
| `-F` | Fast scan (100 most common ports) |
| `--port-ratio <ratio>` | Scan ports with a ratio of popularity (0.0–1.0) |

## 4. Service and Version Detection
| Flag | Description |
|------|-------------|
| `-sV` | Detect service/version info |
| `--version-intensity <0-9>` | Level of version detection |
| `--version-light` | Light version detection |
| `--version-all` | Try every probe for version detection |

## 5. OS Detection
| Flag | Description |
|------|-------------|
| `-O` | Enable OS detection |
| `--osscan-guess` | Guess OS if not certain |
| `--osscan-limit` | Limit OS detection to promising targets |

## 6. Script Scanning
| Flag | Description |
|------|-------------|
| `-sC` | Run default scripts |
| `--script=<script>` | Run specific script(s) |
| `--script-args=<args>` | Provide arguments to scripts |
| `--script-help=<script>` | Show help for scripts |

## 7. Timing and Performance
| Flag | Description |
|------|-------------|
| `-T<0-5>` | Timing template (0 = paranoid, 5 = insane) |
| `--min-rate <number>` | Minimum number of packets/second |
| `--max-rate <number>` | Maximum packets/second |
| `--max-retries <num>` | Max probe retries |

## 8. Output Formats
| Flag | Description |
|------|-------------|
| `-oN <file>` | Normal output |
| `-oX <file>` | XML output |
| `-oG <file>` | Grepable output |
| `-oA <basename>` | Output in all formats (`.nmap`, `.xml`, `.gnmap`) |

## 9. Firewall Evasion and Spoofing
| Flag | Description |
|------|-------------|
| `-D <decoys>` | Use decoy addresses |
| `-S <IP>` | Spoof source IP |
| `-e <iface>` | Use specific network interface |
| `-g <port>` | Use specific source port |
| `--data-length <num>` | Append random data |
| `--spoof-mac <mac>` | Spoof MAC address |
| `--badsum` | Send packets with bad checksums |

## 10. Host Discovery
| Flag | Description |
|------|-------------|
| `-sn` | Ping scan only (host discovery) |
| `-Pn` | Skip host discovery (treat all as online) |
| `-PS <ports>` | TCP SYN ping on given ports |
| `-PA <ports>` | TCP ACK ping |
| `-PU <ports>` | UDP ping |
| `-PE` | ICMP Echo ping |
| `-PP` | ICMP Timestamp ping |
| `-PM` | ICMP Netmask ping |

## 11. Miscellaneous
| Flag | Description |
|------|-------------|
| `-v`, `-vv`, `-vvv` | Verbosity levels |
| `-d`, `-dd`, `-ddd` | Debugging levels |
| `--reason` | Show reason for host/port status |
| `--open` | Show only open ports |
| `--privileged` | Assume script is running with root privileges |
| `--unprivileged` | Assume non-root |
| `--resume <file>` | Resume scan from file |
