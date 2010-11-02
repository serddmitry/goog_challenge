'''
Created on Nov 2, 2010

@author: dmitry.serdyuk
'''
from logging import getLogger

log = getLogger(__name__)

class Median:
    def init(self, sorted_dist):
        count = len(sorted_dist)
        if bool(count % 2):
            median = sorted_dist[int(count / 2)]
        else:
            floor_index = int(count / 2)
            median = (sorted_dist[floor_index]
                     + sorted_dist[floor_index + 1]) / 2
        log.info("Average distance is %d", median)
        self._average_dist = median
    
    def normalize(self, dist):
        return dist / self._average_dist
    
class QuotientOfMax:
    pass