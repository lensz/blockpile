'''
Created on 12.10.2010

@author: simon
'''

import pygame
import util.constants as constants
import copy

class PhysicManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def update(self):
        pass

    def checkMapCol(self):
        pass
    
    def checkLeftCol(self, block, level):
        '''returns true if there is a collision'''
        curBlock = id(block)
        for quadrat in block.quadratList:
            # map
            if block.getPosition()[0] + quadrat.getPosition()[0] - 1 < 0:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    futureBlock = copy.deepcopy(block)
                    futureBlock.position[0] -=1
                    if self.checkColBetweenBlocks(futureBlock, enemyBlock):
                        return True

        return False
    
    def checkRightCol(self, block, level):
        '''returns true if there is a collision'''

        curBlock = id(block)
        for quadrat in block.quadratList:
            # map
            if block.getPosition()[0] + quadrat.getPosition()[0] + 1 >= level.getSize()[0]:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    futureBlock = copy.deepcopy(block)
                    futureBlock.position[0] +=1
                    if self.checkColBetweenBlocks(futureBlock, enemyBlock):
                        return True

        return False
    
    def checkDownCol(self, block, level):
        curBlock = id(block)
        for quadrat in block.quadratList:
            # map
            if block.getPosition()[1] + quadrat.getPosition()[1] + 1 >= level.getSize()[1]:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    futureBlock = copy.deepcopy(block)
                    futureBlock.position[1] +=1
                    if self.checkColBetweenBlocks(futureBlock, enemyBlock):
                        return True
        return False
    
    def checkColBetweenBlocks(self, a, b):
        
        for quadratA in a.quadratList:
            posQA = (a.getPosition()[0]+quadratA.getPosition()[0], a.getPosition()[1]+quadratA.getPosition()[1])
            absPosQA = (posQA[0]*constants.QUADRATSIZE, posQA[1]*constants.QUADRATSIZE)
            
            rectA = pygame.Rect( absPosQA, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
            
            for quadratB in b.quadratList:
                
                posQB = (b.getPosition()[0]+quadratB.getPosition()[0], b.getPosition()[1]+quadratB.getPosition()[1])
                absPosQB = (posQB[0]*constants.QUADRATSIZE, posQB[1]*constants.QUADRATSIZE)
            
                rectB = pygame.Rect( absPosQB, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
                
                if rectA.colliderect(rectB):
                    return True
                
    