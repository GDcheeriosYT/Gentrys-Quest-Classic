# game packages
# entity packages
from ..Entity import Entity
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Stats.StatTypes import StatTypes
from ..Stats.Buff import Buff
from .Verbs import Verbs

# Config packages
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Config.ToggleSetting import ToggleSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# Graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.DescriptionText import DescriptionText

# IO packages
from IO import Window


class Weapon(Entity):
    """
    Makes a weapon

    parameters

    name: string
        the name of the Weapon

    description: string
        the description of the Weapon

    weapon_type: string
        the weapon type

    attack: int
        the attack damage that the Weapon does

    buff: Buff
        the attribute of the user to buff

    verbs: Verbs
        the verbs to be used by the weapon

    star_rating: StarRating
        the star rating of the Weapon

    experience: Experience
        the experience for the Weapon
    """

    name = None
    description = None
    weapon_type = None
    base_attack = None
    attack = None
    buff = None
    verbs = None
    star_rating = None
    experience = None

    def __init__(self, name="fists", description="punches things", weapon_type=None, attack=3,
                 buff=Buff(), verbs=Verbs("punched", "uppercut"),
                 star_rating=StarRating(), experience=None):
        super().__init__(name, description, star_rating, experience)
        self.weapon_type = weapon_type
        self.base_attack = attack
        self.buff = buff
        self.buff.handle_value(self.star_rating.value)
        self.verbs = verbs
        self.settings = [
            StringSetting("name", self.name),
            StringSetting("description", self.description),
            StringSetting("weapon_type", self.weapon_type),
            NumberSetting("base attack", self.base_attack),
            ClassSetting("buff", self.buff),
            ClassSetting("verbs", self.verbs),
            NumberSetting("star_rating", self.star_rating.value, 1, 5),
            NumberSetting("level", self.experience.level, 1)
        ]
        self.update_stats()

    def gacha_info_view(self):
        return f"{self.name} {self.star_rating}\n{self.description}\n\t{self.base_attack} base attack"

    def update_stats(self):
        self.attack = int(self.base_attack + (self.experience.level * self.star_rating.value))
        self.buff.experience.level = self.experience.level
        self.buff.handle_value(self.star_rating.value)

    def jsonify(self):
        return {
            "weapon type": self.weapon_type,
            "stats": {
                "attack": self.base_attack,
                "buff": self.buff.jsonify()
            },
            "name": self.name,
            "description": self.description,
            "verbs": {
                "normal": self.verbs.normal,
                "critical": self.verbs.critical
            },
            "experience": {
                "xp required": self.experience.get_xp_required(self.star_rating.value, False),
                "level": self.experience.level,
                "xp": self.experience.xp,
                "previous xp required": 0
            },
            "star rating": self.star_rating.value
        }

    def __repr__(self):
        return (
            f"""{self.name} {self.star_rating} {self.experience.display_level()}
type: {self.weapon_type}
base attack: {self.attack}
attribute: {self.buff}
##################
{DescriptionText(self.description).raw_output()}
##################
"""
        )

    def test(self):
        Window.clear()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.description = self.settings[1].text
        self.weapon_type = self.settings[2].text
        self.attack = self.settings[3].value
        self.buff = self.settings[4].instance_class
        self.verbs = self.settings[5].instance_class
        self.star_rating = StarRating(self.settings[6].value)
        self.experience.level = self.settings[7].value
        self.update_stats()
        return self
