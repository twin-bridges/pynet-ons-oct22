import requests
import rich
from aruba_auth import auth


def show_command(session, host, command, api_port=4343, uid_aruba=""):

    base_url = f"https://{host}:{api_port}/v1/configuration/showcommand"
    query_string = f"?command={command}"
    if uid_aruba:
        query_string += f"&UIDARUBA={uid_aruba}"

    full_url = f"{base_url}{query_string}"
    return session.get(full_url, verify=False)


if __name__ == "__main__":
    host = "aruba.lasthop.io"
    api_port = "4343"

    session = requests.Session()
    session.headers["Accept"] = "application/json"

    uid_aruba = auth(session, host=host, api_port=api_port)

    command = "show+configuration+node-hierarchy"
    response = show_command(session, host=host, command=command, uid_aruba=uid_aruba)
    data = response.json()
    rich.print(data)
