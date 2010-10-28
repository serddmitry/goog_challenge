'''
Created on Oct 27, 2010

@author: dmitry.serdyuk
'''
from planetwars import player, planet
class Expansion:
    def __init__(self, universe):
        self.u = universe
    
    def act(self):
        #if there is a big planet nearby that can be captured - do it
        sorted_planets = {}
        for my in self.u.my_planets():
            for not_my in self.u.not_my_planets():
#                 score = 
#                 sorted_planets[]
                pass
     
     def calc_score():
         pass