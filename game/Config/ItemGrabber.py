# this is for developer purposes :)
import pyperclip
import json

# <editor-fold desc="Code">

if __name__ == "__main__":

    from Content.Weapons.CoolWeapon import CoolWeapon

    pyperclip.copy(json.dumps(CoolWeapon().jsonify()))

# </editor-fold>
