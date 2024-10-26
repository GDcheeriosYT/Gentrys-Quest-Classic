# built-in packages

from Collection.Inventory.Inventory import Inventory
# content packages
from Content.ContentManager import ContentManager
# graphics packages
from Graphics.Status import Status


# config packages


class GameData:
    """
    returns a GameData object with the given json string

    parameters

    json_string: string
        the game data json string
    """

    inventory = None
    startup_amount = None
    settings = None
    content = None

    def __init__(self, json_data):
        GameData.content = ContentManager()
        if json_data:
            status = Status(text="Loading data")
            status.start()

            GameData.startup_amount = json_data["startup amount"]
            money = json_data["money"]

            status.live_change("Loading items")

            characters = []
            artifacts = []
            weapons = []

            # 0 id
            # 1 type
            # 2 metadata

            for item in json_data["items"]:
                if item[1] == "character":
                    characters.append(item)
                elif item[1] == "artifact":
                    artifacts.append(item)
                elif item[1] == "weapon":
                    weapons.append(item)

            # look for duplications
            # for character in characters:
            #     for artifact in character[2]["equips"]["artifacts"]:
            #     for artifact in chara


            GameData.inventory = Inventory(money, characters, weapons, artifacts)
            status.stop()
        else:
            GameData.startup_amount = 0
            GameData.inventory = Inventory()

    @staticmethod
    def jsonify():
        return {
            "startup amount": GameData.startup_amount,
            "settings": {},
            "inventory": GameData.inventory.jsonify()
        }
