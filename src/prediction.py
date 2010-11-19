'''
Created on Nov 8, 2010

@author: dmitry.serdyuk
'''
from operator import attrgetter
from planetwars import player, fleet
from itertools import groupby
import sys
from logging import getLogger

log = getLogger(__name__)

class Prediction:    
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
                                              key=destination_getter),
                                              destination_getter)
            for dest, fleets_by_dest in destination_iter:
                forces = self._calc_forces(dest, fleets_by_dest)
                log.debug("for turn %d and planet %d forces are %s",
                          turn, dest.id, forces)
                winner = self._battle(forces)
                turn_state[dest.id] = winner
                
            planets[turn] = turn_state
        self._planets = planets
        log.debug("---------------\/----------------")
        log.debug(planets)
        log.debug("---------------/\----------------")
            
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
        
    def _get_planet_state_on_turn(self, planet_id, needed_turn):
        #start searching from newest states
        for iter_turn in sorted(self._planets.iterkeys(), reverse=True):
            if iter_turn <= needed_turn:
                #if record for needed planet exists - return it
                if self._planets[iter_turn].has_key(planet_id):
                    return self._planets[iter_turn][planet_id]
        #if we got here - there were no records for planet
        #it means that no fleets are approaching this planet now
        planet = self.u.planet_by_id(planet_id)
        return planet.owner, planet.ship_count
        
    def ship_count_on_planet(self, planet_id, turns):
        """
        @return: tuple of (planet_owner, ship_count) reflecting planet's state
                 in specified number of turns.
        """
        #does record for this turn exist?
        if self._planets.has_key(turns):
            #does this record contains data for needed planet?
            turn_data = self._planets[turns]
            if turn_data.has_key(planet_id):
                return turn_data[planet_id]
            else:
                return self._get_planet_state_on_turn(planet_id, turns)
        else:
            return self._get_planet_state_on_turn(planet_id, turns)
        