import json

from Interface.Interface import Interface
from Interface.InterfaceContent import InterfaceContent

from Online.Server import Server
from Online.Account import AccountInfo


class Login(Interface):
    def __init__(self, server: Server, server_data: dict):
        super().__init__(f"Login to {server.url}", True)
        self.results = []
        if server.url in server_data.keys():
            for user in server_data[server.url]:
                self.results.append(AccountInfo(user["username"], user["password"]))
        else:
            server_data[server.url] = []
            json.dump(server_data, open("ServerData.json", "w"))

        self.results.append("Login to a new user")
        self.content = InterfaceContent(
            "Select a User",
            self.results,
            False
        )
