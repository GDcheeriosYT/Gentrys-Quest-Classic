# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html
import json
import os

# online packages
from rich.console import Console

# game packages
from GameData import GameData
from Game import Game

# online game packages
from Online.Server import Server
from Online.Account import AccountInfo
from Online.User.User import User

# graphic game packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Status import Status

# testing packages
from testing.TestingHandler import TestingHandler

# IO game packages
from IO.Input import *

# interface packages
from Interface.Interfaces.Login import Login

# external packages
import argparse
import atexit

# important variables
console = Console()  # the console
Window.clear()  # clear window

version = "V2.0.0"

parser = argparse.ArgumentParser(
    prog="Gentry's Quest",
    description="A game"
)

parser.add_argument("-s", "--server")
parser.add_argument("-c", "--character")
parser.add_argument("-t", "--testing", action="store_true")
args = parser.parse_args()

if os.path.isfile('ServerData.json'):
    pass
else:
    json.dump({}, open("ServerData.json", "w+"))

"""
Initializing server connection info.

Incase of someone starting this without arguments we run through try and except blocks.
If a try bock finds an exception we'll use a default value.
"""


def on_exit():
    server.API.update_data(GameData.startup_amount, GameData.inventory.money)

    # we want to delete the token last
    # we can't upload data without the token
    server.API.token.delete()


atexit.register(on_exit)

if args.testing:
    console.rule("Gentry's Quest [DEBUG MODE]")
    TestingHandler().start()
else:
    username = None
    password = None
    account_data = None
    console.rule("Gentry's Quest Classic")
    if args.server is None:
        server = Server("https://gdcheerios.com")  # default server url
    else:
        server = Server(args.server)  # make class to store server info

    while not username and not password:
        account_info = Login(server, json.load(open("ServerData.json", "r"))).visit(return_type=True)
        if isinstance(account_info, str):
            username = get_string("username")
            password = enter_password("password: ")
            account_data = server.API.login(username, password, False)
            if account_data == "nope":
                username, password = None, None
            else:
                server_data = json.load(open("ServerData.json", "r"))
                server_data[server.url].append({
                    "username": username,
                    "password": password
                })
                json.dump(server_data, open("ServerData.json", "w"))
        else:
            username = account_info.username
            password = account_info.password
            account_data = server.API.login(username, password)
            if account_data == "nope":
                username, password = None, None

    if username is not None and password is not None:
        latest_version = server.API.get_version()
        version_differs = version != latest_version
        account_info = AccountInfo(username, password)  # make class to store account info
        user_data = account_data  # game data class initialization
        user = User(user_data["id"], account_info.username)  # user class initialization
        game_data = server.API.retrieve_data()
        game_data = GameData(game_data)
        game = Game(version)
        if version_differs:
            WarningText("You are not on the right Gentry's Quest version!\n"
                        f"Your version: {version}\n"
                        f"latest: {latest_version}\n"
                        "You will not be able to use online features...\n"
                        "You can get the latest version from [link=https://gdcheerios.com/gentrys-quest]https://gdcheerios.com/gentrys-quest[/link].").display()
            enter_to_continue()
            server.API.check_out()
            server.disable()

        game.start(args.character)
