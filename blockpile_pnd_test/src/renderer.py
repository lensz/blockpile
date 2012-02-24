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

        if constants.ISFULLSCR:
            self.screen = pygame.display.set_mode(constants.RESOLUTION, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(constants.RESOLUTION)
        pygame.display.set_caption("Blockpile")
        pygame.mouse.set_visible(False)

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
        
        self.blockColors = {"O_Block" : (211,93,93),
                            "T_Block" : (231,98,42),
                            "I_Block" : (130,225,79),
                            "S_Block" : (21,139,37),
                            "Z_Block" : (23,134,143),
                            "L_Block" : (69,93,143),
                            "J_Block" : (127,72,216)
                            }
    
    def getBlockColor(self, type):
        return self.blockColors[type]
    
    def update(self):
        pass
    
    def renderBG(self):
        self.screen.fill([0,0,0])
    
    def renderMap(self, level):
        pygame.draw.rect(self.screen, (255,255,225), pygame.Rect(self.playboardOffset, (level.getSize()[0]*constants.QUADRATSIZE,level.getSize()[1]*constants.QUADRATSIZE)))
        self.renderMapGrid(level)
    
    def renderGrid(self, level):
        for col in range(level.getSize()[0]):
            pygame.draw.line(self.screen, [0,0,0], Vec2d(col*constants.QUADRATSIZE, 0)+self.playboardOffset, Vec2d(col*constants.QUADRATSIZE, level.getSize()[1]*constants.QUADRATSIZE)+self.playboardOffset)

        for row in range(level.getSize()[1]):
            pygame.draw.line(self.screen, [0,0,0], Vec2d(0, row*constants.QUADRATSIZE)+self.playboardOffset, Vec2d(level.getSize()[0]*constants.QUADRATSIZE, row*constants.QUADRATSIZE)+self.playboardOffset)

    def renderMapGrid(self, level):
        grid = level.getGrid()
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if grid[col][row] != 0:
                    surface = pygame.Surface((constants.QUADRATSIZE, constants.QUADRATSIZE))
                    surface.fill(grid[col][row])

                    absPos = (col*constants.QUADRATSIZE,row*constants.QUADRATSIZE) #in px
                    self.screen.blit(surface, self.playboardOffset + Vec2d(absPos[0], absPos[1]))
