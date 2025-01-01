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

        if self.attribute_type == StatTypes.CritRate or self.attribute_type == StatTypes.CritDamage:
            self.is_percent = False
        else:
            if is_percent is None:
                self.is_percent = random.choice([True, False])
            else:
                self.is_percent = is_percent

        stats = []
        for stat in list(StatTypes):
            stats.append(stat.name)
        self.settings = [
            ListSetting("attribute type", self.attribute_type.name, stats),
            NumberSetting("level", self.experience.level, 1),
            ToggleSetting("is percent type", self.is_percent)
        ]
        self.value = 0

    def handle_value(self, star_rating: int) -> None:
        """
        Determines the value of the buff.
        :param star_rating: the star rating of the parent
        """

        min_value = 0  # the minimum value
        star_rating_influence = 0  # how much the star rating will influence the value
        level_influence = 0  # how much level will influence the value
        percent_change = 1  # how much the value will change depending on if it's a percent

        if self.attribute_type == StatTypes.Health:
            min_value = 100
            star_rating_influence = 25
            level_influence = 30
            percent_change = 15

        elif self.attribute_type == StatTypes.Attack:
            min_value = 10
            star_rating_influence = 10
            level_influence = 5
            percent_change = 1.5

        elif self.attribute_type == StatTypes.Defense:
            min_value = 10
            star_rating_influence = 6
            level_influence = 4
            percent_change = 2

        elif self.attribute_type == StatTypes.CritRate:
            min_value = 2
            star_rating_influence = 2
            level_influence = 2

        elif self.attribute_type == StatTypes.CritDamage:
            min_value = 2
            star_rating_influence = 2
            level_influence = 2

        if not self.is_percent:
            percent_change = 1

        self.value = int((min_value + (star_rating * star_rating_influence) + (self.experience.level * level_influence)) / percent_change)

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
