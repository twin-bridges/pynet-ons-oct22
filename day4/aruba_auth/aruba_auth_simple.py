from getpass import getpass
import requests
import rich
import pdbr

PASSWORD = getpass("Enter Aruba Controller password: ")
HTTP_HEADERS = {"Content-Type": "application/json"}
SSL_VERIFY = False

host = "aruba.lasthop.io"
api_port = "4343"
login_url = f"https://{host}:{api_port}/v1/api/login"
username = "kbyers"

creds = f"username={username}&password={PASSWORD}"

session = requests.Session()
response = session.post(login_url, data=creds, headers=HTTP_HEADERS, verify=SSL_VERIFY)

if response.status_code == 200:
    aruba_ds = response.json().get("_global_result")
    if aruba_ds:
        x_csrf_token = aruba_ds["X-CSRF-Token"]

    HTTP_HEADERS = {}
    HTTP_HEADERS["Accept"] = "application/json"
    HTTP_HEADERS["X-CSRF-Token"] = x_csrf_token

    # Test a GET operation
    relative_url = "object/int_vlan"
    # relative_url = "object/ap_group"
    base_url = "https://aruba.lasthop.io:4343/v1/configuration/"

    full_url = f"{base_url}{relative_url}"
    print(full_url)

    response = session.get(full_url, headers=HTTP_HEADERS, verify=SSL_VERIFY)
    rich.print(response.json())
