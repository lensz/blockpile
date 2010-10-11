'''
Created on 12.10.2010

@author: simon
'''

from util.vector import Vec2d 
from util.matrix import Matrix
import util.constants as constants

class Block(object):
    '''
    classdocs
    '''


    def __init__(self, pos, color):
        '''
        Constructor
        '''
        self.position = Vec2d(pos)
        self.color = color
    
    def getSurface(self):
        # TODO
        pass
        
    def getPosition(self):
        return self.position
    
    def moveDown(self):
        '''gets called if there is no collision for the next step'''
        self.position += constants.QUADRATSIZE
    
class Quad_Block(Block):
    
    def __init__(self, pos, color):
        Block.__init__(self, pos, color)
        
        #TODO: check if matrix representation is useable
        self.matrix = Matrix(2,2)
        print self.matrix
        self.matrix.setitem(1, 1, True)
        self.matrix.setitem(1, 2, True)
        self.matrix.setitem(2, 1, True)
        self.matrix.setitem(2, 2, True)
        print self.matrix

class Pyramide_Block(Block):
    
    def __init__(self, pos, color):
        Block.__init__(self, pos, color)
        
        self.matrix = Matrix(3,2)
        print self.matrix
        self.matrix.setitem(1, 1, False)
        self.matrix.setitem(1, 2, True)
        self.matrix.setitem(1, 3, False)
        self.matrix.setitem(2, 1, True)
        self.matrix.setitem(2, 2, True)
        self.matrix.setitem(2, 3, True)
        print self.matrix
        