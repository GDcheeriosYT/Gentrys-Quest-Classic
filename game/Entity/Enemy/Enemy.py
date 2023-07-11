# game packages
# entity packages
from ..Entity import Entity
from ..Weapon.Weapon import Weapon
from ..Stats.Experience import Experience
from ..Stats.Stat import Stat
from ..Stats.StatTypes import StatTypes

# config packages
from Config.StringSetting import StringSetting
from Config.NumberSetting import NumberSetting
from Config.ClassSetting import ClassSetting
from Config.SettingManager import SettingManager

# IO packages
from IO import Window
from IO.Input import enter_to_continue

# random packages
from Random.Functions import determine_crit

# graphics packages
from Graphics.Text.Text import Text

# built-in packages
import random


class Enemy(Entity):
    """
    makes an enemy

    parameters

    name: string
        the name of the enemy

    health: int
        the health points

    attack: int
        the attack points

    defense: int
        the defense points

    weapon: Weapon
        the weapon that the enemy will carry

    description: string
        the description of the enemy
    """

    def __init__(self, name="enemy", health=0, attack=0, defense=0, weapon=Weapon(), description=None,
                 experience=Experience()):
        super().__init__(name, description, 0, experience)
        self.health = Stat(StatTypes.Health)
        self.attack = Stat(StatTypes.Attack)
        self.defense = Stat(StatTypes.Defense)
        self.damage_negation = 0.005
        self.health_points = health
        self.attack_points = attack
        self.defense_points = defense
        self.weapon = weapon
        self.settings = [
            StringSetting("name", self.name),
            NumberSetting("health", self.health_points, 0),
            NumberSetting("attack", self.attack_points, 0),
            NumberSetting("defense", self.defense_points, 0),
            ClassSetting("weapon", self.weapon),
            StringSetting("description", self.description),
            NumberSetting("level", self.experience.level)
        ]
        self.update_stats()

    def update_stats(self):
        def calculate(variable, multiplier=1):
            return variable * multiplier

        #  follow this for stat help https://genshin-impact.fandom.com/wiki/Level_Scaling/Enemy#:~:text=For%20enemies%2C%20their%20HP%2C%20ATK,are%201%20for%20all%20levels
        difficulty = 1 + (self.experience.level / 20)
        self.health.set_default(int(calculate(500, difficulty) + calculate(self.experience.level, (5 + calculate(self.experience.level, 0.18 + calculate(difficulty, 0.09))) + calculate(self.health_points, 5))))
        self.attack.set_default(int(calculate(30, difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.04 + calculate(difficulty, 0.007))) + calculate(self.attack_points, 2))))
        self.defense.set_default(int(calculate(7, difficulty) + calculate(self.experience.level, (calculate(self.experience.level, 0.03 + calculate(difficulty, 0.006))) + calculate(self.defense_points, 2))))
        if difficulty >= 10:
            self.damage_negation = round(0.05 + calculate(0.001, (difficulty - 10)), 3)
        else:
            self.damage_negation = round(calculate(0.005, difficulty), 3)

    def attack_character(self, character):
        is_crit = determine_crit(20)
        damage = int(self.attack.total_value + ((self.attack.total_value * 0.50) if is_crit else 0))
        defense = int(self.defense.total_value * 0.99) + int(damage * 0.01)
        damage -= defense
        Text(
            f"{self.name} {self.weapon.verbs.critical if is_crit else self.weapon.verbs.normal} {character.name} for {damage} damage").display()
        if damage <= 0:
            Text(f"{character.name} has dodged").display()
        else:
            character.health.total_value -= damage
        enter_to_continue()

    def get_stats(self):
        return [
            self.health,
            self.attack,
            self.defense
        ]

    def get_money(self):
        money = 0
        money += self.defense_points * 1.5
        money += self.attack_points * 2.5
        money += self.health_points * 2
        money += self.experience.level
        return int(money)

    def get_xp(self):
        xp = 0
        xp += self.defense_points * 0.5
        xp += self.attack_points * 1.5
        xp += self.health_points * 1
        xp += self.experience.level * 5
        return int(xp)

    def test(self):
        Window.clear()
        Text(self.__repr__()).display()
        self.show_stats()
        self.settings = SettingManager(self.settings).config_settings()
        self.name = self.settings[0].text
        self.health_points = self.settings[1].value
        self.attack_points = self.settings[2].value
        self.defense_points = self.settings[3].value
        self.weapon = self.settings[4].instance_class
        self.description = self.settings[5].text
        self.experience.level = self.settings[6].value
        self.update_stats()
        return self

    def show_stats(self):
        Text(f"{self.health}\n"
             f"{self.attack}\n"
             f"{self.defense}\n"
             f"{self.description}\n").display()
        if self.effects.get_length() != 0:
            print("effects:")
            for effect in self.effects.content:
                effect.details.show_details()

    def __repr__(self):
        return f"{self.name} level {self.experience.level}"
