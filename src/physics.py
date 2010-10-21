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
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if futureAbsQuadPos[0] < 0:
                        return True
        
        #check for block-block col
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if level.getGridItem(futureAbsQuadPos) != 0:
                        return True
        return False
    
    def checkRightCol(self, block, level):
        '''returns true if there is a collision'''

        offset = Vec2d(1,0) # for calculating the "future" position
        
        #check if out of map
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if futureAbsQuadPos[0] >= level.getSize()[0]:
                        return True
        
        #check for block-block col
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset  
                    if level.getGridItem(futureAbsQuadPos) != 0:
                        return True
        return False
    
    def checkDownCol(self, block, level):
        offset = Vec2d(0,1) # for calculating the "future" position

        #check if out of map
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset
                    if futureAbsQuadPos[1] >= level.getSize()[1]:
                        return True
        
        #check for block-block col
        for col in range(len(block.structureList[block.rotaIndex])):
            for row in range(len(block.structureList[block.rotaIndex][0])):
                if block.structureList[block.rotaIndex][col][row] != 0:
                    relQuadPos = Vec2d((col,row))
                    absQuadPos = relQuadPos+block.position
                    futureAbsQuadPos = absQuadPos+offset
                    if level.getGridItem(futureAbsQuadPos) != 0:
                        level._prettyPrintGrid()
                        return True
        return False
    