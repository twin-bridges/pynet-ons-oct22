import aruba_auth
import requests

host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = aruba_auth.auth(session, host, api_port=api_port)

print(uid_aruba)
