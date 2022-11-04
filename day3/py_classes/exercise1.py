class NetworkDevice:

    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.vendor = "Aruba"

    # def print_ip(self, message, var2):
    #    print(f"My IP Address: {self.ip_addr}")
    #    print(message)
    #    print(var2)


rtr1 = NetworkDevice("1.1.1.1", username="admin", password="whatever")
print(rtr1)
