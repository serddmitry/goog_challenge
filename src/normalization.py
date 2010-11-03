'''
Created on Nov 2, 2010

@author: dmitry.serdyuk
'''
from logging import getLogger

log = getLogger(__name__)

class Linear:
    '''
    Linear normalizes data, so the values [1,2,3,4,5] translated into
    [0, 0.25, 0.5, 0.75, 1], so we could calculate scores using different
    parameters.
    '''
    def init(self, data_set):
        self.xmin = min(data_set)
        self.xmax = max(data_set)
    
    def normalize(self, value):
        return (value - self.xmin) / (self.xmax - self.xmin)