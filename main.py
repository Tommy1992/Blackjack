############### Blackjack Project #####################

#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
##################### Hints #####################
#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.
#Hint 3: Download and read this flow chart I've created: 
# see saved link

from art import logo
import random as rnd

print (logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card = rnd.choice(cards)
cards_player = []
cards_dealer = []
global player_score
player_score = 0
dealer_score = 0
cont_playing = "y"

def draw_a_card():
  card_value = rnd.choice(cards)
  return card_value

# first 2 cards of p1 and print his score
def two_cards_for_player_1for_dealer():
  cards_player.append(draw_a_card())
  cards_player.append(draw_a_card())
  player_score = cards_player[0] + cards_player[1]
  print (f"Your cards: {cards_player} your score is: {player_score}")
  # PCs first card and print his score
  cards_dealer.append(draw_a_card())
  cards_dealer.append(draw_a_card())
  dealer_score = cards_dealer[0] + cards_dealer[1]
  print (f"The PCs first card: {cards_dealer[0]}")
  return player_score

two_cards_for_player_1for_dealer()

def checking_bj_and_over21():  
    if dealer_score == 21: #checking for users and dealers blackjack
      print (logo)
      print (f"The dealer got Blackjack. The game is over.")
    elif player_score == 21:
      print (logo)
      print (f"You got Blackjack. The game is over.")

    # cards_player = [10,10,20] #test
    # player_score = 31 #test
    if player_score > 21: #needs testing
      if cards_player.count(11) != 0:
        player_score -= cards_player.count(11)*10
        if player_score > 21:
          print (f"You got over 21 points. The game is over. #Loser")
      else:
        print (f"You got over 21 points. The game is over. #Loser")

another_card = input("Do you want another card ? Type in y or n. ")
if another_card == "y":
    cards_player.append(draw_a_card())
    player_score = cards_player[0] + cards_player[1] + cards_player[2]
    print (f"Your cards: {cards_player} your score is: {player_score}")
    checking_bj_and_over21()
    
    
    












"""
Testing
#draw_a_card_player(0)
def draw_a_card_player(total_player_score_par):
  card_drawn = rnd.choice(cards)
  # print ("card_drawn: " + str(card_drawn))
  # print (total_player_score)
  total_player_score_arg = total_player_score_par + card_drawn
  card_drawn = rnd.choice(cards)
  # total_player_score = total_player_score + card_drawn
  # print ("card_drawn: " + str(card_drawn))
  print ("total_player_score " + str(total_player_score_arg))
  return total_player_score_arg

if wanna_play == "y":
  draw_a_card_player(total_player_score_arg)
  draw_a_card_player(total_player_score_arg)
  if total_player_score == 21:
    print "BLACKJACK - You won."
  elif:input ()

while cont_playing == "y":
  cont = input("Do you want to draw another round? Type in y or n. ")
  if cont_playing == "n":
    break
  draw_a_card_player(total_player_score_arg)
  draw_a_card_player(total_player_score_arg)
  # temp = card_drawn
  # print (temp)
  print (total_player_score)
  draw_a_card_player(total_player_score)

  print (f"You got a {players_cards[0]} and a {players_cards[1]}.Your score is {int(players_cards[0]) + int(players_cards[1])}.")

  print ("test")
  print ((players_cards))
  print (int(players_cards[0]))
  print ("secodn card: ")
  print (int(players_cards[1]))
  print (f"You got a {players_cards[0]} and a {players_cards[1]}.Your score is {int(players_cards[0]) + int(players_cards[1])}.")
  more_cards = "y"
  while more_cards == "y":
    more_cards = input("Do you want to draw another card? Type in y or n. ")
    if more_cards == "n":
      break

"""
