'''
Created on Jan 4, 2015

@author: argha
'''

from SodukuException import SodukuException

class Board(object):
    '''
    This is the board of the soduku
    '''

    
    def reduce_keys_from_rows(self, x, y):
        print x,y
        for z in xrange(self.vertical_size):
            if self.grid[x][z] != 0:
                self.grid_val[x] = [a.replace(self.grid[x][z], '')  if len(a)>1 else a for a in self.grid_val[x]]
                #pass
    
    def reduce_keys_from_colums(self, x, y):
        pass
    
    
    def reduce_keys_from_box(self, x, y):
        pass
    
    
    def reduce_candidate_keys(self):
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if self.grid[x][y] == 0:
                    self.reduce_keys_from_rows(x, y)
                    self.reduce_keys_from_colums(x, y)
                    self.reduce_keys_from_box(x, y)
        self.print_grid(True)
         
                
    def create_candidate_keys(self):
        self.grid_val = [[0 for _ in xrange(self.vertical_size) ] for _ in xrange(self.horizontal_size)]
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                self.grid_val[x][y] = '123456789' if self.grid[x][y] == 0 else str(self.grid[x][y]) 
        self.reduce_candidate_keys()        
                
    def board_grid(self):
        '''
        create the board_grid
        '''
        self.grid = [[0 for _ in xrange(self.vertical_size) ] for _ in xrange(self.horizontal_size)]
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                val = self.board_string[x * self.vertical_size + y]
                self.grid[x][y] = val if val.isdigit() else 0
           
                
    def print_grid(self, values=False):
        width = 1
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if values:
                    width = 9
                    print str(self.grid_val[x][y]).ljust(width),
                else:
                    print self.grid[x][y],
                if not (y + 1) % 3:
                    print ' | ',
            if not (x + 1) % 3:
                print '\n' + '-' * (9 * width + 20),
            print
    
    
    def get_Grid(self):
        return self.grid
        
        
    def __init__(self, board_string):
        '''
        Constructor
        '''
        self.vertical_size = 9
        self.horizontal_size = 9
        if len(board_string) != self.vertical_size * self.horizontal_size:
            raise SodukuException("Soduku board must have 9*9 grid.")
        else:
            self.board_string = board_string
            self.board_grid()
            self.create_candidate_keys()
