IP_ADDR = "1.1.1.1"


def display_output(msg1):
    print()
    msg2 = "Locally defined variable"
    print("#" * 80)
    print(f"msg1: {msg1}")
    print(f"msg2: {msg2}")
    # Print out a global variable
    print(f"IP Addr: {IP_ADDR}")
    print("#" * 80)
    print()


display_output("Message1")
