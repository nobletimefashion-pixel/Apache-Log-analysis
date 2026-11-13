#creating a suth.log data
import random
from datetime import datetime, timedelta

attackers_ip = [
    "203.0.113.50",   
    "198.51.100.23",  
    "192.0.2.15",     
    "185.220.101.4",  
    "45.33.32.156"
]

internal_ip = [
    "192.168.1.50",
    "192.168.1.62"
]

all_ips = attackers_ip + internal_ip

attackers_usernames = ["ubuntu","admin","user","mongodb"]
staff_username = ["khan","sara","john"]

# using a for loop to write lines
start_time = datetime.now() - timedelta(days=1)

with open("auth.log", "w") as file:
    for i in range(500):
        timestamp = (start_time + timedelta(seconds=i * 170)).strftime("%b %d %H:%M:%S")
        ip = random.choice(all_ips)
        if ip in attackers_ip:
            user = random.choice(attackers_usernames)
            status = "Failed password for"
        else:
            user = random.choice(staff_username)
            status = "Accepted password for"
        
        log_line = f"{timestamp} server sshd[1234]: {status} {user} from {ip} port {random.randint(49152, 65535)} ssh2\n"
        file.write(log_line)