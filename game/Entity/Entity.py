# game packages
# entity packages
# collections packages
from Collection.ItemList import ItemList
# graphics packages
from Graphics.Content.Text.WarningText import WarningText
# IO packages
from IO.StringMethods import text_length_limiter, star_rating_spacer
from Online.Server import Server
from .Stats.Effect.Effect import Effect
from .Stats.Experience import Experience
from .Stats.StarRating import StarRating


# external packages

class Entity:
    """
    makes an Entity

    parameters

    name: string
        the name of the Entity

    description: string
        the description of the Entity

    star_rating: StarRating
        the star rating of the Entity

    experience: Experience
        the experience of the Entity
    """

    name = None
    description = None
    star_rating = None
    experience = None
    id = None

    def __init__(self, name, description="description", star_rating=StarRating(1), experience=None):
        self.name = name
        self.id = None  # set manually
        self.description = description
        self.star_rating = star_rating
        if experience is None:
            self.experience = Experience()
        else:
            self.experience = experience
        self.effects = ItemList(content_type=Effect)

    def level_up(self, amount):
        def level():
            self.experience.level += amount
            try:
                self.experience.xp = 0
                self.update_stats()
            except TypeError:
                pass

        if self.experience.limit is not None:
            if self.experience.level < self.experience.limit:
                level()
            else:
                WarningText("Max level").display()

        else:
            level()

    def get_money_required(self):
        experience_required = self.experience.get_xp_required(self.star_rating.value)
        current_experience = self.experience.xp
        return int((experience_required - current_experience) / 10) + (1 if int(
            str(experience_required - current_experience)[
                len(str(experience_required - current_experience)) - 1]) > 0 else 0)

    def add_xp(self, amount):
        def xp(amount):
            difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
            while amount >= difference:
                if difference == 0:
                    break
                amount -= difference
                self.level_up(1)
                difference = self.experience.get_xp_required(self.star_rating.value) - self.experience.xp
            self.experience.xp += amount

        if self.experience.limit is not None:
            if self.experience.level != self.experience.limit:
                xp(amount)
        else:
            xp(amount)

    def list_view(self, index: int = 1):
        return f"{text_length_limiter(self.name, len(str(index)))}{star_rating_spacer(self.star_rating.__repr__(), self.star_rating.value)}\t{self.experience}"

    def gacha_info_view(self):
        return f"{self.name} {self.star_rating}"

    def name_and_star_rating(self):
        return f"{self.name} {self.star_rating}"

    def jsonify(self): ...

    @staticmethod
    def check_minimum(variable, multiplier=1, subtract_one_true=False):
        if variable < 1:
            return 1 if not subtract_one_true else 0
        else:
            return variable * multiplier

    def add_effect(self, effect):
        self.effects.add(effect)

    def create_server_item(self, item_type: str):
        if not self.id:
            self.id = Server.get_api().add_item(item_type, self.jsonify())["item"]["id"]

    def update_server_data(self):
        if self.id:
            Server.get_api().update_item(self.id, self.jsonify())

    def pre_remove(self):
        if self.id:
            Server.get_api().remove_item(self.id)
