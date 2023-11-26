# game packages
# IO packages
from IO import Window
from IO.Input import get_int

# Interface packages
from .InterfaceContent import InterfaceContent

# Graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.WarningText import WarningText

# external packages
from rich.console import Console


class Interface:
    """
    makes an interface in game

    parameters
    title: string
        the title of the interface

    is_rule: boolean
        if it will display as a rule

    content: dict
        the content of the interface
    """

    title = None
    is_rule = None

    def __init__(self, title="interface", is_rule=False, content=InterfaceContent()):
        self.title = title
        self.is_rule = is_rule
        self.content = content

    @staticmethod
    def choose(selection):
        selection = selection - 1
        return selection

    def visit(self, clear_window=True, return_type: bool = False):
        while True:
            if clear_window:
                Window.clear()
            if self.is_rule:
                Console().rule(self.title)

            Text(self.content.info).display()
            selection = get_int(self.content.show_options())
            return self.content.options[self.choose(selection)] if return_type else self.choose(selection)
