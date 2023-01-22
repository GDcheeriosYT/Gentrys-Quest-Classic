from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience
from Entity.Weapon.Weapon import Weapon
from Entity.Artifact.Artifact import Artifact

from Graphics.Text.Text import Text

from Random.Functions import get_random_name

from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

from Collection.ItemList import ItemList

from IO import Window


class TestCharacterInterface:
    character = None
    settings = None

    def __init__(self):
        name = get_random_name()
        self.character = Character(name, weapon=Weapon())

    def __repr__(self):
        self.character.test()
        return self
