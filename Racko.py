#-Homework No.3 Racko Game
#-Due: Feb.6th,2015
#-Author: Ziyi Han and Hsin-Yu Lee

#-We will be implementing the old game Racko which is a game that involves rearranging
#your hand of cards in order to have an increasing sequence.

#-The objective is to be the first player to arrange all of the cards in your
#rack from lowest to highest. Each players rack has 10 slots i.e. 10 cards will
#ultimately have to be in ascending order for the player to win the game.

import random
import math

def shuffle():
    '''This function shuffles the deck or the discard pile'''
    global deck
    global discard
    if len(deck)>0:
        random.shuffle(deck);
    else:
        random.shuffle(discard);
    

def check_racko(rack):
    '''given a rack determine if Racko has been achieved.'''
    final = rack[:];
    final.sort();
    return final==rack[:]

    
def deal_card():
    '''get the top card from the deck'''
    global deck
    return deck.pop(0)
    
def deal_initial_hands():
    '''start the game off by dealing two hands of 10 cards each'''
    global deck;
    userLst = [];
    computerLst = [];
    for i in range(0,10):
        userLst.append(deck.pop(0));
        computerLst.append(deck.pop(0));

    return userLst, computerLst
    
def does_user_begin():
    '''simulate a coin toss by using the random library'''
    return random.random()>0.5

def print_top_to_bottom(rack):
    '''given a rack print it out from top to bottom in a manner that looks more
        akin to the game.'''
    for i in rack:
        print i;
    

def find_and_replace(newCard,cardToBeReplaced, hand):
    '''fint the cardToBeReplaced in the hand and replace it with newCard'''
    if cardToBeReplaced in hand:
        hand.insert(hand.index(cardToBeReplaced),newCard);
        hand.pop(hand.index(cardToBeReplaced));
        return hand
    else:
        return hand
    

def add_card_to_discard(card):
    '''add the card to the top of the discard pile'''
    global discard
    discard.insert(0,card)
    

def computer_play(hand):
    '''This function will show how computer performs'''
    global deck
    global discard
    
    best_sum = point(hand);
    best_hand = hand[:];
    init_hand = hand[:];

    newCard = discard[0];
    
    for i in range(0,10):
        hand = init_hand[:];
        hand.insert(i,newCard);
        discarded = hand.pop(i+1);
        if best_sum < point(hand):
            best_sum = point(hand);
            best_hand = hand[:];
            best_discard = discarded;
            
    if not (best_hand == init_hand[:]):
        discard.pop(0);
        add_card_to_discard(best_discard);
        return best_hand;
    
    else:
        newCard2 = deal_card();
        for i in range(0,10):
            hand = init_hand[:];
            hand.insert(i,newCard2);
            discarded = hand.pop(i+1);
            if best_sum < point(hand):
                best_sum = point(hand);
                best_hand = hand[:];
                best_discard = discarded;
                
        if best_hand == init_hand[:]:
            add_card_to_discard(newCard2);
            return best_hand;
        else:
            add_card_to_discard(discarded);
            return best_hand;
                
        
            
def point(list):
    '''This function gives the sum of total points.'''
    new_list = [];
    for i in range(0,len(list)):
        new_list.append(list[i]*math.pow(60,i));
    return sum(new_list)

def user_play(human_hand):
    global deck
    global discard
    
    newCard = discard[0];
    print 'The card you get is',newCard;
            
    #ask the user if they want this card
    #print the user¡¯s hand
    ans = raw_input("Do you want this card?(Enter Yes or No):");
    while ans[0] not in ["y","Y","n","N"]:
        ans = raw_input("Error, Please re-enter your answer?(Enter Yes or No):");
                
    #ask the user for the number of the card they want to kick out
    #modify the user¡¯s hand and the discard pile
    #print the user¡¯s hand
    if ans[0] == "y" or ans[0] =="Y":
        cardToBeReplaced = input("Which card do you want to replace: ");
        while cardToBeReplaced not in human_hand:
            cardToReplaced = input("Which card do you want to replace: ");
                    
        find_and_replace(newCard,cardToBeReplaced, human_hand);
        add_card_to_discard(cardToBeReplaced);
        print_top_to_bottom(human_hand);
            
    else:
        newCard2 = deal_card();
        print 'The card you get from the deck is',newCard2;
        ans2 = raw_input("Do you want to keep this card?(Enter Yes or No):");
        while ans2[0] not in ["y","Y","n","N"]:
            ans2 = raw_input("Error, Please re-enter your answer?(Enter Yes or No):");
        if ans2[0] == "y" or ans2[0] == "Y":
            cardToBeReplaced2 = input("Which card do you want to replace: ");
            while cardToBeReplaced2 not in human_hand:
                cardToReplaced2 = input("Which card do you want to replace: ");
            find_and_replace(newCard2,cardToBeReplaced2, human_hand);
            add_card_to_discard(cardToBeReplaced);
            print_top_to_bottom(human_hand);
        else:
            add_card_to_discard(newCard2);
            print_top_to_bottom(human_hand);
        
      
def main():
    global deck
    global discard

    human_racko = False;
    computer_racko = False;
    
    #initialize deck and discard
    deck = range(1,61);
    discard = [];
    shuffle()

    global computer_hand 
    #deal a card to the computer and a card to the user
    #repeat until both have 10 cards
    human_hand, computer_hand = deal_initial_hands();

    #decide who to begin and show the initial cards
    userStarts = does_user_begin();
    print "\tThis is the initial cards you get:\n";
    print_top_to_bottom(human_hand);
    print "\tThis is the initial cards computer gets:\n";
    print_top_to_bottom(computer_hand);

    
    #reveal one card to begin the discard pile
    add_card_to_discard(deal_card());
    Round = 1;
    if userStarts:
        print "You play first";
        while not (human_racko or computer_racko):
            
            print "This is Round",Round;
            Round = Round+ 1;
            print "Now, it's your turn!"
            print_top_to_bottom(human_hand);
            user_play(human_hand);
            print "Please wait for computer..."
            computer_hand = computer_play(computer_hand);
            human_racko = check_racko(human_hand);
            computer_racko = check_racko(computer_hand);
            
    else:
        print "Computer plays first";
        while not (human_racko or computer_racko):
            print "This is Round",Round;
            Round =Round+ 1;
            print "Please wait for computer..."
            computer_hand = computer_play(computer_hand);
            print "Now, it's your turn!"
            print_top_to_bottom(human_hand);
            user_play(human_hand);
            human_racko = check_racko(human_hand);
            computer_racko = check_racko(computer_hand);
            


    if human_racko and not computer_racko:
                 print "Rack O! You Win!"
                 print "Your Final Results"
                 print_top_to_bottom(human_hand);
                 print "Computer Final Results"
                 print_top_to_bottom(computer_hand);

    elif not humna_racko and computer_racko:
                 print "Oops...You lose!"
                 print "Your Final Results"
                 print_top_to_bottom(human_hand);
                 print "Computer Final Results"
                 print_top_to_bottom(computer_hand);

    else:
                 print "It's a tie."
                 print "Your Final Results"
                 print_top_to_bottom(human_hand);
                 print "Computer Final Results"
                 print_top_to_bottom(computer_hand);

    

    restart = raw_input("Enter Yes to restart the game or exit:");
    while restart[0] in ["Y","y"]:
        main()

    print "---Thank you---"

    
    #ask the user if they want this

    #modify user¡¯s hand, the discard pile and then print user¡¯s hand
#print the user¡¯s hand
#check and make sure there are still some cards in the deck
#else reshuffle the discard and restart


if __name__ == '__main__':
    main();
