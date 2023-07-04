# game packages
# entity packages
from Entity.Character.Character import Character
from Entity.Character.Skill import Skill
from Entity.Stats.StarRating import StarRating


class NewTopPlay(Skill):
    def __init__(self):
        super().__init__(
            "New Top Play",
            "Achieve a new top play and deal damage based on the play value.",
            4
        )


class BraydenMesserschmidt(Character):
    def __init__(self):
        super().__init__(
            "Brayden Messerschmidt",
            "An osu player who formed a contract with ppy(Dean Herbert) to not talk to females.",
            StarRating(5),
            None,
            None,
            default_crit_rate_points=4
        )

        self.skills.add_skill(NewTopPlay())
