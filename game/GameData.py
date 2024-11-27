# built-in packages

from Collection.Inventory.Inventory import Inventory
# content packages
from Content.ContentManager import ContentManager
# graphics packages
from Graphics.Status import Status
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# collection packages
from Collection.ItemList import ItemList

# IO packages
from IO.Input import *

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

    def __init__(self, json_data=None):
        GameData.content = ContentManager()
        if json_data:
            status = Status(text="Loading data")
            status.start()

            GameData.startup_amount = json_data["startup amount"]
            money = json_data["money"]
            new_money = json_data["new money"]

            received_new = False

            if new_money > 0:
                received_new = True
                money += new_money

            status.live_change("Loading items")

            characters = []
            artifacts = []
            weapons = []
            new_items = []

            # 0 id
            # 1 type
            # 2 metadata
            # 3 is_new

            for item in json_data["items"]:
                if item[3]:
                    received_new = True
                    new_items.append(item[0])

                if item[1] == "character":
                    characters.append(item)
                elif item[1] == "artifact":
                    artifacts.append(item)
                elif item[1] == "weapon":
                    weapons.append(item)

            GameData.inventory = Inventory(money, characters, weapons, artifacts)
            status.stop()

            if received_new:
                new_characters = []
                new_artifacts = []
                new_weapons = []

                for character in GameData.inventory.character_list.content:
                    if character.id in new_items:
                        new_characters.append(character)

                for artifact in GameData.inventory.artifact_list.content:
                    if artifact.id in new_items:
                        new_artifacts.append(artifact)

                for weapon in GameData.inventory.weapon_list.content:
                    if weapon.id in new_items:
                        new_weapons.append(weapon)

                print("You have received:")
                if new_money > 0:
                    print(f"${new_money}")

                items = new_characters + new_artifacts + new_weapons
                i = 1
                for item in items:
                    Text("[gold1 on black] *New*\t[white on black]" + item.list_view(i)).display()
                    i += 1

                enter_to_continue()

                for item in items:
                    item.update_server_data()

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
