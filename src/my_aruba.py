
def get_request(session, host, relative_url, uid_aruba, config_path="/mm/mynode", api_port="4343"):

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
