# game packages
from Changelog import display_changelog

# graphics packages
from Graphics.Content.Text.QuestionText import QuestionText

# interface packages
from Interface.Interfaces.Testing.Entity.TestInterfaceEntity import TestInterfaceEntity
from Interface.Interfaces.Testing.Location.LocationInterface import LocationInterface
from Interface.Interfaces.Testing.Inventory.InventoryInterface import InventoryInterface
from Interface.Interfaces.Testing.Game.TestGameInterface import TestGameInterface

# IO packages
from IO import Window
from IO.Input import get_int


class TestingHandler:
    """
    Creates an instance of a handler for testing game stuff
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        while True:
            entity_interface = TestInterfaceEntity()
            location_interface = LocationInterface()
            inventory_interface = InventoryInterface()
            game_interface = TestGameInterface()
            QuestionText("What area shall we test today? (Meow:))").display()
            choices = get_int("1. Entity\n"
                              "2. Inventory\n"
                              "3. Location\n"
                              "4. Game\n"
                              "5. Changelog\n"
                              "6. quit\n")
            if choices == 1:
                entity_interface.__repr__()
                Window.clear()

            elif choices == 2:
                inventory_interface.__repr__()
                Window.clear()

            elif choices == 3:
                location_interface.__repr__()
                Window.clear()

            elif choices == 4:
                game_interface.start()
                Window.clear()

            elif choices == 5:
                display_changelog("Testing")

            else:
                break

