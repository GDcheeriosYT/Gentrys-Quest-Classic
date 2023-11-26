# game packages
# entity packages
from .StatTypes import StatTypes


class Stat:

    type = None
    default_value = None
    additional_value = None
    total_value = None
    max_value = None

    def __init__(self, type: StatTypes, max_value=None):
        self.type = type
        self.max_value = max_value
        self.total_value = 0
        self.standalone_total_value = 0
        self.default_value = 0
        self.additional_value = 0
        self.calculate_total()

    def set_default(self, value):
        self.default_value = value
        self.calculate_total()

    def set_additional(self, value):
        self.additional_value = value
        self.calculate_total()

    def calculate_total(self):
        if self.max_value is not None:
            if (self.default_value + self.additional_value) > self.max_value:
                self.total_value = self.max_value
            else:
                self.total_value = self.default_value + self.additional_value
        else:
            self.total_value = self.default_value + self.additional_value

        self.standalone_total_value = self.default_value + self.additional_value

    def __repr__(self):
        return f"{self.type.name}: {self.default_value if self.additional_value > 0 else self.total_value} {f'+ {self.additional_value} ({self.total_value})' if self.additional_value > 0 else ''}{'%' if isinstance(self.default_value, float) else ''}"
