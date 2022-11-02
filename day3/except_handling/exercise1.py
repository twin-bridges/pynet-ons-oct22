def read_file(filename):
    try:
        f = open(filename)
        data = f.read()
        f.close()
    except FileNotFoundError:
        print("\nDarn it...the file was not found\n")
        data = ""

    return data


def find_serial_number(show_ver):
    serial_number = ""
    for line in show_ver.splitlines():
        if "Processor board ID" in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number


my_file = "show_version.txt"
show_ver = read_file(my_file)
serial_number = find_serial_number(show_ver)
print(f"\nSerial Number is {serial_number}\n")
