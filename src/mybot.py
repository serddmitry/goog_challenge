from planetwars import BaseBot, Game
import random
from planetwars.universe import Universe
from strategies.expansion import Expansion

# This shows how you can add your own functionality to game objects (Universe in this case).

class StupidBot(BaseBot):
    """Modified StupidBot that uses new our own MyUniverse (see below)"""
    def do_turn(self):
        strat = Expansion()
        strat.act()

class MyUniverse(Universe):
    pass

Game(StupidBot, universe_class=MyUniverse)