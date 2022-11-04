def read_file(filename):
    data = ""
    try:
        f = open(filename)
        data = f.read()
        f.close()
    except FileNotFoundError:
        print("An error happened")
    return data


def find_serial_number(show_version):
    for line in show_version.splitlines():
        if "Processor board ID" in line:
            fields = line.split()
            serial_number = fields[-1]
            return serial_number


if __name__ == "__main__":
    show_ver = read_file("show_version1.txt")
    if show_ver != "":
        my_serial_num = find_serial_number(show_ver)
        print(f"\n\nSerial Number: {my_serial_num}\n\n")
    else:
        print("Didn't process show version")
