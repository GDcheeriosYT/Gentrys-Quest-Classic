# game packages
# graphics packages
from Graphics.Status import Status

# external packages
import requests
from rich.console import Console

# built-in packages
import time


def login(username, password, server_url):
    log_in_status = Status("Logging in", "dots")
    url = f"{server_url}/api/account/login-json"
    data = {
        'username': username,
        'password': password
    }
    try:
        log_in_status.start()
        response = requests.post(url, json=data).json()
        log_in_status.stop()
        time.sleep(1)
    except:
        log_in_status.stop()
        return "nope"

    return response
