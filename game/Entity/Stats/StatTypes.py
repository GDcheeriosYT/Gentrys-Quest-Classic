from enum import Enum


class StatTypes(Enum):
    Health = 1
    Attack = 2
    Defense = 3
    CritRate = 4
    CritDamage = 5

    def abreviate(self):
        if self.value == 1:
            return "HP"

        elif self.value == 2:
            return "AT"

        elif self.value == 3:
            return "DF"

        elif self.value == 4:
            return "CR"

        else:
            return "CD"

    def __repr__(self):
        return self.name
