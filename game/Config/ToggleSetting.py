import Setting


class ToggleSetting(Setting):
    """
    child of Setting.
    returns a toggleable setting

    parameters

    toggled: boolean
        if setting should be toggled or not
    """

    toggled = None

    def __init__(self, name="setting", toggled=False):
        super().__init__(name)
        self.toggled = toggled

    def __repr__(self):
        return f"{super()} [{self.toggled}]"
