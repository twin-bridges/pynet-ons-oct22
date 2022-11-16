import requests
import json


def get_request(
    session, host, relative_url, uid_aruba, config_path="/mm/mynode", api_port="4343"
):

    # config_path = f"?config_path=/md/40Lab/VH/{mac}"

    # Test a GET operation
    base_url = f"https://{host}:{api_port}/v1/configuration/"
    uid_aruba_qs = f"UIDARUBA={uid_aruba}"

    # Adding the UID_ARUBA query string for compatibility with 8.6.X.X
    query_string = f"?config_path={config_path}"
    if uid_aruba:
        query_string += f"&{uid_aruba_qs}"
    full_url = f"{base_url}{relative_url}{query_string}"

    response = session.get(full_url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Get Request Failed: {response.status_code}")


def show_command(session, host, command, uid_aruba, api_port="4343"):

    base_url = f"https://{host}:{api_port}/v1/configuration/"
    uid_aruba_qs = f"UIDARUBA={uid_aruba}"

    relative_url = f"showcommand?command={command}&{uid_aruba_qs}"
    full_url = f"{base_url}{relative_url}"

    response = session.get(full_url, verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Get Request Failed: {response.status_code}")


def config_change(
    session,
    host,
    relative_url,
    uid_aruba,
    payload="",
    config_path="/mm/mynode",
    api_port="4343",
):

    base_url = f"https://{host}:{api_port}/v1/configuration/"
    uid_aruba_qs = f"UIDARUBA={uid_aruba}"

    # Adding the UID_ARUBA query string for compatibility with 8.6.X.X
    query_string = f"?config_path={config_path}"
    if uid_aruba:
        query_string += f"&{uid_aruba_qs}"

    full_url = f"{base_url}{relative_url}{query_string}"

    if payload:
        response = session.post(full_url, data=json.dumps(payload), verify=False)
    else:
        response = session.post(full_url, verify=False)

    return response.json()


class ArubaAPI:
    def __init__(self, host, username, password, api_port="4343"):
        self.host = host
        self.username = username
        self.password = password
        self.api_port = api_port

        self.session = requests.Session()

    def auth(self):
        http_headers = {"Content-Type": "application/json"}

        # Creds
        creds = f"username={self.username}&password={self.password}"

        # Login URL
        login_url = f"https://{self.host}:{self.api_port}/v1/api/login"

        # Authenticate
        response = self.session.post(
            login_url, data=creds, headers=http_headers, verify=False
        )

        # Verify Authentication Worked
        if response.status_code == 200:
            auth_response = response.json().get("_global_result")
            if auth_response.get("X-CSRF-Token"):
                # Bind headers to requests' session object
                self.session.headers["X-CSRF-Token"] = auth_response["X-CSRF-Token"]

            if auth_response.get("UIDARUBA"):
                self.uid_aruba = auth_response["UIDARUBA"]
            else:
                self.uid_aruba = ""
        elif response.status_code == 401:
            raise ValueError("401 Response code: Authentication Failed")
        else:
            raise ValueError(f"Authentication Failed: {response.status_code}")

    def get_request(self, relative_url, config_path="/mm/mynode", filter_obj=""):

        base_url = f"https://{self.host}:{self.api_port}/v1/configuration/"
        uid_aruba_qs = f"UIDARUBA={self.uid_aruba}"

        # Adding the UID_ARUBA query string for compatibility with 8.6.X.X
        query_string = f"?config_path={config_path}"
        if self.uid_aruba:
            query_string += f"&{uid_aruba_qs}"

        if filter_obj and isinstance(filter_obj, str):
            query_string += f"&filter={filter_obj}"
        else:
            query_string += f"&filter={json.dumps(filter_obj)}"

        full_url = f"{base_url}{relative_url}{query_string}"
        response = self.session.get(full_url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Get Request Failed: {response.status_code}")

    def show_command(self, command):

        base_url = f"https://{self.host}:{self.api_port}/v1/configuration/"
        uid_aruba_qs = f"UIDARUBA={self.uid_aruba}"

        relative_url = f"showcommand?command={command}&{uid_aruba_qs}"
        full_url = f"{base_url}{relative_url}"

        response = self.session.get(full_url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Get Request Failed: {response.status_code}")

    def logout(self):

        url = f"https://{self.host}:{self.api_port}/v1/api/logout"
        if self.uid_aruba:
            query_string = f"?UIDARUBA={self.uid_aruba}"
        else:
            query_string = ""

        full_url = f"{url}{query_string}"
        return self.session.post(full_url, verify=False)
