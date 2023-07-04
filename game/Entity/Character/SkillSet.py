# game packages
# collection packages
from Collection.ItemList import ItemList

# entity packages
from .Skill import Skill


class SkillSet:
    def __init__(self, limit: int):
        self.skills = ItemList(limit, Skill)

    def add_skill(self, skill: Skill):
        self.skills.add(skill)

    def is_empty(self):
        return self.skills.get_length() == 0

    def __repr__(self):
        string = ""
        for skill in self.skills.content:
            string += f"{skill.text_output()}\n"

        return string
