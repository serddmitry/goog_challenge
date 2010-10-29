from planetwars import BaseBot, Game
from planetwars.universe import Universe
from strategies.expansion import Expansion
import math
from planetwars.planet import Planet
from planetwars.fleet import Fleet

# This shows how you can add your own functionality to game objects (Universe in this case).

class MyBot(BaseBot):
    """ My super bot"""    
    def do_turn(self):
        strat = Expansion()
        strat.act()

class MyUniverse(Universe):
    average_dist = 0
    
    def __init__(self, game, planet_class=Planet, fleet_class=Fleet):
        super(MyUniverse, self).__init__(game, planet_class, fleet_class)
        #calculate average distance
        distances = []
        for pl1 in self.planets:
            for pl2 in self.planets:
                distances.append(pl1.distance(pl2))
        sorted_dist = sorted(distances)
        count = len(sorted_dist)
        if bool(count % 2):
            median = sorted_dist[math.ceil(count / 2)]
        else:
            floor_index = int(count / 2)
            median = (sorted_dist[floor_index]
                     + sorted_dist[floor_index + 1]) / 2
        return median
                
    def normalize_dist(self, dist):
        return dist / self.average_dist

Game(MyBot, universe_class=MyUniverse)
