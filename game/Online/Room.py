# collection packages
from Collection.ItemList import ItemList

# online packages
from .GameTypes import GameTypes
from .User.User import User


class Room:
    def __init__(self, name: str, password: str, limit: int, game_type: GameTypes):
        self.name = name
        self.password = password
        self.limit = limit
        self.users = ItemList(limit, User)
        self.game_type = game_type

    def jsonify(self):
        return {
            "room name": self.name,
            "room password": self.password,
            "limit": self.limit,
            "users": [],
            "game type": self.game_type.value
        }

    def __repr__(self):
        return f"{self.name} {'[LOCKED]' if self.password != '' else '[OPEN]'} {self.users.get_length()}/{self.limit} {self.game_type}"
