'''
Created on 12.10.2010

@author: simon
'''

import random

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

    def addBlock(self, index):
        if index == 0:
            pass

    def addRndBlock(self):
        self.addBlock(random.randint(0,0))