#!/usr/bin/env python
from rich import print

my_list = ["David", "Mirav", "Tom", "Juan", "Mike"]
my_list.append("Khalil")
my_list.append("Jesus")
print(my_list.pop(0))

print(f"Length of list: {len(my_list)}")
my_list.sort()
print(my_list)
