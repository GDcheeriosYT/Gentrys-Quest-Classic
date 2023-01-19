# online game packages
from .API.API import API
from .API.Token import Token

# built-in packages
import requests

# graphics game content
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Status import Status


class Server:
    url = None
    API = None
    disabled = None

    def __init__(self, url="https://gdcheerios.com"):
        self.url = url
        self.disabled = False
        server_status = Status("connecting to server", "point")
        try:
            server_status.start()
            requests.get(url)
        except:
            server_status.stop()
            WarningText("Couldn't connect to server...").display()
            exit(1)
        server_status.stop()
        self.API = API(Token(url), self.url)

    def disable(self):
        self.url = None
        self.API = None
        self.disabled = True