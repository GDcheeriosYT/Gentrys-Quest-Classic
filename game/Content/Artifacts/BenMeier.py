# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class BensPants(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            name="Ben's Pants",
            star_rating=star_rating,
            family="Ben Meier",
            main_attribute=Buff(StatTypes.Defense)
        )


class Dumbbell(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            name="Dumbbell",
            star_rating=star_rating,
            family="Ben Meier",
            main_attribute=Buff(StatTypes.CritRate)
        )


class PopTart(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            name="Pop Tart",
            star_rating=star_rating,
            family="Ben Meier",
            main_attribute=Buff(StatTypes.Health)
        )


class EnergyDrink(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            name="Energy Drink",
            star_rating=star_rating,
            family="Ben Meier",
            main_attribute=Buff(StatTypes.CritDamage)
        )


class PocketKnife(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            name="Ben's Pants",
            star_rating=star_rating,
            family="Ben Meier",
            main_attribute=Buff(StatTypes.Attack)
        )
