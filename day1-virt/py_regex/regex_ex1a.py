#!/usr/bin/env python
# Use named regular expressions
import re

with open("show_int_fa4.txt") as f:
    output = f.read()

patterns = {
    "Input": r"(?P<pkts>\d+) packets input, (?P<bytes>\d+) bytes",
    "Output": r"(?P<pkts>\d+) packets output, (?P<bytes>\d+) bytes",
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print(f"\n{label}: ")
        print(f"Packets: {match.group('pkts')}")
        print(f"Bytes: {match.group('bytes')}\n")
