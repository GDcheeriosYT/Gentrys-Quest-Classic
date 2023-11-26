from .CardDeck import CardDeck


class Player:
    def __init__(self, card_deck: CardDeck):
        self.card_deck = card_deck
