import json

# Load JSON data from file
with open('file.json', 'r') as file:
    data = json.load(file)

# Extract the interface status information
interface_status = data['data']['Interface Status']

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<40} {:<20} {:<20} {:<8} {:<8}".format("DN", "x.", "Description", "Speed", "MTU"))
print("-" * 80)

# Print interface status details
for interface in interface_status:
    dn = interface['dn']
    x = interface['x.']
    description = interface['Description']
    speed = interface['Speed']
    mtu = interface['MTU']
    print("{:<40} {:<20} {:<20} {:<8} {:<8}".format(dn, x, description, speed, mtu))
