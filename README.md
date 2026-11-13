# Apache-Log-analysis
# SOC Incident Response & Hardening — Task 1: Authentication Log Triage


# Overview

## Repo Contents

* `auth.log` - contains 500 lines of SSH authentication dataset
* `script.sh` - Log parsing script in bash tools used grep,awk,sort,uniq,sed
* `README.md` - Summary of findings , brute-force pattern analysis and usage instructions

# Top 5 Attacking IP Address Identified

List of top 5 Attacking IP addresses identified

IP: 203.0.113.50 - Failed Attempts: 79
IP: 192.0.2.15 - Failed Attempts: 78
IP: 198.51.100.23 - Failed Attempts: 73
IP: 45.33.32.156 - Failed Attempts: 67
IP: 185.220.101.4 - Failed Attempts: 66

## Summary of Findings: Brute-Force Pattern Analysis
* **Attack Signatures:** External source IPs generated rapid, consecutive failed SSH login attempts within short time windows, systematically cycling through high-privilege and default system usernames (`root`, `admin`, `ubuntu`, `postgres`, `oracle`).
* **Normal User Baseline vs. Attack Behavior:** Internal staff IP addresses (`192.168.1.x`) exhibited only isolated failed attempts (1–3 failures caused by password typos) followed by successful `Accepted publickey` or valid login events. In contrast, the top 5 external IPs recorded zero successful authentications and high-frequency bursts.
* **Recommended Detection Threshold:** Any source IP generating **5 or more failed SSH login attempts within a 5-minute window** without a successful authentication should be flagged as a brute-force incident and blocked at the firewall/Fail2Ban level.

## How to Run the Analysis
1. Clone the repository:
   git clone https://github.com/nobletimefashion-pixel/Apache-Log-analysis.git
   cd Apache-Log-analysis
2. Execute the script:
   bash script.sh
3.Update the Exact Counts and Verify
1. Open `README.md` in `nano` (or your preferred editor) to replace the approximate numbers (`~225`, etc.) and `<your-repo-name>` with your exact script output and GitHub repository name:
   nano README.md
