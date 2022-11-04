# Print out the device_name and ip_addr fields from the first dictionary.
from rich import print

my_ds = [
    {
        "device_name": "rtr1",
        "ip_addr": "22.17.1.1",
        "vendor": "cisco",
        "platform": "ios-xe",
    },
    {
        "device_name": "rtr2",
        "ip_addr": "22.17.1.2",
        "vendor": "cisco",
        "platform": "ios-xe",
    },
    {
        "device_name": "sw1",
        "ip_addr": "22.17.1.20",
        "vendor": "aruba",
        "platform": "aruba-cx",
    },
    {
        "device_name": "sw2",
        "ip_addr": "22.17.1.21",
        "vendor": "aruba",
        "platform": "aruba-cx",
    },
]

print("\nPrint out the last dictionary in the list:")
print(my_ds[-1])
print()

print("Print out the device_name and ip_addr fields from first entry:")
print(f"Device Name: {my_ds[0]['device_name']}")
print(f"IP Addr: {my_ds[0]['ip_addr']}")
print()
