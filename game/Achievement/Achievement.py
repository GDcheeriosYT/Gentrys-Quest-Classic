# game packages
# online packages
from Online.User.Aura import Aura


class Achievement:
    def __init__(self, name: str, is_completed: bool = False, reward: Aura = None):
        self.name = name
        self.is_completed = is_completed
        self.reward = reward