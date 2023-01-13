# list of colors https://rich.readthedocs.io/en/stable/appendix/colors.html

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
from IO import Window

# built-in packages
import sys
import time
import os
import atexit

# external packages
import argparse

# important variables
console = Console()  # the console
Window.clear()  # clear window

version = "V1.0.0"

parser = argparse.ArgumentParser(
    prog="Gentry's Quest",
    description="A game"
)

parser.add_argument("-u", "--username")
parser.add_argument("-p", "--password")
parser.add_argument("-s", "--server")
parser.add_argument("-c", "--character")
args = parser.parse_args()

debug_mode = False
if args.username is None:
    debug_mode = True

"""
Initializing server connection info.

Incase of someone starting this without arguments we run through try and except blocks.
If a try bock finds an exception we'll use a default value.
"""

if debug_mode:
    console.rule("Gentry's Quest [DEBUG MODE]")
    TestingHandler().start()
else:
    console.rule("Gentry's Quest")
    WarningText("No argument for server!\n").display()
    InfoText("Defaulting to https://gdcheerios.com\n").display()
    if args.server is None:
        server = Server("https://gdcheerios.com")  # default server url
    else:
        server = Server(args.server)  # make cl ass to store server info
    if args.username is not None and args.password is not None:
        account_info = AccountInfo(args.username, args.password)  # make class to store account info
        user_data = server.API.login(account_info.username, account_info.password)  # game data class initialization
        user = User(user_data["id"], account_info.username, server.API.get_power_level())  # user class initialization
        game_data = GameData(user_data["metadata"]["Gentry's Quest data"])
        game = Game(game_data, version, server)
        def byebye():
            game_status = Status("Uploading data...")
            game_status.start()
            server.API.upload_data(game.game_data)
            server.API.check_out()
            server.API.token.delete()
            game_status.stop()

        atexit.register(byebye)
        game.start(args.character)