# game packages
# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style


class Aura:
    def __init__(self, name: str, style: Style):
        self.name = name
        self.style = style

    def __repr__(self):
        return Text(self.name, self.style).raw_output()
