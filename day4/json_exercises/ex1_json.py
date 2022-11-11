import json
import rich

with open("show_apgroup.json") as f:
    data = json.load(f)

print()
print(f"\nOur data structure has a type of: {type(data)}\n")

ap_groups = data["AP group List"]
ap_groups_brief = []
for entry in ap_groups:
    ap_groups_brief.append(entry["Name"])
rich.print(ap_groups_brief)

# Alternate form using list-comprehension
ap_groups_alt = [e["Name"] for e in ap_groups]
rich.print(ap_groups_alt)
