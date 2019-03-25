# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 06:18:53 2019

@author: Eric Born
"""
from random import shuffle

playerNum = 3

class Card(object):
    suit = [None, 'Hearts', 'Diamonds', 'Spades', 'Clubs']
    rank = [None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace',]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '%s of %s' % (Card.rank[self.rank],
                             Card.suit[self.suit])

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def add_card(self, card):
        '''Adds a card to the deck.'''
        self.cards.append(card)

    def remove_card(self, card):
        '''Removes a card from the deck.'''
        self.cards.remove(card)    
    
    def pop_card(self, i=-1):
        '''removes a card from the top of the deck'''
        return self.cards.pop(i)
    
    def shuffleDeck(self):
        '''shuffles the cards'''
        shuffle(self.cards)
    
    def deal(self, hand):
        hand.add_card(self.pop_card())
        
class Player(Deck):
    def __init__(self, num=0, label=''):
        self.cards = []
        self.num = num
        self.label = label
    '''    
    def sort(self):
        self.cards.sort
    '''
class Score(Player):
    def __init__(self, score=0):
        self.score = score
        STRAIGHT_FLUSH = 8000000
        FOUR_OF_A_KIND = 7000000
        FULL_HOUSE     = 6000000
        FLUSH          = 5000000
        STRAIGHT       = 4000000
        SET            = 3000000
        TWO_PAIRS      = 2000000
        ONE_PAIR       = 1000000
    
    def valueHand(Player):
        if isFlush(h) and isStraight(h)
            return valueStraightFlush(h)
        else if ( is4s(h) )
            return valueFourOfAKind(h)
        else if ( isFullHouse(h) )
            return valueFullHouse(h)
        else if ( isFlush(h) )
            return valueFlush(h)
        else if ( isStraight(h) )
            return valueStraight(h)
        else if ( is3s(h) )
            return valueSet(h)
        else if ( is22s(h) )
            return valueTwoPairs(h)
        else if ( is2s(h) )
            return valueOnePair(h)
        else
            return valueHighCard(h)
        
def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None 

if __name__ == '__main__':
    deck = Deck()
    deck.shuffleDeck()
    #hand = Hand()
    #print(find_defining_class(hand, 'shuffle'))
    #Player(1, deck.pocket(hand))
    #deck.pocket(hand)
    #hand.sort()
    #deck.deal(players[1]) #deal 1 card to player number
    
    #intialize players based on playerNum variable
    players = []
    for i in range(playerNum):
        #players.append(Player((i+1), deck.deal))
        players.append(Player(i+1))
    
    #deal 2 cards to each player
    for i in range(2):
        for k in range(len(players)):
            deck.deal(players[k])

    #initialize dealer
    dealer = []
    dealer.append(Player(0))
    
    #dealer burns one card
    deck.pop_card()
    
    #dealer takes 3 cards (flop)
    for i in range(3):
        deck.deal(dealer[0])
    
   
    #make prediction here
    
    #dealer takes 1 card (the turn)
    deck.deal(dealer[0])
    
    #dealer takes last card (the river)
    deck.deal(dealer[0])
    
    
    #make final prediciton
    players[0].cards[0].rank
    
    print(players[1])
    print(players[1])
    print(players[2])
    print(dealer[0])
    
    print(deck)