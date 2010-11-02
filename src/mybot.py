from planetwars import BaseBot, Game
from planetwars.universe import Universe
from strategies.expansion import Expansion
import math
from planetwars.planet import Planet
from planetwars.fleet import Fleet
from logging import getLogger
from distances import Median

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
    distance_strategy = Median()
    
    def init(self):
        if self.average_dist == -1:
            self.calc_average_distance()
    
    def calc_average_distance(self):
        #calculate average distance
        distances = []
        planets_list = list(self.planets)
        for i, pl1 in enumerate(planets_list):
            for j in xrange(i+1, len(planets_list)):
                pl2 = planets_list[j]
                distances.append(pl1.distance(pl2))
        sorted_dist = sorted(distances)
        log.debug("distances are %s", str(sorted_dist))
        self.distance_strategy.init(sorted_dist)
                
    def normalize_dist(self, dist):
        return self.distance_strategy.normalize(dist)
    
    def planet_by_id(self, id):
        for pl in self.planets:
            if pl.id == id:
                return pl

Game(MyBot, universe_class=MyUniverse)