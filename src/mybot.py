from planetwars import BaseBot, Game
from planetwars.universe import Universe
from strategies.expansion import Expansion
import math

# This shows how you can add your own functionality to game objects (Universe in this case).

class MyBot(BaseBot):
    """Modified StupidBot that uses new our own MyUniverse (see below)"""
    def do_turn(self):
        strat = Expansion()
        strat.act()

class MyUniverse(Universe):
    average_dist = 0
    
    def __init__(self):
        #calculate average distance
        distances = []
        for pl1 in self.planets:
            for pl2 in self.planets:
                distances.append(pl1.distance(pl2))
        sorted = sorted(distances)
        count = len(sorted)
        if bool(count % 2):
            median = sorted[math.ceil(count / 2)]
        else:
            floor_index = math.floor(count / 2)
            median = (sorted[floor_index] + sorted[floor_index + 1]) / 2
        return median
                
    def normalize_dist(self, dist):
        return dist / self.average_dist

Game(MyBot, universe_class=MyUniverse)
