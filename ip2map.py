import requests
import json

# Function to get geolocation data for an IP address
def get_geolocation(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code} for IP {ip_address}")
            return None
    except requests.RequestException as e:
        print(f"Request failed for IP {ip_address}: {e}")
        return None

# Read the JSON data from "output.json"
with open("D:\\WebServer\\output.json", "r") as file:
    data = json.load(file)

# Check if data is a list and perform operations on each item
if isinstance(data, list):
    for item in data:
        # Extract the destination IP
        dst_ip = item.get("dst_ip")
        if dst_ip:
            # Perform geolocation lookup
            geolocation_data = get_geolocation(dst_ip)
            if geolocation_data:
                # Add the geolocation data to the JSON object
                item["dst_ip_geotag"] = geolocation_data
            else:
                print(f"Geolocation lookup failed for IP {dst_ip}")
else:
    raise ValueError("JSON data is not in the expected format (list of objects).")

# Write the updated JSON to "dst_ip_geotag.json"
with open("D:\\WebServer\\dst_ip_geotag.json", "w") as file:
    json.dump(data, file, indent=4)
