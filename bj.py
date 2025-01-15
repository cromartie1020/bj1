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
#print(four_cards)
#print(temp)
#print(len(temp))
#----------------------------------------------------------
      
card_4=four_cards.pop()
card_3=four_cards.pop()
card_2 =four_cards.pop()
card_1=four_cards.pop()
print (card_1,card_2,card_3,card_4) 
one_of_four=ChooseCard(card_4)

#card_number=one_of_four.select() 
#print(card_4)
suit4=card_suit[card_4]
suit3=card_suit[card_3]
suit2=card_suit[card_2]
suit1=card_suit[card_1]

pick4=ChooseCard(card_4)
card4=pick4.select()

pick3=ChooseCard(card_3)
card3=pick3.select()

pick2=ChooseCard(card_2)
card2=pick2.select() 

pick1=ChooseCard(card_1)
card1=pick1.select()
print()
print() 
print(card1,suit1)
print(card2,suit2)
print(card3,suit3)
print(card4,suit4)



