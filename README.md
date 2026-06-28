# Penetration Testing HomeLab Setup

This is a fundamental homelab setup built using **VirtualBox** that manages two virtual machines: **Windows 11** and **Kali Linux**. The VMs can communicate with each other and are connected using an internal network configuration, isolated from the host device itself and the home network. This setup ensures a secure, safe, and a self-contained environment for experimentation, and security testing towards gaining hands-on experience in red and blue teaming. 

## Overview
This lab demonstrates key cybersecurity concepts and networking fundamentals. An internal network setup isolates the virtual machines in their own network without access to the internet nor the host device. This lab sets up an attacker machine (Kali linux VM) or the threat actor, and the target machine (Windows VM). This builds the foundation of future penetration testing experiments. Network isolation, static IP configuration, cross-platform networking, and cybersecurity lab safety were all demonstrated.


## Environment
| Component        | Details                           |
|------------------|-----------------------------------|
| Hypervisor       | VirtualBox                        |
| VM 1             | Windows 11                        |
| VM 2             | Kali Linux                        |
| Network mode     | Internal Network (`homelabnet`)   |
| Addressing       | Static IPv4, 192.168.1.0/24 subnet|

## Network Architecture

![Network Architecture](Attachments/network-architecture.png)

## Setup and Network Configuration

### 1. Prerequisites   
- Install VirtualBox
- Download Windows 11 iso file
- Download Kali linux iso file

### 2. OS Installation
In VirtualBox, for each VM:
- Select New VM
- Set VM name, ISO image, specify resources allocation, then finish

For Windows:
- RAM: 2 GB
- CPU cores: 2
- Storage: 60 GB
- Video MEM: 128 MB

For Kali linux: 
- RAM: 4 GB
- CPU cores: 4
- Storage: 80 GB
- Video MEM: 128 MB

*resource allocations may be changed*

### 3. Network Config
For each VM:
Go to Settings > Network > Adapter 1
- Enable Network Adapter
- Change the network mode to **Internal Network**
- Rename network name
- Apply changes

### 4. Assign Static IP
- For Windows, set static IPv4 address by: Settings > Network and Internet > Ethernet > config: manual, IP assignment: 192.168.1.15 , subnet mask: 255.255.255.0
- For Kali Linux, ethernet > edit connections > wired connection > settings >ipv4 settings > set method to manual > add address: ip: 192.168.1.16, netmask: 24

*quick TEMPORARY command terminal setup*
```bash
sudo ip addr add 192.168.1.16/24 dev eth0
sudo ip link set eth0 up
```

### 5. Ping Test
In order to check if both virtual machines are indeed in the same internal network and have been configured properly, we must conduct a ping test.

In the Windows 11 VM powershell terminal:
```powershell
ping 192.168.1.16
```
Expected output:
![ping results](Attachments/ping-test-output.png)

## Next Steps
The next steps for this homelab is to use network reconnaissance tools that true red teamers use. These include Nmap to discover open ports leading to vulnerabilities, Wireshark packet capturing to analyse the traffic between the two VMs, and ARP scanning to discover devices in a LAN. It is crucial to practice these skills towards better familiarity and proficiency in using pen testing tools and softwares.

## Developed Proficiencies
- Applied network segmentation principles and configured an isolated internal network in VirtualBox
- Configured manual IP addresses
- Conducted a cross-platform connectivity check using the ping command (ICMP) between Windows 11 and Kali Linux
- Developed Linux proficiency through exposure of linux distros and CLI usage
