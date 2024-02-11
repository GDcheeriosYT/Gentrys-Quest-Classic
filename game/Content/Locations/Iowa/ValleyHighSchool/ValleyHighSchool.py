# game packages
# location packages
from Location.BattleArea.BattleArea import BattleArea

# collection packages
from Collection.ItemList import ItemList

# entity packages
from Entity.Enemy.Enemy import Enemy

# content packages
# enemies
from .Enemies.FeralLunchLady import FeralLunchLady
from .Enemies.FlyingPencil import FlyingPencil
from .Enemies.MrBakey import MrBakey
from .Enemies.RacoonInsideABackpack import RacoonInsideABackpack
from .Enemies.TheWierdStudent import TheWeirdStudent
from .Enemies.TheLocalSecurityGuard import TheLocalSecurityGuard
from Content.Characters.AlecFerchen import AlecFerchen
from Content.Characters.AsherLane import AsherLane
from Content.Characters.Benji import Benji
from Content.Characters.BraydenMesserschmidt import BraydenMesserschmidt
from Content.Characters.BrianHightower import BrianHightower
from Content.Characters.BrodyKrysa import BrodyKrysa
from Content.Characters.CalebJalan import CalebJalan
from Content.Characters.CharlieEddie import CharlieEddie
from Content.Characters.ConnorFogarty import ConnorFogarty
from Content.Characters.ConnorMoya import ConnorMoya
from Content.Characters.DavidNapier import DavidNapier
from Content.Characters.DerekCorona import DerekCorona
from Content.Characters.DylanTopic import DylanTopic
from Content.Characters.DyllonForney import DyllonForney
from Content.Characters.GavinKnudsen import GavinKnudsen
from Content.Characters.GMoney import GMoney
from Content.Characters.GrantArmstrong import GrantArmstrong
from Content.Characters.GrantWiseman import GrantWiseman
from Content.Characters.HannaHardy import HannaHardy
from Content.Characters.JaredQuitevis import JaredQuitevis
from Content.Characters.JoeNuts import JoeNuts
from Content.Characters.Kevin import Kevin
from Content.Characters.KolinCraig import KolinCraig
from Content.Characters.LucasSmidt import LucasSmidt
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
from Content.Characters.LukeEllens import LukeEllens
from Content.Characters.LinLaoShi import LinLaoShi
from Content.Characters.CarterBallard import CarterBallard
from Content.Characters.PeteMarks import PeteMarks
from Content.Characters.MJ import MJ
from Content.Characters.ZachSmith import ZachSmith
from Content.Characters.BenMeier import BenMeier

# weapons
from Content.Weapons.AlecsRock import AlecsRock
from Content.Weapons.HomemadeStaffOfHoney import HomemadeStaffOfHoney
from Content.Weapons.Messerschmidter import Messerschmidter
from Content.Weapons.BraydensOsuPen import BraydensOsuPen
from Content.Weapons.BrodysBroadsword import BrodysBroadsword
from Content.Weapons.Bone import Bone
from Content.Weapons.JasonsJunk import JasonsJunk
from Content.Weapons.SirFarQuad import SirFarQuad
from Content.Weapons.NutBuster import NutBuster
from Content.Weapons.ShitLauncherSupreem import ShitLauncherSupreem
from Content.Weapons.Chopsticks import Chopsticks
from Content.Weapons.AnubisBlade import AnubisBlade
from Content.Weapons.KnutsHammer import KnutsHamemr
from Content.Weapons.CoolWeapon import CoolWeapon
from Content.Weapons.Masonator import Masonator
from Content.Weapons.CypireanScythe import CypireanScythe
from Content.Weapons.Ichimonji import Ichimonji
from Content.Weapons.MasonKiller import MasonKiller
from Content.Weapons.SharpThrowingCards import SharpThrowingCards
from Content.Weapons.RatPoison import RatPoison
from Content.Weapons.DogLeg import DogLeg

# built-in packages
import random


class ValleyHighSchool(BattleArea):
    def __init__(self):
        artifact_families = ItemList(content_type=str)
        artifact_families.add("Alec Ferchen")
        artifact_families.add("Brayden Messerschmidt")
        artifact_families.add("Brody Krysa")
        artifact_families.add("Bryce Anderson")
        artifact_families.add("Caleb Jalan")
        artifact_families.add("Carter Ballard")
        artifact_families.add("Connor Fogarty")
        artifact_families.add("David Napier")
        artifact_families.add("Gavin Knudsen")
        artifact_families.add("GMoney")
        artifact_families.add("Grant Wiseman")
        artifact_families.add("Lucas Smidt")
        artifact_families.add("Mason James")
        artifact_families.add("Max Shrum")
        artifact_families.add("Nathan Tenney")
        artifact_families.add("Nolan Anderson")
        artifact_families.add("Spencer George")
        artifact_families.add("Mr.Gentry")
        artifact_families.add("Ben Meier")
        enemies = ItemList(content_type=Enemy)
        enemies.add(FeralLunchLady())
        enemies.add(FlyingPencil())
        enemies.add(MrBakey())
        enemies.add(RacoonInsideABackpack())
        enemies.add(TheWeirdStudent())
        enemies.add(TheLocalSecurityGuard())
        enemies.add(AlecFerchen().create_enemy(AlecsRock()))
        enemies.add(AsherLane().create_enemy(HomemadeStaffOfHoney()))
        enemies.add(Benji().create_enemy(Messerschmidter()))
        enemies.add(BraydenMesserschmidt().create_enemy(BraydensOsuPen()))
        enemies.add(BrianHightower().create_enemy())
        enemies.add(BrodyKrysa().create_enemy(BrodysBroadsword()))
        enemies.add(CalebJalan().create_enemy())
        enemies.add(CharlieEddie().create_enemy())
        enemies.add(ConnorFogarty().create_enemy(Bone()))
        enemies.add(ConnorMoya().create_enemy())
        enemies.add(DavidNapier().create_enemy(JasonsJunk()))
        enemies.add(DerekCorona().create_enemy())
        enemies.add(DylanTopic().create_enemy(SirFarQuad()))
        enemies.add(DyllonForney().create_enemy())
        enemies.add(GavinKnudsen().create_enemy(NutBuster()))
        enemies.add(GMoney().create_enemy())
        enemies.add(GrantArmstrong().create_enemy())
        enemies.add(GrantWiseman().create_enemy(ShitLauncherSupreem()))
        enemies.add(HannaHardy().create_enemy())
        enemies.add(JaredQuitevis().create_enemy(Chopsticks()))
        enemies.add(JoeNuts().create_enemy(random.choice([AnubisBlade(), KnutsHamemr()])))
        enemies.add(Kevin().create_enemy())
        enemies.add(KolinCraig().create_enemy())
        enemies.add(LucasSmidt().create_enemy(CoolWeapon()))
        enemies.add(MasonJames().create_enemy(Masonator()))
        enemies.add(MaxShrum().create_enemy(CypireanScythe()))
        enemies.add(MaxTramontina().create_enemy())
        enemies.add(NathanTenney().create_enemy(Ichimonji()))
        enemies.add(NolanAnderson().create_enemy(MasonKiller()))
        enemies.add(OliverStrauss().create_enemy())
        enemies.add(RyanMartinez().create_enemy())
        enemies.add(SeanMcbroom().create_enemy())
        enemies.add(SethSmith().create_enemy())
        enemies.add(SpencerGeorge().create_enemy(SharpThrowingCards()))
        enemies.add(WillJohnson().create_enemy())
        enemies.add(LukeEllens().create_enemy())
        enemies.add(CarterBallard().create_enemy())
        enemies.add(LinLaoShi().create_enemy())
        enemies.add(PeteMarks().create_enemy(RatPoison()))
        enemies.add(MJ().create_enemy())
        enemies.add(ZachSmith().create_enemy())
        enemies.add(BenMeier().create_enemy(DogLeg()))
        super().__init__(
            "Valley High School",
            0,
            artifact_families,
            enemies,
            True,
            True
        )
