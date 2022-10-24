while True:
    ip_address = input("\nEnter an IP Address: ")
    octets = ip_address.split(".")
    if len(octets) != 4:
        # Failed length test, try again
        print("\nIP address invalid...please try again.\n")
        continue

    octet_range_error = False
    for octet in octets:
        octet = int(octet)
        # Must check ALL the octets
        if octet < 0 or octet > 255:
            # Outside or range
            octet_range_error = True

    if octet_range_error:
        print("\nIP address invalid...please try again.\n")
    else:
        # Passed all of the tests
        break

banner = "-" * 50
msg = f"""
{banner}
{ip_address}
{banner}

"""
print(msg)
