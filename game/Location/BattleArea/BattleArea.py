# game packages
# location packages
from ..Area.Area import Area
from .Difficulty import Difficulty

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style
from Graphics.Content.Text.WarningText import WarningText

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Entity import Entity
from Entity.Enemy.Enemy import Enemy
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Effect.Effect import Effect
from Entity.Stats.Effect.LiveEffect import LiveEffect

# IO packages
from IO.Input import get_int, enter_to_continue
from IO import Window

# content packages
from Content.ArtifactContentManager import ArtifactContentManager

# random packages
from Random.Functions import generate_artifact_star_rating

# built-in packages
import random
from copy import deepcopy


class EndException(Exception):
    pass


class BattleArea(Area):
    """
    Makes a battle area.
    """

    name = None
    difficulty = None

    def __init__(self, name, difficulty=0, artifact_families=ItemList(content_type=str),
                 enemies=ItemList(content_type=Enemy), is_runnable=True, difficulty_scales=True,
                 difficulty_scales_after=0, difficulty_setback=0, effects=None):
        super().__init__(name)
        self.name = Text(name, Style(text_color="red")).raw_output()
        self.difficulty = Difficulty(difficulty)
        self.artifact_families = artifact_families
        self.enemies = enemies
        self.is_runnable = is_runnable
        self.difficulty_scales = difficulty_scales
        self.difficulty_scales_after = difficulty_scales_after
        self.difficulty_setback = difficulty_setback
        if effects is None:
            self.effects = ItemList(content_type=Effect)
        else:
            self.effects = effects

    def get_difficulty(self, difficulty):
        difficulty -= 1

        def check_difficulty(difficulty_to_check):
            if difficulty_to_check >= 0:
                return difficulty_to_check
            else:
                return 0

        if self.difficulty_scales:
            if difficulty > self.difficulty_scales_after:
                return check_difficulty(difficulty + self.difficulty.value - self.difficulty_setback)
            else:
                return check_difficulty(self.difficulty.value - self.difficulty_setback)
        else:
            return self.difficulty.value

    @staticmethod
    def apply_random_level(number):
        def get_min(number, difference):
            while number - difference <= 0:
                difference -= 1
            return difference

        def get_max(number, difference):
            while number + difference >= 20:
                difference -= 1

            return difference

        number_diff = 3
        min = get_min(number, number_diff)
        max = get_max(number, number_diff)
        return number + random.randint(-abs(min), max)

    def initialize_enemies(self, character):
        enemies = []
        difficulty = self.get_difficulty(character.difficulty)
        if difficulty == 0:
            difficulty = 1

        difficulty_points = difficulty * 10
        while difficulty_points > 0:
            points = 0
            enemy = deepcopy(random.choice(self.enemies.content))
            points += (5 + (enemy.health_points * 2) + (enemy.attack_points * 2.5) + (enemy.defense_points * 1.5))
            level = self.apply_random_level(character.experience.level % 20)
            enemy.experience.level = (20 * (self.get_difficulty(character.difficulty))) + level
            if (random.randint(1, 80) < difficulty * 10) and (self.effects.get_length() != 0):
                effect = random.choice(self.effects.content)
                effect = effect()
                if enemy.effects.get_length() == 0:
                    enemy.effects.add(effect)
                for effect1 in enemy.effects.content:
                    if effect1.details.name.content == effect.details.name.content:
                        enemy.effects.content[enemy.effects.content.index(effect1)].level_up()
                    else:
                        enemy.add_effect(effect)

                points *= 2
            enemy.update_stats()
            enemies.append(enemy)
            difficulty_points -= points

        return enemies

    def initialize_artifacts(self, difficulty, families):
        points = (self.get_difficulty(difficulty) + 1) * 50
        artifacts = []
        artifacts_to_choose_from = []
        for family in self.artifact_families.content:
            for family1 in families:
                if family == family1.name:
                    for artifact in family1.artifacts:
                        artifacts_to_choose_from.append(artifact)

        while points > 0:
            if len(artifacts_to_choose_from) > 0:
                artifact = random.choice(artifacts_to_choose_from)
                star_rating = generate_artifact_star_rating(self.get_difficulty(difficulty) + 1)
                artifact = artifact(StarRating(star_rating))
                artifacts.append(artifact)
                if star_rating == 1:
                    points -= 25

                elif star_rating == 2:
                    points -= 45

                elif star_rating == 3:
                    points -= 65

                elif star_rating == 4:
                    points -= 75

                else:
                    points -= 100

            else:
                break

        return artifacts

    @staticmethod
    def results(percentage, money=0, xp=0, artifacts=None):
        Window.place_rule("Battle Area Results")
        Text(f"completion {percentage}%\n"
             "You received:\n"
             f"${money}\n"
             f"{xp}xp\n").display()
        if artifacts is not None:
            print("\tartifacts")
            for artifact in artifacts.content:
                Text(artifact).display()

        enter_to_continue()
        raise EndException

    def start(self, character, inventory, content):
        turn_counter = 0
        try:
            if character is None:
                WarningText("You do not have a character equipped!").display()
                raise EndException
            character.update_stats()
            character_effects = []
            Text(f"You enter {self.name}!").display()
            enemies = ItemList(content_type=Enemy, content=self.initialize_enemies(character))
            artifacts = ItemList(content_type=Artifact, content=self.initialize_artifacts(character.difficulty, content.families))
            enemies_killed = 0
            money = 0
            xp = 0
            percentage = 0

            def calculate_percentage():
                nonlocal percentage
                percentage = int((enemies_killed / len(enemies.content)) * 100)

            for enemy in enemies.content:
                enemy_effects = []
                calculate_percentage()
                Text(f"{character.name} encountered a {enemy}").display()
                enemy.show_stats()
                while True:
                    Text(f"\n{enemy.name if turn_counter != 0 else ''} {enemy.health if turn_counter != 0 else ''}\n"
                         f"{character.name} {character.health.total_value}\n").display()
                    options = character.get_battle_options()
                    if self.is_runnable:
                        options.append("run")

                    for option in options:
                        print(f"{options.index(option) + 1}. {option}")

                    if character.manage_battle_input(get_int(""), enemy, options):
                        for effect in character.effects.content:
                            if turn_counter % effect.variables.round_cooldown == 0:
                                enemy_effects.append(LiveEffect(effect.details, effect.variables))
                        if enemy.health.total_value <= 0:
                            Text(f"{enemy.name} is dead\n"
                                 f"you received ${enemy.get_money()} and {enemy.get_xp()}xp").display()
                            xp += enemy.get_xp()
                            money += enemy.get_money()
                            inventory.money += enemy.get_money()
                            character.add_xp(enemy.get_xp())
                            enter_to_continue()
                            break
                        else:
                            for effect in enemy_effects:
                                effect.affect(enemy)
                            enemy.attack_character(character)
                            for effect in enemy.effects.content:
                                if turn_counter % effect.variables.round_cooldown == 0:
                                    character_effects.append(LiveEffect(effect.details, effect.variables))
                            if character.health.total_value <= 0:
                                WarningText(f"{character.name} has died").display()
                                enter_to_continue()
                                self.results(percentage, money, xp)

                            for effect in character_effects:
                                effect.affect(character)
                    else:
                        if self.is_runnable:
                            self.results(percentage, money, xp)
                        else:
                            WarningText("Not a valid option!").display()

                    turn_counter += 1

                enemies_killed += 1
                calculate_percentage()

            for artifact in artifacts.content:
                inventory.artifact_list.add(artifact)

            self.results(percentage, money, xp, artifacts)
        except EndException:
            if character is not None:
                character.update_stats()
            pass

    def __repr__(self):
        return f"{self.name} {self.difficulty.__repr__()}"
