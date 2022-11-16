# from aruba_auth import auth
# from my_aruba import get_request, config_change
from my_aruba import ArubaAPI
from rich import print
import requests
import json
from getpass import getpass

host = "aruba.lasthop.io"
username = input("Enter username: ")
password = getpass()

aruba_conn = ArubaAPI(host=host, username=username, password=password)
aruba_conn.auth()

config_path = "/md/40Lab/VH/20:4c:03:39:5a:fc"
relative_url = "object/syscontact"
data = aruba_conn.get_request(relative_url=relative_url, config_path=config_path)
print(data)

payload = {"syscontact": "Gale Sayers, 415.111.1111"}
data = aruba_conn.config_change(relative_url=relative_url, config_path=config_path, payload=payload)
print(data)

data = aruba_conn.config_change(relative_url="object/write_memory", config_path=config_path)
print(data)
