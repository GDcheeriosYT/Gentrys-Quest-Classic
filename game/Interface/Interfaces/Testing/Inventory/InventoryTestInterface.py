# game packages
# collection packages
import random

from Collection.Inventory.Inventory import Inventory

# config packages
from Config.NumberSetting import NumberSetting

# entity packages
from Entity.Character.Character import Character
from Entity.Artifact.Artifact import Artifact
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience

# IO packages
from IO.Input import get_int
from IO import Window

# random packages
from Random.Functions import get_random_name

# content packages
from Content.ContentManager import ContentManager

families = ContentManager().families

artifacts = []
for family in families:
    for artifact in family.artifacts:
        artifacts.append(artifact)


class InventoryTestInterface:
    def __init__(self, game_data_inventory: Inventory):
        self.inventory = game_data_inventory

    def change_money(self):
        money = NumberSetting("money", self.inventory.money, 0)
        money.change_value()
        self.inventory.money = money.value

    def add_character(self):
        self.inventory.add_item(Character("Test Character", "just a test character.", experience=Experience()))

    def add_artifact(self):
        artifact = random.choice(artifacts)
        self.inventory.add_item(artifact(StarRating(random.randint(1, 5))))

    def add_weapon(self):
        self.inventory.add_item((Weapon("Test Weapon", "just a test weapon.", experience=Experience())))

    def __repr__(self):
        while True:
            Window.clear()
            choice = get_int(
                "1. view inventory\n"
                "2. change money\n"
                "3. add character\n"
                "4. add artifact\n"
                "5. add weapon\n"
                "6. back"
            )

            if choice == 1:
                self.inventory.manage_input()

            elif choice == 2:
                self.change_money()

            elif choice == 3:
                self.add_character()

            elif choice == 4:
                self.add_artifact()

            elif choice == 5:
                self.add_weapon()

            else:
                break
