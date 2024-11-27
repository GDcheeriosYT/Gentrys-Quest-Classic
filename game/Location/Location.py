# game packages
# graphics packages
from Graphics.Text.Text import Text

# IO packages
from IO.Input import get_int


class Location:
    """
    Makes a location.

    parameters:

    name: Text
        the name of the location
    """

    name = None
    areas = None

    def __init__(self, name: str, areas: list):
        self.name = Text(name)
        self.areas = areas

    def list_areas(self):
        for area in self.areas:
            Text(f"{self.areas.index(area) + 1}. {area}").display()

        Text(f"{len(self.areas) + 1}. back").display()

    def select_area(self, character, inventory, content):
        choice = get_int("Select an area") - 1
        choice2 = get_int("1. regular fight\n"
                          "2. afk farm\n"
                          "3. back")
        try:
            if choice2 == 1:
                self.areas[choice].start(character, inventory, content)
            elif choice2 == 2:
                self.areas[choice].afk(character, inventory, content)
            else:
                pass
        except IndexError:
            pass

    def __repr__(self):
        return f"{self.name.raw_output()} {len(self.areas)} battle areas"
