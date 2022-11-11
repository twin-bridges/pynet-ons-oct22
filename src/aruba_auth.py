from getpass import getpass


# Host information
SSL_VERIFY = False


def auth(session, host, api_port=4343):
    http_headers = {"Content-Type": "application/json"}

    # Creds
    USERNAME = input("Enter username: ")
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
        if auth_response.get("X-CSRF-Token"):
            # Bind headers to requests' session object
            session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]

        if auth_response.get("UIDARUBA"):
            return auth_response["UIDARUBA"]
        else:
            return None
    elif response.status_code == 401:
        raise ValueError("401 Response code: Authentication Failed")
    else:
        raise ValueError(f"Authentication Failed: {response.status_code}")


def get_request(session, host, api_port=4343, relative_url="", config_path="", uid_aruba=""):

    base_url = f"https://{host}:{api_port}/v1/configuration/"

    if config_path:
        query_string = f"?config_path={config_path}"
        if uid_aruba:
            query_string += f"&UIDARUBA={uid_aruba}"
    else:
        if uid_aruba:
            query_string = f"?UIDARUBA={uid_aruba}"
        else:
            query_string = ""

    full_url = f"{base_url}{relative_url}{query_string}"
    return session.get(full_url, verify=False)
