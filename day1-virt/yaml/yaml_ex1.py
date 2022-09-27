#!/usr/bin/env python
import yaml
from rich import print


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    filename = "yaml_ex1.yml"
    print(read_yaml(filename))
