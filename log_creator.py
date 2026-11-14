# creating an auth.log dataset
import random
from datetime import datetime, timedelta

# Top 5 primary brute-force attackers
top_attackers_ip = [
    "203.0.113.50",   # #1 Top attacker
    "198.51.100.23",  # #2 Heavy attacker
    "192.0.2.15",     # #3 Moderate attacker
    "185.220.101.4",  # #4 Moderate attacker
    "45.33.32.156"    # #5 Low-tier brute-forcer
]

# 4 low-volume external background scanners (1-5 attempts each)
background_scanners_ip = [
    "104.21.44.12",
    "172.67.18.90",
    "91.189.91.48",
    "140.82.121.4"
]

# Legitimate internal staff IPs
internal_ip = [
    "192.168.1.50",
    "192.168.1.62"
]

all_attackers = top_attackers_ip + background_scanners_ip
all_ips = all_attackers + internal_ip

# Weighted probabilities: heavy skew for top 5, small tail for scanners, realistic share for staff
weights = [180, 110, 65, 45, 30, 4, 3, 2, 1, 30, 30]

attackers_usernames = ["ubuntu", "admin", "user", "mongodb"]
staff_username = ["khan", "sara", "john"]

start_time = datetime.now() - timedelta(days=1)

with open("auth.log", "w") as file:
    for i in range(500):
        timestamp = (start_time + timedelta(seconds=i * 170)).strftime("%b %d %H:%M:%S")
        ip = random.choices(all_ips, weights=weights, k=1)[0]
        
        if ip in all_attackers:
            user = random.choice(attackers_usernames)
            status = "Failed password for"
        else:
            user = random.choice(staff_username)
            status = "Accepted password for"
        
        log_line = f"{timestamp} server sshd[1234]: {status} {user} from {ip} port {random.randint(49152, 65535)} ssh2\n"
        file.write(log_line)