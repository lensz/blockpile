'''
Created on 12.10.2010

@author: simon
'''

from util.vector import Vec2d

class Block(object):
    '''
    classdocs
    '''


    def __init__(self, level, pos, color):
        '''
        Constructor
        '''
        self.level = level
        self.renderer = level.renderer
        self.physics = level.physics
        self.color = color
        self.movespeed = Vec2d(1, 1)
        
        self.velocity = Vec2d((0,0))
        self.rotationVel = 0

        self.position = Vec2d(pos)
        self.rotation = 0 # in degree 0-359
        self.rotaIndex = self.calcRotaIndex(self.rotation)

        self.structureList = [] #list of structures (>for every 90degree one item)
        
        self.curStateGrid = []
        self.level._initGrid(self.curStateGrid)

    def moveY(self):
        if self.velocity[1] > 0:
            # move down
            if not self.physics.checkDownCol(self, self.level):
                # there is no collision
                self.position[1] += self.velocity[1]
            else:
                self.level.mergeActiveBlock()
  
    def moveX(self):
        if self.velocity[0] > 0:
            # move right
            if not self.physics.checkRightCol(self, self.level):
                # there is no collision
                self.position[0] += self.velocity[0]
            else:
                print "right col"
        elif self.velocity[0] < 0:
            # move left
            if not self.physics.checkLeftCol(self, self.level):
                # there is no collision
                self.position[0] += self.velocity[0]
            else:
                print "left col"
        


    def update(self, dir):
        ''' gets called every tick(active block)'''
        self._deleteOldState()
        if dir == "X":
            self.moveX()
        elif dir == "Y":
            self.moveY()
        self._updateBlockInLevelGrid()
        self._storeState()

    def _deleteOldState(self):
        for col in range(len(self.curStateGrid)):
            for row in range(len(self.curStateGrid[0])):
                if self.curStateGrid[col][row] != 0:
                    self.level.setGridItem((col,row), 0)

    def _updateBlockInLevelGrid(self):
        for col in range(len(self.structureList[self.rotaIndex])):
            for row in range(len(self.structureList[self.rotaIndex][0])):
                if self.structureList[self.rotaIndex][col][row] != 0:
                    self.level.setGridItem(Vec2d(col,row)+self.position, self.color)

    def _storeState(self):
        for col in range(len(self.structureList[self.rotaIndex])):
            for row in range(len(self.structureList[self.rotaIndex][0])):
                if self.structureList[self.rotaIndex][col][row] != 0:
                    self.curStateGrid[col+self.position[0]][row+self.position[1]] = self.color
    
    def calcRotaIndex(self, rota):
        temp = int(round(rota/90.0))
        if temp == 4:
            temp = 0
        return temp

    def getPos(self):
        return self.position

    def updateRota(self):
        self.rotation += self.rotationVel
        if self.rotation >= 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360

        self.rotaIndex = self.calcRotaIndex(self.rotation)

        self.rotationVel = 0

    def turnLeft(self):
        self.rotationVel = 90
    
    def turnRight(self):
        self.rotationVel = -90
    
    def moveDown(self):

        self.velocity = Vec2d(self.velocity[0],self.movespeed[1])
        
    def moveLeft(self):

        self.velocity = Vec2d(-self.movespeed[0],self.velocity[1])
        
    def moveRight(self):

        self.velocity = Vec2d(self.movespeed[0],self.velocity[1])
        
    def moveStop(self):
        self.velocity = Vec2d(0,0)
        
    def rotaStop(self):
        self.rotationVel = 0
        
class Rotation_test(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (0,     color),
                                (color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (color,     0),
                                (color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color),
                                (color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color),
                                (0,     color)
                            )
                            )



"""
class Point_Block(Block):
    '''
        more for testing reasons
    '''
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append((
                            (1,1),
                            [
                                Quadrat((0,0), color)
                            ]
                            ))
        self.structureList.append((
                            (1,1),
                            [
                                Quadrat((0,0), color)
                            ]
                            ))
        self.structureList.append((
                            (1,1),
                            [
                                Quadrat((0,0), color)
                            ]
                            ))
        self.structureList.append((
                            (1,1),
                            [
                                Quadrat((0,0), color)
                            ]
                            ))
        
        #self.surface = self.renderer.generateBlockSurface(self)
    
class Quad_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        
        #self.surface = self.renderer.generateBlockSurface(self)
        
        
class Pyramide_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append((
                            (3,2),
                            [
                                                       Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), Quadrat((2,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,3),
                            [
                                                       Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color),
                                                       Quadrat((1,2), color)
                            ]
                            ))
        self.structureList.append((
                            (3,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color), Quadrat((2,0), color),
                                                       Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,3),
                            [   
                                Quadrat((0,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), 
                                Quadrat((0,2), color)
                            ]
                            ))
        
        #self.surface = self.renderer.generateBlockSurface(self)
        
class H_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        

        self.structureList.append((
                            (3,3),
                            [
                                Quadrat((0,0), color),                        Quadrat((2,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), Quadrat((2,1), color),
                                Quadrat((0,2), color),                        Quadrat((2,2), color)
                            ]
                            ))
        self.structureList.append((
                            (3,3),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color), Quadrat((2,0), color),
                                                       Quadrat((1,1), color),
                                Quadrat((0,2), color), Quadrat((1,2), color), Quadrat((2,2), color)
                            ]
                            ))
        self.structureList.append((
                            (3,3),
                            [
                                Quadrat((0,0), color),                        Quadrat((2,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), Quadrat((2,1), color),
                                Quadrat((0,2), color),                        Quadrat((2,2), color)
                            ]
                            ))
        self.structureList.append((
                            (3,3),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color), Quadrat((2,0), color),
                                                       Quadrat((1,1), color),
                                Quadrat((0,2), color), Quadrat((1,2), color), Quadrat((2,2), color)
                            ]
                            ))
        
        #self.surface = self.renderer.generateBlockSurface(self)
"""
        