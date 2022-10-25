
1. Read the contents of "show_vlan.txt". This is from an Arista vEOS switch.

2. Using either readlines() or splitlines() loop over the contents of this file. Skip the header information.

3. Create a new dictionary where the key is the vlan_id. The corresponding value should be a dictionary containing the
following key-value pairs: vlan_name, status, ports. The ports should be a list of ports.

4. Use rich.print to print out your final data structure. Your final data structure should be similar to the following:

{
    '1': {'vlan_name': 'default', 'vlan_status': 'active', 'ports': ['Cpu,', 'Et1']},
    '2': {'vlan_name': 'VLAN0002', 'vlan_status': 'active', 'ports': ['Et2']},
    '3': {'vlan_name': 'VLAN0003', 'vlan_status': 'active', 'ports': ['Et3']},
    '4': {'vlan_name': 'VLAN0004', 'vlan_status': 'active', 'ports': ['Et4']},
    '5': {'vlan_name': 'VLAN0005', 'vlan_status': 'active', 'ports': ['Et5']},
    '6': {'vlan_name': 'VLAN0006', 'vlan_status': 'active', 'ports': ['Et6']},
    '7': {'vlan_name': 'VLAN0007', 'vlan_status': 'active', 'ports': ['Et7']}
}
