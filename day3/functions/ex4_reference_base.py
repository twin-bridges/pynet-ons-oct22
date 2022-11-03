f = open("show_version.txt")
data = f.read()

for line in data.splitlines():
    if "Processor board ID" in line:
        fields = line.split()
        serial_number = fields[-1]
        print(f"\n\nSerial Number: {serial_number}\n\n")

f.close()
