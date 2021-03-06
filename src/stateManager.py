'''
Created on 11.10.2010

@author: simon
'''

import pygame
import renderer
import levelManager
import physics
import interface
import score
import util.constants as constants
from intro import Intro

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
        
        self.intro = Intro()
        
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
            
    def endGame(self):
        self.run = False
        
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
        self.score = score.Score()
        self.interface = interface.Interface(self.score)

        self.levelManager = levelManager.LevelManager(self.gameRenderer, self.physicManager, self.score)
    
        self.levelManager.curLevel.addRndBlock()
        
        pygame.time.set_timer(constants.BLOCK_VERTI_TICK, 300)
        pygame.time.set_timer(constants.BLOCK_HORI_TICK, 75)

    def update(self):
        self.physicManager.update()
        self.gameRenderer.update()
    
    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                self.stateManager.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.run = False
                elif event.key == pygame.K_LEFT:
                    self.levelManager.curLevel.activeBlock.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    self.levelManager.curLevel.activeBlock.moveRight()
                elif event.key == pygame.K_UP or event.key == pygame.K_END or event.key == pygame.K_HOME or event.key == pygame.K_PAGEUP:
                    self.levelManager.curLevel.activeBlock.turnLeft()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_PAGEDOWN:
                    self.levelManager.curLevel.activeBlock.update("lowest-Y")
                
                if constants.ISDEBUG:
                    if event.key == pygame.K_m:
                        self.levelManager.curLevel._prettyPrintGrid()
                    elif event.key == pygame.K_n:
                        print self.levelManager.curLevel.activeBlock.rotaIndex, self.levelManager.curLevel.activeBlock.structureList[self.levelManager.curLevel.activeBlock.rotaIndex]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.levelManager.curLevel.activeBlock.moveStop()
                elif event.key == pygame.K_RIGHT:
                    self.levelManager.curLevel.activeBlock.moveStop()

            elif event.type == constants.BLOCK_VERTI_TICK:
                self.levelManager.curLevel.activeBlock.moveDown()
                self.levelManager.curLevel.activeBlock.update("normal-Y")
            elif event.type == constants.BLOCK_HORI_TICK:
                self.levelManager.curLevel.activeBlock.update("normal-X")
            elif event.type == constants.ENDGAME:
                self.stateManager.endGame()        

    def render(self):
        self.gameRenderer.renderBG()
        self.gameRenderer.renderMap(self.levelManager.curLevel)
        self.gameRenderer.renderGrid(self.levelManager.curLevel)
        self.interface.render(self.gameRenderer.screen)

class PauseState(State):
    
    def __init__(self, stateManager):
        State.__init__(self, stateManager)
    
    def update(self):
        pass
    
    def handleInput(self):
        pass
    
    def render(self):
        pass