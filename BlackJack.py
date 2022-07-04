import random
import time
from os import system, name

def clear():
    '''Clear the screen'''
    
    if name == 'nt':
      _ = system('cls')

#Define the cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

def deal(cards):
  """Returns a random card from the cards"""
  card = random.choice(cards)
  return card


def calculate_score(hand):
    '''Calculate the score of the player and dealer'''
    
    #Check if the hand is blackjack
    if sum(hand) == 21 and len(hand) == 2:
        return 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare_hands(player_hand, dealer_hand):
    #Calculate the score of the player and dealer
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    #Check if the player and dealer have score more than 21
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose"
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 21:
        return "Lose, opponent has BLACKJACK"
    elif player_score == 21:
        return "Win with a BLACKJACK"
    elif player_score > 21:
        return "You went over, You lose"
    elif dealer_score > 21:
        return "Opponent went over, You win"
    elif player_score > dealer_score:
        return "You win, Congrats"
    else:
        return "You lose"
    
def play_game():
    '''Play the game'''
    user_hand = []
    dealer_hand = []
    
    user_hand.append(deal(cards))
    dealer_hand.append(deal(cards))
    
    game_over = False
    
    while not game_over:
        
        player_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f'Your hand is {user_hand} and your score is {player_score}')
        time.sleep(1)
        print(f'Dealer first card is {dealer_hand}')
        
        if player_score == 0 or dealer_score == 0:
            game_over = True
            
        ask_to_deal = input('Do you want to deal? (y/n)').lower()
        
        if ask_to_deal == 'y':
            user_hand.append(deal(cards))
        else :
            game_over = True
    while dealer_score < 17 and dealer_score != 0 :
        
        dealer_hand.append(deal(cards))
        dealer_score = calculate_score(dealer_hand)
        
    print(f'Your cards : {user_hand}, Your score : {player_score}')
    print(f'Dealer cards : {dealer_hand}, Dealer score : {dealer_score}')
    print(compare_hands(user_hand, dealer_hand))

while input('Do you want play Blackjack? (y/n)').lower() == 'y':
    clear()
    play_game()
        
        
        
        
