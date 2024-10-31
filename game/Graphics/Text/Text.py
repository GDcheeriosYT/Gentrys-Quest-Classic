# game packages
# graphics packages
import time

from .Style import Style

# IO packages
from IO.Input import enter_to_continue

# external packages
from rich.console import Console


class Text:
    """
    Makes text for the game

    parameters

    content: string
        the content of the text

    style: Style
        the style of the text

    text_animation: TextAnimation
        the text animation
    """

    content = None
    style = None
    text_animation = None

    def __init__(self, content="text", style=Style("", "white")):
        self.content = content
        self.style = style

    def display(self, same_line=False, enter_prompt=False, sleep: int = 0):
        Console().print(f"{self.style}{self.content}", end='\r' if same_line else '\n')
        if enter_prompt:
            enter_to_continue()

        if sleep > 0:
            time.sleep(sleep)

    def raw_output(self):
        return f"{self.style}{self.content}[white on black]"
