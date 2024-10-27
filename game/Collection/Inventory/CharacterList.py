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

# content packages
from Content.ContentManager import ContentManager

# IO packages
from IO.Input import get_int

# built-in packages
import time

# vars

content = ContentManager()


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
            id = character[0]  # id
            character_data = character[2]  # json data
            artifact_list = ItemList(5, Artifact, True)
            experience = character_data["experience"]
            equips = character_data["equips"]
            for artifact in equips["artifacts"]:
                artifact_list.add(ArtifactObjectHandler(artifact).create_artifact())
            stat_points = character_data["stats"]
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
                character_data["name"],
                character_data["description"],
                StarRating(character_data["star rating"]),
                ExperienceObjectHandler(experience).create_experience(),
                weapon,
                artifact_list,
                stat_points["health"],
                stat_points["attack"],
                stat_points["defense"],
                stat_points["critRate"],
                stat_points["critDamage"]
            )
            new_character.id = id
            self.characters.append(new_character)
            # time.sleep(0.1)

        load_data_status.stop()

    def give_item_list(self):
        return ItemList(content_type=Character, content=self.characters)
