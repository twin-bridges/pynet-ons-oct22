with open("show_version.txt") as f:
    output = f.read()

for line in output.splitlines():
    if "Processor board" in line:
        fields = line.split()
        serial_number = fields[-1]
        print(serial_number)
        break
