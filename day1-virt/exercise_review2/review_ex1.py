#!/usr/bin/env python
import pathlib
import yaml
from rich import print
from netmiko import ConnectHandler


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":

    # Load the .netmiko.yml file
    netmiko_yml = pathlib.PosixPath("~/.netmiko.yml")
    netmiko_yml = netmiko_yml.expanduser()
    my_devices = read_yaml(netmiko_yml)

    print()
    for device_name, device_dict in my_devices.items():
        # Skip the groups
        if isinstance(device_dict, list):
            continue

        print(f"Connecting to -> {device_name}")
        with ConnectHandler(**device_dict) as nc:
            print(nc.find_prompt())
            print()

    print()
    print()
