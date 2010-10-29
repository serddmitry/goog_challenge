'''
Created on Oct 27, 2010

@author: dmitry.serdyuk
'''
from planetwars import player, planet
import math
class Expansion:
    def __init__(self, universe):
        self.u = universe
    
    def act(self):
        #if there is a big planet nearby that can be captured - do it
        scores = {} #{planet id: [(score, planet2)]}
        for my in self.u.my_planets():
            scores[my.id] = self.scores_for_planets(my, self.u.not_my_planets)
        selected_planets = self.find_planet_to_attack(scores)
        ships_to_send = self.ships_to_send(selected_planets)
        self.u.send_fleet(selected_planets[0], selected_planets[1],
                          ships_to_send)
     
    def score_for_planet(self, my_planet, not_my_planet):
        return not_my_planet.growth_rate;

    def scores_for_planets(self, my_planet, planets):
        result = []
        for pl in planets:
            score = self.calc_score(my_planet, pl)
            result.append((score, pl))
        return result
    
    ''' @return: tuple of source planet and destination planet '''        
    def find_planet_to_attack(self, scores):
        pass
    
    def ships_to_send(self, planets):
        return min(planets[0].ship_count, planets[1].ship_count);
    