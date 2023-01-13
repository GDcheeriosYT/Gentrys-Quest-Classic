# game packages
# entity packages
from Entity.Artifact.Artifact import Artifact
from Entity.Stats.Buff import Buff
from Entity.Stats.StatTypes import StatTypes


class WintonOverwatAmulet(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "A Winton Overwat Amulet",
            star_rating,
            "Ohio",
            Buff(StatTypes.Attack)
        )

class AmongUsGlasses(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Among Us Glasses",
            star_rating,
            "Ohio",
            Buff(StatTypes.CritRate)
        )


class SaulGoodmansMoney(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Saul Goodman's Money",
            star_rating,
            "Ohio",
            Buff(StatTypes.Health)
        )


class ElonMusksPhone(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Elon Musk's Phone",
            star_rating,
            "Ohio",
            Buff(StatTypes.CritRate)
        )

class WalterWhitesDropPhone(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Walter White's Drop Phone",
            star_rating,
            "Ohio",
            Buff(StatTypes.CritDamage)
        )

class LiverKingsLiver(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Walter White's Drop Phone",
            star_rating,
            "Ohio",
            Buff(StatTypes.Health)
        )

class BarbariansSword(Artifact):
    def __init__(self, star_rating):
        super().__init__(
            "Barbarian's Sword",
            star_rating,
            "Ohio",
            Buff(StatTypes.Attack)
        )




