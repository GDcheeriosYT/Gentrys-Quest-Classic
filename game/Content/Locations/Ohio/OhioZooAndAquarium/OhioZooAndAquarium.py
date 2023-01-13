# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.HarambesCousin import HarambesCousin
from .Enemies.FishNamedBryan import FishNamedBryan
from .Enemies.BabyDragon import BabyDragon
from .Enemies.WinstonOW import WinstonOW
from .Enemies.RacoonWith45 import RacoonWith45


class OhioZooAndAquarium(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Ohio")
        enemies = ItemList(content_type=Enemy)
        enemies.add(HarambesCousin())
        enemies.add(FishNamedBryan())
        enemies.add(BabyDragon())
        enemies.add(WinstonOW())
        enemies.add(RacoonWith45())
        super().__init__(
            "Ohio's Zoo and Aquarium",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
