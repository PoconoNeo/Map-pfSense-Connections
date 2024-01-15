import paramiko
import time
import re
import json

def parse_firewall_state_line(line):
    # Regex pattern to extract the necessary fields
    pattern = r"(all \S+) (\S+):(\d+) \((\S+):(\d+)\) -> (\S+):(\d+) (.+)"
    match = re.match(pattern, line)
    if match:
        return {
            "protocol": match.group(1),
            "src_ip_translated": match.group(2),
            "src_port_translated": match.group(3),
            "src_ip_original": match.group(4),
            "src_port_original": match.group(5),
            "dst_ip": match.group(6),
            "dst_port": match.group(7),
            "state": match.group(8)
        }
    return None

def get_pfsense_firewall_states(host, username, password, command='pfctl -ss'):
    try:
        # Set up the SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to pfSense
        client.connect(host, username=username, password=password)

        # Get the shell
        shell = client.invoke_shell()

        # Send '8' to access the shell, then a newline
        shell.send('8\n')
        time.sleep(1)  # Wait a bit for the command to be executed

        # Execute the command
        shell.send(command + '\n')
        time.sleep(1)  # Wait for the command to execute

        # Receive the output
        output = shell.recv(9999).decode()

        # Close the SSH connection
        client.close()

        return output
    except Exception as e:
        return f"An error occurred: {e}"
# Replace with your pfSense details
pfsense_ip = '[ip address of your pfSense srver]'
username = '<[username]'
password = '[password]'

# Get firewall states
firewall_states_raw = get_pfsense_firewall_states(pfsense_ip, username, password)

# Parse the firewall states into a structured format
firewall_states_parsed = []
for line in firewall_states_raw.splitlines():
    parsed_line = parse_firewall_state_line(line)
    if parsed_line:
        firewall_states_parsed.append(parsed_line)

# Save to a file named 'output.json' in JSON format
with open('output.json', 'w') as file:
    json.dump(firewall_states_parsed, file, indent=4)