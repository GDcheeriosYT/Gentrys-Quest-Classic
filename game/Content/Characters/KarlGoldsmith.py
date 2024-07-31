# game pakcages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class KarlGoldsmith(Character):
    """
    Skill:

    Can manipulate the elements around the character.  (like Magneto from Xmen)

    """

    def __init__(self):
        super().__init__(
            "Karl Goldsmith",
            "Master of Chemicals",
            StarRating(5),
            default_health_points=2,
            default_attack_points=1,
            default_defense_points=1
        )
