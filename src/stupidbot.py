from planetwars import BaseBot, Game
import random

class StupidBot(BaseBot):
    def calc_big_nearby_planet_score(self, planet):
        pass
    
    """Stupid bot that randomly spews out ships."""
    def do_turn(self):
        #for each of my planets?
        #find big nearby planet and send a fleet to it
        big_nearby = {}
        for p in self.universe.nobodies_planets:
            score = self.calc_big_nearby_planet_score(p) 
            big_nearby[score] = p
        for p in self.universe.my_planets:
            if p.ship_count > 50:
                p.send_fleet(random.choice(list(self.universe.not_my_planets)), p.ship_count / 2)

Game(StupidBot)