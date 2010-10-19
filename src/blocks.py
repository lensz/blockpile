'''
Created on 12.10.2010

@author: simon
'''

from util.vector import Vec2d
import util.constants as constants
import pygame

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
        self.movespeed = constants.QUADRATSIZE
        
        self.velocity = Vec2d((0,0))
        self.rotationVel = 0

        self.position = Vec2d(pos) # abs px in screen
        self.rotation = 0 # in degree 0-359
        self.rotaIndex = self.calcRotaIndex(self.rotation)

        self.structureList = [] #list of dim | structures (>for every 90degree one item)
    
    def calcRotaIndex(self, rota):
        temp = int(round(rota/90.0))
        if temp == 4:
            temp = 0
        return temp
    
    def getSurface(self):
        return self.surface
        
    def getAbsPos(self):
        return self.position
    
    def updatePosX(self):
        if self.velocity[0] > 0:
            if not self.physics.checkRightCol(self, self.level):
                self.position[0] += self.velocity[0]
        elif self.velocity[0] < 0:
            if not self.physics.checkLeftCol(self, self.level):
                self.position[0] += self.velocity[0]
              
        #self.velocity[0] = 0
        
    def updatePosY(self):

        if not self.physics.checkDownCol(self, self.level):
            self.position[1] += self.velocity[1]
        else:
            self.rotation = self.rotaIndex * 90
            self.level.addRndBlock()
        
        #self.velocity[1] = 0
    
    def updateRota(self):
        self.rotation += self.rotationVel
        if self.rotation >= 360:
            self.rotation -= 360
        elif self.rotation < 0:
            self.rotation += 360
        #print self.rotation
        self.rotaIndex = self.calcRotaIndex(self.rotation)
        #print self.rotaIndex
        
        self.rotationVel = 0
        
    def turnLeft(self):
        self.rotationVel = 90
    
    def turnRight(self):
        self.rotationVel = -90
    
    def moveDown(self):
        '''gets called if there is no collision for the next step'''
        
        #if self.physics.checkDownCol(self, self.level):
        #    self.level.addRndBlock()
        #    self.rotation = self.rotaIndex * 90
        #    return
        self.velocity = Vec2d(self.velocity[0],self.movespeed)
        
    def moveLeft(self):
        #if self.physics.checkLeftCol(self, self.level):
        #    return
        self.velocity = Vec2d(-self.movespeed,self.velocity[1])
        
    def moveRight(self):
        #if self.physics.checkRightCol(self, self.level):
        #    return
        self.velocity = Vec2d(self.movespeed,self.velocity[1])
        
    def moveStop(self):
        self.velocity = Vec2d(0,0)
        
    def rotaStop(self):
        self.rotationVel = 0
        
class Rotation_test(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), 
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                                       Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                                       Quadrat((1,1), color)
                            ]
                            ))
        self.structureList.append((
                            (2,2),
                            [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color)                          
                            ]
                            ))

        self.surface = self.renderer.generateBlockSurface(self)

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
        
        self.surface = self.renderer.generateBlockSurface(self)
    
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
        
        self.surface = self.renderer.generateBlockSurface(self)
        
        
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
        
        self.surface = self.renderer.generateBlockSurface(self)
        
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
        
        self.surface = self.renderer.generateBlockSurface(self)

class Quadrat(object):
    def __init__(self, pos, color):
        self.pos = pos
        self.surface = pygame.Surface((constants.QUADRATSIZE, constants.QUADRATSIZE))
        self.surface.fill(color)
    
    def getAbsPos(self):
        return (self.pos[0]*constants.QUADRATSIZE,self.pos[1]*constants.QUADRATSIZE)
    
    def getPosition(self):
        return self.pos
        