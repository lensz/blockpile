'''
Created on 23.10.2010

@author: simon
'''

import pygame
from util.vector import Vec2d
import util.constants as constants 

class Interface(object):

    def __init__(self, score):
        self.score = score
        self.schriftart = pygame.font.Font(None,30)
        self.overlay = pygame.Surface((200,constants.RESOLUTION[1]//2))
        self.overlay.fill((255,192,124))
        
        self.overlayPos = Vec2d(constants.RESOLUTION[0]-(self.overlay.get_width()+30), constants.RESOLUTION[1]//4 - 5)
        self.scorePos = Vec2d(constants.RESOLUTION[0]-(self.overlay.get_width() + 25), constants.RESOLUTION[1]//4)
        self.completeLinesPos = Vec2d(constants.RESOLUTION[0]-(self.overlay.get_width() + 25), constants.RESOLUTION[1]//4 + 40)

    def render(self, screen):
        screen.blit(self.overlay,self.overlayPos)
        screen.blit(self.schriftart.render('Score: ' + str(self.score.score),1,[0,0,0]),self.scorePos)
        screen.blit(self.schriftart.render('Lines: ' + str(self.score.completedLines),1,[0,0,0]),self.completeLinesPos)
