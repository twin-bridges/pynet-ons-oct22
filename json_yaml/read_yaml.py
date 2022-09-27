import yaml
from rich import print

yaml_file = "my_file.yml"
with open(yaml_file) as f:
    output = yaml.safe_load(f)

print(output)
