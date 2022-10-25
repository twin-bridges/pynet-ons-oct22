f = open("show_ip_bgp.txt")
data = f.read()
f.close()

for line in data.splitlines():
    print(line)

