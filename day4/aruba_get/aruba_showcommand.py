import requests
import rich
from aruba_auth import auth

host = "aruba.lasthop.io"
api_port = "4343"

session = requests.Session()
session.headers["Accept"] = "application/json"

uid_aruba = auth(session, host=host, api_port=api_port)
uid_aruba_qs = f"UIDARUBA={uid_aruba}"

# Test a GET operation
base_url = f"https://{host}:{api_port}/v1/configuration/"

# Adding the UID_ARUBA query string for compatibility with 8.6.X.X
command = "show+ap+database-summary"
command = "show+ap+radio-database"
relative_url = f"showcommand?command={command}&{uid_aruba_qs}"
full_url = f"{base_url}{relative_url}"

response = session.get(full_url, verify=False)
rich.print(response.json())

