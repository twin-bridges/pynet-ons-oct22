#!/usr/bin/env python
import yaml
from rich import print

my_list = list(range(10))
my_list.append("whatever")
my_list.append("some thing")

new_dict = {"name": "Kirk Byers"}

my_dict = {"key1": "val1", "key2": "val2", "key3": "val3"}
my_dict["key4"] = my_list
my_dict["key5"] = False
my_dict["key6"] = new_dict

print()
print("-" * 80)
print("PYTHON:")
print("-" * 8)
print(my_dict)
print("-" * 80)
print()

print()
print("-" * 80)
print("YAML:")
print("-" * 8)
print(yaml.dump(my_dict, default_flow_style=True))
print("-" * 80)
print("YAML (expanded format):")
print("-" * 8)
print(yaml.dump(my_dict, default_flow_style=False))
print("-" * 80)
print()

with open("my_file.yml", "w") as f:
    f.write(yaml.dump(my_dict, default_flow_style=False))
