# Packet Capture & Traffic Analysis (using netstat/ss, tcpdump, and wireshark)

*(1–2 sentence intro, in your own words — what this lab does and why it
moves one layer below the log-based work in Projects 1–3. See the Purpose
section of Project 4's briefing for the framing if you want a reminder.)*

## Purpose
- Showcase the use of `ss` and `netstat` to confirm a listening service and correlate live socket state against packet-level evidence
- Capture live network traffic with `tcpdump` and save it to a portable pcap file
- Analyze the capture in Wireshark, using display filters and Follow TCP Stream to reconstruct a full conversation
- Recover a cleartext credential directly from the wire, to make the risk of unencrypted protocols concrete rather than theoretical
- Develop networking knowledge of protocol encapsulation (Ethernet → IP → TCP → application data)

## Software/Tools Used
Ubuntu Server:
- `vsftpd`
- `ss`, `netstat`
- `tcpdump`

Kali Linux:
- `ftp` (client)
- Wireshark

---

## FTP Service Setup

```bash
sudo apt install vsftpd
sudo systemctl status vsftpd
sudo adduser ftpuser
# throwaway password, lab use only
```

Result:

![alt text](Attachments/vsftpd-install.png)

*(What did the status check show? Was the account created cleanly?)*

## Confirming the Listening Socket (`ss` and `netstat`)

```bash
sudo ss -tlnp | grep vsftpd
sudo netstat -tlnp | grep vsftpd
```

Result:

![alt text](Attachments/ss-netstat-listening.png)

*(Note the port and PID/process here. How did the `ss` output compare to `netstat`'s?)*

## Packet Capture Setup (`tcpdump`)

```bash
sudo tcpdump -i <interface> port 21 -w ftp_capture.pcap
```

*(Which interface did you use, and how did you confirm it was the right one?)*

## Traffic Generation (FTP Login from Kali)

```bash
ftp 192.168.1.17
```

Result:

![alt text](Attachments/ftp-login.png)

## Live Socket Snapshot (Mid-Session)

```bash
sudo ss -tun state established | grep :21
```

Result:

![alt text](Attachments/ss-established-snapshot.png)

## Stopping the Capture

*(Note the wall-clock time and confirm `ftp_capture.pcap` was written.)*

## Wireshark Analysis

Display filter used:
```
ftp
```

Result:

![alt text](Attachments/wireshark-ftp-filter.png)

## Following the TCP Stream

Result:

![alt text](Attachments/wireshark-follow-stream.png)

*(What credential did you recover? Quote the exact `USER`/`PASS` lines. Then
confirm the IP:port pair matches the `ss` snapshot from Step 5 — write the
match out explicitly.)*

## Findings

*(In your own words: what was recovered, how many packets it took, and why
this was possible — no encryption on the wire. Contrast briefly with what
FTPS/SFTP would have shown instead.)*

---

## Stretch Goals *(optional — fill in if attempted)*

### A. Encrypted Channel Comparison

*(sftp/HTTPS capture — what did Wireshark show instead of a readable credential?)*

### B. Credential Extraction via `tcpdump` Alone

```bash
sudo tcpdump -r ftp_capture.pcap -A | grep -iE "USER|PASS"
```

Result:

![alt text](Attachments/tcpdump-A-extraction.png)

### C. Three-Way Handshake

```bash
sudo tcpdump -r ftp_capture.pcap -S -n 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0' | head -5
```

Result:

![alt text](Attachments/tcpdump-handshake.png)

*(Identify the SYN, SYN-ACK, and ACK packets and their sequence/ack numbers.)*

---

## Conclusion

*(Summarize: the credential recovered, how the `ss`/`netstat` evidence
corroborated the Wireshark evidence, and what this demonstrates about
cleartext protocols in general.)*

- Packet capture with `tcpdump`, scoped with capture filters
- Reading a real protocol conversation in Wireshark (display filters, Follow TCP Stream)
- Understanding why cleartext protocols leak credentials, from direct observation
- Using `ss`/`netstat` to correlate live socket state against packet-level evidence
- Distinguishing capture filters from display filters, and CLI (`tcpdump -A`) from GUI (Wireshark) analysis

## Next Step

Week 3 shifts to **Python for Security** — sockets, `requests`, and
`argparse` — building toward the Week 4 port-scanner artefact. The TCP
handshake and socket concepts read directly off the wire in this project are
exactly what that scanner script will be automating.
