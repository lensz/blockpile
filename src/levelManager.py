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
        self.levelList.append(Level((12,20), renderer, physics))
        
        self.curLevel = self.levelList[0]
        
class Level(object):

    def __init__(self, dim, renderer, physics):
        self.renderer = renderer
        self.physics = physics
        self.mapDim = dim
        
        self.blockList = []
        
        self.activeBlock = None

    def addBlock(self, index):
        # 1-255 in order to avoid fitting the color-key
        color = (random.randint(0,255), random.randint(1,255), random.randint(0,255))

        if index == 0:
            self.blockList.append(blocks.Quad_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color ))
            self.activeBlock = self.blockList[-1]
        elif index == 1:
            self.blockList.append(blocks.Pyramide_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color ))
            self.activeBlock = self.blockList[-1]
        elif index == 2:
            self.blockList.append(blocks.Point_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  ))
            self.activeBlock = self.blockList[-1]
        elif index == 3:
            self.blockList.append(blocks.H_Block( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  ))
            self.activeBlock = self.blockList[-1]
        elif index == 4:
            self.blockList.append(blocks.Rotation_test( self, (self.mapDim[0]//2*constants.QUADRATSIZE, 0), color  ))
            self.activeBlock = self.blockList[-1]

    def addRndBlock(self):
        self.addBlock(random.randint(0,4))
        
    def getBlockList(self):
        return self.blockList
    
    def getSize(self):
        return self.mapDim