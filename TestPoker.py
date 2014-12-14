# Test File for Poker
# Author: Argha Sen
# Start Date : 14th December 2014
# Last Update: 14th December 2014
import poker
def testPoker():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	assert poker.cardRanks(sf) == [10, 9, 8, 7, 6]
	assert poker.cardRanks(fk) == [9, 9, 9, 9, 7 ]
	assert poker.cardRanks(fh) == [10, 10, 10, 7, 7]
	assert poker.straight([9, 8, 7, 6, 5]) == true
	assert poker.straight([9, 8, 7, 6, 4]) == false
	assert poker.flush(sf) == true
	assert poker.flush(fk) == false
	assert poker.poker( [ sf, fk, fh ] ) == sf
	assert poker.poker( [ fk, fh ] ) == fk
	assert poker.poker( [ fh, fh ] ) == fh
	assert poker.poker( [ sf, fh ] ) == sf
	assert poker.poker( [ sf ] + 99 * [ fh ] ) == sf
	assert poker.handRank( sf ) == ( 8, 10 )
	assert poker.handRank( fk ) == ( 7, 9, 7 )
	assert poker.handRank( fh ) == ( 6, 10, 7 )
	return "tests pass"

print testPoker()