'''
Created on 12.10.2010

@author: simon
'''

import random
import blocks
from util import constants

class LevelManager(object):
    '''
    classdocs
    '''


    def __init__(self, renderer, physics):
        '''
        Constructor
        '''
        self.levelList = []
        self.levelList.append(Level((2,3), renderer, physics))
        #self.levelList.append(Level((12,20), renderer, physics))
        
        self.curLevel = self.levelList[0]
        
class Level(object):

    def __init__(self, dim, renderer, physics):
        self.renderer = renderer
        self.physics = physics
        self.mapDim = dim
        
        #self.blockList = []
        self.grid = []
        self._initGrid()
        self._prettyPrintGrid()
        self.activeBlock = None
    
    def _initGrid(self):
        for x in range(self.mapDim[0]):
            line = []
            for y in range(self.mapDim[1]):
                line.append(0)
            self.grid.append(line)
    
    def _prettyPrintGrid(self):
        print "grid:"
        for y in range(len(self.grid[0])):
            line = []
            for x in range(len(self.grid)):
                line.append(0)
            print line
        print "---"

    def addBlock(self, index):
        # 1-255 in order to avoid fitting the color-key
        color = (random.randint(0,255), random.randint(1,255), random.randint(0,255))

        if index == 0:
            self.activeBlock = blocks.Quad_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color )
        elif index == 1:
            self.activeBlock = blocks.Pyramide_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color )
        elif index == 2:
            self.activeBlock = blocks.Point_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  )
        elif index == 3:
            self.activeBlock = blocks.H_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  )
        elif index == 4:
            self.activeBlock = blocks.Rotation_test( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  )

    def addRndBlock(self):
        self.addBlock(random.randint(0,4))
        
    def getBlockList(self):
        return self.blockList
    
    def getSize(self):
        return self.mapDim
    
    def getGrid(self):
        return self.grid