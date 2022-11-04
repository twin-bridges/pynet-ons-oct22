
def split_ip(ip_addr, message, network):
    print(message)
    print(f"Network is {network}")
    octets = ip_addr.split(".")
    return octets

my_octets = split_ip("192.168.1.9", "Hello", "whatever")
print(my_octets)