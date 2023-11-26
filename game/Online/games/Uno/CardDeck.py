from .Card import Card

from Collection.ItemList import ItemList


class CardDeck:
    def __init__(self, card_limit: int = 50):
        self.content = ItemList(card_limit, Card)

    def __add__(self, card: Card):
        self.content.add(card)

    def get(self, index):
        card = self.content.get(index)
        self.content.content.remove(card)
        return card
