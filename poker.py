# Poker Implemantaion in Python
# Author: Argha Sen
# Start Date : 14th December 2014
# Last Update: 14th December 2014

def poker( hands ):
	"Given a set of hands find the best hand"
	return max( hands, key = hand_rank );

def hand_rank( hand ):
	"Given a hand return the rank of the hand"
	return 0;
