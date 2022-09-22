#!/usr/bin/env python

ip_addr = input("\nPlease enter IP address: ")
octets = ip_addr.split(".")

# One solution
print()
print(f"{octets[0]:<12}{octets[1]:<12}{octets[2]:<12}{octets[3]:<12}")
print()

# Alternate solution using unpacking
print()
print("{:<12}{:<12}{:<12}{:<12}".format(*octets))
print()
