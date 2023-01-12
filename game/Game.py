# game packages
from Changelog import display_changelog

# collection packages
from Collection.ItemList import ItemList

# location packages
from Location.Location import Location

# content packages
from Content.Locations.Iowa.Iowa import Iowa
from Content.Stories.Intro import Intro
from Content.Gachas.ValleyHighSchool import ValleyHighSchool
from Content.Gachas.BaseGacha import BaseGacha
from Content.CharacterContentManager import CharacterContentManager
#from Content.Stories.GentrysQuest import GentrysQuest

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

# online packages
from Online.Server import Server

# built-in packages
import time


class Game:
    def __init__(self, game_data, version, server):
        self.game_data = game_data
        self.version = version
        self.server: Server = server
        self.equipped_character = None
        self.locations = ItemList(content_type=Location)

    def start_intro(self, character_name):
        intro_scene = Intro()
        Window.clear()
        characters = self.game_data.content.characters
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
        self.game_data.inventory.character_list.add(character)
        time.sleep(1)
        intro_scene.start(self.equipped_character, self.game_data.inventory, self.game_data.content)
        character.weapon = self.game_data.inventory.weapon_list.content[0]
        self.game_data.inventory.weapon_list.content.pop(0)

    def start(self, character_arg):
        if self.game_data.startup_amount < 1:
            self.start_intro(character_arg)

        self.game_data.startup_amount += 1
        in_game = True
        while in_game:
            try:
                choices = get_int("Main Menu\n"
                                  "1. Play\n"
                                  "2. Settings\n"
                                  "3. Credits\n"
                                  "4. Online\n"
                                  "5. Changelog\n"
                                  "6. Quit")

                if choices == 1:
                    while True:
                        choices1 = get_int("1. Singleplayer\n"
                                           "2. Back")
                        if choices1 == 1:
                            while True:
                                choices2 = get_int("1. Story\n"
                                                   "2. Travel\n"
                                                   "3. Gacha\n"
                                                   "4. Inventory\n"
                                                   "5. Back")

                                if choices2 == 1:
                                    self.game_data

                                elif choices2 == 2:
                                    while True:
                                        if self.equipped_character is None:
                                            character = "nobody"
                                        else:
                                            character = self.equipped_character.list_view()

                                        Text(f"you currently have {character} equipped").display()
                                        locations = self.game_data.content.locations
                                        for location in locations:
                                            Text(f"{locations.index(location) + 1}. {location}").display()
                                        choices3 = get_int(f"{len(locations) + 1}. back")

                                        if choices3 != len(locations) + 1:
                                            try:
                                                location = locations[choices3 - 1]
                                                Text(f"you currently have {character} equipped").display()
                                                location.list_areas()
                                                location.select_area(self.equipped_character, self.game_data.inventory, self.game_data.content)
                                            except IndexError:
                                                pass

                                        else:
                                            break

                                elif choices2 == 3:
                                    valley_high_school = ValleyHighSchool()
                                    base_gacha = BaseGacha()
                                    Text(f"1. {valley_high_school.name.raw_output()}\n"
                                         f"2. {base_gacha.name.raw_output()}").display()
                                    choices3 = get_int("3. back")

                                    if choices3 == 1:
                                        valley_high_school.manage_input(self.game_data.inventory)

                                    elif choices3 == 2:
                                        base_gacha.manage_input(self.game_data.inventory)

                                elif choices2 == 4:
                                    inventory_results = self.game_data.inventory.manage_input(self.equipped_character)
                                    if inventory_results is not None:
                                        self.equipped_character = inventory_results

                                else:
                                    break

                        else:
                            break

                elif choices == 2:
                    Window.clear()
                    try:
                        self.game_data.settings = SettingsInterface(self.game_data).visit()
                    except TypeError:
                        Window.clear()

                elif choices == 3:
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

                    enter_to_continue()

                elif choices == 4:
                    choices2 = get_int("1. Online Users\n"
                                       "2. Leaderboard\n"
                                       "3. Back")

                    if choices2 == 1:
                        Window.place_rule("Online Users")
                        online_status = Status("Uploading data..")
                        online_status.start()
                        self.server.API.upload_data(self.game_data)
                        online_status.stop()
                        online_status.modify_status("fetching online users...")
                        online_status.start()
                        players = ItemList(content=self.server.API.get_online_players())
                        online_status.stop()
                        players.list_content(False)
                        enter_to_continue()

                    elif choices2 == 2:
                        Window.place_rule("Gentry's Quest Leaderboard")
                        online_status = Status("Uploading data..")
                        online_status.start()
                        self.server.API.upload_data(self.game_data)
                        online_status.stop()
                        online_status.modify_status("fetching leaderboard data...")
                        online_status.start()
                        players = ItemList(content=self.server.API.get_leaderboard())
                        online_status.stop()
                        players.list_content(False)
                        enter_to_continue()

                elif choices == 5:
                    display_changelog(self.version)

                elif choices == 6:
                    in_game = False
            except ValueError:
                WarningText("Number please...").display()
