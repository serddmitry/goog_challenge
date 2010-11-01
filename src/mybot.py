from planetwars import BaseBot, Game
from planetwars.universe import Universe
from strategies.expansion import Expansion
import math
from planetwars.planet import Planet
from planetwars.fleet import Fleet
from logging import getLogger

# This shows how you can add your own functionality to game objects (Universe in this case).
log = getLogger(__name__)

class MyBot(BaseBot):
    """ My super bot"""    
    def do_turn(self):
        self.universe.init()
        log.info("do turn")
        strat = Expansion(self.universe)
        log.info("Strategy selected")
        strat.act()

class MyUniverse(Universe):
    average_dist = -1
    
    def init(self):
        if self.average_dist == -1:
            self.calc_average_distance()
    
    def calc_average_distance(self):
        #calculate average distance
        distances = []
        for pl1 in self.planets:
            for pl2 in self.planets:
                distances.append(pl1.distance(pl2))
        sorted_dist = sorted(distances)
        count = len(sorted_dist)
        if bool(count % 2):
            median = sorted_dist[int(count / 2)]
        else:
            floor_index = int(count / 2)
            median = (sorted_dist[floor_index]
                     + sorted_dist[floor_index + 1]) / 2
        log.debug("average distance is %d", median)
        self.average_dist = median
                
    def normalize_dist(self, dist):
        return dist / self.average_dist

Game(MyBot, universe_class=MyUniverse)