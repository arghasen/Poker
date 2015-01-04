'''
Created on Jan 4, 2015

@author: argha
'''

from SodukuException import SodukuException

class Board(object):
    '''
    This is the board of the soduku
    '''
    def board_grid(self):
        '''
        create the board_grid
        '''
        self.grid = [[0 for _ in xrange(self.vertical_size) ] for _ in xrange(self.horizontal_size)]
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                val =self.board_string[x*self.vertical_size+y]
                self.grid[x][y] = val if val.isdigit() else 0
                
    def print_grid(self):
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                print self.grid[x][y],
            print
            
    def __init__(self, board_string):
        '''
        Constructor
        '''
        self.vertical_size = 9
        self.horizontal_size = 9
        if len(board_string) != self.vertical_size*self.horizontal_size:
            raise SodukuException("Soduku board must have 9*9 grid.")
        else:
            self.board_string = board_string
            self.board_grid()