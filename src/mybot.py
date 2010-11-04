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
    
    distance_norm = None
    growth_norm = None
    
    
    
    def init(self):
        if not self.distance_norm:
            self.distance_norm = self.normalization_strategy()
            distances = []
            planets_list = list(self.planets)
            for i, pl1 in enumerate(planets_list):
                for j in xrange(i+1, len(planets_list)):
                    pl2 = planets_list[j]
                    distances.append(pl1.distance(pl2))
            self.distance_norm.init(distances)
        if not self.growth_norm:
            self.growth_norm = self.normalization_strategy()
            growth_rates = set()
            for pl in self.planets:
                growth_rates.add(pl.growth_rate)
            self.growth_norm.init(growth_rates)
                
    def normalize_dist(self, dist):
        return 1-self.distance_norm.normalize(dist)
    
    def normalize_growth(self, growth):
        return self.growth_norm.normalize(growth)
    
    def planet_by_id(self, id):
        for pl in self.planets:
            if pl.id == id:
                return pl

Game(MyBot, universe_class=MyUniverse)