# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class BenMeier(Character):
    def __init__(self):
        super().__init__(
            "Ben Meier",
            description="Probably in the bathroom right now...",
            star_rating=StarRating(5),
            experience=None,
            weapon=None,
            default_attack_points=4
        )
