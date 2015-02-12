import math
import random


def check_racko(rack):
    '''given a rack determine if Racko has been achieved.'''
    final = rack[:];
    final.sort();
    return final==rack[:]

def print_top_to_bottom(rack):
    '''given a rack print it out from top to bottom in a manner that looks more
        akin to the game.'''
    for i in rack:
        print i;

def point(hand):
    point = 0
    
    for i in range(0,len(hand)):
        point += hand[i]*math.pow(60,9-i);

    opim = hand[:]

    opim.sort()
    return point - sum(opim)
    
def computer_play(hand,newcard):
    point_init = point(hand);
    init_hand = hand[:]
    best_hand = hand[:]
    for i in range(0,len(hand)):
        hand = init_hand[:]
        hand.insert(i,newcard)
        discard = hand.pop(i+1)
        if point(hand)<point(init_hand):
            best_hand = hand[:]
            best_card = discard

    return best_hand
        

def main():
    global deck
    global computer
    computer = []
    deck = range(1,61)
    random.shuffle(deck);
    for i in range(0,10):
        computer.append(deck.pop(0))
        
    random.shuffle(computer)
    count = 1
    while not check_racko(computer):
        
        print "------------"+str(count)+"---------------"
        computer = computer_play(computer,deck.pop(0))
        print_top_to_bottom(computer)
        count += 1
        
   

main()
    
