import os

# List of IP addresses to test
ip_addresses = [
    "192.168.1.1",
    "192.168.1.12",
    "192.168.1.194",
    "192.168.1.195",
    "192.168.1.196",
    "192.168.1.198",
    "192.168.1.200"
]

def ping_ip(ip):
    print(f"Pinging {ip}...")
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"{ip} is reachable.")
        return True
    else:
        print(f"{ip} is not reachable.")
        return False

def ssh_test(ip):
    print(f"Testing SSH on {ip}...")
    response = os.system(f"ssh -o BatchMode=yes -o ConnectTimeout=5 pi@{ip} exit > /dev/null 2>&1")
    if response == 0:
        print(f"Success! {ip} is your Raspberry Pi.")
        return True
    else:
        print(f"SSH failed for {ip}.")
        return False

for ip in ip_addresses:
    if ping_ip(ip):
        if ssh_test(ip):
            break
else:
    print("Could not identify the Raspberry Pi on the network.")
