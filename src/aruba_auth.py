import json
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


def logout(session, host, api_port=4343, uid_aruba=""):

    url = f"https://{host}:{api_port}/v1/api/logout"
    if uid_aruba:
        query_string = f"?UIDARUBA={uid_aruba}"
    else:
        query_string = ""

    full_url = f"{url}{query_string}"

    return session.post(
        full_url, verify=False
    )


def get_request(
    session, host, api_port=4343, relative_url="", config_path="", uid_aruba=""
):

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


def get_request_filter(
    session,
    host,
    api_port=4343,
    relative_url="",
    config_path="",
    filter_str="",
    uid_aruba="",
):

    base_url = f"https://{host}:{api_port}/v1/configuration/"

    filter_qs = ""
    if filter_str:
        filter_qs = f"filter={json.dumps(filter_str)}"

    if config_path:
        query_string = f"?config_path={config_path}"
        if uid_aruba:
            query_string += f"&UIDARUBA={uid_aruba}"
    else:
        if uid_aruba:
            query_string = f"?UIDARUBA={uid_aruba}"
        else:
            query_string = ""

    if filter_qs:
        query_string += f"&{filter_qs}"

    full_url = f"{base_url}{relative_url}{query_string}"
    return session.get(full_url, verify=False)


def show_command(session, host, command, api_port=4343, uid_aruba=""):

    base_url = f"https://{host}:{api_port}/v1/configuration/showcommand"
    query_string = f"?command={command}"
    if uid_aruba:
        query_string += f"&UIDARUBA={uid_aruba}"

    full_url = f"{base_url}{query_string}"
    return session.get(full_url, verify=False)


def config_change(
    session,
    host,
    api_port=4343,
    relative_url="",
    config_path="",
    config_payload="",
    uid_aruba="",
):

    session.headers["Content-Type"] = "application/json"
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
    if config_payload:
        return session.post(full_url, data=json.dumps(config_payload), verify=False)
    else:
        # Allow POSTs like "write memory" that have no payload
        return session.post(full_url, verify=False)
