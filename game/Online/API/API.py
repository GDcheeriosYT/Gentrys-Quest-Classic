# online game packages
from .Login import login
from .UploadData import upload_data
from .GetPowerLevel import get_power_level
from ..User.User import User

# graphics game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText

# external packages
import time
import requests

class API:
    """
    makes a class that handles all the api calls

    token: string
        token used for authenticating api calls
    """

    token = None
    url = None
    id = None

    def __init__(self, token=None, url=None, id=None):
        self.token = token
        self.url = url
        self.id = id

    def login(self, username, password):
        self.token.verify()
        login_result = login(username, password, self.url)
        if login_result == "nope":
            WarningText("Couldn't Log In...").display()
            time.sleep(1)
            self.token.delete()
            exit(0)
        else:
            self.id = login_result["id"]
            requests.post(f"{self.url}/api/gq/check-in/{self.id}")
            return login_result

    def upload_data(self, data):
        upload_data(self.url, self.id, data, self.token.token)

    def get_power_level(self):
        return get_power_level(self.id, self.url)

    def get_online_players(self):
        player_list: dict = requests.get(f"{self.url}/api/gq/get-online-players").json()
        online_players = []
        for id in player_list.keys():
            user = User(int(id), player_list[id]["username"], player_list[id]["power level"])
            user.ranking = player_list[id]["ranking"]
            online_players.append(user)

        return online_players

    def check_out(self):
        requests.post(f"{self.url}/api/gq/check-out/{self.id}")

