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

    def __init__(self, url="https://gdcheerios.com", fallback_url="http://gdcheerios.com"):
        self.url = url
        self.disabled = False
        server_status = Status("connecting to server", "point")
        try:
            server_status.start()
            requests.get(self.url)
        except:
            server_status.stop()
            WarningText(f"Couldn't connect to server({self.url})...").display()
            time.sleep(1)
            InfoText("Trying fallback server").display()
            time.sleep(1)
            self.url = fallback_url
            try:
                server_status.stop()
                requests.get(self.url)
            except:
                exit(1)
        server_status.stop()
        self.API = API(Token(self.url), self.url)

    def disable(self):
        self.url = None
        self.API = None
        self.disabled = True