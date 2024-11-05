from Entity.Character.Character import Character
from Entity.Stats.StarRating import StarRating


class MekhiElliot(Character):
    def __init__(self):
        super().__init__(
            "Mekhi Elliot",
            "Big biggest and baddest gentry warrior the biggest alpha sigma of them all.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=4
        )
