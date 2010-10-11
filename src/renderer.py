'''
Created on 12.10.2010

@author: simon
'''

import util.constants as constants
import pygame

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
        
    def update(self):
        print "update renderer"
    
    def renderMap(self):
        print "render map"
    
    def renderBlocks(self):
        print "render blocks"