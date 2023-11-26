from Config.ListSetting import ListSetting
from Config.NumberSetting import NumberSetting
from Config.StringSetting import StringSetting
from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent
from Online.Room import Room
from Online.GameTypes import GameTypes


class RoomCreation(Interface):
    def __init__(self):
        super().__init__("Room creation")
        self.content = InterfaceContent(
            "Room details",
            [
                StringSetting("Name", "room name"),
                StringSetting("Password", ""),
                NumberSetting("Limit", 0, 0),
                ListSetting("Mode", "Uno", ["Uno"]),
                "Done"
            ],
            True
        )

    def visit(self, clear_window=True, return_type: bool = False):
        result = super().visit(clear_window, return_type)
        if isinstance(result, StringSetting):
            result.change()

        elif isinstance(result, NumberSetting):
            result.change_value()

        elif isinstance(result, ListSetting):
            result.select()

        else:
            if result == "Done":
                return True

            else:
                return False

    def get_room(self) -> Room:
        config = self.content.options
        return Room(
            config[0].text,
            config[1].text,
            config[2].value,
            GameTypes.Uno
        )
