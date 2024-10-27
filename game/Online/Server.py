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
    API = None
    disabled = None

    def __init__(self, url="https://gdcheerios.com"):
        Server.url = url
        Server.disabled = False
        server_status = Status("connecting to server", "point")
        try:
            server_status.start()
            time.sleep(1)
            requests.get(self.url)
        except:
            server_status.stop()
            WarningText(f"Couldn't connect to server({self.url})...").display()
            time.sleep(1)
            try:
                server_status.stop()
                requests.get(self.url)
            except:
                exit(1)
        server_status.stop()
        Server.API = API(Token(self.url), self.url)

    @staticmethod
    def disable():
        Server.url = None
        Server.API = None
        Server.disabled = True

    @staticmethod
    def get_api():
        # sometimes the api is not initialized yet,
        return API
