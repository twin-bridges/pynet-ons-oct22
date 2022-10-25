from rich import print

with open("show_ip_int_brief.txt") as my_file:
    show_ip = my_file.read()

my_ds = {}
for line in show_ip.splitlines():
    if "Interface" in line and "Protocol" in line:
        continue

    intf, ip_addr, _, _, line_status, line_protocol = line.split()
    my_ds[intf] = line_protocol

print()
print(my_ds)
print()
