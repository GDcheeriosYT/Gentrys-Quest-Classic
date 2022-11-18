# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class BryceAnderson(Character):
    def __init__(self):
        super().__init__(
            "Bryce Anderson",
            "Tall guy.",
            StarRating(5),
            None,
            None,
            default_health_points=1,
            default_attack_points=2,
            default_crit_damage_points=1
        )
