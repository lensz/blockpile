'''
Created on 12.10.2010

@author: simon
'''

from util.vector import Vec2d

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
        offset = Vec2d(-1,0) # for calculating the "future" position
        
        #check if out of map
        for col in range(len(block.structureList[block.rotation])):
            for row in range(len(block.structureList[block.rotation][0])):
                if block.structureList[block.rotation][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if futureAbsQuadPos[0] < 0:
                        return True
        
        #check for block-block col
        if self.checkBlockBlockCol(block, level, offset):
            return True
        return False
    
    def checkRightCol(self, block, level):
        '''returns true if there is a collision'''

        offset = Vec2d(1,0) # for calculating the "future" position
        
        #check if out of map
        for col in range(len(block.structureList[block.rotation])):
            for row in range(len(block.structureList[block.rotation][0])):
                if block.structureList[block.rotation][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if futureAbsQuadPos[0] >= level.getSize()[0]:
                        return True
        
        #check for block-block col
        if self.checkBlockBlockCol(block, level, offset):
            return True
        return False
    
    def checkDownCol(self, block, level):
        offset = Vec2d(0,1) # for calculating the "future" position

        #check if out of map
        for col in range(len(block.structureList[block.rotation])):
            for row in range(len(block.structureList[block.rotation][0])):
                if block.structureList[block.rotation][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset
                    if futureAbsQuadPos[1] >= level.getSize()[1]:
                        return True
        
        #check for block-block col
        if self.checkBlockBlockCol(block, level, offset):
            return True
        return False
    
    def checkBlockBlockCol(self, block, level, offset):
        for col in range(len(block.structureList[block.rotation])):
            for row in range(len(block.structureList[block.rotation][0])):
                if block.structureList[block.rotation][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset
                    if level.getGridItem(futureAbsQuadPos) != 0:
                        return True
        return False
    
    def calcLowestPosition(self, block, level):
        offset = [0,0]
        while True:
            if offset[1]-1 >= level.getSize()[1]- (block.position[1]+len(block.structureList[block.rotation][0])):
                break
            if self.checkBlockBlockCol(block, level, offset):
                break
            offset[1] += 1

        newYpos = block.position[1]+(offset[1]-1)
        return newYpos
        #block.position[1] = newYpos
    