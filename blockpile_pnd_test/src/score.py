'''
Created on 23.10.2010

@author: simon
'''

class Score(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.score = 0
        self.completedLines = 0
        
    def update(self,params):
        self.score = params[0]
        self.completedLines = params[1]