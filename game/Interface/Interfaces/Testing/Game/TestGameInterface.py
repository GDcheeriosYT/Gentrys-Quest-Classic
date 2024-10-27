# game packages
from Game import Game
from GameData import GameData

# testing packages
from ..Inventory.InventoryTestInterface import InventoryTestInterface

# collection packages
from Collection.Inventory.Inventory import Inventory

# IO packages
from IO.Input import get_int


class TestGameInterface:
    def __init__(self):
        self.game = Game("Testing")

    def start(self):
        while True:
            choice = get_int("1. play\n"
                             "2. edit data\n"
                             "3. quit")

            if choice == 1:
                self.game.start(None)

            elif choice == 2:
                test_inventory_interface = InventoryTestInterface()
                test_inventory_interface.inventory = self.game.game_data.inventory
                test_inventory_interface.__repr__()
                self.game.game_data.inventory = test_inventory_interface.inventory

            else:
                break
