# game packages
import IO.Input
from Changelog import display_changelog

# collection packages
from Collection.ItemList import ItemList
from GameData import GameData

# location packages
from Location.Location import Location

# content packages
from Content.Stories.Intro import Intro
from Content.Gachas.ValleyHighSchool import ValleyHighSchool
from Content.Gachas.BaseGacha import BaseGacha

# collection packages
from Collection.ItemList import ItemList

# IO packages
from IO.Input import get_int, get_string, enter_to_continue
from IO import Window

# entity packages
from Entity.Character.Character import Character
from Entity.Weapon.Weapon import Weapon

# interface packages
from Interface.Interfaces.Settings import SettingsInterface

# graphics packages
from Graphics.Content.Text.InfoText import InfoText
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style
from Graphics.Status import Status
from Online.API.API import API

# online packages
from Online.Server import Server
from Online.API.Presence.Presence import GamePresence

# built-in packages
import time

# content packages
from Content.Stories.GentrysQuest import GentrysQuest


class Game:
    version = None
    equipped_character = None
    locations = None
    story = None
    story_index = None

    def __init__(self, version):
        self.version = version
        self.equipped_character = None
        self.locations = ItemList(content_type=Location)
        self.story = GentrysQuest()
        self.story_index = 0
        self.presence = GamePresence()

    def start_intro(self, character_name):
        self.presence.update_status("Playing intro")
        intro_scene = Intro()
        Window.clear()
        characters = GameData.content.characters
        self.equipped_character = None
        if character_name is not None:
            for character in characters:
                try:
                    character = character()
                    if character.name == character_name:
                        Text("Thanks for contributing to Gentry's Quest!\nAs a gift take this:").display()
                        Text(character.list_view()).display()
                        self.equipped_character = character
                        enter_to_continue()
                        break
                except TypeError:
                    pass

            if self.equipped_character is None:
                WarningText("We couldn't find this character...").display()
                exit(1)

        else:
            name = get_string("What is this protagonists name?\n")
            character = Character(
                name,
                "The Guy",
                default_attack_points=1,
                default_health_points=1,
                default_defense_points=1,
                default_crit_damage_points=1,
                default_crit_rate_points=1
            )
            self.equipped_character = character

        self.equipped_character.weapon = Weapon()
        GameData.inventory.add_item(character)
        time.sleep(1)
        intro_scene.start(self.equipped_character, GameData.inventory, GameData.content)
        character.weapon = GameData.inventory.weapon_list.content[0]
        character.weapon.pre_remove()
        GameData.inventory.weapon_list.content.pop(0)

    def start(self, character_arg):
        global GameData, WarningText
        if GameData.startup_amount == 0:
            self.start_intro(character_arg)

        GameData.startup_amount += 1
        in_game = True
        while in_game:
            try:
                choices = get_int("Main Menu\n"
                                  "1. Play\n"
                                  "2. Credits\n"
                                  "3. Online\n"
                                  "4. Changelog\n"
                                  "5. Quit")

                if choices == 1:
                    self.presence.update_status("In menu")
                    while True:
                        choices2 = get_int("1. Story\n"
                                           "2. Travel\n"
                                           "3. Gacha\n"
                                           "4. Inventory\n"
                                           "5. View Families\n"
                                           "6. Back")

                        if choices2 == 1:
                            InfoText("Coming soon...").display()
                            enter_to_continue()

                        elif choices2 == 2:
                            while True:
                                if self.equipped_character is None:
                                    character = "nobody"
                                else:
                                    character = self.equipped_character.name

                                Text(f"you currently have {character} equipped").display()
                                locations = GameData.content.locations
                                for location in locations:
                                    Text(f"{locations.index(location) + 1}. {location}").display()
                                choices3 = get_int(f"{len(locations) + 1}. back")

                                if choices3 != len(locations) + 1:
                                    try:
                                        location = locations[choices3 - 1]
                                        self.presence.update_status("At location", location.name.content)
                                        Text(f"you currently have {character} equipped").display()
                                        location.list_areas()
                                        location.select_area(self.equipped_character, GameData.inventory,
                                                             GameData.content)
                                    except IndexError:
                                        pass

                                else:
                                    break

                        elif choices2 == 3:
                            self.presence.update_status("gacha-ing")
                            valley_high_school = ValleyHighSchool()
                            base_gacha = BaseGacha()
                            Text(f"1. {valley_high_school.name.raw_output()}\n"
                                 f"2. {base_gacha.name.raw_output()}").display()
                            choices3 = get_int("3. back")

                            if choices3 == 1:
                                valley_high_school.manage_input(GameData.inventory)

                            elif choices3 == 2:
                                base_gacha.manage_input(GameData.inventory)

                        elif choices2 == 4:
                            self.presence.update_status("In inventory")
                            inventory_results = GameData.inventory.manage_input(self.equipped_character)
                            if inventory_results is not None:
                                self.equipped_character = inventory_results

                        elif choices2 == 5:
                            self.presence.update_status("Viewing artifact families")
                            GameData.content.display_artifact_families()

                        else:
                            break

                elif choices == 2:
                    Window.place_rule("Game Developers")
                    Text("Brayden", Style(text_color="green")).display()
                    Text("Carter", Style("green", "bright_magenta", ["italic"])).display()
                    print("\n")

                    Window.place_rule("Special Thanks")
                    Text("Dylan").display()
                    Text("Brody").display()
                    Text("Nolan").display()
                    Text("Bryce").display()
                    Text("Jared").display()
                    Text("Zach").display()
                    Text("Luke").display()
                    Text("Kelly").display()
                    Text("Asher").display()
                    Text("Alec").display()
                    Text("Spencer").display()
                    Text("David").display()
                    Text("Nathan").display()
                    Text("Joe").display()
                    Text("Grant").display()
                    Text("Gavin").display()
                    Text("Pete").display()
                    Text("MJ").display()
                    Text("Mr.Lin(林老师)").display()
                    Text("Mr.Gentry").display()
                    Text("Mr.Goldsmith").display()
                    Text("Cody").display()
                    Text("Mason").display()
                    Text("Max").display()
                    Text("Greg").display()
                    Text("Hanna").display()
                    Text("Caleb", Style(text_color="bright_cyan")).display()
                    Text("Benji").display()
                    Text("Derek").display()
                    Text("Charlie").display()
                    Text("other Grant").display()
                    Text("Dyllon").display()
                    Text("Jack").display()
                    Text("Jaycee").display()
                    Text("Luke").display()
                    Text("Kolin").display()
                    Text("Mak").display()
                    Text("Matheu").display()
                    Text("Ryan").display()
                    Text("Sean").display()
                    Text("Connor").display()
                    Text("Seth").display()
                    Text("Will").display()
                    Text("Seth").display()
                    Text("Oliver").display()
                    Text("Toby").display()
                    Text("Ben Meier").display()

                    enter_to_continue()

                elif choices == 3:
                    if not Server.disabled:
                        choices2 = get_int("1. Leaderboard\n"
                                           "2. Online players\n"
                                           "3. Back")

                        if choices2 == 1:
                            Window.place_rule("Gentry's Quest Leaderboard")
                            players = ItemList(content=API.get_leaderboard())
                            players.list_content(False)
                            enter_to_continue()

                        if choices2 == 2:
                            Window.place_rule("Online Players")
                            players = ItemList(content=API.get_leaderboard(True))
                            players.list_content(False)
                            enter_to_continue()

                    else:
                        WarningText("Your server functions are disabled try checking your version...").display()

                elif choices == 4:
                    display_changelog(self.version)

                elif choices == 5:
                    in_game = False
            except ValueError:
                WarningText("Number please...").display()
