#!/usr/bin/env python

with open("show_version.txt") as my_file:
    data = my_file.readlines()

print(f"\nLength of list {len(data)}\n")

print("Print line number1")
print("-" * 40)
print(data[0].rstrip())
print("-" * 40)

print()
print("Print line number34")
print("-" * 40)
print(data[34].rstrip())
print("-" * 40)
print()

fields = data[0].split(",")
os_version = fields[2].strip()
print("OS Version:")
print(os_version)
print()
