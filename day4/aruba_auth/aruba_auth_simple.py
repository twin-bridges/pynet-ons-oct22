from getpass import getpass
import requests
import rich
from aruba_auth import logout


username = input("Enter username: ")
PASSWORD = getpass("Enter Aruba Controller password: ")
SSL_VERIFY = False

host = "aruba.lasthop.io"
api_port = "4343"
login_url = f"https://{host}:{api_port}/v1/api/login"

creds = f"username={username}&password={PASSWORD}"

session = requests.Session()
session.headers["Accept"] = "application/json"
response = session.post(login_url, data=creds, verify=SSL_VERIFY)

if response.status_code == 200:
    auth_response = response.json().get("_global_result")
    if auth_response.get("X-CSRF-Token"):
        session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]

    # For Aruba Controllers <= 8.6.X
    uid_aruba = auth_response["UIDARUBA"]
    uid_aruba_qs = f"UIDARUBA={uid_aruba}"

    # Test a GET operation
    relative_url = "object/int_vlan"
    base_url = f"https://{host}:{api_port}/v1/configuration/"
    full_url = f"{base_url}{relative_url}?{uid_aruba_qs}"
    print(full_url)

    response = session.get(full_url, verify=SSL_VERIFY)
    rich.print(response.json())

    response = logout(session, host, uid_aruba=uid_aruba)
    print(response)
