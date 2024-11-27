# game packages
# interface packages
import traceback

from GameData import GameData
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from .InventoryTestInterface import InventoryTestInterface


class InventoryInterface(Interface):
    def __init__(self):
        super().__init__("Welcome to the Test Location Interface",
                         content=InterfaceContent("Meow this is some great info",
                                                  ["Inventory"]))

    def __repr__(self):
        action = self.visit()
        if action == 0:
            test_interface = InventoryTestInterface(GameData.inventory)
            while True:
                try:
                    test_interface.__repr__()
                except TypeError:
                    traceback.print_exc()
                    break