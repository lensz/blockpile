'''
Created on 12.10.2010

@author: simon
'''

import random
import blocks

class LevelManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.levelList = []
        self.levelList.append(Level((20,20), 1000))
        
        self.curLevel = self.levelList[0]
        
class Level(object):

    def __init__(self, dim, speed):
        self.mapDim = dim
        self.blockSpeed = speed
        
        self.blockList = []

    def addBlock(self, index):
        # quad block
        if index == 0:
            self.blockList.append(blocks.Quad_Block( (self.mapDim[0]//2, 0), (255,0,255) ))
        elif index == 1:
            self.blockList.append(blocks.Pyramide_Block( (self.mapDim[0]//2, 0), (255,0,255) ))

    def addRndBlock(self):
        self.addBlock(random.randint(0,1))
        
    def getBlockList(self):
        return self.blockList