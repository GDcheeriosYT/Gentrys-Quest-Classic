# game packages
# IO packages
from IO.Input import get_int

# graphics packages
from Graphics.Text.Text import Text

class Dictionary:
    def __init__(self, pages: list, page_content: list):
        self.pages = pages
        self.page_content = page_content

    def read(self):
        counter = 0
        while True:
            Text(self.pages[counter]).display()
            for content in self.page_content[counter]:
                Text(f"\t{content}").display()

            option_string = ""
            one = False
            two = False
            if counter > 0:
                one = True
                option_string += "1. previous page\n"

            if counter < len(self.pages)-1:
                two = True
                option_string += "2. next page\n"

            option_string += "3. back\n"

            option = get_int(option_string)

            if option == 1 and one:
                counter -= 1

            elif option == 2 and two:
                counter += 1

            else:
                break