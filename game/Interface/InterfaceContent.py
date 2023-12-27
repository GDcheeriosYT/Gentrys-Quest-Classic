class InterfaceContent:
    """
    Makes content for an Interface

    parameters

    info: Text or String
        the main content of the interface

    options: list
        the list of options
    """

    content = None

    def __init__(self, info="this is an interface", options=["do nothing"], contain_back: bool = True):
        self.info = info
        self.options = options
        if contain_back:
            self.options.append("back")

    def show_options(self):
        string = ""
        for option in self.options:
            string += f"{self.options.index(option) + 1}. {option}\n"

        return string
