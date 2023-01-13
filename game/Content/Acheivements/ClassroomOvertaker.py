# game packages
# achievement pacakges
from Achievement.Achievement import Achievement
from Achievement.Achievement import Aura

# content pacakges
from Content.Auras.Gamer import Gamer


class ClassroomOvertaker(Achievement):
    def __init__(self):
        super().__init__(
            "Classroom Overtaker",
            reward=Gamer()
        )