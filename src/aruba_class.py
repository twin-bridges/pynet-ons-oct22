import requests


class ArubaAPI:
    def __init__(self, host, username, password, api_port="4343"):
        self.host = host
        self.api_port = api_port
        self.username = username
        self.password = password

    def auth(self):

        self.session = requests.Session()
        http_headers = {"Content-Type": "application/json"}

        creds = f"username={self.username}&password={self.password}"
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
            return None
        elif response.status_code == 401:
            raise ValueError("401 Response code: Authentication Failed")
        else:
            raise ValueError(f"Authentication Failed: {response.status_code}")

    def get_request(self, relative_url, config_path="/mm/mynode"):

        base_url = f"https://{self.host}:{self.api_port}/v1/configuration/"
        if self.uid_aruba:
            uid_aruba_qs = f"UIDARUBA={self.uid_aruba}"

        # Adding the UID_ARUBA query string for compatibility with 8.6.X.X
        query_string = f"?config_path={config_path}"
        if self.uid_aruba:
            query_string += f"&{uid_aruba_qs}"
        full_url = f"{base_url}{relative_url}{query_string}"

        response = self.session.get(full_url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Get Request Failed: {response.status_code}")

    def show_command(self, command):

        base_url = f"https://{self.host}:{self.api_port}/v1/configuration/"
        if self.uid_aruba:
            uid_aruba_qs = f"UIDARUBA={self.uid_aruba}"
        else:
            uid_aruba_qs = ""

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
