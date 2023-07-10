from Config.ToggleSetting import ToggleSetting
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ListSetting import ListSetting


class GameSettings:
    def __init__(self):
        self.settings = [
            ToggleSetting("GPSystem inventory details", False),
            ToggleSetting("GPSystem prefer weighted", True)
        ]
