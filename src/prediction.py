'''
Created on Nov 8, 2010

@author: dmitry.serdyuk
'''
from operator import attrgetter
from planetwars import player, fleet
from itertools import groupby

class Prediction:
    planets = None
    
    def __init__(self, universe):
        self.u = universe
        
    def init_turn(self):
        """Calculate the number of ships with their respective owners, that
           will be based on planets, taking in account all the ships in motion.
        """
        planets = dict()
        for turn, fleets_by_turn in self.u.fleets.arrivals():
            turn_state = dict()
            
            destination_getter = attrgetter("destination")
            destination_iter = groupby(sorted(fleets_by_turn,
                                              key=destination_getter))
            for dest, fleets_by_dest in destination_iter:
                forces = self._calc_forces(dest, fleets_by_dest)
                winner = self._battle(forces)
                turn_state[dest.id] = winner
                
            planets[turn] = turn_state
        self.planets = planets
            
    def _calc_forces(self, planet, fleets):
        """Aggregate forces approaching the planet on same turn by owner"""
        forces = dict()
        #home force
        forces[planet.owner] = planet.ship_count
        #arriving fleets
        for fleet in fleets:
            if forces.has_key(fleet.owner):
                forces[fleet.owner] += fleet.ship_count
            else:
                forces[fleet.owner] = fleet.ship_count
        return forces

    def _battle(self, forces):
        """
        @return: tuple of (planet_owner, ship_count) which specifies the
                 winner force
        """
        if len(forces) == 1:
            return forces.items()[0]
        sorted_forces = sorted(forces.items(), key=lambda x:x[1],
                               reverse=True)
        winner = sorted_forces[0][0]
        ship_count = sorted_forces[0][1] - sorted_forces[1][1]
        return winner, ship_count
        
    def ship_count_on_planet(self, planet, turns):
        """
        @return: tuple of (planet_owner, ship_count) describing planet's state
                 in specified number of turns.
        """
        
        