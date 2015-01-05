'''
Created on Jan 4, 2015

@author: argha
'''

from SodukuException import SodukuException

class Board(object):
    '''
    This is the board of the soduku
    '''

    
    def reduce_keys_from_rows(self, x):
        for z in xrange(self.vertical_size):
            if self.grid[(x,z)] != 0:
                for y in xrange(self.horizontal_size):
                    if z!=y:
                        self.grid_val[(x,y)] = self.grid_val[(x,y)].replace(self.grid[(x,z)], '')
        
    
    def reduce_keys_from_colums(self, y):
        for z in xrange(self.horizontal_size):
            if self.grid[(z,y)] != 0:
                for x in xrange(self.vertical_size):
                    if z!=x:
                        self.grid_val[(x,y)] = self.grid_val[(x,y)].replace(self.grid[(z,y)], '')
    
    
    def reduce_keys_from_box(self, x, y):
        '''
        reduces keys based on the box. Assumes a 3*3 box
        '''
        grid_nos = (divmod(x, 3)[0], divmod(y, 3)[0])
        
        for a in xrange(grid_nos[0] * 3, grid_nos[0] * 3 + 3):
            for b in xrange(grid_nos[1] * 3, grid_nos[1] * 3 + 3):
                if self.grid[(a,b)] != 0:
                    c = self.grid_val[(x,y)]
                    self.grid_val[(x,y)] = c.replace(self.grid[(a,b)], '')  if len(c) > 1 else c 
                    
                    
    def hidden_singles(self):
        pass
        
    def box_locked_candidate(self):
        pass
    
    def row_column_locked_candidate(self):
        pass
    
    def reduce_candidate_keys(self):
        'This is basically the singles rule'
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if self.grid[(x, y)] == 0:
                    self.reduce_keys_from_rows(x)
                    self.reduce_keys_from_colums( y)
                    self.reduce_keys_from_box(x, y)
                    pass
        self.print_grid(True)
         
                
    def create_candidate_keys(self):
        self.grid_val = {}
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                self.grid_val[(x, y)] = '123456789' if self.grid[(x, y)] == 0 else self.grid[(x, y)]
        self.reduce_candidate_keys()        
                
    def board_grid(self):
        '''
        create the board_grid
        '''
        self.grid = {}
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                val = self.board_string[x * self.vertical_size + y]
                self.grid[(x, y)] = val if val.isdigit() else 0
           
                
    def print_grid(self, values=False):
        width = 1
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if values:
                    width = 9
                    print str(self.grid_val[(x, y)]).ljust(width),
                else:
                    print self.grid[(x, y)],
                if not (y + 1) % 3:
                    print ' | ',
            if not (x + 1) % 3:
                print '\n' + '-' * (9 * width + 20),
            print
        print "Remaining elements", self.grid.values().count(0)
        
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
            # self.hidden_singles()
