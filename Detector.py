#!/usr/bin/env python3
# GitLab CVE-2026-110264 - Defensive Version Checker
# Author: Fari
# Only checks version, does NOT exploit

import requests
import sys

VULNERABLE_VERSIONS = ["16.0", "16.1", "16.2", "16.3", "16.4", "17.0", "18.x"]

def check_gitlab_version(target_url):
    try:
        print(f"[+] Checking {target_url}")
        # GitLab exposes version via /api/v4/version (if public)
        # Or via meta tags - we use safe method
        r = requests.get(f"{target_url}/api/v4/version", timeout=5, verify=False)
        if r.status_code == 200:
            data = r.json()
            version = data.get('version', 'unknown')
            print(f"[*] Detected GitLab version: {version}")
            
            # Simple check logic
            if version.startswith("16.") or version.startswith("17.") or "18.0" in version:
                print(f"[!] POTENTIALLY VULNERABLE to CVE-2026-110264 - Please patch immediately!")
                print(f"[*] Fix: Upgrade to latest patched version per GitLab advisory.")
            else:
                print(f"[+] Appears patched or not in affected range.")
        else:
            print(f"[-] Could not get version info (Status: {r.status_code}). Manual check needed.")
            
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 detector.py https://gitlab.example.com")
        sys.exit(1)
    check_gitlab_version(sys.argv[1])
