import requests
import rich
from aruba_auth import auth, show_command, logout


host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"
uid_aruba = auth(session, host=host, api_port=api_port)

command = "show+ap+radio-database"
response = show_command(
    session,
    host=host,
    command=command,
    uid_aruba=uid_aruba,
)
print()
ap_data = response.json()
ap_data = ap_data["AP Radio Database"]
ap_list = [(e['Name'], e["IP Address"]) for e in ap_data]
rich.print(ap_list)
print()

response = logout(session, host=host, uid_aruba=uid_aruba)
print()
rich.print(response.json())
print()
