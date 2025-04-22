# Cryptographic Attacks - Cracking Weak Password Hashes & Exploiting Poor Authentication in Databases


---

## Objectives

1. Identify and exploit cryptographic weaknesses in database authentication.
2. Perform offline hash cracking on discovered password hashes.
3. Investigate real-world cryptographic failures.
4. Propose secure cryptographic solutions.

---

## Tools Used

| Tool       | Use                          |
|------------|-------------------------------|
| `nmap`     | Port scanning & service detection |
| `nc`       | Quick port scan                |
| `mysql`    | Access and enumeration         |
| `hashid`   | Identify hash types            |
| `john`     | Cracking password hashes       |
| `hashcat`  | GPU-based hash cracking        |
| `Wireshark`| Network traffic analysis       |

---
## Lab Setup

- **Attacker Machine**: Kali Linux
- **Target**: Vulnerable machine running an exposed database service
- **Tools Used**: `nmap`, `nc`, `mysql`, `hashid`, `john`, `hashcat`, `Wireshark`

---

## Task 1: Service Enumeration and Initial Access

### Step-by-Step

```bash
nmap -sS -sV -p- 192.168.1.100
```
- `-sS`: SYN scan (stealthy)
- `-sV`: Service version detection
- `-p-`: Scan all 65535 TCP ports

Discovered port **3306** open → MySQL service detected.

### Alternative
```bash
nc -zv 192.168.1.100 1-1000
```
- `-z`: Scan without sending data
- `-v`: Verbose output

Not stealthy (full TCP handshake), better for basic connectivity check.

### Connection Attempt
```bash
mysql -h 192.168.1.100 -u root
```
- No password prompt = potential misconfiguration.

### Problem Encountered
- Could not connect initially: `Host is not allowed to connect`
- Resolved by modifying `/etc/mysql/my.cnf` on target to allow external IPs.

---

## Task 2: Enumeration of Users and Authentication Weakness

### Enumeration
```sql
SELECT user, host, authentication_string FROM mysql.user;
```

### Findings
- User `admin` had **empty password**.
- User `test` had a weak hash in `authentication_string`.

### Access Attempt
```bash
mysql -h 192.168.1.100 -u admin
```
- Gained access without password.

### Question: Is no password a cryptographic failure?
**Yes.** It completely bypasses cryptographic authentication. A secure system must require password hashing + proper access control.

---

## Task 3: Password Hash Discovery and Hash Identification

### Locate Hash Table
```sql
USE users_db;
SELECT * FROM credentials;
```

Extracted hashes:
```text
$1$eGczHgEg$3gqZB9kPEyoq5QNEa74mv/
```

### Identify Hash
```bash
hashid '$1$eGczHgEg$3gqZB9kPEyoq5QNEa74mv/'
```
- Result: **MD5 Crypt**
- Weak due to collision resistance and speed (fast to brute-force)

---

## Task 4: Offline Hash Cracking

### Using John the Ripper
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```
- Cracked password: `admin123`

### Using Hashcat (alternative)
```bash
hashcat -m 500 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```
- `-m 500`: MD5 Crypt
- `-a 0`: Dictionary attack

### Password Strength
- Low entropy, common word found in `rockyou.txt` = insecure.

---

## Task 5: Cryptographic Analysis and Mitigation

### Issues Found
- No password on some accounts
- Weak password hashes (MD5 Crypt)
- Potential plaintext transmission

### Solutions
- Enforce strong password policy
- Use secure hash functions (e.g., bcrypt, Argon2)
- Enable SSL/TLS for database communication

### Optional Wireshark Analysis
Captured MySQL login traffic → No SSL → Username and hashed password transmitted in plaintext.

---



---

## Conclusion
This lab showed how poor cryptographic practices (empty passwords, weak hashes, no SSL) can easily be exploited. Stronger authentication, hashing, and encrypted communication are essential to secure systems.

---



---



