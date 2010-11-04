'''
Created on Oct 27, 2010

@author: dmitry.serdyuk
'''
from logging import getLogger
import __future__
import sys

log = getLogger(__name__)

class Expansion:
    growth_weight = 1
    dist_weight = 1.5
    available_ships_weight = 1
    
    def __init__(self, universe):
        self.u = universe
    
    def act(self):
        if len(self.u.my_fleets) == 2:
            return
        #if there is a big planet nearby that can be captured - do it
        scores = {} #{planet id: [(score, planet2)]}
        for my in self.u.my_planets:
            scores[my.id] = self.scores_for_planets(my, self.u.not_my_planets)
        selected_planets = self.find_planet_to_attack(scores)
        ships_to_send = self.ships_to_send(selected_planets)
        self.u.send_fleet(selected_planets[0], selected_planets[1],
                          ships_to_send)
     
    def score_for_planet(self, my_planet, not_my_planet):
        norm_dist = self.u.normalize_dist(my_planet.distance(not_my_planet))
        norm_growth = self.u.normalize_growth(not_my_planet.growth_rate)
        norm_force = self.u.normalize_based_force(my_planet.ship_count)
        log.debug("norm_force for planet(shipcount is %d) %s is %f",my_planet.ship_count,my_planet, norm_force)
        return self.dist_weight * norm_dist +\
               self.growth_weight * norm_growth +\
               self.available_ships_weight * norm_force;

    def scores_for_planets(self, my_planet, planets):
        result = []
        for pl in planets:
            score = self.score_for_planet(my_planet, pl)
            result.append((score, pl))
        return result
    
    '''
    Finds a tuple of (my_planet's_id, not_my_planet) that has best score
    @param scores: A dictionary having ids of my planets as keys
                   and list of tuples of kind (score, not_my_planet).
    @return: tuple of source planet and destination planet
    '''        
    def find_planet_to_attack(self, scores):
        max_score = 0,
        for my_planet_id, tuples_list in scores.iteritems():
            for score, not_my_planet in tuples_list:
                if score > max_score[0]:
                    max_score = (score, my_planet_id, not_my_planet)
        log.info("Found  best score (%d) for my planet {%d} and not_my_planet\
                  {%s}", max_score[0], max_score[1], max_score[2])
        return (self.u.planet_by_id(max_score[1]), max_score[2])        
        
    
    def ships_to_send(self, planets):
        return min(planets[0].ship_count, planets[1].ship_count)
    