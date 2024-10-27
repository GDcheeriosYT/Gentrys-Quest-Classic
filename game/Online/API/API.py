# online game packages
# external packages
import time

import requests

# graphics game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Status import loading_status
# io game packages
from IO import Window
from .GetPowerLevel import get_power_level
from .Login import login
from .RecievePlayer import receive_player
from ..User.User import User


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
        API.token = token
        API.url = url
        API.id = id

    def login(self, username, password, do_exit: bool = True):
        API.token.verify()
        login_result = login(username, password, API.url)
        if login_result == "nope":
            WarningText("Couldn't Log In...").display()
            time.sleep(1)
            if do_exit:
                API.token.delete()
                exit(0)
            else:
                return login_result
        else:
            API.id = login_result["id"]
            return login_result

    @staticmethod
    def get_power_level():
        return get_power_level(API.id, API.url)

    @staticmethod
    def retrieve_data():
        return requests.get(f"{API.url}/api/gqc/get-data/{API.id}").json()

    @staticmethod
    def get_online_players():
        player_list: dict = requests.get(f"{API.url}/api/gq/get-online-players").json()
        online_players = []
        for id in player_list.keys():
            user = User(int(id), player_list[id]["username"], player_list[id]["power level"]["weighted"])
            user.placement = player_list[id]["placement"]
            user.ranking = player_list[id]["ranking"]["rank"], player_list[id]["ranking"]["tier"]
            online_players.append(user)

        def sort_thing(user: User):
            return user.placement

        online_players.sort(key=sort_thing)
        return online_players

    @staticmethod
    def get_leaderboard():
        player_list: dict = requests.get(f"{API.url}/api/gq/get-leaderboard/0+{int(Window.console.height - 3)}").json()
        leaderboard = []

        for id in player_list.keys():
            user = User(int(id), player_list[id]["username"], player_list[id]["power level"]["weighted"])
            user.placement = player_list[id]["placement"]
            user.ranking = player_list[id]["ranking"]["rank"], player_list[id]["ranking"]["tier"]
            leaderboard.append(user)

        def sort_thing(user: User):
            return user.placement

        leaderboard.sort(key=sort_thing)
        return leaderboard

    @staticmethod
    def check_out():
        requests.post(f"{API.url}/api/gq/check-out/{API.id}")

    @staticmethod
    def get_version():
        return requests.get(f"{API.url}/api/gqc/get-version").text

    @staticmethod
    def receive_player(username_or_id):
        return receive_player(username_or_id, API.url)

    @staticmethod
    def add_item(item_type: str, item_json):
        if API.id:
            return requests.post(f"{API.url}/api/gqc/add-item/{item_type}+{API.id}", json=item_json,
                                 headers={"Authorization": API.token.token}).json()

    @staticmethod
    def remove_item(id):
        if id:
            return requests.post(f"{API.url}/api/gqc/remove-item/{id}",
                                 headers={"Authorization": API.token.token}).json()

    @staticmethod
    def update_item(id, item_json):
        if id:
            return requests.post(f"{API.url}/api/gqc/update-item/{id}", json=item_json,
                                 headers={"Authorization": API.token.token}).json()

    @staticmethod
    @loading_status
    def update_data(startup_amount: int, money: int):
        return requests.post(f"{API.url}/api/gqc/update-data/{API.id}", json={
            'startup amount': startup_amount,
            'money': money
        },
                      headers={"Authorization": API.token.token}
                      ).json()
