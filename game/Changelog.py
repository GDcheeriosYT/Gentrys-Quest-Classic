# game packages
# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style
from Graphics.Content.Text.InfoText import InfoText

# IO packages
from IO.Input import enter_to_continue
from IO import Window

# change log groupings
gameplay = [
    InfoText("Changed character pull rates in gacha by GDcheerios"),
    InfoText("Added GP display to inventory by GDcheerios")
]
graphics = []
content = []
online = [
    InfoText("Changed leaderboard user display amount to match height of window by GDcheerios")
]
code_structure = [
    InfoText("Updated required libraries by GDcheerios"),
    InfoText("Made game class static by GDcheerios")
]
testing = []


def display_changelog(version: str):
    Window.clear()
    Window.place_rule(f"Changelog {version}")
    if len(gameplay) > 0:
        Window.place_rule("Gameplay")
        for gameplay_change in gameplay:
            gameplay_change.display()

    if len(graphics) > 0:
        Window.place_rule("Graphics")
        for graphics_change in graphics:
            graphics_change.display()

    if len(content) > 0:
        Window.place_rule("Content")
        for content_change in content:
            content_change.display()

    if len(online) > 0:
        Window.place_rule("Online")
        for online_change in online:
            online_change.display()

    if len(code_structure) > 0:
        Window.place_rule("Code Structure")
        for code_structure_change in code_structure:
            code_structure_change.display()

    if len(testing) > 0:
        Window.place_rule("Testing")
        for testing_change in testing:
            testing_change.display()

    print("\n")

    enter_to_continue()
