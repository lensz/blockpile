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
        self.position = Vec2d(pos)
        self.color = color
        self.renderer = level.renderer
        self.physics = level.physics
    
    def getSurface(self):
        return self.surface
        
    def getPosition(self):
        return self.position
    
    def moveDown(self):
        '''gets called if there is no collision for the next step'''
        
        if self.physics.checkDownCol(self, self.level):
            self.level.addRndBlock()
            return
        self.position[1] += 1
        
    def moveLeft(self):
        if self.physics.checkLeftCol(self, self.level):
            return
        self.position[0] -= 1
        
    def moveRight(self):
        if self.physics.checkRightCol(self, self.level):
            return
        self.position[0] += 1

class Point_Block(Block):
    '''
        more for testing reasons
    '''
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.dim = (1,1)
        self.quadratList = [
                                Quadrat((0,0), color)
                            ]
        
        self.surface = self.renderer.generateBlockSurface(self)
        

    
class Quad_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.dim = (2,2)
        self.quadratList = [
                                Quadrat((0,0), color), Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color)
                            ]
        
        #self.matrix = [[Quadrat(),Quadrat()], [Quadrat(),Quadrat()]]
        
        self.surface = self.renderer.generateBlockSurface(self)
        
        
class Pyramide_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.dim = (3,2)
        self.quadratList = [
                                                       Quadrat((1,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), Quadrat((2,1), color)
                            ]
        
        self.surface = self.renderer.generateBlockSurface(self)
        
class H_Block(Block):
    
    def __init__(self, level, pos, color):
        Block.__init__(self, level, pos, color)
        
        self.dim = (3,3)
        self.quadratList = [
                                Quadrat((0,0), color),                        Quadrat((2,0), color),
                                Quadrat((0,1), color), Quadrat((1,1), color), Quadrat((2,1), color),
                                Quadrat((0,2), color),                        Quadrat((2,2), color)
                            ]
        
        self.surface = self.renderer.generateBlockSurface(self)

class Quadrat(object):
    def __init__(self, pos, color):
        self.pos = pos
        self.surface = pygame.Surface((constants.QUADRATSIZE, constants.QUADRATSIZE))
        self.surface.fill(color)
    
    def getPosition(self):
        return self.pos
        