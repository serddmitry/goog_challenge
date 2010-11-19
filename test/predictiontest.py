'''
Created on Nov 9, 2010

@author: dmitry.serdyuk
'''
from planetwars import Planet
from planetwars.fleet import Fleet, Fleets
from planetwars.player import NOBODY, ME, PLAYER2
import unittest
from prediction import Prediction

class PredictionCalcForceBattleTest(unittest.TestCase):
    class UniverseDouble:
        class PlanetsDouble:
            def get(self, *args):
                pass
        _planets = PlanetsDouble()
             
    def test_calc_force(self):
        universe = self.UniverseDouble()

        planet = Planet(universe,1,0,0,0,10,5)
        fleet1 = Fleet(universe,0,1,15,0,1,0,0)
        fleet2 = Fleet(universe,0,1,20,0,1,0,0)
        fleet3 = Fleet(universe,0,2,5,0,1,0,0)

        fleets = Fleets()
        fleets.add(fleet1)
        fleets.add(fleet2)
        fleets.add(fleet3)

        prediction = Prediction(universe)
        forces = prediction._calc_forces(planet, fleets)
        self.assertEquals(10, forces[NOBODY])
        self.assertEquals(35, forces[ME])
        self.assertEquals(5, forces[PLAYER2])

    def test_one_force_battle(self):
        forces = {ME: 25}
        prediction = Prediction(self.UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 25), winner)

    def test_two_forces_battle(self):
        forces = {NOBODY: 10, ME: 25}
        prediction = Prediction(self.UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 15), winner)

    def test_three_forces_battle(self):
        forces = {NOBODY: 10, ME: 25, PLAYER2: 5}
        prediction = Prediction(self.UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 15), winner)
        
class PredictionPlanetFindTest(unittest.TestCase):
    class UniverseDouble:
        def __init__(self):
            #four planets initially
            self.planets = {1:Planet(self, 1, 0, 0, ME, 10, 5),
                            2:Planet(self, 2, 0, 0, NOBODY, 20, 4),
                            3:Planet(self, 3, 0, 0, PLAYER2, 30, 4),
                            4:Planet(self, 4, 0, 0, ME, 40, 2)}
        
        def planet_by_id(self, id):
            return self.planets[id]
    
    def setUp(self):
        self.u = self.UniverseDouble()
        self.predict = Prediction(self.u)
        #putting planet state changes
        state_change_3 = {1:(ME, 111), 3:(ME, 333), 5:(PLAYER2, 555)}
        state_change_2 = {1:(NOBODY, 22), 2:(PLAYER2, 11)}
        state_change_1 = {1:(PLAYER2, 1)}
        self.predict._planets = {1: state_change_3,
                            4: state_change_2,
                            7: state_change_1}
    
    def test_find_planet_with_3_state_changes(self):
        planet_state = self.predict.ship_count_on_planet(1, 8)
        self.assertEquals((PLAYER2, 1), planet_state)
        
    def test_find_planet_with_2_state_changes(self):
        pass
    def test_find_planet_with_1_state_changes(self):
        pass
    def test_find_planet_with_0_state_changes(self):
        pass
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_calc_force']
    unittest.main()