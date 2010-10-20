'''
Created on 12.10.2010

@author: simon
'''

import pygame
import util.constants as constants

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
        for quadrat in block.structureList[block.rotaIndex][1]:
            # map
            if block.getAbsPos()[0] + quadrat.getAbsPos()[0] <= 0: 
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    #futureBlock = copy.deepcopy(block)
                    #futureBlock.position[0] -= 1
                    futureOffset = (block.velocity[0],0)
                    if self.checkColBetweenBlocks(block, enemyBlock, futureOffset):
                        return True

        return False
    
    def checkRightCol(self, block, level):
        '''returns true if there is a collision'''

        curBlock = id(block)
        for quadrat in block.structureList[block.rotaIndex][1]:
            # map
            if block.getAbsPos()[0] + quadrat.getAbsPos()[0] + constants.QUADRATSIZE >= level.getSize()[0]*constants.QUADRATSIZE:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    #futureBlock = copy.deepcopy(block)
                    #futureBlock.position[0] += 1
                    futureOffset = (block.velocity[0],0)
                    if self.checkColBetweenBlocks(block, enemyBlock, futureOffset):
                        return True

        return False
    
    def checkDownCol(self, block, level):
        curBlock = id(block)
        for quadrat in block.structureList[block.rotaIndex][1]:
            # map
            if block.getAbsPos()[1] + quadrat.getAbsPos()[1] + block.velocity[1] >= level.getSize()[1]*constants.QUADRATSIZE:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    #futureBlock = copy.deepcopy(block)
                    #futureBlock.position[1] += 1
                    futureOffset = (0,block.velocity[1])
                    if self.checkColBetweenBlocks(block, enemyBlock, futureOffset):
                        return True
        return False
    
    def checkBlockIsSetted(self, block, level):
        curBlock = id(block)
        for quadrat in block.structureList[block.rotaIndex][1]:
            # map
            if block.getAbsPos()[1] + quadrat.getAbsPos()[1] + constants.QUADRATSIZE >= level.getSize()[1]*constants.QUADRATSIZE:
                return True
            # blocks
            for enemyBlock in level.blockList:
                if id(enemyBlock) != curBlock:
                    #futureBlock = copy.deepcopy(block)
                    #futureBlock.position[1] += 1
                    futureOffset = (0,1)
                    if self.checkColBetweenBlocks(block, enemyBlock, futureOffset):
                        return True
        return False
    
    def checkColBetweenBlocks(self, a, b, futureOffset):
        
        for quadratA in a.structureList[a.rotaIndex][1]:
            posQA = (a.getAbsPos()[0]+futureOffset[0]+quadratA.getAbsPos()[0], a.getAbsPos()[1]+futureOffset[1]+quadratA.getAbsPos()[1])
            absPosQA = (posQA[0], posQA[1])
            
            rectA = pygame.Rect( absPosQA, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
            
            for quadratB in b.structureList[b.rotaIndex][1]:
                #print b.getAbsPos()
                posQB = (b.getAbsPos()[0]+quadratB.getAbsPos()[0], b.getAbsPos()[1]+quadratB.getAbsPos()[1])
                absPosQB = (posQB[0], posQB[1])
            
                rectB = pygame.Rect( absPosQB, (constants.QUADRATSIZE, constants.QUADRATSIZE) )
                
                if rectA.colliderect(rectB):
                    return True
    