# Portfolio Project 2

## Overview
This portfolio project builds on the homelab from Project 1, shifting from manual defense and inspection to **offensive tooling written in Python**. The narrative arc is **build the tool → use the tool → understand the vulnerability**. Across four labs it moves from network reconnaissance to web application exploitation: labs 1 and 2 build Python recon tools (a threaded port scanner with banner grabbing, and an HTTP enumeration tool), lab 3 stands up a deliberately vulnerable web app and exploits the OWASP Top 10 by hand with Burp Suite, and lab 4 rebuilds one of those manual exploits as a Python script to prove end-to-end understanding of what the tooling does under the hood. Together they cover offensive fundamentals (recon, scanning, enumeration, web exploitation) and the Python needed to automate them.

## Software/Util/Tools used
**Attacker (Kali Linux — 192.168.1.16):**
- Python 3 — custom recon and exploitation scripts (`socket`, `requests`, `concurrent.futures`, `argparse`, `re`)
- Burp Suite — intercepting proxy for manual web exploitation
- nmap — baseline comparison for the custom port scanner
- web browser — manual exploitation and validation

**Target (Ubuntu Server — 192.168.1.17):**
- DVWA (Damn Vulnerable Web App) / OWASP Juice Shop — deliberately vulnerable web application
- Docker / Apache + MySQL / Node — hosting the vulnerable app
- vsftpd, SSH — additional services used as scan/enumeration targets

**Network:**
- Internal isolated network (`homelabnet`, 192.168.1.0/24) — vulnerable apps are never exposed to the home LAN or internet.

## Lab 1-4 summary in form of a table
| Lab | Title | Focus | Key Tools | Outcome |
|-----|-------|-------|-----------|---------|
| 1 | Python Port Scanner | Recon / Tooling | Python `socket`, `concurrent.futures`, `argparse`, nmap | Built a TCP connect scanner, added threading and service banner grabbing, and validated results against nmap. |
| 2 | HTTP Recon Tool | Enumeration / Tooling | Python `requests`, `argparse`, OOP | Built a script to fingerprint a web target — headers, server/tech detection, status codes, and common-path discovery (`/admin`, `/robots.txt`). |
| 3 | OWASP Web Exploitation | Web Attacks | DVWA / Juice Shop, Burp Suite, browser | Exploited 5+ OWASP Top 10 vulnerabilities by hand (SQLi, XSS, CSRF, IDOR, broken auth), documenting each with screenshots. |
| 4 | Automating an Exploit in Python | Automation | Python `requests`, `re`, `argparse` | Rebuilt a manual exploit (e.g. an SQL injection data dumper or login brute-forcer) as a Python script, demonstrating what Burp does under the hood. |

## Concepts learned
- **Python for security:** file I/O, the `requests` library, raw `socket` programming, `argparse` for CLIs, threading with `concurrent.futures`, and basic OOP for structuring tools.
- **Reconnaissance & scanning:** how a TCP connect scan works at the socket level, banner grabbing for service/version detection, and why results differ from nmap.
- **Web enumeration:** fingerprinting a target from HTTP headers and responses, and discovering hidden paths and misconfigurations.
- **OWASP Top 10:** hands-on exploitation of SQL injection, XSS, CSRF, IDOR, and broken authentication, plus reading HTTP requests/responses in depth with Burp Suite.
- **Manual → automated:** translating a point-and-click Burp exploit into a repeatable Python script, cementing understanding of the underlying vulnerability.
- **Safe lab practice:** running deliberately vulnerable applications only on an isolated internal network.

## Conclusion
This project moves from the blue-team focus of Project 1 into offensive security, using Python as the connective tissue. By building recon tools from scratch, exploiting real web vulnerabilities by hand, and then automating those exploits in code, it demonstrates not just how to use security tools but how they actually work. The recurring lesson is that understanding a vulnerability deeply enough to script an attack against it is what separates tool operation from genuine security skill.

## Next steps
Future work could extend this toward a full engagement workflow: chaining the recon tools into an automated enumeration pipeline, expanding coverage to more of the OWASP Top 10 (SSRF, insecure deserialization), and practicing against realistic targets on the TryHackMe "Jr Penetration Tester" path to reinforce the methodology end to end.
