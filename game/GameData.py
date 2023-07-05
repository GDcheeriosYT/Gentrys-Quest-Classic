# built-in packages
import json
import time

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
        game_settings = GameSettings().settings
        self.content = ContentManager()
        if json_data is None:
            data = {
                "startupamount": 0,
                "settings": {},
                "inventory": {
                    "characters": [],
                    "artifacts": [],
                    "weapons": [],
                    "money": 0
                }
            }
            self.inventory = Inventory(data["inventory"])
            self.startup_amount = data["startupamount"]
            config_status = Status("Loading config data", "dots")
            config_status.start()
            self.settings = []
            for game_setting in game_settings:
                self.settings.append(game_setting)
                time.sleep(0.1)

            config_status.stop()
        else:
            json_object = json_data
            self.inventory = Inventory(json_object["inventory"])
            self.startup_amount = json_object["startupamount"]
            config_status = Status("Loading config data", "dots")
            config_status.start()
            self.settings = []
            for setting in json_object["settings"]:
                key = setting
                value = json_object["settings"][key]
                for game_setting in game_settings:
                    if game_setting.name == key:
                        if isinstance(value, bool):
                            self.settings.append(ToggleSetting(key, value))
                        elif isinstance(value, int):
                            self.settings.append(NumberSetting(key, value))
                        else:
                            self.settings.append(StringSetting(key, value))

            game_setting_names = []
            loaded_setting_names = []

            for setting in self.settings:
                loaded_setting_names.append(setting.name)

            for setting in game_settings:
                game_setting_names.append(setting.name)

            for game_setting_name in game_setting_names:
                if game_setting_name not in loaded_setting_names:
                    self.settings.append(game_settings[game_setting_names.index(game_setting_name)])

                time.sleep(0.1)
            config_status.stop()

    def obtain(self):
        return self.inventory, self.startup_amount, self.settings

    def jsonify(self):
        return {
            "startupamount": self.startup_amount,
            "settings": {},
            "inventory": self.inventory.jsonify()
        }
