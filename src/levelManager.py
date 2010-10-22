'''
Created on 12.10.2010

@author: simon
'''

import random
import blocks
from util import constants
import pygame

class LevelManager(object):
    '''
    classdocs
    '''


    def __init__(self, renderer, physics):
        '''
        Constructor
        '''
        self.levelList = []
        #self.levelList.append(Level((2,3), renderer, physics))
        self.levelList.append(Level((12,20), renderer, physics))
        
        self.curLevel = self.levelList[0]
        
class Level(object):

    def __init__(self, dim, renderer, physics):
        self.renderer = renderer
        self.physics = physics
        self.mapDim = dim
        
        #self.blockList = []
        self.grid = []
        self._initGrid(self.grid)

        self.activeBlock = None
        
        self.upperBorder = 5 #No static tile should be above this border
    
    def _initGrid(self, grid):
        for x in range(self.mapDim[0]):
            line = []
            for y in range(self.mapDim[1]):
                line.append(0)
            grid.append(line)
    
    def _prettyPrintGrid(self):
        print "grid:"
        for y in range(len(self.grid[0])):
            line = []
            for x in range(len(self.grid)):
                if self.grid[x][y] != 0:
                    line.append(1)
                else:
                    line.append(0)
            print y, line
        print "---"

    def addBlock(self, index):
        # 1-255 in order to avoid fitting the color-key
        color = (random.randint(0,255), random.randint(1,255), random.randint(0,255))

        if index == 1:
            self.activeBlock = blocks.Quad_Block( self, (self.mapDim[0]//2, 0), color )
        elif index == 2:
            self.activeBlock = blocks.Pyramide_Block( self, (self.mapDim[0]//2, 0), color )
        elif index == 3:
            self.activeBlock = blocks.I_Block( self, (self.mapDim[0]//2, 0), color  )
        elif index == 4:
            self.activeBlock = blocks.Rotation_test( self, (self.mapDim[0]//2, 0), color  )

    def addRndBlock(self):
        self.addBlock(random.randint(1,4))

    def mergeActiveBlock(self):
        # check if the upper border is reached. If yes, end game
        if self.activeBlock.position[1] <= self.upperBorder:
            pygame.event.post(pygame.event.Event(constants.ENDGAME)) 
        self.addRndBlock()

    def getBlockList(self):
        return self.blockList
    
    def getSize(self):
        return self.mapDim
    
    def getGrid(self):
        return self.grid
    
    def getGridItem(self, pos):
        return self.grid[pos[0]][pos[1]]
    
    def setGridItem(self, pos, color):
        self.grid[pos[0]][pos[1]] = color
