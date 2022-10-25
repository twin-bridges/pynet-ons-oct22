with open("show_version.txt") as my_var:
    data = my_var.read()

data2 = data.splitlines()
for line in data2:
    if "Processor board ID" in line:
        line_ser_no = line

words = line_ser_no.split()

serial_number = words[3]
print("-" * 50)
print(serial_number)
print("-" * 50)
