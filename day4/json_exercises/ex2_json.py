import json

json_str = """{
    "VLAN CONFIGURATION": [
        {
            "AAA Profile": "N/A",
            "Description": "Default",
            "Option-82": "Disabled",
            "Ports": "GE0/0/1 Pc0-7",
            "VLAN": "1"
        },
        {
            "AAA Profile": "N/A",
            "Description": "VLAN0235",
            "Option-82": "Disabled",
            "Ports": "GE0/0/0",
            "VLAN": "235"
        }
    ],
    "_meta": [ "VLAN", "Description", "Ports", "AAA Profile", "Option-82"]
}"""

# Convert the JSON string over to structured data. Note, the extra 's' on json.loads
# json.load is load from a file
# json.loads is load from a string
data = json.loads(json_str)

print(f"\n\nOur returned data structure is of type: {type(data)}\n\n")
