# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.AmongUsCrewmate import AmongUsCrewmate
from .Enemies.AmongUsImposter import AmongUsImposter
from .Enemies.LiverKing import LiverKing
from .Enemies.WalterWhiteIncarnate import WalterWhiteIncarnate
from .Enemies.SaulGoodman import SaulGoodman
from .Enemies.ElonMusk import ElonMusk

class OhioCity(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Ohio")
        enemies = ItemList(content_type=Enemy)
        enemies.add(AmongUsCrewmate())
        enemies.add(AmongUsImposter())
        enemies.add(LiverKing())
        enemies.add(WalterWhiteIncarnate())
        enemies.add(SaulGoodman())
        enemies.add(ElonMusk())
        super().__init__(
            "Ohio City",
            0,
            artifact_families,
            enemies,
            False,
            True
        )
