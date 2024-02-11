# game packages
# collection packages
from .ArtifactList import ArtifactList
from .CharacterList import CharacterList
from .WeaponList import WeaponList

# graphics packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int
from IO.Window import clear

# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Weapon.Weapon import Weapon

# config packages
from Config.ListSetting import ListSetting
from Config.ToggleSetting import ToggleSetting

# built-in packages
from copy import deepcopy

# external packages
from GPSystem.GPmain import GPSystem


class Inventory:
    """
    Holds all the users owned items

    returns an Inventory

    parameters

    inventory_data: json object
        data used to construct inventory
    """

    inventory_data = None
    character_list = None
    artifact_list = None
    weapon_list = None
    money = None

    def __init__(self, inventory_data):
        if inventory_data is None:
            inventory_data = {
                "money": 0,
                "characters": [],
                "weapons": [],
                "artifacts": []
            }

        self.money = inventory_data["money"]
        self.character_list = CharacterList(inventory_data["characters"]).give_item_list()
        self.weapon_list = WeaponList(inventory_data["weapons"]).give_item_list()
        self.artifact_list = ArtifactList(inventory_data["artifacts"]).give_item_list()
        self.sort_type = ListSetting("sort", "Star Rating", [
            "Star Rating",
            "Level",
            "Name"
        ])
        self.reverse_sort = ToggleSetting("Reverse Sort", True)

    def upgrade(self):
        pass

    def manage_input(self, equipped_character=None):
        def is_not_empty(list, string):
            if len(list) != 0:
                return True
            else:
                WarningText(f"You don't have any {string}s").display()

        while True:
            try:
                num = get_int(self.__repr__())
                if num == 1:
                    if is_not_empty(self.character_list.content, "character"):
                        selection = self.character_list.select(remove=False)
                        if selection != "":
                            equipped_character = self.manage_character(selection)

                elif num == 2:
                    if is_not_empty(self.weapon_list.content, "weapon"):
                        self.manage_weapon(self.weapon_list.select(remove=False))
                elif num == 3:
                    if is_not_empty(self.artifact_list.content, "artifact"):
                        self.manage_artifact(self.artifact_list.select(remove=False))
                elif num == 4:
                    if is_not_empty(self.artifact_list.content, "artifact"):
                        while True:
                            selections = self.artifact_list.select(False, list_content=True)
                            if selections is None:
                                pass

                            elif isinstance(selections, list):
                                for artifact_index in selections:
                                    self.money += int(self.exchange_artifact(self.artifact_list.get(artifact_index), True) / 5)

                                break


                elif num == 5:
                    self.sort_type.select()
                    self.sort_things()
                    clear()
                elif num == 6:
                    self.reverse_sort.toggle_setting()
                    self.sort_things()
                    clear()
                else:
                    break
            except IndexError:
                break

        return equipped_character

    def sort_things(self):
        if self.sort_type.selected_value == "Star Rating":
            self.character_list.content = sorted(self.character_list.content, key=lambda x: x.star_rating.value, reverse=self.reverse_sort.toggled)
            self.weapon_list.content = sorted(self.weapon_list.content, key=lambda x: x.star_rating.value, reverse=self.reverse_sort.toggled)
            self.artifact_list.content = sorted(self.artifact_list.content, key=lambda x: x.star_rating.value, reverse=self.reverse_sort.toggled)

        elif self.sort_type.selected_value == "Level":
            self.character_list.content = sorted(self.character_list.content, key=lambda x: x.experience.level, reverse=self.reverse_sort.toggled)
            self.weapon_list.content = sorted(self.weapon_list.content, key=lambda x: x.experience.level, reverse=self.reverse_sort.toggled)
            self.artifact_list.content = sorted(self.artifact_list.content, key=lambda x: x.experience.level, reverse=self.reverse_sort.toggled)

        else:
            self.character_list.content = sorted(self.character_list.content, key=lambda x: x.name, reverse=self.reverse_sort.toggled)
            self.weapon_list.content = sorted(self.weapon_list.content, key=lambda x: x.name, reverse=self.reverse_sort.toggled)
            self.artifact_list.content = sorted(self.artifact_list.content, key=lambda x: x.name, reverse=self.reverse_sort.toggled)

    def can_afford(self, amount):
        if self.money >= amount:
            return True
        else:
            WarningText("You can not afford this").display()
            return False

    def level_up_prompt(self, entity):
        while True:
            money = get_int(f"lvl {entity.experience.display_level()}\n"
                            f"xp {entity.experience.display_xp()}/{entity.experience.get_xp_required(entity.star_rating.value)}xp\n"
                            f"${self.money}/${entity.get_money_required()}\n"
                            "$1 = 10xp\n"
                            "0 to go back")

            if money == 0:
                break

            if self.can_afford(money):
                self.money -= money
                entity.add_xp(money * 10)

    def exchange_artifact(self, artifact: Artifact, remove: bool = True):
        star_rating = artifact.star_rating.value
        level = artifact.experience.level
        if remove:
            self.artifact_list.content.remove(artifact)
        return int((level * star_rating) * 100)

    def exchange_weapon(self, weapon: Weapon, remove: bool = True):
        star_rating = weapon.star_rating.value
        level = weapon.experience.level
        if remove:
            self.weapon_list.content.remove(weapon)
        return int((level * star_rating) * 100)

    def manage_artifact(self, artifact: Artifact, is_equipped=False):
        while True:
            if artifact is None:
                artifact = self.swap_artifact(artifact)
                return artifact
            elif artifact == "":
                break

            Text(artifact).display()
            choice = get_int(f"1. switch artifact{'' if is_equipped else '(Not equipped)'}\n"
                             f"2. remove artifact{'' if is_equipped else '(Not equipped)'}\n"
                             "3. upgrade artifact\n"
                             "4. back")

            if choice == 1:
                if is_equipped:
                    artifact = self.swap_artifact(artifact)

            elif choice == 2:
                if is_equipped:
                    self.artifact_list.add(artifact)
                    return None

            elif choice == 3:
                if artifact.experience.level != artifact.experience.limit:
                    if not is_equipped:
                        self.artifact_list.content.remove(artifact)

                    while True:
                        self.artifact_list.list_content()
                        InfoText("\n\nartifact after level up:\n\n").display()
                        artifact_copy: Artifact = deepcopy(artifact)

                        for item in self.artifact_list.get_selections():
                            artifact_copy.add_xp(self.exchange_artifact(item, False), False)

                        Text(artifact_copy.name_and_star_rating()).display()
                        Text(f"{artifact_copy.experience.display_level()} {artifact_copy.experience.display_xp()}/{artifact_copy.experience.get_xp_required(artifact_copy.star_rating.value)} xp").display()
                        Text(f"+{int(int(artifact_copy.experience.level/4) - int(artifact.experience.level/4))} attributes").display()

                        inp = self.artifact_list.select(False, list_content=False)

                        if inp is None:
                            break

                        elif isinstance(inp, list):
                            counter = 0
                            while counter < len(inp):
                                artifact.add_xp(self.exchange_artifact(self.artifact_list.get(inp[counter])))
                                inp = [x - 1 for x in inp]
                                counter += 1

                                if artifact.experience.level == artifact.experience.limit:
                                    break

                            break

                    if not is_equipped:
                        self.artifact_list.add(artifact)  # adds the artifact back

                else:
                    WarningText("Artifact is max level!").display()
            else:
                break

        return artifact

    def upgrade_weapon(self, weapon):
        is_equipped = not weapon in self.weapon_list.content
        choice2 = get_int("1. with money\n"
                          "2. with weapons\n"
                          "3. back\n")
        if choice2 == 1:
            self.level_up_prompt(weapon)

        elif choice2 == 2:
            if not is_equipped:
                self.weapon_list.content.remove(weapon)

            while True:
                self.weapon_list.list_content()
                InfoText("\n\nweapon after level up:\n\n").display()
                weapon_copy: Weapon = deepcopy(weapon)
                weapon_copy.display_info = False

                for item in self.weapon_list.get_selections():
                    weapon_copy.add_xp(self.exchange_weapon(item, False))

                Text(weapon_copy.name_and_star_rating()).display()
                Text(f"attack: {weapon_copy.attack}").display()
                Text(f"{weapon_copy.experience.display_level()} {weapon_copy.experience.display_xp()}/{weapon_copy.experience.get_xp_required(weapon_copy.star_rating.value)} xp").display()
                print("\n")

                inp = self.weapon_list.select(False, list_content=False)
                if inp is None:
                    break

                elif isinstance(inp, list):
                    counter = 0
                    while counter < len(inp):
                        weapon.add_xp(self.exchange_weapon(self.weapon_list.get(inp[counter])))
                        inp = [x - 1 for x in inp]
                        counter += 1

                    break

            if not is_equipped:
                self.weapon_list.add(weapon)  # adds the weapon back

    def manage_weapon(self, weapon):
        while True:
            if weapon is None or weapon == "":
                break

            Text(weapon).display()
            choice = get_int("1. level up\n"
                             "2. back\n")

            if choice == 1:
                self.upgrade_weapon(weapon)

            else:
                break

    def manage_character(self, character):
        while True:
            if character is None:
                break
            character.update_stats()
            choice = character.get_option()
            if choice == 1:
                self.level_up_prompt(character)

            elif choice == 2:
                if character.weapon is None:
                    self.swap_weapon(character)

                while character.weapon is not None:
                    Text(character.weapon).display()
                    choice = get_int("1. level up\n"
                                     "2. swap weapon\n"
                                     "3. remove weapon\n"
                                     "4. back\n")

                    if choice == 1:
                        self.upgrade_weapon(character.weapon)

                    elif choice == 2:
                        self.swap_weapon(character)
                        character.update_stats()

                    elif choice == 3:
                        self.weapon_list.add(character.weapon)
                        character.weapon = None

                    else:
                        break

            elif choice == 3:
                for artifact_index in range(5):
                    artifact = character.artifacts.get(artifact_index)
                    Text(f"{artifact_index + 1}. {artifact.list_view() if artifact is not None else 'empty'}").display()
                choice2 = get_int("6. back")
                if choice2 < 6:
                    character.artifacts.set(choice2 - 1,
                                            self.manage_artifact(character.artifacts.get(choice2 - 1), True), True)
                    character.update_stats()

            elif choice == 4:
                return character

            else:
                break

    def swap_artifact(self, artifact_to_swap):
        selection = self.artifact_list.select()

        if selection != "":
            artifact = selection

            if artifact_to_swap is not None:
                self.artifact_list.add(artifact_to_swap)

            return artifact

    def swap_weapon(self, character):
        if self.weapon_list.get_length() == 0:
            WarningText("You have no weapons to swap...").display()

        else:
            character_weapon = character.weapon
            selection = self.weapon_list.select()

            if selection != "":
                character.weapon = selection

                if character_weapon is not None:
                    self.weapon_list.add(character_weapon)

                if character.weapon is not None:
                    Text(f"You have equipped {character.weapon.name}").display()

    def jsonify(self):
        return {
            "artifacts": self.artifact_list.jsonify(),
            "weapons": self.weapon_list.jsonify(),
            "characters": self.character_list.jsonify(),
            "money": self.money
        }

    def format_length(self, number):
        if number >= 1000:
            return f"{int(number / 1000)}k"
        return number

    def __repr__(self):
        rating_details = GPSystem.rater.generate_power_details(
            {'inventory': self.jsonify()}
        )

        overall_gp = rating_details['rating']
        ranking = f"{rating_details['ranking']['rank']}[{rating_details['ranking']['tier']}]"
        character_gp = rating_details['totals']['characters']
        weapon_gp = rating_details['totals']['weapons']
        artifact_gp = rating_details['totals']['artifacts']
        return (
            f"""
{overall_gp["weighted"]}|{overall_gp["unweighted"]}gp {ranking}\t V{GPSystem.version}

${self.money}
1. characters\t{self.format_length(self.character_list.get_length())}\t\t {character_gp['weighted']}|{character_gp['unweighted']}gp
2. weapons   \t{self.format_length(self.weapon_list.get_length())}\t\t {weapon_gp['weighted']}|{weapon_gp['unweighted']}gp
3. artifacts \t{self.format_length(self.artifact_list.get_length())}\t\t {artifact_gp['weighted']}|{artifact_gp['unweighted']}gp

4. transfer artifacts to money

5. sort type    {self.sort_type}
6. reverse sort {self.reverse_sort}
7. back
"""
        )
