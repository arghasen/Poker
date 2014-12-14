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
	assert poker.poker( [ sf, fk, fh ] ) == sf
	assert poker.poker( [ fk, fh ] ) == fk
	assert poker.poker( [ fh, fh ] ) == fh
	assert poker.poker( [ sf, fh ] ) == sf
	assert poker.poker( [ sf ] + 99 * [ fh ] ) == sf
	return "tests pass"

print testPoker()