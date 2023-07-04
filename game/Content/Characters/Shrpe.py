# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class Shrpe(Character):
    def __init__(self):
        super().__init__(
            "Shrpe",
            "Child prodigy who also specializes in making cupcakes for the the once famous Philadelphia eagles superfan.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=1,
            default_attack_points=3
        )
