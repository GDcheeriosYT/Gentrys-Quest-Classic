# built-in packages
import json
import time

from Entity.Character.Character import Character
# graphics packages
from Graphics.Status import Status

# content packages
from Content.Settings.GameSettings import GameSettings
from Content.ContentManager import ContentManager
from Collection.Inventory.Inventory import Inventory

# config packages
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ToggleSetting import ToggleSetting


class GameData:
    """
    returns a GameData object with the given json string

    parameters

    json_string: string
        the game data json string
    """

    inventory = None
    startup_amount = None
    settings = None
    content = None

    def __init__(self, json_data):
        self.content = ContentManager()
        if json_data:
            status = Status(text="Loading data")
            status.start()

            self.startup_amount = json_data["startup amount"]
            money = json_data["money"]

            status.live_change("Loading items")

            characters = []
            artifacts = []
            weapons = []

            for item in json_data["items"]:
                if item[1] == "character":
                    characters.append(item)
                elif item[1] == "artifact":
                    artifacts.append(item)
                elif item[1] == "weapon":
                    weapons.append(item)

            self.inventory = Inventory(money, characters, weapons, artifacts)
            status.stop()
        else:
            self.startup_amount = 0
            self.inventory = Inventory()

    def obtain(self):
        return self.inventory, self.startup_amount, self.settings

    def jsonify(self):
        return {
            "startupamount": self.startup_amount,
            "settings": {},
            "inventory": self.inventory.jsonify()
        }
