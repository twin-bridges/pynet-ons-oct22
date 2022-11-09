from getpass import getpass
import requests
import rich
import pdbr  # noqa


# Host information
SSL_VERIFY = False


def auth(session, host, api_port):
    http_headers = {"Content-Type": "application/json"}

    # Creds
    USERNAME = "kbyers"
    PASSWORD = getpass("Enter Aruba Controller password: ")
    creds = f"username={USERNAME}&password={PASSWORD}"

    # Login URL
    login_url = f"https://{host}:{api_port}/v1/api/login"

    # Authenticate
    response = session.post(
        login_url, data=creds, headers=http_headers, verify=SSL_VERIFY
    )

    # Verify Authentication Worked
    if response.status_code == 200:
        auth_response = response.json().get("_global_result")
        if auth_response:
            # Bind headers to requests' session object
            session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]
    elif response.status_code == 401:
        raise ValueError("401 Response code: Authentication Failed")
    else:
        raise ValueError(f"Authentication Failed: {response.status_code}")


def aruba_get(session, host, port, relative_url):

    base_url = f"https://{host}:{port}/v1/configuration/"
    full_url = f"{base_url}{relative_url}"
    return session.get(full_url, verify=SSL_VERIFY)


def main():
    host = "aruba.lasthop.io"
    api_port = "4343"

    session = requests.Session()
    session.headers["Accept"] = "application/json"
    auth(session, host=host, api_port=api_port)

    # Test a GET operation
    # relative_url = "object/aaa_prof?config_path=/md"
    # response = aruba_get(session, relative_url)
    # rich.print(response.json())

    # List of all of the objects
    # relative_url = "object"
    # response = aruba_get(session, relative_url)
    # rich.print(response.json())

    # relative_url = "object/int_vlan"
    # relative_url = "object/vlan_id"
    aruba_obj = "container/WAN"
    # aruba_obj = "object/vlan_id"
    # aruba_obj = "object/int_vlan"
    # aruba_obj = "object/vlan_name_id"
    # aruba_obj = "object/int_vlan"
    # relative_url = f"{aruba_obj}"
    config_path = "?config_path=/mm"
    api_type = "&type='meta-only'"
    relative_url = f"{aruba_obj}{config_path}{api_type}"
    response = aruba_get(session, host=host, port=api_port, relative_url=relative_url)
    my_ds = response.json()
    rich.print(response.json())
    print(relative_url)
    # /md = managed devices
    # config_path = "?config_path=/md"

    # /mm = Common to both mobility masters

    # response = aruba_get(session, relative_url)
    # rich.print(response.json())


if __name__ == "__main__":
    main()
