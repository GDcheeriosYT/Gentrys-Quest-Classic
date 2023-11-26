class AccountInfo:
    """
    provider of account info

    parameters
    username: string
        the username of the account

    password: string
        the password of the account
    """

    username = None
    password = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username}"
