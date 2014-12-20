# Poker Implemantaion in Python
# Author: Argha Sen
# Start Date : 18th December 2014
import poker
handNames=["Straight Flush","4 Kind","Full House","Flush","Straight"
			"3 Kind", "2 Pair", "Pair", "High Card"
		]
def randomSimulation(n =700000):
	counts=[0]*9
	for i in range(n):
		for hand in poker.deal(10):
			ranking = poker.handRank(hand)[0]
			counts[ranking]+=1
	for i in reversed(range(9)):
		print "%14s: %d %6.3f %%" %(i, counts[i], (100.*counts[i])/(n*10))
	print(sum(counts))
randomSimulation()