import requests
import rich
from aruba_auth import auth
from aruba_auth import get as aruba_get

host = "aruba.lasthop.io"
api_port = "4343"
base_url = f"https://{host}:{api_port}/v1/configuration/"

session = requests.Session()
session.headers["Accept"] = "application/json"
auth(session, host=host, api_port=api_port)

# Test a GET operation
# relative_url = "object/ap_group"
relative_url = "object/ap_name"
config_path = "?config_path=/md/40Lab"
# config_path = "?config_path=/md/40Lab/VH/20:4c:03:39:5a:fc"
url_config_path = f"{relative_url}{config_path}"

response = aruba_get(session, base_url, relative_url=url_config_path)
rich.print(response.json())
