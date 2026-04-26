<div align="center">

```
███████╗██╗   ██╗██╗██╗     ██╗ █████╗     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝██║   ██║██║██║     ██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
███████╗██║   ██║██║██║     ██║███████║    ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
╚════██║╚██╗ ██╔╝██║██║     ██║██╔══██║    ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
███████║ ╚████╔╝ ██║███████╗██║██║  ██║    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚══════╝  ╚═══╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
                              S C A N N E R  v1.0.0
```

### ⚡ All-in-One Port & Network Reconnaissance Framework for Security Researchers

---

[![Version](https://img.shields.io/badge/version-v1.0.0-brightgreen?style=for-the-badge&logo=github)](https://github.com/svilia/recon-scanner)
[![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-cyan?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/svilia/recon-scanner?style=for-the-badge&color=yellow)](https://github.com/svilia/recon-scanner/stargazers)
[![Forks](https://img.shields.io/github/forks/svilia/recon-scanner?style=for-the-badge&color=orange)](https://github.com/svilia/recon-scanner/network)
[![Last Commit](https://img.shields.io/github/last-commit/svilia/recon-scanner?style=for-the-badge&color=purple)](https://github.com/svilia/recon-scanner/commits)

[![Linux](https://img.shields.io/badge/Linux-✔-success?style=flat-square&logo=linux)](https://linux.org)
[![Kali](https://img.shields.io/badge/Kali_Linux-✔-success?style=flat-square&logo=kalilinux)](https://kali.org)
[![ParrotOS](https://img.shields.io/badge/ParrotOS-✔-success?style=flat-square)](https://parrotsec.org)
[![Modules](https://img.shields.io/badge/modules-18-blueviolet?style=flat-square)]()
[![Ports](https://img.shields.io/badge/ports-65535-red?style=flat-square)]()

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [What's New in v1.0.0](#-whats-new-in-v100)
- [Modules](#-modules)
- [Installation](#-installation)
- [Usage & Commands](#-usage--commands)
- [Port Reference Table](#-port-reference-table)
- [Supported Platforms](#-supported-platforms)
- [Contributors](#-contributors)
- [Legal Disclaimer](#️-legal-disclaimer)

---

## 🎯 About

**Svilia Recon Scanner** is a high-speed, modular network reconnaissance framework designed for security professionals, ethical hackers, and CTF enthusiasts.

Built with **Python 3.10+**, it combines multi-threaded port scanning, banner grabbing, OS fingerprinting, and OSINT intelligence gathering into a single unified terminal interface.

> 💡 Unlike traditional scanners, Svilia features an **intelligent module engine** that automatically recommends the right scan profile based on your target — combined with a clean, hacker-aesthetic CLI that makes complex recon workflows simple.

```
┌─────────────────────────────────────────────────────────┐
│  📡 65,535 Ports   │  🧩 18 Modules   │  ⚡ 0.3s Avg   │
│  🔍 400+ Techniques │  🐳 Docker Ready │  📊 5 Exports  │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 What's New in v1.0.0

| # | Feature | Description |
|---|---------|-------------|
| 🚀 | **Async Port Engine** | Rewritten with `asyncio` — scan 65,535 ports in under 2 seconds on LAN |
| 🧠 | **Smart Profiling** | Type `/` to search all modules by name, tag, or description |
| 🏴 | **Banner Grabbing** | Automatic service fingerprinting & version detection on all open ports |
| 🌐 | **OSINT Layer** | Passive recon: WHOIS, DNS enum, Shodan API, certificate transparency |
| 🎯 | **Target Profiler** | Type `r` — *"I want to scan a web server"* → shows relevant profile |
| 🐳 | **Docker Ready** | Zero-dependency Docker build — fully self-contained |
| 📦 | **One-liner Install** | `curl -sSL svilia.sh/install \| sudo bash` — zero manual steps |
| 📊 | **Export Reports** | JSON, XML, HTML, Markdown, CSV output formats |
| 🔧 | **Plugin System** | Drop `.svp` files into `~/.svilia/plugins/` — auto-loads on next run |
| 🔒 | **Stealth Mode** | SYN scan, decoy IPs, fragmented packets, randomized timing |

---

## 🧩 Modules

```
┌─────────────────┬──────────────────┬──────────────────┐
│  📡 PORT SCAN   │  🏴 BANNER GRAB  │  🌐 DNS ENUM     │
│  TCP/UDP/SYN    │  Version detect  │  Subdomain brute │
├─────────────────┼──────────────────┼──────────────────┤
│  🔍 WHOIS       │  🛰️ SHODAN       │  🔐 SSL/TLS      │
│  ASN + IP range │  Passive intel   │  Cert inspect    │
├─────────────────┼──────────────────┼──────────────────┤
│  🕸️ WEB CRAWL   │  👤 USER ENUM    │  💉 VULN SCAN    │
│  Hidden dirs    │  SSH/FTP/SMTP    │  CVE matching    │
├─────────────────┼──────────────────┼──────────────────┤
│  🗺️ TRACEROUTE  │  📧 EMAIL RECON  │  🐳 DOCKER SCAN  │
│  Hop latency    │  SPF/DKIM/DMARC  │  Misconfigs      │
└─────────────────┴──────────────────┴──────────────────┘
```

---

## 💻 Installation

### ⚡ One-liner (Recommended)

```bash
curl -sSL https://svilia.sh/install | sudo bash
```

### 🐍 Manual (pip)

```bash
# Clone repository
git clone https://github.com/svilia/recon-scanner.git
cd recon-scanner

# Setup virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install
sudo python3 setup.py install

# Verify
svilia --version
```

### 🐳 Docker

```bash
docker build -t svilia-recon .
docker run --rm -it svilia-recon 192.168.1.1
```

---

## ⚡ Usage & Commands

```bash
# Basic port scan (top 1000 ports)
svilia 192.168.1.1

# Full scan — all 65535 ports
svilia 192.168.1.1 -p 1-65535

# Stealth SYN scan with decoy IPs
sudo svilia 192.168.1.1 -sS --stealth --decoy 10.0.0.1,10.0.0.2

# OSINT mode (passive, no direct contact)
svilia --osint example.com

# Full recon profile
svilia example.com --full --output report.html

# Scan subnet
svilia 192.168.1.0/24 --threads 512

# Vulnerability check
svilia 192.168.1.1 --vuln --cve-db local

# Export results
svilia 192.168.1.1 --export json,html,csv
```

### 🖥️ Live Scan Output Example

```
████████████████████████████████████████████
  SVILIA RECON SCANNER v1.0.0 — INITIALIZING
████████████████████████████████████████████

  [*] Target     : 192.168.1.105
  [*] Scan Type  : FULL TCP SYN + UDP
  [*] Port Range : 1-65535
  [*] Threads    : 1024
  [*] Timeout    : 0.5s

  [SCAN] Starting async port sweep...
  ............................................
  [OPEN]  22/tcp   → SSH-2.0-OpenSSH_8.9p1
  [OPEN]  80/tcp   → Apache httpd 2.4.54
  [OPEN]  443/tcp  → nginx/1.22.0 (TLS 1.3)
  [FILT]  8080/tcp → Filtered (no response)
  [OPEN]  3306/tcp → MySQL 8.0.31
  [WARN]  3306/tcp → Port exposed! Consider firewall rule
  [OPEN]  6379/tcp → Redis 7.0.7 (NO AUTH)
  [CRIT]  6379/tcp → Redis unauthenticated — HIGH RISK

  [*] Scan complete in 1.34s
  [*] 5 open ports | 1 filtered | 65529 closed
  [*] Report saved → ./reports/192.168.1.105_scan.html
```

---

## 🗂️ Port Reference Table

| Port | Protocol | Service | Risk |
|------|----------|---------|------|
| `21` | TCP | FTP | 🔴 HIGH |
| `22` | TCP | SSH | 🟡 MEDIUM |
| `23` | TCP | Telnet | 🔴 CRITICAL |
| `25` | TCP | SMTP | 🟡 MEDIUM |
| `53` | UDP/TCP | DNS | 🟢 LOW |
| `80` | TCP | HTTP | 🟡 MEDIUM |
| `443` | TCP | HTTPS (TLS) | 🟢 LOW |
| `445` | TCP | SMB | 🔴 CRITICAL |
| `3306` | TCP | MySQL | 🔴 HIGH |
| `3389` | TCP | RDP | 🔴 HIGH |
| `5432` | TCP | PostgreSQL | 🔴 HIGH |
| `6379` | TCP | Redis | 🔴 CRITICAL |
| `8080` | TCP | HTTP Proxy | 🟡 MEDIUM |
| `9200` | TCP | Elasticsearch | 🔴 CRITICAL |
| `27017` | TCP | MongoDB | 🔴 HIGH |

---

## 🖥️ Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Kali Linux | ✅ Full Support | Recommended |
| ParrotOS | ✅ Full Support | Recommended |
| Ubuntu 20.04+ | ✅ Full Support | |
| BlackArch | ✅ Full Support | |
| Debian | ✅ Full Support | |
| macOS | ⚠️ Partial | Some modules limited |
| Windows WSL2 | ⚠️ Partial | SYN scan requires root |

---

## 🛠️ Built With

The entire project is built using:

<div align="left">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Asyncio](https://img.shields.io/badge/asyncio-FFD43B?style=for-the-badge&logo=python&logoColor=black)
![Scapy](https://img.shields.io/badge/Scapy-1F8B4C?style=for-the-badge&logo=python&logoColor=white)
![Socket](https://img.shields.io/badge/Socket-FF6B35?style=for-the-badge&logo=python&logoColor=white)
![Threading](https://img.shields.io/badge/Threading-8B5CF6?style=for-the-badge&logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich_TUI-E91E8C?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-20B2AA?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

</div>

---

## 📊 Project Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api/pin/?username=svilia&repo=recon-scanner&theme=github_dark&border_color=00ff88&title_color=00ff88&icon_color=00cfff&text_color=c9d1d9)

</div>

---

## 👥 Contributors

<div align="center">

<table>
  <tr>
    <td align="center" width="250">
      <a href="https://github.com/svilia">
        <img src="https://github.com/svilia.png" width="110" height="110"/>
      </a>
      <br/><br/>
      <a href="https://github.com/svilia"><b>svilia</b></a>
      <br/>
      <sub>⚡ Project Lead & Creator</sub>
      <br/><br/>
      <img src="https://img.shields.io/badge/LEAD-00ff88?style=flat-square"/>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/Scapy-1F8B4C?style=flat-square&logo=python&logoColor=white"/>
    </td>
    <td align="center" width="250">
      <a href="https://github.com/wortex213433">
        <img src="https://github.com/wortex213433.png" width="110" height="110"/>
      </a>
      <br/><br/>
      <a href="https://github.com/wortex213433"><b>wortex213433</b></a>
      <br/>
      <sub>🔧 Core Contributor</sub>
      <br/><br/>
      <img src="https://img.shields.io/badge/CORE-00cfff?style=flat-square"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white"/>
    </td>
  </tr>
</table>

</div>

> Katkıda bulunmak ister misin? [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını oku ve PR aç! 🚀

---

## ⚠️ Legal Disclaimer

> **FOR AUTHORIZED USE ONLY.**
>
> Svilia Recon Scanner is provided for **educational and authorized security testing purposes only**.
> Unauthorized scanning or probing of systems you do not own or have explicit written permission to test
> is **illegal** and may violate the Computer Fraud and Abuse Act (CFAA), EU Computer Misuse laws,
> and equivalent regulations worldwide.
>
> The developers and contributors assume **no liability** for any misuse of this software.
> **Use responsibly. Hack ethically.**

---

<div align="center">

```
© 2024 svilia • MIT License • Made with ❤️ for the security community
```

[![GitHub](https://img.shields.io/badge/GitHub-svilia-black?style=for-the-badge&logo=github)](https://github.com/svilia)
[![GitHub](https://img.shields.io/badge/GitHub-wortex213433-black?style=for-the-badge&logo=github)](https://github.com/wortex213433)

</div>
