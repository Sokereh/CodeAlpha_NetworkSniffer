# CodeAlpha_NetworkSniffer
This project is a Basic Network Sniffer developed during my Cyber Security Internship at CodeAlpha. It is a Python-based tool designed to capture, monitor, and analyze live network traffic to understand data flow and protocol structures.

As a student pursuing an MSc in Cybersecurity and Digital Forensics, I built this tool to demonstrate the practical application of network security principles and packet analysis.

Technical Features

Real-Time Packet Capture: Interfaces with the network adapter to intercept incoming and outgoing traffic.

Protocol Dissection: Automatically identifies and labels TCP, UDP, and ICMP protocols.

IP Tracking: Extracts and displays Source and Destination IP addresses for every captured packet.

Payload Inspection: Provides a hexadecimal snippet of the packet data for deeper analysis.


 Getting Started

Prerequisites: Python 3.x

Scapy Library: Install via pip install scapy.

Npcap: Required for Windows systems to enable raw packet capturing.


Installation & Execution

Clone this repository to your local machine.

Open your terminal (Command Prompt or VS Code Terminal) as an Administrator.


Run the script:

python network_sniffer.py


Security Analysis

This project serves as a practical exercise in Network Security. By observing unencrypted traffic, it highlights the critical need for encryption protocols like HTTPS and TLS to protect sensitive data from being intercepted by unauthorized sniffers.

Intern Name: Okereh Star

Student ID: CA/DF1/40819

Domain: Cyber Security
