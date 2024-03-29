
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

In this programming assignment, you will simulate a regular Poker game otherwise known as the 5-Card Draw. Regular Poker is played with a standard deck of 52 cards. Cards are ranked from high to low in the following order: Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2. The value of an Ace is higher than a King, which is higher than a Queen and so on. There are four suits - Spades, Hearts, Clubs, and Diamonds. The suits are of equal value.

Rules of the Game

Each player is dealt five cards. The player with the highest valued hand wins. The best to worst hands are ranked in the following order:

1. Royal Flush
2. Straight Flush
3. Four of a Kind
4. Full House
5. Flush
6. Straight
7. Three of a Kind
8. Two Pair
9. One Pair
10. High Card

Royal Flush: A Royal Flush is made of 10, Jack, Queen, King, and Ace all of the same of suit.

Hand 1: 10S JS QS KS AS

Hand 2: 10H JH QH KH AH

The probability of getting a royal flush is so low that ties are not broken.

Straight Flush: A straight flush is made of 5 cards in numerical sequence but of the same suit.

Hand 1: 3C 4C 5C 6C 7C

Hand 2: 8D 9D 10D JD QD

If there are two straight flushes, then whichever hand has the highest card value wins. In the above example, Hand 2 wins.

Four of a Kind: In four of a kind, the hand must have four cards of the same numerical rank, e.g. four aces or four queens.

Hand 1: 9S 9H 9C 9D 10C

Hand 2: QS QH QC QD 8S

In the event of a tie, the hand that has the highest ranking four of a kind cards wins. In the above example, Hand 2 wins.

Full House: For a full house, three of the cards must have the same numerical rank, and the two remaining cards must also have the same numerical rank but obviously different rank than the other three.

Hand 1: JS JH JD 4S 4C

Hand 2: KH KC KD 10C 10D

If there are two full houses, then the hand that has the higher-ranking cards for the three of a kind wins. In the above example, Hand 2 wins.

Flush: In a flush, there are 5 cards all of the same suit. The numerical order does not matter.

Hand 1: 3S 5S 8S 10S KS

Hand 2: 2D 6D 8D JD QD

In the event of two flushes, the one with the highest-ranking card wins. In the above example, Hand 1 wins.

Straight: In a straight hand, the 5 cards are in numerical order but are not all of the same suit.

Hand 1: 3S 4D 5S 6H 7C

Hand 2: 5D 6S 7C 8H 9H

When there are two straight hands, then the one with the highest-ranking card wins. In the above example, Hand 2 wins.

Three of a Kind: In three of a kind hand, there are 3 cards of the same rank, and the other two are unrelated.

Hand 1: 6D 6S 6C KC 4H

Hand 2: 8S 8D 8C 2H 5C

When there are two three of a kind hands, the hand with the highest ranking three of a kind card wins. In the above example, Hand 2 wins.

Two Pair: In a two pair hand, there are two cards of a matching rank, another two cards of a different matching rank, and a fifth random card.

Hand 1: 4D 4H 7S 7C 9S

Hand 2: 9H 9D 5S 5C 3D

When there are two hands that are two pair, the hand having the highest pair wins. If the highest pair in both hands are of the same rank, then the highest second pair wins. If the two hands have two identical pairs, then the hand with the highest ranking fifth card wins. In the example above, Hand 2 wins.

One Pair: In a one pair hand, there are two cards of the same rank, and the other three cards are unrelated.

Hand 1: 8S 8H 3D KC 7S

Hand 2: 6D 6C 8S 5H 10D

In the event of a tie, then the hand with the highest pair wins. If the two pairs are the same, then the highest side card wins, and if necessary, the second highest side card, and finally, the third highest side card can be used to break the tie. In the above example, Hand 1 wins.

High Card: If none of the hands in a game qualified under the categories listed above, then the hand having the highest ranking card wins.

Hand 1: 9S 10D 4S 6H KC

Hand 2: QS 3D 7H 10C 6D

To break a tie, the second-highest, third-highest, fourth-highest, and the smallest card can be used in order. In the above example, Hand 1 wins.

Poker Game Simulation

The overall structure of the program will be as follows:

class Card (object):
  ...

class Deck (object):
  ...

class Poker (object):
  ...

def main():
  ...

main()

In the function main(), you will read the number of players from a file poker.in. Assume that the number of players is between 2 and 6 inclusive. You do not have to do any error checking. In the class Poker, you will create that many hands from a single deck of cards.

Most of the programming will be concentrated on writing the functions in the Poker class. Now, these functions will return a 0 if the hand does not fulfill that particular condition. For example, if the hand is not four of a kind, the function is_four_kind() will return 0. Otherwise, it will return a number greater than 0 that can be used to order the hands and even break a tie according to the rules given above. There is a scheme that is suggested below that we want you to use.

Assignment of Points to a Hand: 

This scheme assumes that you will systematically check if a hand meets the requirements from a Royal Flush to a High Card. Once a hand has met certain criteria, say Straight Flush, then you will not check if it meets the criteria lower down the ranking scale.

Here are the points (h) allotted for a hand:

Royal Flush: 10
Straight Flush: 9
Four of a Kind: 8
Full House: 7
Flush: 6
Straight: 5
Three of a Kind: 4
Two Pair: 3
One Pair: 2
High Card: 1

The total points are calculated as follows:

total_points = h * 15**5 + c1 * 15**4 + c2 * 15**3 + c3 * 15**2 + c4 * 15 + c5

where c1, c2, c3, c4, and c5 are the ranks of the cards in the hand, where c1 is the highest-ranking card, and c5 is the lowest-ranking card. There are some variations to this rule that are mentioned below:

Four of a Kind
	c1, c2, c3, and c4 are the ranks of the four of a kind cards, and c5 is the side card.

Full House
	c1, c2, and c3 are the ranks of the three cards having the same rank, and c4 and c5 are the ranks of the two remaining cards having the same rank.

Three of a Kind
	c1, c2, and c3 are the ranks of the three cards of the same rank, and c4 and c5 are the ranks of the remaining cards where c4 has a higher rank than c5.

Two Pair
	c1 and c2 are the ranks of the first and higher ranking pair. c3 and c4 are the ranks of the second and lower ranking pair. c5 is the rank of the remaining side card.

One Pair
	c1 and c2 are the ranks of the pair of cards having the same rank. c3, c4, and c5 are the ranks of the side cards from highest to lowest rank.

Your output session will look as follows:

Number of players: 3

Player 1: 9D 9H 8C 8S 6C
Player 2: AS JD 8H 4S 2C
Player 3: 7D 6H 5S 4H 3C

Player 1: Two Pair
Player 2: High Card
Player 3: Straight

Player 3 wins.

We are only concerned with ties for the winning hand. We do not consider ties for the losing hands. Two hands are said to be tied if they are the same type of hand - e.g. two straights. If there are ties, then print out the hands in descending order of points. The first player in the tie has the most points, and the last player in the tie has the least points.

Player 4 ties.
Player 6 ties.

