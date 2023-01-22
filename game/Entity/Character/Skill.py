# game packages
# graphics packages
from Graphics.Text.Text import Text

class Skill:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return Text(f"{self.name}: {self.description}").raw_output()
