'''
Created on Nov 8, 2010

@author: dmitry.serdyuk
'''
from operator import attrgetter
from planetwars import player, fleet
from itertools import groupby

class Prediction:
    def __init__(self, universe):
        self.u = universe
        
    def init_turn(self):
        destinations = dict()
        for turn, fleets_by_turn in self.u.fleets.arrivals():
            ##This is the approach below!
            destination_getter = attrgetter("destination")
            destination_iter = groupby(sorted(fleets_by_turn,
                                              key=destination_getter))
            for dest, fleets_by_dest in destination_iter:
                
#            for dest, fleets_by_destination in sorted(groupby)
            #calculate forces
#            forces = dict() #dict of forces: owner => forces
            #--home force
#            forces[]
            #--arriving fleets
#            for fleet in fleets:
#                if forces.has_key(fleet.owner):
#                    forces[fleet.owner] += fleet.ship_count
#                else:
#                    forces[fleet.owner] = fleet.ship_count 
            #battle
            
            #save results
                pass
            
    def _calc_forces(self, planet, fleets):
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
        
    def ship_count_on_planet(self, planet, turns):
        """
        Calculate the number of ships that will be present on planet in 
        specified number of turns.
        @return: Ships count as int. Positive if planets will be mine, negative
                 otherwise.
        """
        #initial value
        result = planet.ship_count
        #+growth rate
        if planet.owner != player.NOBODY:
            result += planet.growth_rate * turns
        if planet.owner != player.ME:
            sign = -1
        else:
            sign = 1            
        result *= sign
        #+my fleets
        
#        for fleet in planet.reinforcement_fleets:
#            if fleet
        #-opponent's fleets
        