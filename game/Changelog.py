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
    InfoText("Added Changelog! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/35]PR\[#35][/link] by GDcheerios"),
    InfoText("Reworked scaling! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/44]PR\[#44][/link] by GDcheerios"),
    InfoText("Added credits! by GDcheerios"),
    InfoText("Changed Gacha to give duplicate weapons rather than upgrading weapons! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/47]PR\[#47][/link] by GDcheerios"),
    InfoText("Added multiple selection of items when upgrading weapon or artifacts! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/47]PR\[#47][/link] by GDcheerios"),
    InfoText("Added visualization of item after leveling up! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/47]PR\[#47][/link] by GDcheerios"),
    InfoText("Reworked Inventory Functions! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/47]PR\[#47][/link] by GDcheerios"),
    InfoText("Added display of what character you have equipped when in travel menu! by GDcheerios")
]
graphics = []
content = [
    InfoText("Added Nigeria location! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/41]PR\[#41][/link] by GDcheerios"),
    InfoText("Added content to Brayden's House by GDcheerios"),
    InfoText("Added Ohio location! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/42]PR\[#42][/link] by CarlBla123"),
    InfoText("Added China location! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/42]PR\[#42][/link] by CarlBla123"),
    InfoText("Added Nigeria location! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/41]PR\[#41][/link] by GDcheerios"),
    InfoText("Added content to Brayden's House! by GDcheerios"),
    InfoText("Added Gentry's House location! by GDcheerios")
]
online = [
    InfoText("Added online features! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/49]PR\[#49][/link] by GDcheerios")
]
code_structure = [
    InfoText("Changed enemy initialization in battle area to use deepcopy()! by GDcheerios")
]
testing = [
    InfoText("Added Changelog View Testing! [link=https://github.com/GDcheeriosYT/Gentrys-Quest-Python/pull/35]PR\[#35][/link] by GDcheerios")
]


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

    enter_to_continue()
