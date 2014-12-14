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
	elif fullHouse(ranks):
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
	ranks.sort(reverse = True)
	return ranks

def straight(ranks):
	return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"Given a set of ranks, return the first rank that is exactly n times"
	"If no such card exists return none"
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None;		

def fullHouse(ranks):
	"If a 3 of a kind and 2 of a kind exists in the same hand"
	return kind(3,ranks) and kind(2,ranks)

def twoPair(ranks):
	"if 2pairs are avialable in the hand return the tuple else None"
	highPair = kind(2,ranks)
	lowPair = kind(2, list(reversed(ranks)))
	if highPair and highPair != lowPair:
		return (highPair, lowPair)
	else:
		return None
