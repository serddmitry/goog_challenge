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
    normalize = None
    
    def init(self, data_set):
        self.xmin = min(data_set)
        self.xmax = max(data_set)
        if self.xmax == self.xmin:
            self.normalize = lambda x: 0
        else:
            self.normalize = lambda x: (x - self.xmin) / float(self.xmax - self.xmin)
            
            
if __name__ == "__main__":
    norm_test = Linear()
    norm_test.init([2])
    print norm_test.normalize(2)