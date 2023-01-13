# game packages
# IO packages
from IO.Input import get_int

# graphics packages
from Graphics.Text.Text import Text


class CheckPoint:
    def will_continue(self):
        Text(f"You're at a checkpoint!").display()
        option = get_int("1. continue\n"
                         "2. exit")

        if option == 1:
            return True
        else:
            return False
