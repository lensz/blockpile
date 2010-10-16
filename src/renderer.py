'''
Created on 12.10.2010

@author: simon
'''

import util.constants as constants
import pygame
from util.vector import Vec2d

class Renderer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.screen = pygame.display.set_mode(constants.RESOLUTION, constants.ISFULLSCR)

    def update(self):
        pass
    
    def renderMap(self):
        pass
    
    def renderBlocks(self):
        pass
        
class GameRenderer(Renderer):
    
    def __init__(self):
        Renderer.__init__(self)
        
        self.playboardOffset = Vec2d(250,75) #in px
        
    def update(self):
        pass
    
    def renderBG(self):
        self.screen.fill([0,0,0])
    
    def renderMap(self, level):
        pygame.draw.rect(self.screen, (255,255,225), pygame.Rect(self.playboardOffset, (level.getSize()[0]*constants.QUADRATSIZE,level.getSize()[1]*constants.QUADRATSIZE)))

    def generateBlockSurface(self, block):
        surface = pygame.Surface( (block.dim[0]*constants.QUADRATSIZE, block.dim[1]*constants.QUADRATSIZE))
        surface.fill((255,0,255))
        surface.set_colorkey((255,0,255))

        for quadrat in block.quadratList:
            surface.blit( quadrat.surface, (quadrat.getPosition()[0]*constants.QUADRATSIZE, quadrat.getPosition()[1]*constants.QUADRATSIZE) )
        
        return surface

    def renderBlocks(self, blockList):

        for block in blockList:
            blockSur = block.getSurface()
            blockSur = pygame.transform.rotate(blockSur, block.rotation)
            self.screen.blit(blockSur , self.playboardOffset + Vec2d(block.getAbsPos()[0], block.getAbsPos()[1]))
