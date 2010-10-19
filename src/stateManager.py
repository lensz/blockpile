'''
Created on 11.10.2010

@author: simon
'''

import pygame
import renderer
import levelManager
import physics
import util.constants as constants

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
        
        self.clock = pygame.time.Clock()
        
    def switchState(self, index):
        self.curState = self.stateList[index]
        
    def runGame(self):
        while self.run:
            self.clock.tick()
            #print self.clock.get_fps()
            
            self.curState.update()
            self.curState.handleInput()
            self.curState.render()
            
            pygame.display.update()
        
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

        self.gameRenderer = renderer.GameRenderer()
        self.physicManager = physics.PhysicManager()

        self.levelManager = levelManager.LevelManager(self.gameRenderer, self.physicManager)
    
        self.levelManager.curLevel.addRndBlock()
        
        pygame.time.set_timer(constants.BLOCK_DOWNTICK, 300)
        pygame.time.set_timer(constants.BLOCK_ROTATICK, 75)

    def update(self):
        self.physicManager.update()
        self.gameRenderer.update()
    
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stateManager.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.run = False
                elif event.key == pygame.K_LEFT:
                    self.levelManager.curLevel.activeBlock.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    self.levelManager.curLevel.activeBlock.moveRight()
                elif event.key == pygame.K_UP:
                    self.levelManager.curLevel.activeBlock.turnLeft()
                elif event.key == pygame.K_DOWN:
                    self.levelManager.curLevel.activeBlock.turnRight()
                elif event.key == pygame.K_SPACE:
                    pass
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.levelManager.curLevel.activeBlock.moveStop()
                elif event.key == pygame.K_RIGHT:
                    self.levelManager.curLevel.activeBlock.moveStop()
                elif event.key == pygame.K_UP:
                    self.levelManager.curLevel.activeBlock.rotaStop()
                elif event.key == pygame.K_DOWN:
                    self.levelManager.curLevel.activeBlock.rotaStop()
                elif event.key == pygame.K_SPACE:
                    pass
            
            elif event.type == constants.BLOCK_DOWNTICK:
                self.levelManager.curLevel.activeBlock.moveDown()
                self.levelManager.curLevel.activeBlock.updatePosY()
            elif event.type == constants.BLOCK_ROTATICK:
                self.levelManager.curLevel.activeBlock.updatePosX()
                self.levelManager.curLevel.activeBlock.updateRota()          

    def render(self):
        self.gameRenderer.renderBG()
        self.gameRenderer.renderMap(self.levelManager.curLevel)
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