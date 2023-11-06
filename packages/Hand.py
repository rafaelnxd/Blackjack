from Card import Card
from Deck import Deck


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
print(hand.cards[0])