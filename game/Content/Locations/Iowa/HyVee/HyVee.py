# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
from .Enemies.CustomerServiceManager import CustomerServiceManager
from .Enemies.Baker import Baker
from .Enemies.Butcher import Butcher
from .Enemies.Checker import Checker
from .Enemies.ChineseChef import ChineseChef
from .Enemies.CourtesyClerk import CourtesyClerk
from .Enemies.RudeCustomer import RudeCustomer
from .Enemies.Karen import Karen

from .Weapons.Carts import Carts

from Content.Characters.BenMeier import BenMeier
from Content.Characters.BraydenMesserschmidt import BraydenMesserschmidt


class HyVee(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Hyvee")
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Ben Meier")
        enemies = ItemList(content_type=Enemy)
        enemies.add(CustomerServiceManager())
        enemies.add(BraydenMesserschmidt().create_enemy(Carts))
        enemies.add(BenMeier().create_enemy(Carts))
        enemies.add(Baker())
        enemies.add(Karen())
        enemies.add(Butcher())
        enemies.add(Checker())
        enemies.add(ChineseChef())
        enemies.add(CourtesyClerk())
        enemies.add(RudeCustomer())
        super().__init__(
            "HyVee",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
