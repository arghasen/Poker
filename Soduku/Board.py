'''
Created on Jan 4, 2015

@author: argha
'''

from SodukuException import SodukuException

class Board(object):
    '''
    This is the board of the soduku
    '''


    def __init__(self, board_string):
        '''
        Constructor
        '''
        if len(board_string) != 81:
            raise SodukuException("Soduku board must have 9*9 grid.")
        else:
            pass