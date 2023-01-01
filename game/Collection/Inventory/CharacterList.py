# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating

# collection packages
from ..Handlers.BuffArrayHandler import BuffArrayHandler
from ..Handlers.ExperienceObjectHandler import ExperienceObjectHandler
from ..ItemList import ItemList
from ..Handlers.ArtifactObjectHandler import ArtifactObjectHandler

# graphics packages
from Graphics.Status import Status
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int

# built-in packages
import time


class CharacterList:
    """
    Makes a list of characters

    parameters:
    characters: list
        the list of characters
    """

    characters = None

    def __init__(self, characters=[]):
        load_data_status = Status("Loading your character data", "dots")
        load_data_status.start()
        self.characters = []
        for character in characters:
            artifact_list = ItemList(5, Artifact, True)
            experience = character["experience"]
            equips = character["equips"]
            for artifact in equips["artifacts"]:
                artifact_list.add(ArtifactObjectHandler(artifact).create_artifact())
            stat_points = character["stats"]
            try:
                weapon = equips["weapon"]
                weapon = Weapon(
                    weapon["name"],
                    weapon["description"],
                    weapon["weapon type"],
                    weapon["stats"]["attack"],
                    BuffArrayHandler(weapon["stats"]["buff"]).create_buff(),
                    Verbs(weapon["verbs"]["normal"], weapon["verbs"]["critical"]),
                    StarRating(weapon["star rating"]),
                    ExperienceObjectHandler(weapon["experience"]).create_experience()
                )
            except KeyError:
                weapon = None
            except TypeError:
                weapon = None
            new_character = Character(
                character["name"],
                character["description"],
                StarRating(character["star rating"]),
                ExperienceObjectHandler(experience).create_experience(),
                weapon,
                artifact_list,
                stat_points["health"],
                stat_points["attack"],
                stat_points["defense"],
                stat_points["critRate"],
                stat_points["critDamage"]
            )
            self.characters.append(new_character)
            # time.sleep(0.1)

        load_data_status.stop()

    def give_item_list(self):
        return ItemList(content_type=Character, content=self.characters)
