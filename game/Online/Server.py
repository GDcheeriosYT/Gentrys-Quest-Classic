# online game packages
import time

from .API.API import API
from .API.Token import Token

# built-in packages
import requests

# graphics game content
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Status import Status


class Server:
    url = None
    disabled = None

    def __init__(self, url=None):
        Server.url = url
        if url:
            Server.disabled = False
            server_status = Status("connecting to server", "point")
            try:
                server_status.start()
                requests.get(self.url)
            except:
                server_status.stop()
                WarningText(f"Couldn't connect to server({self.url})...").display(sleep=2)
                exit(1)
            server_status.stop()
            API.token = Token(self.url)
            API.url = self.url
        else:
            self.disable()

    @staticmethod
    def disable():
        API.disabled = True
        Server.disabled = True

    @staticmethod
    def get_api():
        # sometimes the api is not initialized yet,
        return API
