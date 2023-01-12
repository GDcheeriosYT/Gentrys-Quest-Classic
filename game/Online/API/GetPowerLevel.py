# game packages

# external packages
import requests


def get_power_level(id, server_url):
    try:
        return int(requests.get(f"{server_url}/api/gq/get-power-level/{id}").content)
    except ValueError:
        return 0
