# game packages
# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style


class Skill:
    def __init__(self, name: str, description: str, cooldown: int = 1):
        self.name = name
        self.description = description
        self.cooldown = cooldown
        self.tracker = 0

    def do_stuff(self):
        if self.is_ready():
            self.tracker = 0
            Text("You did stuff!").display()
            return 0
        else:
            return 0

    def is_ready(self):
        if self.tracker >= self.cooldown:
            return True
        else:
            return False

    def text_output(self):
        return Text(f"{self.name}: {self.description}").raw_output()

    def __repr__(self):
        return Text(f"{self.name}: {self.description}", Style(text_color="green" if self.is_ready() else "bright_black")).raw_output()
