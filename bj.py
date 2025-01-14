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
#print(len(temp))
#----------------------------------------------------------
      
card_4=four_cards.pop()
one_of_four=ChooseCard(card_4)
card_number=one_of_four.select() 
#print(card_4)
suit=card_suit[card_4]
print(card_number,suit)