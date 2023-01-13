# game packages
# IO packages
from IO.Input import enter_to_continue, get_int

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# location packages
from Location.BattleArea.BattleArea import BattleArea

# entity packages
from Entity.Artifact.Artifact import Artifact

# gacha packages
from Gacha.GachaEvent import GachaEvent

# story packages
from .CheckPoint import CheckPoint


class Story:
    def __init__(self, events: list):
        self.events = events

    def start(self, character, inventory, content, index = 0):
        while index < len(self.events):
            event = self.events[index]
            if isinstance(event, str):
                Text(event.replace("{player}", character.name)).display()
                enter_to_continue()

            elif isinstance(event, BattleArea):
                event.start(character, inventory, content)
            elif isinstance(event, Artifact):
                inventory.artifact_list.add(event)
                Text(f"You have received {event}\n"
                     f"Go to {Text('manage artifacts', Style(text_style=['bold'])).raw_output()} to equip it").display()
                enter_to_continue()
                inventory.manage_character(character)

            elif isinstance(event, GachaEvent):
                event.pull(inventory)

            elif isinstance(event, CheckPoint):
                if not event.will_continue():
                    return index

            index += 1

        return "done"
