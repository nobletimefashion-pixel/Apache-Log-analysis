# SOC Incident Response & Hardening — Task 1: Authentication Log Triage

## Overview
This repository contains the Task 1 deliverable for **HiveSpace Coworking**, focusing on analyzing and triaging SSH authentication logs (`auth.log`) to detect brute-force login activity and establish a detection baseline for the local management server[cite: 1, 2].

## Repository Contents
* `log_creator.py` — Python script used to generate the simulated 500-line SSH `auth.log` dataset.
* `auth.log` — Simulated 500-line SSH authentication log dataset containing external failed login attempts and internal successful logins[cite: 2].
* `script.sh` — Bash log-parsing script using `grep`, `awk`, `sort`, `uniq`, and `sed` to extract and rank the top 5 attacking IP addresses[cite: 2].
* `README.md` — Summary of findings, brute-force pattern analysis, and usage instructions[cite: 2].

## Top 5 Attacking IP Addresses Identified

Out of **8 distinct external source IPs** responsible for the 437 failed login attempts, the top 5 attacking IPs account for **425 attempts (97.3%)**:

| Rank | Source IP Address | Failed Attempts | Share of Failed Attempts (437) |
| :--- | :--- | :--- | :--- |
| 1 | `203.0.113.50` | 179 | 41.0% |
| 2 | `198.51.100.23` | 109 | 24.9% |
| 3 | `192.0.2.15` | 60 | 13.7% |
| 4 | `185.220.101.4` | 47 | 10.8% |
| 5 | `45.33.32.156` | 30 | 6.9% |

*(The remaining 12 failed attempts came from 3 low-volume external scanner IPs: `172.67.18.90` with 8 attempts, `91.189.91.48` with 2 attempts, and `104.21.44.12` with 2 attempts.)*

## Summary of Findings: Brute-Force Pattern Analysis
* **Skewed Brute-Force Signature:** Out of 500 total log entries in `auth.log`, **437** are `Failed password` attempts originating from 8 distinct external source IPs, and **63** are legitimate `Accepted password` logins from 2 internal IP addresses (`192.168.1.50` and `192.168.1.62`). The attack traffic is heavily concentrated in the top two sources (`203.0.113.50` and `198.51.100.23`), which together generated 288 failed attempts (65.9% of all failures).
* **Targeted Accounts:** Failed login attempts were evenly distributed across four common usernames: `ubuntu` (114), `admin` (113), `mongodb` (109), and `user` (101) across randomized high source ports.
* **Normal User Baseline vs. Attack Behavior:** Internal IP addresses recorded only `Accepted password` events (63 total) with zero failed login attempts, meaning this sample dataset contains no accidental staff password typos. Distinguishing normal activity from attacks relies on persistence and lack of success: the top 5 external IPs generated 30–179 consecutive failures each with zero successful authentications, clearly separating automated brute-force bursts from low-volume background scanners (2–8 attempts).
* **Recommended Detection Threshold:** Time-span analysis of the top attacking IP (`203.0.113.50`) shows **179 failed attempts spread across ~23.5 hours** (~7.6 attempts/hour, or 1 attempt every ~8 minutes), representing a sustained, low-rate ("slow-and-steady") brute-force attack rather than a rapid burst. Therefore, a short 5-minute threshold would miss this pattern; HiveSpace should enforce a sliding threshold of **10 or more failed SSH login attempts within a 2-hour window** (or **15+ failures within 24 hours**) without a successful authentication to catch persistent distributed attacks while ignoring isolated 1–2 attempt staff typos.

## How to Run the Analysis
1. Clone the repository:
   ```bash
   git clone [https://github.com/nobletimefashion-pixel/Apache-Log-analysis.git](https://github.com/nobletimefashion-pixel/Apache-Log-analysis.git)
   cd Apache-Log-analysis