#!/usr/bin/env python
class NetDevice:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password


my_obj1 = NetDevice(ip_addr="1.1.1.1", username="admin", password="pwd")
my_obj2 = NetDevice(ip_addr="1.1.1.2", username="admin", password="pwd")
my_obj3 = NetDevice(ip_addr="1.1.1.3", username="admin", password="pwd")
my_obj4 = NetDevice(ip_addr="1.1.1.4", username="admin", password="pwd")

print()
print(f"Object: {my_obj4}")
print(f"IP Addr: {my_obj4.ip_addr}")
print(f"Username: {my_obj4.username}")
print(f"Password: {my_obj4.password}")
print()
