import json

def parse_data(data_file):
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
        return []

    interfaces = []
    for item in data["imdata"]:
        interface = {
            "dn": item["l1PhysIf"]["attributes"]["dn"],
            "description": item["l1PhysIf"]["attributes"]['descr'],
            "speed": item["l1PhysIf"]["attributes"]['speed'],
            "mtu": item["l1PhysIf"]["attributes"]['mtu']
        }
        interfaces.append(interface)
    return interfaces


def format_output(interfaces):
    """Formats interface data into a table-like string."""
    header = "{:<45}    {:10}   {:10}   {:5}".format("DN", 
                                                "Description", 
                                                "Speed", 
                                                "MTU")
    output = header + "\n" + "=" * len(header) + "\n"
    for interface in interfaces:
        output += "{:<45}     {:10}    {:10} {:5}".format(
            interface["dn"][:50], 
            interface["description"], 
            interface["speed"], 
            interface['mtu']
        ) + "\n"
    return output


data_file = "lab4\sample-data.json"
interfaces = parse_data(data_file)
output = format_output(interfaces)
print(output)

