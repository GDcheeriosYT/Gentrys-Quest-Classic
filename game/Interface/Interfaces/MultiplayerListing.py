from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from Online.Room import Room
from Online.GameTypes import GameTypes


class MultiplayerListing(Interface):
    def __init__(self, server):
        super().__init__("Multiplayer Listing", True)
        self.content = InterfaceContent(
            "Rooms",
            ["Create Room"],
            False
        )

        rooms = server.API.get_multiplayer_rooms()
        for room in rooms.keys():
            name = room
            room = rooms[room]
            room = Room(
                name,
                room["room password"],
                room["limit"],
                GameTypes.Uno
            )

            self.content.options.append(room)

        self.content.options.append("back")
