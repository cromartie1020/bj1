from cards import card_suit, card_ace, card_number, ChooseCard
from shuffle import Shuffle, temp, four_cards, cards

#______________print 4 cards_____________________

cards52 = Shuffle(cards,temp, four_cards)
temp = cards52.select_card()
class Deal(Shuffle):
    def __init__(self,temp, four_cards, cards):
        super().__init__(temp,four_cards, cards)
#--------Deal four cards from the top of the deck-----------
deal_four = Deal(temp,four_cards, cards)
four_cards=deal_four.four()
print(four_cards)
print(temp)
print(len(temp))