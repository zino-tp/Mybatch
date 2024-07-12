import subprocess

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

# Execute each command and print output
for cmd in commands:
    print(f"Executing command: {cmd}")
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    print(result.stdout)
    print("=" * 40)  # Separator between command outputs
