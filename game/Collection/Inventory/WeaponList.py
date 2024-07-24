# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating

# collection packages
from ..Handlers.BuffArrayHandler import BuffArrayHandler
from ..Handlers.ExperienceObjectHandler import ExperienceObjectHandler
from ..ItemList import ItemList

# graphics packages
from Graphics.Status import Status
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int

# built-in packages
import time


class WeaponList:
    """
    Makes a list of weapons

    parameters:
    weapons: list
        the list of weapons
    """

    weapons = None

    def __init__(self, weapons=[]):
        load_data_status = Status("Loading your weapon data", "dots")
        load_data_status.start()
        self.weapons = []
        for weapon in weapons:
            id = weapon[0]  # id
            weapon = weapon[2]  # json data
            experience = weapon["experience"]
            stats = weapon["stats"]
            verbs = weapon["verbs"]
            verbs = Verbs(verbs["normal"], verbs["critical"])
            new_weapon = Weapon(
                weapon["name"],
                weapon["description"],
                weapon["weapon type"],
                weapon["stats"]["attack"],
                BuffArrayHandler(weapon["stats"]["buff"]).create_buff(),
                Verbs(weapon["verbs"]["normal"], weapon["verbs"]["critical"]),
                StarRating(weapon["star rating"]),
                ExperienceObjectHandler(weapon["experience"]).create_experience()
            )
            new_weapon.id = id
            self.weapons.append(new_weapon)
            # time.sleep(0.1)
        load_data_status.stop()

    def give_item_list(self):
        return ItemList(content_type=Weapon, content=self.weapons)
