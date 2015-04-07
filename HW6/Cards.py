import random  # needed for shuffling a Deck

class Card(object):
    #the card has a suit which is one of 'S','C','H' or 'D'
    #the card has a rank 
    
    def __init__(self, r, s):
        #implement
        #where r is the rank, s is suit
        if type(r) is int and r in range(2,11):
            self.r = r
        elif type(r) is str and r.upper() in ['A','J','Q','K']:
            self.r = r.upper()
        else:
            raise RuntimeError, 'Illegal rank!'
        
        if type(s) is str and s.upper() in ['S','C','H','D']:
            self.s = s.upper()
        else:
            raise RuntimeError, 'No such a suit'
        #return NotImplementedError

    def __str__(self):
        return str(self.r)+str(self.s)

    def get_rank(self):
        return self.r

    def get_suit(self):
        return self.s

class Deck(object):
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        #correct the code below
        self.__deck = []
        rankrange = []
        rankrange.extend(range(2,11))
        rankrange.extend(['J','Q','K','A'])
        for rank in rankrange:
            for suit in ['S','D','C','H']:
                self.__deck.append(Card(rank,suit))

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        return self.__deck

    def deal(self):
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        return self.__deck.pop(-1)
    
    def __str__(self):
        """Represent the whole deck as a string for printing -- very useful during code development"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        string = []
        for card in self.__deck:
            string.append(str(card))
        return '\n'.join(string)

