# Portfolio Project 1

## Overview
This portfolio project is a fundamental cybersecurity homelab built around a hardened Ubuntu Server VM and a Kali Linux attacker VM. Across four labs, it follows a single narrative arc: **prevention → detection → inspection**. Labs 1 and 2 lock the server down (SSH hardening and firewall-based attack surface reduction), lab 3 shifts from stopping attacks to detecting and reconstructing them from logs, and lab 4 goes one layer deeper to inspect the raw network traffic itself at the packet level. Together they cover both blue-team (defense, detection, forensics) and red-team (brute-force, port scanning) fundamentals.

## Software/Util/Tools used
**Attacker (Kali Linux — 192.168.1.16):**
- hydra — brute-force login cracker
- nmap — network/port scanner
- ftp — client used to generate traffic for capture

**Target (Ubuntu Server — 192.168.1.17):**
- fail2ban — intrusion prevention (log monitoring + IP banning)
- ufw / iptables (+ iptables-persistent) — firewall configuration
- ss & netstat — socket/connection monitoring
- journalctl, auth.log, grep — log inspection and reconstruction
- tcpdump — command-line packet capture
- vsftpd — FTP server (used as an unencrypted-protocol example)

**Analysis (Windows machine — 192.168.1.15):**
- Wireshark — GUI deep packet inspection

## Lab 1-4 summary in form of a table
| Lab | Title | Focus | Key Tools | Outcome |
|-----|-------|-------|-----------|---------|
| 1 | SSH Hardening | Prevention | hydra, fail2ban, ssh-keygen, ufw | Switched to key-pair auth, disabled password/root login, banned brute-force attempts, and set a default-deny firewall so only port 22 is open. |
| 2 | Attack Surface Reduction | Prevention | nmap, iptables, iptables-persistent | Rebuilt the firewall with iptables (loopback + port 22 allow, default DROP). Before/after nmap scans show all other ports hidden from scanning. |
| 3 | Attack Detection & Log Reconstruction | Detection | hydra, ss, journalctl, auth.log, fail2ban | Simulated a brute-force attack and reconstructed the full timeline purely from logs and socket stats, confirming the attack was detected and the attacker IP banned. |
| 4 | Packet Capture & Traffic Analysis | Inspection | ss/netstat, tcpdump, Wireshark | Captured a plaintext FTP session and recovered the login credentials and commands directly from the packets, demonstrating why encryption matters on the wire. |

## Concepts learned
- **Firewalls & default-deny:** configuring rules with both ufw and iptables, understanding chains (INPUT/OUTPUT/FORWARD), targets (ACCEPT/DROP/REJECT), and why DROP hides a host from scanning.
- **Authentication hardening:** key-pair (ed25519) authentication over passwords, disabling root login, and using a non-root sudo user for accountability.
- **Intrusion prevention & detection:** fail2ban for automated banning, and reconstructing an attack timeline from `auth.log`, `journalctl`, socket statistics, and the fail2ban log.
- **Attack surface & reconnaissance:** port scanning with nmap and reducing exposed services.
- **Packet-level analysis:** capturing traffic with tcpdump and following TCP streams in Wireshark, seeing firsthand how unencrypted protocols (FTP) leak credentials.
- **Linux proficiency:** command-line navigation, user/permission management, and service management across Ubuntu Server and Kali Linux.

## Conclusion
This project built a practical, end-to-end understanding of securing and analyzing a Linux server. Starting from prevention (hardening SSH and reducing the attack surface with firewalls), moving to detection (reconstructing an intrusion from logs alone), and finishing with inspection (reading raw packets off the wire), it demonstrates how the different layers of security work together. The recurring lesson is that prevention alone is not enough — visibility through logs and packet capture is what lets you detect, understand, and respond to what actually happens on a network, and that encryption is essential to keep that same visibility from being abused by an attacker.

## Next steps
The next project could build on these fundamentals with more advanced, enterprise-oriented tooling: Active Directory (AD) for identity and access management, a SIEM for centralized security information and event management, and intrusion detection/prevention systems (IDS/IPS) for automated network monitoring and response.
