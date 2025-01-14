card_number = 0
card_ace    = 0
card_suit={1:'ACE HEARTS',2:'ACE SPADES',3:'ACE DIAMONDS',4:'ACE CLUBS',\
    5:'2 of HEARTS',6:'2 of SPADES', 7:'2 of DIAMONDS',8:'2 of CLUBS',\
    9:'3 of HEARTS',10:'3 of SPADES', 11:'3 of DIAMONDS',12:'3 of CLUBS',\
    13:'4 of HEARTS',14:'4 of SPADES', 15:'4 of DIAMONDS',16:'4 of CLUBS',\
    17:'5 of HEARTS',18:'5 of SPADES', 19:'5 of DIAMONDS',20:'5 of CLUBS',\
    21:'6 of HEARTS',22:'6 of SPADES', 23:'6 of DIAMONDS',24:'6 of CLUBS',\
    25:'7 of HEARTS',26:'7 of SPADES', 27:'7 of DIAMONDS',28:'7 of CLUBS',\
    29:'8 of HEARTS',30:'8 of SPADES', 31:'8 of DIAMONDS',32:'8 of CLUBS',\
    33:'9 of HEARTS',34:'9 of SPADES', 35:'9 of DIAMONDS',36:'9 of CLUBS',\
    37:'10 of HEARTS',38:'10 of SPADES', 39:'10 of DIAMONDS',40:'10 of CLUBS',\
    41:'JACK of HEARTS',42:'JACK of SPADES', 43:'JACK of DIAMONDS',44:'JACK of CLUBS',\
    45:'QUEEN of HEARTS',46:'QUEEN of SPADES', 47:'QUEEN of DIAMONDS',48:'QUEEN of CLUBS',\
    49:'KING of HEARTS',50:'KING of SPADES', 51:'KING of DIAMONDS',52:'KING of CLUBS'                
}   

class ChooseCard:
    def __init__(self,card_number):
        self.card_number = card_number
        
    def select(self):
        if self.card_number>0 and self.card_number < 5:
            self.card_number = 1
            card_ace    = 11
        if self.card_number>4 and self.card_number < 9:
            self.card_number = 2
        if self.card_number>8 and self.card_number < 13:
            self.card_number = 3
        if self.card_number>12 and self.card_number < 17:
            self.card_number = 4
        if self.card_number> 16 and self.card_number < 21:
            self.card_number = 5
        if self.card_number>20 and self.card_number < 25:
            self.card_number = 6
        if self.card_number>24 and self.card_number < 29:
            self.card_number = 7
        if self.card_number>28 and self.card_number < 33:
            self.card_number = 8
        if self.card_number>32 and self.card_number < 37:
            self.card_number = 9
        if self.card_number>36 and self.card_number < 53:
            self.card_number = 10    
        return self.card_number                                                                            