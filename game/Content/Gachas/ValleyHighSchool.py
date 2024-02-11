# game packages
# gacha packages
from Gacha.Gacha import Gacha

# graphics packages
from Graphics.Text.Text import Text
from Graphics.Text.Style import Style

# content packages
# characters
from Content.Characters.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.AlecFerchen import AlecFerchen
from Content.Characters.AsherLane import AsherLane
from Content.Characters.LucasSmidt import LucasSmidt
from Content.Characters.ConnorFogarty import ConnorFogarty
from Content.Characters.ConnorMoya import ConnorMoya
from Content.Characters.CharlieEddie import CharlieEddie
from Content.Characters.DavidNapier import DavidNapier
from Content.Characters.DylanTopic import DylanTopic
from Content.Characters.DyllonForney import DyllonForney
from Content.Characters.HannaHardy import HannaHardy
from Content.Characters.GMoney import GMoney
from Content.Characters.CalebJalan import CalebJalan
from Content.Characters.Benji import Benji
from Content.Characters.BrianHightower import BrianHightower
from Content.Characters.BrodyKrysa import BrodyKrysa
from Content.Characters.DerekCorona import DerekCorona
from Content.Characters.BryceAnderson import BryceAnderson
from Content.Characters.GavinKnudsen import GavinKnudsen
from Content.Characters.GrantArmstrong import GrantArmstrong
from Content.Characters.JoeNuts import JoeNuts
from Content.Characters.MasonJames import MasonJames
from Content.Characters.MaxShrum import MaxShrum
from Content.Characters.MaxTramontina import MaxTramontina
from Content.Characters.NathanTenney import NathanTenney
from Content.Characters.NolanAnderson import NolanAnderson
from Content.Characters.OliverStrauss import OliverStrauss
from Content.Characters.RyanMartinez import RyanMartinez
from Content.Characters.SeanMcbroom import SeanMcbroom
from Content.Characters.SethSmith import SethSmith
from Content.Characters.SpencerGeorge import SpencerGeorge
from Content.Characters.WillJohnson import WillJohnson
from Content.Characters.JaredQuitevis import JaredQuitevis
from Content.Characters.LukeEllens import LukeEllens
from Content.Characters.LinLaoShi import LinLaoShi
from Content.Characters.CarterBallard import CarterBallard
from Content.Characters.PeteMarks import PeteMarks
from Content.Characters.MJ import MJ
from Content.Characters.ZachSmith import ZachSmith
from Content.Characters.BenMeier import BenMeier

# weapons
from Content.Weapons.AlecsRock import AlecsRock
from Content.Weapons.AnubisBlade import AnubisBlade
from Content.Weapons.Bone import Bone
from Content.Weapons.BraydensOsuPen import BraydensOsuPen
from Content.Weapons.BrodysBroadsword import BrodysBroadsword
from Content.Weapons.Chopsticks import Chopsticks
from Content.Weapons.CoolWeapon import CoolWeapon
from Content.Weapons.CypireanScythe import CypireanScythe
from Content.Weapons.HomemadeStaffOfHoney import HomemadeStaffOfHoney
from Content.Weapons.Ichimonji import Ichimonji
from Content.Weapons.KnutsHammer import KnutsHamemr
from Content.Weapons.Messerschmidter import Messerschmidter
from Content.Weapons.Masonator import Masonator
from Content.Weapons.MasonKiller import MasonKiller
from Content.Weapons.NutBuster import NutBuster
from Content.Weapons.QuandaleDingle import QuandaleDingle
from Content.Weapons.SharpThrowingCards import SharpThrowingCards
from Content.Weapons.ShitLauncherSupreem import ShitLauncherSupreem
from Content.Weapons.SirFarQuad import SirFarQuad
from Content.Weapons.RatPoison import RatPoison
from Content.Weapons.DogLeg import DogLeg


class ValleyHighSchool(Gacha):
    def __init__(self):
        super().__init__(
            Text("Valley High School", Style(text_color="orange3")),
            [
                BraydenMesserschmidt(),
                AlecFerchen(),
                AsherLane(),
                LucasSmidt(),
                ConnorFogarty(),
                ConnorMoya(),
                CharlieEddie(),
                DavidNapier(),
                DylanTopic(),
                DyllonForney(),
                HannaHardy(),
                GMoney(),
                CalebJalan(),
                Benji(),
                BrianHightower(),
                BrodyKrysa(),
                DerekCorona(),
                BryceAnderson(),
                GavinKnudsen(),
                GrantArmstrong(),
                JoeNuts(),
                MasonJames(),
                MaxShrum(),
                MaxTramontina(),
                NathanTenney(),
                NolanAnderson(),
                OliverStrauss(),
                RyanMartinez(),
                SeanMcbroom(),
                SethSmith(),
                SpencerGeorge(),
                WillJohnson(),
                JaredQuitevis(),
                LukeEllens(),
                LinLaoShi(),
                LukeEllens(),
                CarterBallard(),
                PeteMarks(),
                MJ(),
                ZachSmith(),
                BenMeier()
            ],
            [
                AlecsRock(),
                AnubisBlade(),
                Bone(),
                BraydensOsuPen(),
                BrodysBroadsword(),
                Chopsticks(),
                CoolWeapon(),
                CypireanScythe(),
                HomemadeStaffOfHoney(),
                Ichimonji(),
                KnutsHamemr(),
                Messerschmidter(),
                Masonator(),
                MasonKiller(),
                NutBuster(),
                QuandaleDingle(),
                SharpThrowingCards(),
                ShitLauncherSupreem(),
                SirFarQuad(),
                RatPoison(),
                DogLeg()
            ],
            1000
        )
