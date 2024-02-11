# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class DogLeg(Weapon):
    def __init__(self):
        super().__init__(
            "Dog Leg",
            "My mom took my dog but not before I got it's leg.",
            "Dog Leg",
            29,
            Buff(StatTypes.Health),
            Verbs("swung at", "beat"),
            StarRating(2)
        )