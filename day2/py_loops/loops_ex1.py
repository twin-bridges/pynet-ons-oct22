# Read BGP file
with open("show_ip_bgp.txt") as f:
    bgp_data = f.read()


f = open("bgp_output.txt", "w")
bgp_header = True
for line in bgp_data.splitlines():

    # Ignore all of the header lines
    if bgp_header:
        if "Network" in line and "Path" in line:
            bgp_header = False
        continue

    # Process BGP table
    fields = line.split()
    as_path = fields[5:-1]
    prefix = fields[1]

    f.write(f"{prefix} -> {as_path}\n")

f.close()
