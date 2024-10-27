# game packages
# IO packages
from IO.Input import get_int, enter_to_continue

# graphics packages
from Graphics.Text.Text import Text

# collection packages
from Collection.Inventory.Inventory import Inventory

# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Character.Character import Character

# built-in packages
import random


def star_rating_sort(entity):
    return entity.star_rating.value


def length_based_sperator(length: int, seperator: str):
    string = ""
    for i in range(length):
        string += seperator

    print("\n", string, "\n")


class Gacha:
    characters = None
    weapons = None
    price = None

    def __init__(self, name: Text, characters: list, weapons: list, price: int):
        self.name = name
        self.characters = characters
        self.weapons = weapons
        self.price = price
        self.characters.sort(key=star_rating_sort, reverse=True)
        self.weapons.sort(key=star_rating_sort, reverse=True)

    def display_info(self):
        Text(f"{self.name.raw_output()} gacha details:").display()
        print(f"${self.price} for one weapon or character")
        print("\n^^^^^^Characters^^^^^^^")
        for character in self.characters:
            length_based_sperator(32, "=")
            Text(character.gacha_info_view()).display()

        print("\n^^^^^^Weapons^^^^^^^")
        for weapon in self.weapons:
            length_based_sperator(32, "=")
            Text(weapon.gacha_info_view()).display()

        enter_to_continue()

    @staticmethod
    def generate_output(objects, inventory):
        object_mapping = {}
        for object in objects:
            object_details = object.name_and_star_rating()
            if object_details not in object_mapping.keys():
                object_mapping[object_details] = 1
            else:
                object_mapping[object_details] += 1

            if isinstance(object, Weapon):
                inventory.add_item(object)

            if isinstance(object, Character):
                in_inventory = False
                for character in inventory.character_list.content:
                    if character.name == object.name:
                        in_inventory = True
                        character.add_xp(character.star_rating.value * 100)
                        character.update_server_data()

                if not in_inventory:
                    inventory.add_item(object)

        print("You got:")
        for object in object_mapping.keys():
            Text(f"{object} {object_mapping[object]}").display()

        enter_to_continue()

    def manage_input(self, inventory: Inventory):
        while True:
            choice = get_int("1. pull characters\n"
                             "2. pull weapons\n"
                             "3. view info\n"
                             "4. back")

            if choice == 1:
                objects_obtained = []
                choice2 = get_int("How many characters would you like to pull?\n")
                if inventory.can_afford(self.price * choice2):
                    inventory.money -= self.price * choice2
                    for i in range(choice2):
                        objects_obtained.append(self.pull_character())

                self.generate_output(objects_obtained, inventory)

            if choice == 2:
                objects_obtained = []
                choice2 = get_int("How many weapons would you like to pull?\n")
                if inventory.can_afford(self.price * choice2):
                    inventory.money -= self.price * choice2
                    for i in range(choice2):
                        objects_obtained.append(self.pull_weapon())

                self.generate_output(objects_obtained, inventory)

            elif choice == 3:
                self.display_info()

            else:
                break

    def get_entity_pool(self, entity_list):
        entity_pool = []
        random_value = random.randint(0, 10000)
        star_rating = 1
        if random_value <= 100:
            star_rating = 5

        elif random_value <= 500:
            star_rating = 4

        elif random_value <= 1000:
            star_rating = 3

        elif random_value <= 5000:
            star_rating = 2

        for entity in entity_list:
            if entity.star_rating.value == star_rating:
                entity_pool.append(type(entity)())

        return entity_pool

    def pull_character(self):
        while True:
            try:
                return random.choice(self.get_entity_pool(self.characters))
            except IndexError:
                pass

    def pull_weapon(self):
        while True:
            try:
                return random.choice(self.get_entity_pool(self.weapons))
            except IndexError:
                pass
