'''
Created on 11.10.2010

@author: simon
'''

import pygame
import renderer
import levelManager

class Statemanager(object):
    '''
    classdocs
    '''
    
    MENUSTATE = 0
    GAMESTATE = 1
    PAUSESTATE = 2

    def __init__(self):
        '''
        Constructor
        '''
        
        pygame.init()
        
        self.run = True
        self.curState = None
        
        self.stateList = []
        self.stateList.append(MenuState(self))
        self.stateList.append(GameState(self))
        self.stateList.append(PauseState(self))
        
        self.switchState(self.GAMESTATE)
        
    def switchState(self, index):
        self.curState = self.stateList[index]
        
    def runGame(self):
        while self.run:
            self.curState.update()
            self.curState.handleInput()
            self.curState.render()
        
class State(object):
    
    def __init__(self, stateManager):
        self.stateManager = stateManager
    
    def update(self):
        pass
    
    def handleInput(self):
        pass
    
    def render(self):
        pass
    
class MenuState(State):
    
    def __init__(self, stateManager):
        State.__init__(self, stateManager)
    
    def update(self):
        pass
    
    def handleInput(self):
        pass
    
    def render(self):
        pass
    
class GameState(State):
    
    def __init__(self, stateManager):
        State.__init__(self, stateManager)

        self.stateManager = stateManager
        # create rendering, physics, level -management classes
        self.levelManager = levelManager.LevelManager()
        self.gameRenderer = renderer.GameRenderer()

    def update(self):
        self.gameRenderer.update()
    
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stateManager.run = False
    
    def render(self):
        self.gameRenderer.renderMap()
        self.gameRenderer.renderBlocks( self.levelManager.curLevel.getBlockList() )
    
class PauseState(State):
    
    def __init__(self, stateManager):
        State.__init__(self, stateManager)
    
    def update(self):
        pass
    
    def handleInput(self):
        pass
    
    def render(self):
        pass