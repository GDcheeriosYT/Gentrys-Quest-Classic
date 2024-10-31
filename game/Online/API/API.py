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
    _can_check_out = True

    def __init__(self, token=None, url=None, id=None):
        API.token = token
        API.url = url
        API.id = id

    @staticmethod
    def login(username, password, do_exit: bool = True):
        API.token.verify()
        login_result = login(username, password, API.url)
        if login_result == "nope":
            WarningText("Couldn't Log In...").display(sleep=1)
            if do_exit:
                API.token.delete()
                exit(0)
            else:
                return login_result
        else:
            if login_result["status"] == "restricted":
                WarningText("Your account is currently restricted...").display(enter_prompt=True)
                API.token.delete()
                exit(0)

            elif login_result["status"] == "gqc_online":
                WarningText("You are currently logged in somewhere else...").display(enter_prompt=True)
                API.token.delete()
                exit(0)

            elif login_result["status"] == "test":
                API._can_check_out = False

            print(f"Welcome {username}!")
            API.id = login_result["id"]
            return login_result

    @staticmethod
    def get_power_level():
        return get_power_level(API.id, API.url)

    @staticmethod
    def retrieve_data():
        return requests.get(f"{API.url}/api/gqc/get-data/{API.id}").json()

    @staticmethod
    @loading_status
    def get_leaderboard(online: bool = False):
        player_list = requests.get(f"{API.url}/api/gqc/get-leaderboard/0+{int(Window.console.height - 3)}+{'true' if online else 'false'}").json()
        leaderboard = []

        ranking = 1
        for player in player_list:
            user = User(
                player[0],
                player[1],
                player[2]
            )

            user.placement = ranking
            user.ranking = player[3], player[4]

            leaderboard.append(user)
            ranking += 1

        return leaderboard

    @staticmethod
    @loading_status
    def check_in():
        requests.post(f"{API.url}/api/gqc/check-in/{API.id}")

    @staticmethod
    @loading_status
    def check_out():
        if API._can_check_out:
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
    def remove_items(id_list: list):
        return requests.post(
            f"{API.url}/api/gqc/remove-items",
            json={"items": id_list},
            headers={"Authorization": API.token.token}
        ).json()

    @staticmethod
    def update_item(id, item_json):
        if id:
            return requests.post(f"{API.url}/api/gqc/update-item/{id}", json=item_json,
                                 headers={"Authorization": API.token.token}).json()

    @staticmethod
    @loading_status
    def update_data(startup_amount: int, money: int):
        return requests.post(f"{API.url}/api/gqc/update-data/{API.id}",
                             json={
                                 'startup amount': startup_amount,
                                 'money': money
                             },
                             headers={
                                 "Authorization": API.token.token
                             }
                             )
