# game packages
# graphics packages
from Graphics.Status import Status

# external packages
import requests

# built-in packages
import json


def receive_player(username_or_id, server_url):
    find_player_status = Status("Finding player")
    find_player_status.start()
    result = requests.get(f"{server_url}/api/account/grab/{username_or_id}").text
    find_player_status.stop()

    if result != "Not Found":
        result = json.loads(result)

    return result
