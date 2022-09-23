#!/usr/bin/env python
import re

with open("show_int_fa4.txt") as f:
    output = f.read()

patterns = {
    "Input": r"(\d+) packets input, (\d+) bytes",
    "Output": r"(\d+) packets output, (\d+) bytes",
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print("\n{}: ".format(label))
        print("Packets: {}".format(match.group(1)))
        print("Bytes: {}\n".format(match.group(2)))
