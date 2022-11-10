from getpass import getpass
import requests
import rich

SSL_VERIFY = False


def login(session, host, api_port=4343):
    username = input("Enter username: ")
    PASSWORD = getpass("Enter Aruba Controller password: ")
    creds = f"username={username}&password={PASSWORD}"

    response = session.post(login_url, data=creds, verify=SSL_VERIFY)

    if response.status_code == 200:
        auth_response = response.json().get("_global_result")
        if auth_response.get("X-CSRF-Token"):
            session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]

        # For Aruba Controllers <= 8.6.X
        if auth_response.get("UIDARUBA"):
            return auth_response["UIDARUBA"]
        else:
            return None
    elif response.status_code == 401:
        msg = "401 Authentication Error"
        raise ValueError(msg)
    else:
        raise ValueError(
            f"Authentication failed with an unknown status code: {response.status_code}"
        )


if __name__ == "__main__":
    host = "aruba.lasthop.io"
    api_port = "4343"
    login_url = f"https://{host}:{api_port}/v1/api/login"

    session = requests.Session()
    session.headers["Accept"] = "application/json"

    uid_aruba = login(session, host, api_port=api_port)
    if uid_aruba is None:
        raise ValueError("UIDARUBA not returned in authentication request")
    uid_aruba_qs = f"UIDARUBA={uid_aruba}"

    # Test a GET operation
    relative_url = "object/int_vlan"
    base_url = f"https://{host}:{api_port}/v1/configuration/"
    full_url = f"{base_url}{relative_url}?{uid_aruba_qs}"

    response = session.get(full_url, verify=SSL_VERIFY)
    rich.print(response.json())
