import os,json
from random import choice
os.system('cls')

temp=[]
cards=[card for card in range(1,53)]
class Shuffle:
        
    def __init__(self,cards,temp):
        self.cards = cards 
        self.temp=temp
    def  select_card(self):    
        while len(cards)!= 0:
            selected=choice(cards)                              # Selects a random card.
            temp.append(selected)                               # Append that card to temp. 
            cards.remove(selected)                              # Now remove the selected card from cards. 
            
        print(temp) 
         
         
         
#new_card=Shuffle(temp)
#temp=new_card.random_cards()
#test = Shuffle(cards,temp)
#temp = test.select_card()
#print(temp)