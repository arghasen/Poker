# Poker Implemantaion in Python
# Author: Argha Sen
# Start Date : 14th December 2014
# Last Update: 14th December 2014

def poker(hands):
	"Given a set of hands find the best hand"
	return max(hands, key = handRank);

def handRank(hand ):
	"Given a hand return the rank of the hand"
	ranks = cardRanks(hand);
	if straight(ranks) and flush(hand):
		return (8, max(ranks)) # Highest card in the stright gives the entire hand.
	elif kind(4, ranks):
	 	return (7, kind(4, ranks), kind(1, ranks)) # Break ties by using which card is 4 times and if still equal use the final card. 
	elif fullHouse(hand):
		return (6, kind(3, ranks), kind(2,ranks)) #Break ties by using the cards in the full house.
	elif flush(hand):
		return (5, ranks)
	elif stright(hands):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), ranks)
	elif twoPair(hands):
		return (2, twoPair(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks);

def cardRanks(cards):
	"Given a set of cards return their ranks, in sorted order"
	ranks = ['--23456789TJQA'.index(r) for r,s in cards]
	ranks.sort(reverse = true)
	return ranks