#!/usr/bin/env python
class NetDevice(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def print_ip(self):
        print(f"Device IP address is: {self.ip_addr}")

    def print_creds(self):
        print(f"Device username: {self.username}")
        print(f"Device password: {self.password}")


if __name__ == "__main__":

    print()
    # Validation code
    my_obj1 = NetDevice(ip_addr="1.1.1.1", username="admin", password="pwd")
    my_obj1.print_ip()
    my_obj1.print_creds()
    print()
