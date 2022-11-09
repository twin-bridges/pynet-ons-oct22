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
    """
        {'_global_result': {'status': '0', 'status_str': "You've logged in successfully.", 'UIDARUBA':
    'NTQ4ODM4M2YtMGI0NS00N2Y2LWJjMTEtMDEx', 'X-CSRF-Token': 'OGMwMGE0MGMtM2E3NC00NDAyLWFiY2EtYTVh'}}
    """
    aruba_ds = response.json().get("_global_result")
    if aruba_ds:
        rich.print(aruba_ds)
        # Aruba Docs state:
        # Starting from ArubaOS 8.7.0.0, UIDARUBA is deprecated. The X-CSRF-Token will be
        # usedinthe header. The UIDARUBAis still available for backward compatibility with
        # older ArubaOS firmware versions.

        pdbr.set_trace()
        uid_aruba = aruba_ds["UIDARUBA"]
        x_csrf_token = aruba_ds["X-CSRF-Token"]
        print(x_csrf_token)

    HTTP_HEADERS = {}
    HTTP_HEADERS["Accept"] = "application/json"
    HTTP_HEADERS["X-CSRF-Token"] = x_csrf_token

    # session = {"SESSION": uid_aruba}

    # Test a GET operation
    relative_url = "/object/int_vlan"

    base_url = "https://aruba.lasthop.io:4343/v1/configuration/"
    relative_url = "object/aaa_prof?config_path=/md"

    full_url = f"{base_url}{relative_url}"
    pdbr.set_trace()

    response = session.get(full_url, headers=HTTP_HEADERS, verify=SSL_VERIFY)
    # response = requests.get(full_url, headers=HTTP_HEADERS, verify=SSL_VERIFY)
    # response = requests.get(full_url, cookies=session, verify=SSL_VERIFY)
    rich.print(response.json())
