
# GitLab2Safe-Defensive-Checker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CVE](https://img.shields.io/badge/CVE-CVE--2026--110264-red)
![Type](https://img.shields.io/badge/Type-Defensive%20Only-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

A defensive security scanner for **CVE-2026-110264** - GitLab CE/EE Arbitrary File Write (PHP2Shell).

This tool does **NOT** contain any exploit code. It is 100% safe and educational.

### What is CVE-2026-110264?
GitLab CE/EE < 18.3.5 is vulnerable to a file-write vulnerability in the OAuth redirect handling (GLSA-2026-01). Attackers can abuse it to write PHP files and get shell access (PHP2Shell). This is being used as the case study for PHP2Shell research.

### Who uses this?
- Security Teams to check if their GitLab is patched
- Bug Bounty Hunters for initial verification
- Students for defensive security learning

### Features
- Version detection via GitLab API
- Patch status check (Safe / Vulnerable)
- No exploit, no payload, 100% defensive
- Fast scan with Python requests

### Installation
```bash
git clone https://github.com/YOUR-USERNAME/GitLab2Safe-Defensive-Checker
cd GitLab2Safe-Defensive-Checker
pip install requests
### Usage
python3 checker.py --url https://gitlab.example.com
Output:
[+] Target: https://gitlab.example.com
[+] Version Found: 18.3.2
[!] VULNERABLE - Please upgrade to 18.3.5 or later
### Disclaimer
This tool is for *educational and defensive purposes only*. No exploit code included. Use only on systems you own.

### Author
Made by Fari - Learning Defensive Security

### References
- GitLab Security Release: 18.3.5
- GLSA-2026-01

