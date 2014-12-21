# Test File for Poker
# Author: Argha Sen
# Start Date : 14th December 2014
# Last Update: 14th December 2014
import poker
def test_Poker():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	tp = "5S 5D 9H 9C 6S".split() # Two Pairs
	fkranks = poker.cardRanks(fk)
	tpranks = poker.cardRanks(tp)
	assert poker.allMax([1, 2, 3, 3, 3, 2]) == [3, 3, 3 ]
	assert poker.kind(4, fkranks) == 9
	assert poker.kind(3, fkranks) == None
	assert poker.kind(2, fkranks) == None
	assert poker.kind(1, fkranks) == 7
	assert poker.twoPair(fkranks) == None
	assert poker.twoPair(tpranks) == (9, 5)
	assert poker.cardRanks(sf) == [10, 9, 8, 7, 6]
	assert poker.cardRanks(fk) == [9, 9, 9, 9, 7 ]
	assert poker.cardRanks(fh) == [10, 10, 10, 7, 7]
	assert poker.straight([9, 8, 7, 6, 5]) == True
	assert poker.straight([9, 8, 7, 6, 4]) == False
	assert poker.flush(sf) == True
	assert poker.flush(fk) == False
	assert poker.poker( [ sf, fk, fh ] ) == [sf]
	assert poker.poker( [ fk, fh ] ) == [fk]
	assert poker.poker( [ fh, fh ] ) == [fh, fh]
	assert poker.poker( [ sf, fh ] ) == [sf]
	assert poker.poker( [ sf ] + 99 * [ fh ] ) == [sf]
	assert poker.handRank( sf ) == ( 8, 10 )
	assert poker.handRank( fk ) == ( 7, 9, 7 )
	assert poker.handRank( fh ) == ( 6, 10, 7 )
	return "tests pass"

print test_Poker()