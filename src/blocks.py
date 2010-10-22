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

        self.position = Vec2d(pos)
        self.rotation = 0 # index of structure list

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
        elif self.velocity[0] < 0:
            # move left
            if not self.physics.checkLeftCol(self, self.level):
                # there is no collision
                self.position[0] += self.velocity[0]

    def update(self, dir):
        ''' gets called every tick(active block)'''
        self._deleteOldState()
        if dir == "normal-X":
            self.moveX()
        elif dir == "normal-Y":
            self.moveY()
        elif dir == "lowest-Y":
            self.position[1] = self.physics.calcLowestPosition(self, self.level)
        self.level.checkForCompletesLines()
        self._updateBlockInLevelGrid()
        self._storeState()
        
        

    def _deleteOldState(self):
        for col in range(len(self.curStateGrid)):
            for row in range(len(self.curStateGrid[0])):
                if self.curStateGrid[col][row] != 0:
                    self.level.setGridItem((col,row), 0)

    def _updateBlockInLevelGrid(self):
        for col in range(len(self.structureList[self.rotation])):
            for row in range(len(self.structureList[self.rotation][0])):
                if self.structureList[self.rotation][col][row] != 0:
                    self.level.setGridItem(Vec2d(col,row)+self.position, self.color)

    def _storeState(self):
        for col in range(len(self.structureList[self.rotation])):
            for row in range(len(self.structureList[self.rotation][0])):
                if self.structureList[self.rotation][col][row] != 0:
                    self.curStateGrid[col+self.position[0]][row+self.position[1]] = self.color

    def getPos(self):
        return self.position

    def updateRota(self, offset):
        
        rota = self.rotation
        oldRota = self.rotation
        rota += offset

        rota %= 4

        if self.physics.checkRotaCol(self, self.level, rota):
            self.rotation = oldRota
        else:
            self.rotation = rota

    def turnLeft(self):
        self.updateRota(1)

    def turnRight(self):
        self.updateRota(-1)
    
    def moveDown(self):

        self.velocity = Vec2d(self.velocity[0],self.movespeed[1])
        
    def moveLeft(self):

        self.velocity = Vec2d(-self.movespeed[0],self.velocity[1])
        
    def moveRight(self):

        self.velocity = Vec2d(self.movespeed[0],self.velocity[1])
        
    def moveStop(self):
        self.velocity = Vec2d(0,0)

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

class O_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append(
                            (
                                (color, color),
                                (color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color),
                                (color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color),
                                (color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color),
                                (color, color)
                            )
                            )

class T_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append(
                            (
                                (0    , color,     0),
                                (color, color, color),
                                (0    ,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    , color,     0),
                                (0    , color, color),
                                (0    , color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (color, color, color),
                                (0    , color,     0)
                                
                            )
                            )
        self.structureList.append(
                            (
                                (0    , color,     0),
                                (color, color,     0),
                                (0    , color,     0)
                            )
                            )

class I_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (0    , color,     0,     0),
                                (0    , color,     0,     0),
                                (0    , color,     0,     0),
                                (0    , color,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0,     0),
                                (color, color, color, color),
                                (0    ,     0,     0,     0),
                                (0    ,     0,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    , color,     0,     0),
                                (0    , color,     0,     0),
                                (0    , color,     0,     0),
                                (0    , color,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0,     0),
                                (color, color, color, color),
                                (0    ,     0,     0,     0),
                                (0    ,     0,     0,     0)
                            )
                            )
        
class S_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (0    , color,     0),
                                (color, color,     0),
                                (color,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (color, color,     0),
                                (0    , color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (0    , color,     0),
                                (color, color,     0),
                                (color,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (color, color,     0),
                                (0    , color, color)
                            )
                            )

class Z_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (color,     0,     0),
                                (color, color,     0),
                                (0    , color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (0    , color, color),
                                (color, color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (color,     0,     0),
                                (color, color,     0),
                                (0    , color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (0    , color, color),
                                (color, color,     0)
                            )
                            )
        
class L_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (0    , color, color),
                                (0    , color,     0),
                                (0    , color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (color, color, color),
                                (0    ,     0, color)
                            )
                            )
        self.structureList.append(
                            (
                                (0    , color,     0),
                                (0    , color,     0),
                                (color, color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (color,     0,     0),
                                (color, color, color),
                                (0    ,     0,     0)
                            )
                            )

class J_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)

        self.structureList.append(
                            (
                                (0    , color,     0),
                                (0    , color,     0),
                                (0    , color, color)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0,     0),
                                (color, color, color),
                                (color,     0,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (color, color,     0),
                                (0    , color,     0),
                                (0    , color,     0)
                            )
                            )
        self.structureList.append(
                            (
                                (0    ,     0, color),
                                (color, color, color),
                                (0    ,     0,     0)
                            )
                            )