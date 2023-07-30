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
        self.placement = 0
        self.ranking = "unranked", ''

    def __repr__(self):
        ranking_string = f"{self.ranking[0]}[{self.ranking[1]}]" if self.ranking[0] != "" else "unranked"
        return f"#{self.placement} {self.username} {self.powerlevel}gp {ranking_string}"
