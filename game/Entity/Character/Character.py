# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.StatTypes import StatTypes
from ..Stats.StarRating import StarRating
from ..Stats.Experience import Experience
from ..Artifact.Artifact import Artifact
from ..Enemy.Enemy import Enemy
from ..Stats.Stat import Stat
from .Skill import Skill
from .SkillSet import SkillSet

# collection packages
from Collection.ItemList import ItemList

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Content.Text.DescriptionText import DescriptionText

# IO packages
from IO import Window
from IO.Input import get_int, enter_to_continue

# config packages
from Config.SettingManager import SettingManager
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.ToggleSetting import ToggleSetting

# random packages
from Random.Functions import determine_crit

# built-in packages
import random


class Character(Entity):
    """
    Makes a Character class

    parameters

    name: string
        the name of the Character

    description: string
        the description of the Character

    star_rating: int
        the star rating of the Character

    experience: Experience
        the experience of the Character

    weapon: Weapon
        the Weapon that the Character has equipped

    artifacts: ItemList
        the Artifacts that the character has

    default_health_points: int
        the default health points the Character has

    default_attack_points: int
        the default attack points damage that the Character does

    default_defense_points: int
        the default defense points that the Character has

    default_crit_rate_points: int
        the default crit rate points the Character has

    default_crit_damage_points: int
        the default crit damage points the character has
    """

    name = None
    description = None
    star_rating = None
    experience = None
    weapon = None
    artifacts = None
    default_health_points = None
    default_attack_points = None
    default_defense_points = None
    default_crit_rate_points = None
    default_crit_damage_points = None
    health = None
    attack = None
    defense = None
    critRate = None
    critDamage = None
    difficulty = None

    def __init__(self, name, description="description", star_rating=StarRating(1), experience=None, weapon=None,
                 artifacts=ItemList(5, Artifact, True), default_health_points=0, default_attack_points=0,
                 default_defense_points=0, default_crit_rate_points=0,
                 default_crit_damage_points=0):
        super().__init__(name, description, star_rating, experience)
        self.default_health_points = default_health_points
        self.default_attack_points = default_attack_points
        self.default_crit_rate_points = default_crit_rate_points
        self.default_defense_points = default_defense_points
        self.default_crit_damage_points = default_crit_damage_points
        self.health = Stat(StatTypes.Health)
        self.attack = Stat(StatTypes.Attack)
        self.defense = Stat(StatTypes.Defense)
        self.critRate = Stat(StatTypes.CritRate, 100)
        self.critDamage = Stat(StatTypes.CritDamage)
        self.weapon = weapon
        self.artifacts = artifacts
        self.update_stats()
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("health points", 0, 0, 4),
            NumberSetting("attack points", 0, 0, 4),
            NumberSetting("defense points", 0, 0, 4),
            NumberSetting("critRate points", 0, 0, 4),
            NumberSetting("critDamage points", 0, 0, 4),
            NumberSetting("star rating", self.star_rating.value, 1, 5),
            NumberSetting("level", self.experience.level, 1),
            ClassSetting("weapon", self.weapon),
            ClassSetting("artifacts", self.artifacts),
            StringSetting("description", self.description),
            ToggleSetting("has test skill", False)
        ]
        self.skills = SkillSet(self.star_rating.value)

    def test(self):
        class TestSkill(Skill):
            def __init__(self):
                super().__init__(
                    "Test Skill",
                    "hits the enemy for 50% more damage",
                    2
                )

            def do_stuff(self):
                if self.is_ready():
                    self.tracker = 0
                    damage = 0
                    damage += self.character.attack + self.character.weapon.attack + (self.character.attack / 2)
                    Text(f"You hit the enemy for [red] {damage}").display()
                    return damage
                else:
                    return 0

        Window.clear()
        Text(self.__repr__()).display()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.default_health_points = self.settings[1].value
        self.default_attack_points = self.settings[2].value
        self.default_defense_points = self.settings[3].value
        self.default_crit_rate_points = self.settings[4].value
        self.default_crit_damage_points = self.settings[5].value
        self.star_rating = StarRating(self.settings[6].value)
        self.experience.level = self.settings[7].value
        self.weapon = self.settings[8].instance_class
        self.artifacts = self.settings[9].instance_class
        self.description = self.settings[10].text
        if self.settings[11].toggled:
            skill = TestSkill()

            self.skills.add_skill(TestSkill())
        else:
            self.skills.skills.content = []
        self.update_stats()
        return self

    def get_battle_options(self):
        options = []
        if self.weapon is not None:
            options.append("attack")

        if not self.skills.is_empty():
            options.append("skills")

        return options

    def gacha_info_view(self):
        def perk_point_string_gen(perk, perk_string):
            if perk > 0:
                return f"\t+{perk} {perk_string}\n"
            else:
                return ""

        perks = "\n"

        perks += perk_point_string_gen(self.default_health_points, "Health")
        perks += perk_point_string_gen(self.default_attack_points, "Attack")
        perks += perk_point_string_gen(self.default_defense_points, "Defense")
        perks += perk_point_string_gen(self.default_crit_rate_points, "CritRate")
        perks += perk_point_string_gen(self.default_crit_damage_points, "CritDamage")

        return f"{self.name} {self.star_rating}\n{self.description} {perks}"

    def attack_enemy(self, enemy, is_skill=False):
        damage = self.attack.total_value + self.weapon.attack
        is_crit = determine_crit(self.critRate.total_value)
        damage += self.attack.total_value * (self.critDamage.total_value / 100) if is_crit else 0
        defense = int(enemy.defense.total_value + (damage * enemy.damage_negation))
        damage = int(damage - defense)
        Text(f"{self.name} {self.weapon.verbs.critical if is_crit else self.weapon.verbs.normal} {enemy.name} for {damage} damage").display()
        if damage <= 0:
            WarningText(f"{enemy.name} has dodged").display()
        else:
            enemy.health.total_value -= damage
        enter_to_continue()

    def manage_battle_input(self, choice, enemy, choices):
        while True:
            Text(enemy.show_stats()).display()
            try:
                if choices[choice - 1] == "attack":
                    self.attack_enemy(enemy)
                    return True

                elif choices[choice - 1] == "skills":
                    x = 1
                    for skill in self.skills.skills.content:
                        Text(f"{x}. {skill}").display()
                        x += 1

                    option = get_int(f"{x}. back")
                    if option < x:
                        selection = self.skills.skills.content[option - 1]
                        if selection.is_ready():
                            selection.do_stuff()
                        else:
                            WarningText(f"{selection.name} is not ready yet!").display()



                else:
                    return False
            except IndexError:
                return False

    def update_stats(self):
        def calculate(variable, multiplier=1):
            return variable * multiplier

        self.difficulty = int(1 + (self.experience.level / 20))
        self.health.set_default(int((calculate(self.experience.level, 57) + calculate(self.experience.level, calculate(self.star_rating.value, 2)) + calculate(self.experience.level, calculate(self.check_minimum(self.default_health_points, 4)))) + calculate(self.difficulty, 1000) + calculate(self.default_health_points, 10) + calculate(self.star_rating.value, 5)))
        self.attack.set_default(int((calculate(self.experience.level, 1.25) + calculate(self.star_rating.value, 1.50) + calculate(self.star_rating.value, calculate(self.check_minimum(self.default_attack_points))) + calculate(self.difficulty - 1, 20)) + 45 + calculate(self.check_minimum(self.default_attack_points, 3)) + calculate(self.star_rating.value, 3)))
        self.defense.set_default(int((calculate(self.experience.level, 2.25) + calculate(self.star_rating.value, 2.50) + calculate(self.star_rating.value, calculate(self.check_minimum(self.default_defense_points)))) + calculate(50, self.difficulty) + calculate(self.check_minimum(self.default_defense_points, 3)) + calculate(self.star_rating.value, 3)))
        self.critRate.set_default(float(self.star_rating.value + calculate(self.default_crit_rate_points, 2)))
        self.critDamage.set_default(float(50 + calculate(self.default_crit_damage_points, 5)))
        self.get_buff_values()

    def get_buff_values(self):
        buffs = self.create_buff_groups()
        health = 0
        attack = 0
        defense = 0
        critRate = 0
        critDamage = 0

        def determine_value(default_stat, buff):
            if buff.is_percent:
                return int(default_stat * (buff.value * 0.01))
            else:
                return buff.value

        for buff in buffs["health"]:
            health += determine_value(self.health.default_value, buff)

        for buff in buffs["attack"]:
            attack += determine_value(self.attack.default_value, buff)

        for buff in buffs["defense"]:
            defense += determine_value(self.defense.default_value, buff)

        for buff in buffs["critRate"]:
            critRate += determine_value(self.critRate.default_value, buff)

        for buff in buffs["critDamage"]:
            critDamage += determine_value(self.critDamage.default_value, buff)

        self.health.set_additional(health)
        self.attack.set_additional(attack)
        self.defense.set_additional(defense)
        self.critRate.set_additional(critRate)
        critDamage += (self.critRate.standalone_total_value - 100) if self.critRate.standalone_total_value > 100 else 0
        self.critDamage.set_additional(critDamage)

    def create_buff_groups(self):
        health = []
        attack = []
        defense = []
        critRate = []
        critDamage = []

        def check_buff(buff):
            if buff.attribute_type == StatTypes.Health:
                health.append(buff)
            elif buff.attribute_type == StatTypes.Attack:
                attack.append(buff)
            elif buff.attribute_type == StatTypes.Defense:
                defense.append(buff)
            elif buff.attribute_type == StatTypes.CritRate:
                critRate.append(buff)
            elif buff.attribute_type == StatTypes.CritDamage:
                critDamage.append(buff)

        if self.weapon is not None:
            check_buff(self.weapon.buff)

        for artifact in self.artifacts.content:
            if artifact is not None:
                check_buff(artifact.main_attribute)
                for attribute in artifact.attributes:
                    check_buff(attribute)

        return {
            "health": health,
            "attack": attack,
            "defense": defense,
            "critRate": critRate,
            "critDamage": critDamage,
        }

    def get_stats(self):
        return [
            self.health,
            self.attack,
            self.defense,
            self.critRate,
            self.critDamage
        ]

    def get_option(self):
        Text(self.__repr__()).display()
        return(get_int("1. level up\n"
                       "2. manage weapon\n"
                       "3. manage artifacts\n"
                       "4. equip character\n"
                       "5. back"))

    def jsonify(self):
        artifacts = []
        for artifact in self.artifacts.content:
            if artifact is not None:
                artifacts.append(artifact.jsonify())

        return {
            "stats": {
                "defense": self.default_defense_points,
                "attack": self.default_attack_points,
                "critDamage": self.default_crit_damage_points,
                "health": self.default_health_points,
                "critRate": self.default_crit_rate_points
            },
            "name": self.name,
            "description": self.description,
            "equips": {
                "weapon": self.weapon.jsonify() if self.weapon is not None else None,
                "artifacts": artifacts
            },
            "experience": {
                "level": self.experience.level,
                "xp": self.experience.xp
            },
            "star rating": self.star_rating.value
        }

    def create_enemy(self, weapon=Weapon()):
        enemy = Enemy(
            self.name,
            self.default_health_points,
            self.default_attack_points + self.default_crit_rate_points + self.default_crit_damage_points,
            self.default_defense_points,
            weapon,
            self.description
        )
        return enemy

    def __repr__(self):
        return (
            f"""
{self.name} {self.star_rating}
level {self.experience.level}
xp: {self.experience.xp} / {self.experience.get_xp_required(self.star_rating.value)} ({round((self.experience.xp / self.experience.get_xp_required(self.star_rating.value) * 100), 2)})%
{self.health}
{self.attack}
{self.defense}
{self.critRate}
{self.critDamage}
--------weapon--------
{self.weapon}
^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(0)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(1)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(2)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(3)}

^^^^^^^^artifact^^^^^^^^
{self.artifacts.get(4)}

skills: 
{f"{self.skills}" if not self.skills.is_empty() else 'This character has no skills...'}
====================
{DescriptionText(self.description).raw_output()}
====================
"""
        )
