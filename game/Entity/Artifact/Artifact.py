# game packages
# entity packages
from ..Entity import Entity
from ..Stats.Buff import Buff
from ..Stats.Experience import Experience
from ..Stats.StarRating import StarRating

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.InfoText import InfoText

# collection packages
from Collection.ItemList import ItemList

# config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window
from IO.Input import enter_to_continue
from IO.StringMethods import text_length_limiter, star_rating_spacer


class Artifact(Entity):
    """
    Makes an artifact

    parameters

    name: string
        the name of the Artifact

    star_rating: StarRating
        the star rating of the Artifact

    family: ArtifactFamily
        the family that the Artifact is in

    main_attribute: Buff
        the main attribute of the Artifact

    attributes: list
        the attributes that this artifact has

    experience: Experience
        the experience of the Artifact
    """

    name = None
    star_rating = None
    family = None
    main_attribute = None
    attributes = None
    experience = None

    def __init__(self, name, star_rating=StarRating(), family=None, main_attribute=None, attributes=None,
                 experience=None):
        super().__init__(name=name, description="description", star_rating=star_rating, experience=experience)
        buff_bonus_points = 0
        if attributes is None:
            attributes = []
            if self.star_rating.value - 2 >= 1:
                buff_bonus_points = self.star_rating.value - 2

        self.family = family
        if main_attribute is None:
            main_attribute = Buff()
        self.main_attribute = main_attribute
        self.main_attribute.handle_value(self.star_rating.value)
        self.attributes = attributes
        for attribute in self.attributes:
            attribute.handle_value(self.star_rating.value)
        self.experience.limit = self.star_rating.value * 4
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("star rating", self.star_rating.value, 1, 5),
            StringSetting("family", self.family),
            ClassSetting("main attribute", self.main_attribute),
            NumberSetting("level", self.experience.level, 1, self.experience.limit)
        ]
        for i in range(buff_bonus_points):
            self.add_new_attribute()

    def level_up(self, amount):
        if self.experience.level < self.star_rating.value * 4:
            self.experience.level += amount
            self.experience.xp = 0
            print(f"Your artifact is now level {self.experience.level}!")
            if self.experience.level % 4 == 0:
                self.add_new_attribute(True)
            self.main_attribute.experience.level = self.experience.level
            self.main_attribute.handle_value(self.star_rating.value)
        else:
            WarningText("Artifact is max level!").display()

        enter_to_continue()

    def add_new_attribute(self, display_info: bool = False):
        new_attribute = Buff(experience=Experience(1))
        while (new_attribute.attribute_type == self.main_attribute.attribute_type) and (new_attribute.is_percent == self.main_attribute.is_percent):
            new_attribute = Buff(experience=Experience(1))

        if display_info:
            InfoText(f"^{new_attribute.attribute_type.name}{'%' if new_attribute.is_percent else ''}^").display()
        for attribute in self.attributes:
            if (new_attribute.attribute_type == attribute.attribute_type) and (
                    new_attribute.is_percent == attribute.is_percent):
                attribute.experience.level += 1
                attribute.handle_value(self.star_rating.value)
                return None
        new_attribute.handle_value(self.star_rating.value)
        self.attributes.append(new_attribute)

    def display_attributes(self):
        string = "\n"
        for attribute in self.attributes:
            string += f"{attribute}\n"

        return string

    def list_view(self, index: int = 1):
        attribute_text = f"*{self.main_attribute.attribute_type.abreviate()}{'%' if self.main_attribute.is_percent else ''}* "
        for buff in self.attributes:
            attribute_text += f"{buff.attribute_type.abreviate()}{'%' if buff.is_percent else ''} "
        spacing_text = "      "

        counter = len(attribute_text)

        while counter < (8 * 4):
            spacing_text += " "
            counter += 1

        try:
            return f"{text_length_limiter(self.name, len(str(index + 1)))}{star_rating_spacer(self.star_rating.__repr__(), self.star_rating.value)}\t  {attribute_text}{spacing_text}\t{self.experience}"
        except TypeError:
            return self.name

    def __repr__(self):
        try:
            percentage = round((self.experience.xp / self.experience.get_xp_required(self.star_rating.value)) * 100, 2)
        except ZeroDivisionError:
            percentage = 0
        return (
            f"""{self.name} {self.star_rating}
apart of the {self.family} family
{self.experience.display_level()} {self.experience.display_xp()}/{self.experience.get_xp_required(self.star_rating.value)}xp ({int(percentage)})%
* {self.main_attribute} *
{f"attributes{self.display_attributes()}" if len(self.attributes) > 0 else ""}"""
        )

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.star_rating = StarRating(self.settings[1].value)
        self.experience.limit = self.star_rating.value * 4
        self.family = self.settings[2].text
        self.main_attribute = self.settings[3].instance_class
        self.experience.level = self.settings[4].value
        self.settings[4] = NumberSetting("level", self.experience.level, 1, self.experience.limit)
        self.main_attribute.experience.level = self.experience.level
        self.main_attribute.handle_value(self.star_rating.value)
        self.attributes = []
        for i in range(int(self.experience.level/4)):
            self.add_new_attribute()
        return self

    def jsonify(self):
        attributes = []
        for attribute in self.attributes:
            attributes.append(attribute.jsonify())

        return {
            "stats": {
                "attributes": attributes,
                "main attribute": self.main_attribute.jsonify()
            },
            "name": self.name,
            "family": self.family,
            "experience": {
                "xp required": self.experience.get_xp_required(self.star_rating.value),
                "level": self.experience.level,
                "xp": self.experience.xp,
                "previous xp required": 0
            },
            "star rating": self.star_rating.value
        }
