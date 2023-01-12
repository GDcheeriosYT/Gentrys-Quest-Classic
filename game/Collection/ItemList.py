# game packages
# graphics packages
from Graphics.Content.Text.WarningText import WarningText
from Graphics.Text.Text import Text

# IO packages
from IO import Window
from IO.Input import get_int, get_range_or_int

# external packages
from rich.console import Console

# Collection packages
from .RangeGroup import RangeGroup

class ItemList:
    """
    Makes an ItemList

    an ItemList is a special type of list. It can have a specified size and a specified type of "thing".
    say you want to hold a maximum of 8 tacos. It will only allow for 8 things of the type Taco.

    parameters

    size: int
        the maximum size of the list

    content_type: class type
        the content that will be filled in the list
    """

    size = None
    content_type = None

    def __init__(self, size: int = None, content_type=None, fill: bool = False, output: bool = True, content: list = None):
        if content is None:
            self.content = []
        else:
            self.content = content
        self.size = size
        if fill and size is not None:
            for i in range(size):
                self.content.append(None)
        self.content_type = content_type
        self.output = output
        self.selections = []

    def add(self, item):
        if isinstance(item, self.content_type):
            if self.check_item_and_space(item):
                if None in self.content:
                    self.content[self.content.index(None)] = item
                else:
                    self.content.append(item)

            elif None in self.content:
                self.content[self.content.index(None)] = item

            else:
                if self.output:
                    WarningText(
                        f"The {type(item)} {item.name} isn't accepted in this list. \nEither it's full or it doesn't accept {type(item)}").display()

    def remove(self):
        for item in self.content:
            Console().print(f"{self.content.index(item) + 1}. {item}")

        selection = input("which item would you like to remove?\n")
        try:
            return self.content.pop(self.content.index(int(selection) - 1))
        except IndexError:
            WarningText(f"Couldn't find item at {selection}").display()

    def fill(self, list):
        for item in list:
            self.add(item)

    def get(self, index):
        try:
            return self.content[index]
        except IndexError:
            return None

    def check_item_and_space(self, item, supports_none=False):
        if isinstance(item, self.content_type) or self.content_type is None:
            if self.size is not None:
                if (len(self.content) < self.size) or (None in self.content):
                    return True
                else:
                    return False
            else:
                return True
        else:
            if supports_none:
                if self.size is not None:
                    if (len(self.content) < self.size) or (None in self.content):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

    def set(self, index, item, supports_none=False):
        try:
            if supports_none and item is None:
                self.content[index] = item
            elif not supports_none and item is not None:
                self.content[index] = item
            elif supports_none and item is not None:
                self.content[index] = item
            else:
                WarningText(
                    f"The {type(item)} {item} isn't accepted in this list. \nEither it's full or it doesn't accept {type(item)}").display()
        except IndexError:
            WarningText(f"Can't put that here").display()

    def test(self):
        while True:
            try:
                Window.clear()
                counter = 1
                for item in self.content:
                    print(f"{counter}. {item}")
                    counter += 1
                print(f"{counter}. back")
                num = int(input())
                if self.content[num - 1] is None:
                    self.content[num - 1] = self.content_type("Test Item")
                    self.content[num - 1] = self.content[num - 1].test()
                else:
                    self.content[num - 1] = self.content[num - 1].test()
            except ValueError:
                Window.clear()
                WarningText("Not a number!").display()
            except NameError:
                WarningText("Couldn't find a test method for this class").display()
                break
            except IndexError:
                break

    def delete_after(self, index):
        x = len(self.content) - 1
        while x != index:
            self.content[x].pop()
            x -= 1

    def get_selections(self):
        selections = []
        for index in self.selections:
            selections.append(self.content[index])

        return selections

    def list_content(self, display_number: bool = True):
        for item in self.content:
            if hasattr(item, "list_view"):
                item_string = item.list_view()
            else:
                item_string = item
            color = "[green on black]" if self.content.index(item) in self.selections else "[white on black]"
            if display_number:
                Text(f"{color}{self.content.index(item) + 1}. {item_string}").display()
            else:
                Text(f"{color}{item_string}").display()

        if display_number:
            print("0. back")

    def change_limit(self, amount):
        Window.clear()
        if amount < self.size:
            WarningText(
                "You are lowering the size.\nThis could permanently delete stuff.\nAre you sure you want to continue?\n").display()
            num = get_int("1. yes\n2. no")
            if num == 1:
                self.size = amount
                self.delete_after(self.size)

    def get_length(self):
        return len(self.content)

    def get_index(self, item):
        return self.content.index(item)

    def select(self, single: bool = True, remove: bool = True, list_content: bool = True):
        if self.get_length() == 0:
            WarningText("This list is empty...").display()
            return None

        if list_content:
            self.list_content(True)

        if single:
            index = get_int("pick one\n") - 1
            if index < 0 or index >= self.get_length():
                return ""
            item = self.content[index]
            if remove:
                self.content.pop(index)
            return item

        else:
            selection = get_range_or_int("provide a number or range to select items \n type \"done\" when done with selecting items")
            Window.clear()
            if isinstance(selection, int):
                if selection == 0:
                    self.selections = []
                    return None
                elif selection - 1 >= self.get_length():
                    WarningText("This is not in the list!").display()
                    return ""

                else:
                    selection -= 1
                    if selection in self.selections:
                        self.selections.remove(selection)
                    else:
                        self.selections.append(selection)

                    return ""

            elif isinstance(selection, list):
                for range_group in selection:
                    x = range_group.start_index
                    if range_group.end_index >= self.get_length():
                        range_group.end_index = self.get_length() - 1
                    while x <= range_group.end_index:
                        if x in self.selections:
                            self.selections.remove(x)
                        else:
                            self.selections.append(x)

                        x += 1

                return ""

            else:
                if selection == "done":
                    selection_copy = self.selections
                    self.selections = []
                    return selection_copy

    def jsonify(self):

        """
        assuming all the items in the list have a jsonify method it will return jsonified item data
        """

        data = []
        for item in self.content:
            data.append(item.jsonify())

        return data

    def __repr__(self):
        return str({
            "size": self.size,
            "content type": self.content_type,
            "content": self.content
        })
