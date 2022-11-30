# game packages
# effect packages
from .EffectDetails import EffectDetails
from .EffectVariables import EffectVariables


class Effect:
    def __init__(self, details: EffectDetails, variables: EffectVariables):
        self.details = EffectDetails
        self.variables = EffectVariables
