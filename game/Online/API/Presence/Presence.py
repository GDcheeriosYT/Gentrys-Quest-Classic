from pypresence import Presence


class GamePresence:
    def __init__(self):
        try:
            self.id = 1115885237910634587
            self.RPC = Presence(self.id)
            self.RPC.connect()
        except:
            pass

    def update_status(self, state: str, details: str = None):
        try:
            self.RPC.update(
                state=state,
                details=details
            )
        except:
            pass

    def end(self):
        try:
            self.RPC.close()
        except:
            pass
