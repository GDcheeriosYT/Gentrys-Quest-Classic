# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# enemy packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.RileyReid import RileyReid


class PureTabooSet(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Mason James")
        enemies = ItemList(content_type=Enemy)
        enemies.add(RileyReid())
        super().__init__(
            "Pure Taboo Set",
            1,
            artifact_families,
            enemies,
            one_enemy=True
        )