#!/usr/bin/env python
from rich import print

my_list = ["hello", "new", "something", "else", "now"]
my_list.append("whatever")
my_list.append("xyz")
print(my_list.pop(0))

print(f"Length of list: {len(my_list)}")
my_list.sort()
print(my_list)
