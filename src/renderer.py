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
        
        self.playboardOffset = Vec2d(275,40) #in px
        
    def update(self):
        pass
    
    def renderBG(self):
        self.screen.fill([0,0,0])
    
    def renderMap(self, level):
        pygame.draw.rect(self.screen, (255,255,225), pygame.Rect(self.playboardOffset, (level.getSize()[0]*constants.QUADRATSIZE,level.getSize()[1]*constants.QUADRATSIZE)))
        self.renderMapGrid(level)
    
    def renderMapGrid(self, level):
        grid = level.getGrid()
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] != 0:
                    surface = pygame.Surface((constants.QUADRATSIZE, constants.QUADRATSIZE))
                    surface.fill(grid[col][row])

                    absPos = (col*constants.QUADRATSIZE,row*constants.QUADRATSIZE) #in px
                    self.screen.blit(surface, self.playboardOffset + Vec2d(absPos[0], absPos[1]))
