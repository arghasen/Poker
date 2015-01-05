'''
Created on Jan 4, 2015

@author: argha
'''

from SodukuException import SodukuException

class Board(object):
    '''
    This is the board of the soduku
    '''
    def count_candidates(self):
        counter = 0
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                counter += len(self.grid_val[(x, y)])
        print "Total Keys:", counter
    
    def reduce_keys_from_rows(self, x):
        for z in xrange(self.vertical_size):
            if self.grid[(x, z)] != 0:
                for y in xrange(self.horizontal_size):
                    if z != y:
                        self.grid_val[(x, y)] = self.grid_val[(x, y)].replace(self.grid[(x, z)], '')
        
    
    def reduce_keys_from_colums(self, y):
        for z in xrange(self.horizontal_size):
            if self.grid[(z, y)] != 0:
                for x in xrange(self.vertical_size):
                    if z != x:
                        self.grid_val[(x, y)] = self.grid_val[(x, y)].replace(self.grid[(z, y)], '')
    
    
    def reduce_keys_from_box(self, x, y):
        '''
        reduces keys based on the box. Assumes a 3*3 box
        '''
        grid_nos = (divmod(x, 3)[0], divmod(y, 3)[0])
        
        for a in xrange(grid_nos[0] * 3, grid_nos[0] * 3 + 3):
            for b in xrange(grid_nos[1] * 3, grid_nos[1] * 3 + 3):
                if self.grid[(a, b)] != 0:
                    c = self.grid_val[(x, y)]
                    self.grid_val[(x, y)] = c.replace(self.grid[(a, b)], '')  if len(c) > 1 else c 
                    
                    
    def hidden_singles(self):
        pass
        

    def remove_key_from_row(self, xposition, key):
        for z in xrange(self.horizontal_size):
            if z / self.hgrid  != xposition / self.hgrid :
                self.grid_val[(xposition, z)] = self.grid_val[(xposition, z)].replace(key, '')
    
    def remove_key_from_column(self, yposition, key):
        for z in xrange(self.horizontal_size):
            if z / self.vgrid  != yposition / self.vgrid:
                self.grid_val[(z, yposition)] = self.grid_val[(z,yposition)].replace(key, '')
      
    
    def box_locked_candidate(self):
        self.count_candidates()
        a = [(r, s) for r in range(self.vgrid) for s in range(self.hgrid)]
        key_list = {}
        for a1 in a:
            for b in xrange(a1[0] * self.vgrid , a1[0] * self.vgrid + self.vgrid):
                for c in xrange(a1[1] * self.hgrid, a1[1] * self.hgrid + self.hgrid):
                    val = self.grid_val[(b, c)]
                    val_list = list(val)
                    for v in val_list:
                        try:
                            key_list[v] += [(b, c)]
                        except KeyError:
                            key_list[v] = [(b, c)]
            for key in key_list.keys():
                positions = key_list[key]
                if len(positions) > 1:
                    xpositions = set(_[0] for _ in positions)
                    ypositions = set(_[1] for _ in positions)
                    if len(xpositions) == 1:
                        self.remove_key_from_row(xpositions.pop(), key)
                    if len(ypositions) == 1:
                        self.remove_key_from_column(ypositions.pop(), key)   
        self.count_candidates()                
                        
    def row_column_locked_candidate(self):
        pass
    

    def remove_pair_from_row(self, x, pairkey):
        for y in xrange(self.vertical_size):
            if self.grid_val[(x,y)] != pairkey:
                self.grid_val[(x,y)] = self.grid_val[(x,y)].translate(None,pairkey)
    

    def remove_pair_from_column(self, y, pairkey):
        for x in xrange(self.vertical_size):
            if self.grid_val[(x,y)] != pairkey:
                self.grid_val[(x,y)] = self.grid_val[(x,y)].translate(None,pairkey)
    
    
    def remove_pair_from_grid(self, gridnum, pairkey):
        for x in xrange(gridnum[0] * self.vgrid , gridnum[0] * self.vgrid + self.vgrid):
            for y in xrange(gridnum[1] * self.hgrid, gridnum[1] * self.hgrid + self.hgrid):
                if self.grid_val[(x,y)] != pairkey:
                    self.grid_val[(x,y)] = self.grid_val[(x,y)].translate(None,pairkey)
    
    
    def pair(self):
        self.count_candidates()
        # pair in a row
        for x in xrange(self.horizontal_size):
            candidate_pairs = set()
            for y in xrange(self.vertical_size):
                if len(self.grid_val[(x,y)]) == 2:
                    if self.grid_val[(x,y)] in candidate_pairs:
                        self.remove_pair_from_row( x, self.grid_val[(x,y)])
                    else:
                        candidate_pairs.add(self.grid_val[(x,y)])
        # pair in a column
        for y in xrange(self.horizontal_size):
            candidate_pairs = set()
            for x in xrange(self.vertical_size):
                if len(self.grid_val[(x,y)]) == 2:
                    if self.grid_val[(x,y)] in candidate_pairs:
                        self.remove_pair_from_column( y, self.grid_val[(x,y)])
                    else:
                        candidate_pairs.add(self.grid_val[(x,y)])   
        #TODO: pair in a box  
        a = [(r, s) for r in range(self.vgrid) for s in range(self.hgrid)]
        for a1 in a:
            candidate_pairs = set()
            for b in xrange(a1[0] * self.vgrid , a1[0] * self.vgrid + self.vgrid):
                for c in xrange(a1[1] * self.hgrid, a1[1] * self.hgrid + self.hgrid):
                    val = self.grid_val[(b, c)]
                    if len(val) == 2:
                        if self.grid_val[(b,c)] in candidate_pairs:
                            self.remove_pair_from_grid( a1, self.grid_val[(b,c)])
                        else:
                            candidate_pairs.add(self.grid_val[(b,c)])  
        self.count_candidates()      
        
                              
    def reduce_candidate_keys(self):
        'This is basically the singles rule'
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if self.grid[(x, y)] == 0:
                    self.reduce_keys_from_rows(x)
                    self.reduce_keys_from_colums(y)
                    self.reduce_keys_from_box(x, y)
                    pass
        self.print_grid(True)
         
                
    def update_grid(self):
        updated = False
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                if len(self.grid_val[(x, y)]) == 1 and self.grid[(x, y)] == 0:
                    self.grid[(x, y)] = self.grid_val[(x, y)]
                    updated = True
        return updated
    
    def create_candidate_keys(self):
        self.grid_val = {}
        for x in xrange(self.horizontal_size):
            for y in xrange(self.vertical_size):
                self.grid_val[(x, y)] = '123456789' if self.grid[(x, y)] == 0 else self.grid[(x, y)]
        self.print_grid()
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
        print "Remaining elements", sum(len(_) > 1 for _ in self.grid_val.values())
        
    def get_Grid(self):
        return self.grid
        
        
    def __init__(self, board_string):
        '''
        Constructor
        '''
        self.vertical_size = 9
        self.horizontal_size = 9
        self.hgrid = 3
        self.vgrid = 3
        if len(board_string) != self.vertical_size * self.horizontal_size:
            raise SodukuException("Soduku board must have 9*9 grid.")
        else:
            self.board_string = board_string
            self.board_grid()
            self.create_candidate_keys()
            while(self.update_grid()):
                self.reduce_candidate_keys()
            # self.hidden_singles()
                self.box_locked_candidate()
                self.pair()
#             while(self.update_grid()):
#                 self.reduce_candidate_keys()
#             self.pair()
            self.print_grid(True)
