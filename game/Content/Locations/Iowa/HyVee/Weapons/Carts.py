# game packages
# entity packages
from Entity.Weapon.Weapon import Weapon
from Entity.Stats.Buff import Buff
from Entity.Weapon.Verbs import Verbs
from Entity.Stats.StarRating import StarRating
from Entity.Stats.Experience import Experience


class Carts(Weapon):
    def __init__(self):
        super().__init__(
            "Carts",
            "Hyvee carts",
            "Cart",
            0,
            Buff(),
            Verbs("rammed into", "wiped out on"),
            StarRating(1),
            Experience()
        )
