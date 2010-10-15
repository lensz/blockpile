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
            if block.getAbsPos()[0] + quadrat.getAbsPos()[0] - constants.QUADRATSIZE < 0: 
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
            if block.getAbsPos()[0] + quadrat.getAbsPos()[0] + constants.QUADRATSIZE >= level.getSize()[0]*constants.QUADRATSIZE:
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
            if block.getAbsPos()[1] + quadrat.getAbsPos()[1] + constants.QUADRATSIZE >= level.getSize()[1]*constants.QUADRATSIZE:
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
            posQA = (a.getAbsPos()[0]+quadratA.getAbsPos()[0], a.getAbsPos()[1]+quadratA.getAbsPos()[1])
            absPosQA = (posQA[0], posQA[1])
            
            rectA = pygame.Rect( absPosQA, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
            
            for quadratB in b.quadratList:
                
                posQB = (b.getAbsPos()[0]+quadratB.getAbsPos()[0], b.getAbsPos()[1]+quadratB.getAbsPos()[1])
                absPosQB = (posQB[0], posQB[1])
            
                rectB = pygame.Rect( absPosQB, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
                
                if rectA.colliderect(rectB):
                    return True
                
    