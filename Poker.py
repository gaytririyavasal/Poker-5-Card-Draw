#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Poker.py

#  Description: The following program simulates a game of Poker and returns the result of the game

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 2/7/2022

#  Date Last Modified: 2/14/2022

import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards
    self.num_players = num_players

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # print number of players
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
    print()

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand
    
    # evaluates and appends types and points of each hand to hand_type and hand_points
    self.check_hand(hand_type, hand_points)
    
    print()
    
    # stores the max value
    highest_points = max(hand_points)
    # dictionary for ties
    ties = {}
    # index of max value
    index = hand_points.index(highest_points)
    # type of max value
    max_type = hand_type[index]

    # appends player number and points if i has the same type as max value
    for i in range(len(hand_type)):
        if hand_type[i] == max_type:
            ties[i] = hand_points[i]
            
    # checks there's more than one tie
    if len(ties) > 1:
        # sorts dictionary by value
        sorted_ties = self.sort_dict_by_value(ties)
        
        
        # prints keys (player numbers)
        for i in sorted_ties.keys():
            print("Player " + str(i+1) + " ties.")
    else:
        print("Player " + str(index + 1) + " wins.")
        
    
  # sorts a dictionary in descending order by value 
  # takes as argument a dictionary
  # returns a sorted dictionary in descending order of value
  def sort_dict_by_value (self, ties):
      # sorts values
      sorted_values = sorted(ties.values(), reverse = True)
      sorted_ties = {}
      # loops through values
      for i in sorted_values:
          # loops through keys
          for j in ties.keys():
              # sets i to value of sorted_ties at j
              if ties[j] == i:
                  sorted_ties[j] = ties[j]
      return sorted_ties
    

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'


  # determine if a hand is straight flush
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_straight_flush (self, hand):
      # flags straight flush as false
      straight_flush = False
      # loops through hand
      for i in range(1, len(hand)):
          # checks if each card is the same suit and is one number higher than the last
          if(hand[i].rank == (hand[i-1].rank - 1) and hand[i].suit == hand[i-1].suit):
              straight_flush = True
          else:
              straight_flush = False
              break
              
      if (not straight_flush):
          return 0, ''
      
      # calculates points
      points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      
      return points, 'Straight Flush'
          

  
  # determine if a hand is four kind
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_four_kind (self, hand):
      # flags four_kind as false
      four_kind = False
      # list of ranks of the hand
      hand_values = [card.rank for card in hand]
      # loops through hand values
      for i in hand_values:
          # checks to see if there is 4 of one rank
          if hand_values.count(i) == 4:
              four_kind = True
              break
          
      if (not four_kind):
          return 0, ''
      
      if hand_values[0] != hand_values[1]:
          hand_values.append(hand_values.pop(0))
      
      
      # calculates points
      points = 8 * 15 ** 5 + (hand_values[0]) * 15 ** 4 + (hand_values[1]) * 15 ** 3
      points = points + (hand_values[2]) * 15 ** 2 + (hand_values[3]) * 15 ** 1
      points = points + (hand_values[4])
      
      return points, 'Four of a Kind'
          
      
  # determine if a hand is full house
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_full_house (self, hand):
     # flags full house as false
     full_house = False
     
     # empty lists to store three pair and two pair
     three_pair = []
     two_pair = []
     
     # list of ranks of the hand
     hand_values = [card.rank for card in hand]
     # loops through hand values
     for i in hand_values:
         # appends if there are three of the same rank
         if hand_values.count(i) == 3:
             three_pair.append(i)
         # appends if there are two of the same rank
         elif hand_values.count(i) == 2:
             two_pair.append(i)
      
     # checks if three_pair has three cards and two_pair has two cards
     if len(three_pair) == 3 and len(two_pair) == 2:
         full_house = True
         
     if (not full_house):
         return 0, ''
     
     
     # calculates points
     points = 7 * 15 ** 5 + (three_pair[0]) * 15 ** 4 + (three_pair[1]) * 15 ** 3
     points = points + (three_pair[2]) * 15 ** 2 + (two_pair[0]) * 15 ** 1
     points = points + (two_pair[1])
     
     return points, 'Full House'
         
     
  # determine if a hand is flush
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_flush (self, hand):
     # sets flush to false
     flush = False
     # loops through hand
     for i in range(1, len(hand)):
         # checks to see if all 5 cards have same suit
         if hand[i].suit == hand[i-1].suit:
             flush = True
         else:
             flush = False
             break
         
     if (not flush):
         return 0, ''
     
     # calculates points
     points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
     points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
     points = points + (hand[4].rank)
     
     return points, 'Flush'


  # determine if a hand is straight flush
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_straight (self, hand):
      # sets straight to false
     straight = False
     for i in range(1, len(hand)):
         # checks to see if all 5 cards have the same rank
         if hand[i].rank == hand[i-1].rank - 1:
             straight = True
         else:
             straight = False
             break
         
     if (not straight):
         return 0, ''
     
     # calculates points
     points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
     points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
     points = points + (hand[4].rank)
     
     return points, 'Straight'

  # determine if a hand is three kind
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_three_kind (self, hand):
      # sets three_kind to false
      three_kind = False
      # list of ranks of hand
      hand_values = [card.rank for card in hand]
      # keeps track of three kind rank
      value = 0
      # loops through hand values
      for i in hand_values:
          # checks if there is 3 of one rank
          if hand_values.count(i) == 3:
              three_kind = True
              # assigns value to i
              value = i
              break
          
      if (not three_kind):
          return 0, ''
      
      # moves ranks that are not equal to value at the end of the list
      for j in range(len(hand_values)):
          if j == value:
              hand_values.append(hand_values.pop(j))
      
      # calculates points
      points = 4 * 15 ** 5 + (hand_values[0]) * 15 ** 4 + (hand_values[1]) * 15 ** 3
      points = points + (hand_values[2]) * 15 ** 2 + (hand_values[3]) * 15 ** 1
      points = points + (hand_values[4])
      
      return points, 'Three of a Kind'

  # determine if a hand is two pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_two_pair (self, hand):
     # sets tow_pair to false
     two_pair = False
     # counts the number of pairs
     counter = 0
     # index of hand
     i = 0
     hand_values = []
     # loops while index is less than length of hand - 1
     while i < len(hand) - 1:
         # checks to see if a pair exists
         if hand[i].rank == hand[i+1].rank:
             # increase counter by one
             counter += 1
             # appends pair in value list
             hand_values.append(hand[i].rank)
             hand_values.append(hand[i+1].rank)
             # skips the second card in pair
             i += 2
             
         else:
             # moves index to next card
             i += 1
     
     # checks if theres 2 pairs
     if counter == 2:
          two_pair = True
     
    # sorts the pairs
     hand_values = sorted(hand_values, reverse = True)
     # appends element not in the pairs
     for i in range(len(hand)):
         if hand[i].rank not in hand_values:
             hand_values.append(hand[i].rank)
          
          
     if (not two_pair):
         return 0, ''
     
     
     
     
     # calculates points
     points = 3 * 15 ** 5 + (hand_values[0]) * 15 ** 4 + (hand_values[1]) * 15 ** 3
     points = points + (hand_values[2]) * 15 ** 2 + (hand_values[3]) * 15 ** 1
     points = points + (hand_values[4])

     return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    hand_values = []
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        # appends the pair in values list
        hand_values.append(hand[i].rank)
        hand_values.append(hand[i+1].rank)
        break
    # appends rest of elements not a pair
    for i in range(len(hand)):
        if hand[i].rank not in hand_values:
            hand_values.append(hand[i].rank)
    if (not one_pair):
      return 0, ''

    points = 2 * 15 ** 5 + (hand_values[0]) * 15 ** 4 + (hand_values[1]) * 15 ** 3
    points = points + (hand_values[2]) * 15 ** 2 + (hand_values[3]) * 15 ** 1
    points = points + (hand_values[4])

    return points, 'One Pair'


  # determine if a hand is high card
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_high_card (self,hand):
    # calculates points
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

  # determines type of hand and number of points for each player's hand
  # takes as argument a list of hand types and hand points
  # appends each type of hand and number of points to respective list and prints type of hand for each player
  def check_hand(self, hand_type, hand_points):
    for i in range(len(self.players_hands)):
    
      if self.is_royal(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Royal Flush')
        hand_type.append(self.is_royal(self.players_hands[i])[1])
        hand_points.append(self.is_royal(self.players_hands[i])[0])
        
      elif self.is_straight_flush(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Straight Flush')
        hand_type.append(self.is_straight_flush(self.players_hands[i])[1])
        hand_points.append(self.is_straight_flush(self.players_hands[i])[0])

      elif self.is_four_kind(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Four of a Kind')
        hand_type.append(self.is_four_kind(self.players_hands[i])[1])
        hand_points.append(self.is_four_kind(self.players_hands[i])[0])

      elif self.is_full_house(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Full House')
        hand_type.append(self.is_full_house(self.players_hands[i])[1])
        hand_points.append(self.is_full_house(self.players_hands[i])[0])
        
      elif self.is_flush(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Flush')
        hand_type.append(self.is_flush(self.players_hands[i])[1])
        hand_points.append(self.is_flush(self.players_hands[i])[0])

      elif self.is_straight(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Straight')
        hand_type.append(self.is_straight(self.players_hands[i])[1])
        hand_points.append(self.is_straight(self.players_hands[i])[0])

      elif self.is_three_kind(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'Three of a Kind')
        hand_type.append(self.is_three_kind(self.players_hands[i])[1])
        hand_points.append(self.is_three_kind(self.players_hands[i])[0])

      elif self.is_two_pair(self.players_hands[i]) != (0,  ''):
        print ('Player ' + str(i+1) + ': ' + 'Two Pair')
        hand_type.append(self.is_two_pair(self.players_hands[i])[1])
        hand_points.append(self.is_two_pair(self.players_hands[i])[0])

      elif self.is_one_pair(self.players_hands[i]) != (0, ''):
        print ('Player ' + str(i+1) + ': ' + 'One Pair')
        hand_type.append(self.is_one_pair(self.players_hands[i])[1])
        hand_points.append(self.is_one_pair(self.players_hands[i])[0])

      elif self.is_high_card(self.players_hands[i]):
        print ('Player ' + str(i+1) + ': ' + 'High Card')
        hand_type.append(self.is_high_card(self.players_hands[i])[1])
        hand_points.append(self.is_high_card(self.players_hands[i])[0])
  
def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
  
