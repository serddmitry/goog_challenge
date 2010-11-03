from logging import getLogger
import normalization
from planetwars import BaseBot, Game
from planetwars.universe import Universe
from strategies.expansion import Expansion

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
    normalization_strategy = normalization.Linear
    
    distances_norm = None
    
    
    def init(self):
        if not self.distances_norm:
            self.distances_norm = self.normalization_strategy()
            distances = []
            planets_list = list(self.planets)
            for i, pl1 in enumerate(planets_list):
                for j in xrange(i+1, len(planets_list)):
                    pl2 = planets_list[j]
                    distances.append(pl1.distance(pl2))
            self.distances_norm.init(distances)
            log.debug("normalizing distance %d",self.distances_norm.normalize(1))
                
    def normalize_dist(self, dist):
        return self.distance_strategy.normalize(dist)
    
    def planet_by_id(self, id):
        for pl in self.planets:
            if pl.id == id:
                return pl

Game(MyBot, universe_class=MyUniverse)