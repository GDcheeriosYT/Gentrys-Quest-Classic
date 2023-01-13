# game packages
# achievement packages
from Achievement.Achievement import Aura

# graphics packages
from Graphics.Text.Style import Style


class Gamer(Aura):
    def __init__(self):
        super().__init__(
            "Gamer",
            Style(
                text_color="green"
            )
        )