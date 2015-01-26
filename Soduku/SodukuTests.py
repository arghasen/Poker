'''
Created on Jan 5, 2015

@author: argha
'''
import unittest
from Board import Board


class Test(unittest.TestCase):


    def testLastEmptySquare(self):
        board = Board("2564891733746159829817234565932748617128.6549468591327635147298127958634849362715")

    def testNakedSingle(self):
        board = Board("3.542.81.4879.15.6.29.5637485.793.416132.8957.74.6528.2413.9.655.867.192.965124.8")
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLastEmptySquare']
    unittest.main()