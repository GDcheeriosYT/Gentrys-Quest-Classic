# built-in packages
import time

# external packages
from rich.console import Console


class Status:
    """
    Makes a status indicator from the rich.console api

    parameters

    text: string
        the text to display

    style: string
        the spinner style type
    """

    text = None
    style = None

    def __init__(self, text="doing something", style="dots"):
        self.text = text
        self.style = style
        self.console = Console()
        self.status = self.console.status(text, spinner=style)

    def start(self):
        self.status.start()

    def stop(self):
        #time.sleep(0.5)
        self.status.stop()

    def modify_status(self, text="doing something", style="dots"):
        self.status = self.console.status(text, spinner=style)
        time.sleep(0.2)

    def live_change(self, text="doing something", style="dots"):
        self.stop()
        self.modify_status(text, style)
        self.start()
