#!/usr/bin/env python
from rich import print
import json

filename = "my_file.json"
with open(filename) as f:
    json_data = json.load(f)

print(json_data)
