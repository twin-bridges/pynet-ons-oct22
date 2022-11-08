# Create a data structure that is a list of dictionaries.

# The list should have four elements. Each of the elements should be a dictionary
# with four keys: device_name, ip_addr, vendor, and platform.

# Print out the last dictionary using rich.print.

# Print out the name and ip_addr fields from the first dictionary.
from rich import print

new_ds1 = {
    "device_name": "rtr1",
    "ip_addr": "1.1.1.1",
    "vendor": "Cisco",
    "platform": "IOS",
}
new_ds2 = {
    "device_name": "rtr1",
    "ip_addr": "1.1.1.2",
    "vendor": "Cisco",
    "platform": "IOS",
}
new_ds3 = {
    "device_name": "sw1",
    "ip_addr": "1.1.1.21",
    "vendor": "Aruba",
    "platform": "CX",
}
new_ds4 = {
    "device_name": "sw2",
    "ip_addr": "1.1.1.22",
    "vendor": "Aruba",
    "platform": "CX",
}

my_list = [new_ds1, new_ds2, new_ds3, new_ds4]
print()
print("Entire Data Strcture")
print(my_list)
print()

print()
print("Print out last entry")
print(my_list[-1])
print()

print()
print("Print out fields from first entry")
ds1 = my_list[0]
print(f"Device Name: {my_list[0]['device_name']}")
print(f"IP Addr: {ds1['ip_addr']}")
print()
