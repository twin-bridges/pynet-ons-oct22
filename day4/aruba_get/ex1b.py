from aruba_auth import auth
from my_aruba import get_request
import requests
import rich


session = requests.Session()
# host = "10.5.235.16"
host = "aruba.lasthop.io"
api_port = "4343"

uid_aruba = auth(session, host=host)
relative_url = "object/hostname"

config_path = "/mm/mynode"
data = get_request(
    session,
    host=host,
    relative_url=relative_url,
    config_path=config_path,
    uid_aruba=uid_aruba,
)
rich.print(data)
