"Poker Implemantaion in Python"
# Author: Argha Sen
# Start Date : 14th December 2014
import random


def poker(hands):
    "Given a set of hands find the list of best hands"
    return allMax(hands, key=handRank)


def allMax(iterable, key=lambda x: x):
    "return a list of all items equal to the max of the list"
    maxval = None
    maxval = max(iterable, key=key)
    allmax = [x for x in iterable if x == maxval]
    return allmax


def handRank(hand):
    "Given a hand return the rank of the hand"
    ranks = cardRanks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))  # Highest card in the stright gives the entire hand.
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
        # Break ties by using which card is 4 times and if still equal use the final card.
    elif fullHouse(ranks):
        return (6, kind(3, ranks), kind(2, ranks))  #Break ties by using the cards in the full house.
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif twoPair(ranks):
        return (2, twoPair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def cardRanks(cards):
    "Given a set of cards return their ranks, in sorted order"
    ranks = ['--23456789TJQA'.index(r) for r, _ in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    "Find a straight"
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    "find a flush"
    suits = [s for _, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    "Given a set of ranks, return the first rank that is exactly n times \
    If no such card exists return none"
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def fullHouse(ranks):
    "If a 3 of a kind and 2 of a kind exists in the same hand"
    return kind(3, ranks) and kind(2, ranks)


def twoPair(ranks):
    "if 2pairs are avialable in the hand return the tuple else None"
    high_pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if high_pair and high_pair != low_pair:
        return (high_pair, low_pair)
    else:
        return None


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQA' for s in 'SHDC']):
    "Shuffle the card and deal out num hands of n card each"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
