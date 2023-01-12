# game packages
# entity packages
from .StatTypes import StatTypes
from .Experience import Experience

# config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.ListSetting import ListSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window

# graphics packages
from Graphics.Text.Text import Text

# built-in packages
import random


class Buff:
    """
    Makes a buff for attributes

    parameters

    attribute_type: StatTypes
        the attribute for the buff to buff

    experience: Experience
        the experience of the buff

    is_percent: boolean
        determines if the buff is a percent type
    """

    attribute_type = None
    experience = None
    is_percent = None

    def __init__(self, attribute_type: StatTypes = None, experience : Experience = None, is_percent : bool = None):
        if attribute_type is None:
            self.attribute_type = random.choice(list(StatTypes))
        else:
            self.attribute_type = attribute_type

        if experience is None:
            self.experience = Experience()
        else:
            self.experience = experience

        if is_percent is None:
            self.is_percent = random.choice([True, False])
        else:
            self.is_percent = is_percent

        if attribute_type == StatTypes.CritRate or attribute_type == StatTypes.CritDamage:
            self.is_percent = False

        stats = []
        for stat in list(StatTypes):
            stats.append(stat.name)
        self.settings = [
            ListSetting("attribute type", self.attribute_type.name, stats),
            NumberSetting("level", self.experience.level, 1),
            ToggleSetting("is percent type", self.is_percent)
        ]
        self.value = 0

    def handle_value(self, star_rating):
        calculation = ((self.experience.level * 1.75) + (star_rating * 1.25) + (star_rating * int(self.experience.level / star_rating)))
        if self.attribute_type == StatTypes.CritRate:
            calculation /= 4
        self.value = int(calculation) if not self.is_percent else float(calculation)

    def __repr__(self):
        return f"{self.attribute_type.name} {self.value}{'%' if self.is_percent else ''}"

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        counter = 0
        for stat_type in list(StatTypes):
            if str(stat_type) == f"StatTypes.{self.settings[0].selected_value}":
                self.attribute_type = StatTypes(counter + 1)
                break

            counter += 1

        self.experience.level = self.settings[1].value
        self.is_percent = self.settings[2].toggled
        return self

    def jsonify(self):
        return {"buff": [
            self.attribute_type.value,
            1 if self.is_percent else 0,
            self.experience.level
        ]}
