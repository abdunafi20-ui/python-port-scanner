# python-port-scanner
Advanced Python port scanner with banner grabbing and file output
# 🔍 Advanced Python Port Scanner

## 📌 Description
This is a Python-based port scanner that scans a target system to identify open ports and detect running services using banner grabbing.

## 🚀 Features
- Scans ports from 1 to 1000
- Detects open ports
- Banner grabbing (service detection)
- Saves scan results to a file
- Handles errors and interruptions

## 🛠️ Technologies Used
- Python
- Socket Programming

## 🧠 How It Works
The tool attempts to establish TCP connections to multiple ports on a target system. If a connection is successful, the port is marked as open. It also tries to retrieve service information from the port.

## ▶️ How to Run

```bash
python port_scanner.py
