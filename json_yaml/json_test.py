#!/usr/bin/env python
import json
from rich import print

my_list = list(range(10))
my_list.append("whatever")
my_list.append("some thing")

my_dict = {"key1": "val1", "key2": "val2", "key3": "val3"}
my_dict["key4"] = my_list
my_dict["key5"] = False

print()
print("-" * 80)
print("PYTHON:")
print("-" * 8)
print(my_dict)
print("-" * 80)

print()
print()
print("-" * 80)
print("JSON:")
print("-" * 8)
print(json.dumps(my_dict, indent=4))
print("-" * 80)
print()

with open("my_file.json", "w") as f:
    json.dump(my_dict, f)
