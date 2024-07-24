# game packages
# graphics packages

from Graphics.Content.Text.WarningText import WarningText
from Graphics.Status import Status

# external packages
import requests

# built-in packages
import time


class Token:
    """
    Token for api calling

    parameters

    url : string
        the url for managing token
    """

    url = None
    token = None

    def __init__(self, url):
        self.url = url
        token_status = Status("Generating token", "dots8Bit")
        token_status.start()
        time.sleep(1)
        self.token = requests.get(f"{url}/api/generate-token").text
        token_status.stop()

    def delete(self):
        requests.post(f"{self.url}/api/delete-token/{self.token}")

    def verify(self):
        if requests.get(f"{self.url}/api/verify-token/{self.token}").text == "False":
            WarningText("Couldn't verify token").display()
            self.delete()
            exit(0)
