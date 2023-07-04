# game packages


class User:
    """
    makes a user object

    parameters
    username: string
        the username of the user

    powerlevel: PowerLevel
        the powerlevel of the user

    aura: Aura
        the aura of the user
    """

    id = None
    username = None
    powerlevel = None
    aura = None

    def __init__(self, id: int, username: str, powerlevel: int = 0):
        self.id = id
        self.username = username
        self.powerlevel = powerlevel
        self.ranking = "unranked"

    def __repr__(self):
        return f"#{self.ranking} {self.username} {self.powerlevel}gp"