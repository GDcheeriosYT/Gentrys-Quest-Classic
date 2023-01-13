# game packages
# story packages
from Story.Story import Story

# collection packages
from Collection.ItemList import ItemList

# location packages
from Location.BattleArea.BattleArea import BattleArea

# entity packages
from Entity.Enemy.Enemy import Enemy
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.Buff import Buff
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating
from Entity.Stats.StatTypes import StatTypes

# content packages
from Content.Gachas.BaseGacha import BaseGacha

# gacha packages
from Gacha.GachaEvent import GachaEvent

# built-in packages
import random


class GentrysQuest(Story):
    def __init__(self):
        super().__init__(
            [
                "You find yourself out on a journey",
                ""
            ]
        )