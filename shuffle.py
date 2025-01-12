import os,json
from random import choice
os.system('cls')
four_cards=[]
temp=[]
cards=[card for card in range(1,53)]

class Shuffle:
    '''
      Requires cards a list including 1 to 52. An empty
      temp list.
      def __init__(self,cards,temp): 
    '''    
    def __init__(self,cards,temp, four_cards):
        self.cards = cards 
        self.temp=temp
        self.four_cards=four_cards
        
    def  select_card(self):    
        while len(cards)!= 0:
            selected=choice(cards)                              # Selects a random card.
            temp.append(selected)                               # Append that card to temp. 
            cards.remove(selected)                              # Now remove the selected card from cards. 
            
        #print(temp)
        return temp 
         
    def four(self):
        hold = []
        four_cards.append(temp.pop())
        four_cards.append(temp.pop())
        four_cards.append(temp.pop())
        four_cards.append(temp.pop())
        return four_cards     
#-----------------Test the class.-----------------------------------------------------         


#test = Shuffle(cards,temp,four_cards)
#temp = test.select_card()
#print(test.select_card())
#print(test.four())