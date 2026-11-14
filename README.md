# SOC Incident Response & Hardening — Task 1: Authentication Log Triage

## Overview
This repository contains the Task 1 deliverable for **HiveSpace Coworking**, focusing on analyzing and triaging SSH authentication logs (`auth.log`) to detect brute-force login activity and establish a detection baseline for the local management server.

## Repository Contents
* `auth.log` — Simulated 500-line SSH authentication log dataset containing external failed login attempts and internal successful logins.
* `script.sh` — Bash log-parsing script using `grep`, `awk`, `sort`, `uniq`, and `sed` to extract and rank the top 5 attacking IP addresses.
* `README.md` — Summary of findings, brute-force pattern analysis, and usage instructions.

## Top 5 Attacking IP Addresses Identified

| Rank | Source IP Address | Failed Attempts | Share of Failed Attempts |
| :--- | :--- | :--- | :--- |
| 1 | `203.0.113.50` | 79 | 21.8% |
| 2 | `192.0.2.15` | 78 | 21.5% |
| 3 | `198.51.100.23` | 73 | 20.1% |
| 4 | `45.33.32.156` | 67 | 18.5% |
| 5 | `185.220.101.4` | 66 | 18.2% |

## Summary of Findings: Brute-Force Pattern Analysis
* **Distributed Brute-Force Signature:** Out of 500 total log entries in `auth.log`, **363** are `Failed password` attempts originating from external source IPs and **137** are legitimate `Accepted password` logins from internal IP addresses. Rather than a single noisy source, the top 5 external IPs generated a sustained, nearly uniform volume of failed attempts (66–79 failures each).
* **Targeted Accounts:** Failed login attempts targeted `Ubuntu,mongodb,user,admin` across randomized high source ports.
* **Normal User Baseline vs. Attack Behavior:** Internal IP addresses recorded only `Accepted password` events with zero failed login attempts, meaning this sample dataset contains no accidental user password typos. Distinguishing normal activity from attacks relies on persistence and lack of success: external attacking IPs generated dozens of consecutive failures with zero successful authentications.
* **Recommended Detection Threshold:** Any source IP generating **5 or more failed SSH login attempts within a 5-minute window** without a successful authentication should be classified as a brute-force attack and blocked via firewall rules or Fail2Ban.

## How to Run the Analysis
1. Clone the repository:
   ```bash
   git clone [https://github.com/nobletimefashion-pixel/Apache-Log-analysis.git](https://github.com/nobletimefashion-pixel/Apache-Log-analysis.git)
   cd Apache-Log-analysis

# results

     94 ubuntu
     94 mongodb
     89 user
     86 admin
