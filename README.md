# Python Projects

A collection of small security and utility tools written in Python. Built as part of learning Python for cybersecurity and penetration testing.

---

## Tools

### 🔍 PortScanner.py
TCP port scanner with threading, service detection, and open/closed/filtered state detection.
```bash
python PortScanner.py <host> [ports]
python PortScanner.py 192.168.1.1 22,80,443
python PortScanner.py 192.168.1.1 1-1024
```

### 📂 DirEnum.py
Directory enumerator that checks for existing, forbidden, and failed paths on a web target.
```bash
python DirEnum.py <url> <wordlist>
python DirEnum.py http://example.com wordlist.txt
```

### #️⃣ HashCalculator.py
Computes hashes for any input string using common algorithms.
```
Supported: md5, sha1, sha256, sha512, sha3_256
```
```bash
python HashCalculator.py
```

### 🔑 PassGenerator.py
Cryptographically secure password generator with strength rating.
```bash
python PassGenerator.py
```

### 🌐 IpValidator.py
Validates an IPv4 address and shows its type (private, public, loopback, multicast).
```bash
python IpValidator.py
```

### 🖧 SubnetCalculator.py
Calculates network address, broadcast, subnet mask, first/last host, and total usable hosts.
```bash
python SubnetCalculator.py
```

### 📁 ExtentionScanner.py
Scans a directory and counts files by extension, sorted by frequency with percentages.
```bash
python ExtentionScanner.py
```

### 🌍 ApiClient.py
Simple REST API client that fetches and displays product data from a test API in a formatted table.
```bash
python ApiClient.py
```

---

## Requirements

Most tools use the Python standard library only. `DirEnum.py` and `ApiClient.py` require `requests`:

```bash
pip install requests
```

---

## Setup

```bash
git clone git@github.com:therezayekta/Python-Projects.git
cd Python-Projects
pip install requests
```

---

## Notes

- Only use `PortScanner.py` and `DirEnum.py` on systems you own or have explicit permission to test.
- Built and tested on Linux (Kali).

---

## Author

**therezayekta** — Computer Engineering student | Aspiring penetration tester
