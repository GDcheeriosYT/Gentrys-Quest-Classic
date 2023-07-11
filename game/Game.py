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
from Online.API.Presence.Presence import GamePresence

# built-in packages
import time

# content packages
from Content.Stories.GentrysQuest import GentrysQuest


class Game:
    game_data = None
    version = None
    server = None
    equipped_character = None
    locations = None
    story = None
    story_index = None
    
    def __init__(Game, game_data, version, server):
        Game.game_data = game_data
        Game.version = version
        Game.server: Server = server
        Game.equipped_character = None
        Game.locations = ItemList(content_type=Location)
        Game.story = GentrysQuest()
        Game.story_index = 0
        Game.presence = GamePresence()

    def start_intro(Game, character_name):
        Game.presence.update_status("Playing intro")
        intro_scene = Intro()
        Window.clear()
        characters = Game.game_data.content.characters
        Game.equipped_character = None
        if character_name is not None:
            for character in characters:
                try:
                    character = character()
                    if character.name == character_name:
                        Text("Thanks for contributing to Gentry's Quest!\nAs a gift take this:").display()
                        Text(character.list_view()).display()
                        Game.equipped_character = character
                        enter_to_continue()
                        break
                except TypeError:
                    pass

            if Game.equipped_character is None:
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
            Game.equipped_character = character

        Game.equipped_character.weapon = Weapon()
        Game.game_data.inventory.character_list.add(character)
        time.sleep(1)
        intro_scene.start(Game.equipped_character, Game.game_data.inventory, Game.game_data.content)
        character.weapon = Game.game_data.inventory.weapon_list.content[0]
        Game.game_data.inventory.weapon_list.content.pop(0)

    def start(Game, character_arg):
        if Game.game_data.startup_amount < 1:
            Game.start_intro(character_arg)

        Game.game_data.startup_amount += 1
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
                    Game.presence.update_status("In menu")
                    while True:
                        choices1 = get_int("1. Singleplayer\n"
                                           "2. Back")
                        if choices1 == 1:
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
                                    #Game.story.start(Game.equipped_character, Game.game_data.inventory, Game.game_data.content, Game.story_index)

                                elif choices2 == 2:
                                    while True:
                                        if Game.equipped_character is None:
                                            character = "nobody"
                                        else:
                                            character = Game.equipped_character.list_view(1)

                                        Text(f"you currently have {character} equipped").display()
                                        locations = Game.game_data.content.locations
                                        for location in locations:
                                            Text(f"{locations.index(location) + 1}. {location}").display()
                                        choices3 = get_int(f"{len(locations) + 1}. back")

                                        if choices3 != len(locations) + 1:
                                            try:
                                                location = locations[choices3 - 1]
                                                Game.presence.update_status("At location", location.name.content)
                                                Text(f"you currently have {character} equipped").display()
                                                location.list_areas()
                                                location.select_area(Game.equipped_character, Game.game_data.inventory, Game.game_data.content)
                                            except IndexError:
                                                pass

                                        else:
                                            break

                                elif choices2 == 3:
                                    Game.presence.update_status("gacha-ing")
                                    valley_high_school = ValleyHighSchool()
                                    base_gacha = BaseGacha()
                                    Text(f"1. {valley_high_school.name.raw_output()}\n"
                                         f"2. {base_gacha.name.raw_output()}").display()
                                    choices3 = get_int("3. back")

                                    if choices3 == 1:
                                        valley_high_school.manage_input(Game.game_data.inventory)

                                    elif choices3 == 2:
                                        base_gacha.manage_input(Game.game_data.inventory)

                                elif choices2 == 4:
                                    Game.presence.update_status("In inventory")
                                    inventory_results = Game.game_data.inventory.manage_input(Game.equipped_character)
                                    if inventory_results is not None:
                                        Game.equipped_character = inventory_results

                                elif choices2 == 5:
                                    Game.presence.update_status("Viewing artifact families")
                                    Game.game_data.content.display_artifact_families()

                                else:
                                    break

                        else:
                            break

                elif choices == 2:
                    Window.clear()
                    try:
                        Game.game_data.settings = SettingsInterface(Game.game_data).visit()
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
                    if not Game.server.disabled:
                        choices2 = get_int("1. Online Users\n"
                                           "2. Leaderboard\n"
                                           "3. Back")

                        if choices2 == 1:
                            Window.place_rule("Online Users")
                            online_status = Status("Uploading data..")
                            online_status.start()
                            Game.server.API.upload_data(Game.game_data)
                            online_status.stop()
                            online_status.modify_status("fetching online users...")
                            online_status.start()
                            players = ItemList(content=Game.server.API.get_online_players())
                            online_status.stop()
                            players.list_content(False)
                            enter_to_continue()

                        elif choices2 == 2:
                            Window.place_rule("Gentry's Quest Leaderboard")
                            online_status = Status("Uploading data..")
                            online_status.start()
                            Game.server.API.upload_data(Game.game_data)
                            online_status.stop()
                            online_status.modify_status("fetching leaderboard data...")
                            online_status.start()
                            players = ItemList(content=Game.server.API.get_leaderboard())
                            online_status.stop()
                            players.list_content(False)
                            enter_to_continue()
                    else:
                        WarningText("Your server functions are disabled try checking your version...").display()

                elif choices == 5:
                    display_changelog(Game.version)

                elif choices == 6:
                    in_game = False
            except ValueError:
                WarningText("Number please...").display()
