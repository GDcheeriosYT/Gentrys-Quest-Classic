from game.Config.ToggleSetting import ToggleSetting
from game.Config.NumberSetting import NumberSetting
from game.Config.StringSetting import StringSetting


class GameSettings:
    debug = ToggleSetting("debug", False)
    timeout = ToggleSetting("timeout", False)