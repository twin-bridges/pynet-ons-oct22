from rich import print

nested_dict = {
    "rtr1": {"ip_addr": "22.17.1.1", "vendor": "cisco", "platform": "ios-xe"},
    "rtr2": {"ip_addr": "22.17.1.2", "vendor": "cisco", "platform": "ios-xe"},
    "sw1": {"ip_addr": "22.17.1.20", "vendor": "aruba", "platform": "aruba-cx"},
    "sw2": {"ip_addr": "22.17.1.21", "vendor": "aruba", "platform": "aruba-cx"},
}

print("\nNested Dictionary:")
print(nested_dict)

print()
print("RTR2 Entry:")
print(nested_dict["rtr2"])
print()

print("SW1 Entry, Platform Field:")
print(nested_dict["sw1"]["platform"])
print()
