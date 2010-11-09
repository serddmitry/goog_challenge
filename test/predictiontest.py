'''
Created on Nov 9, 2010

@author: dmitry.serdyuk
'''
from planetwars import Planet
from planetwars.fleet import Fleet, Fleets
from planetwars.player import NOBODY, ME, PLAYER2
import unittest
from prediction import Prediction

class UniverseDouble:
    class PlanetsDouble:
        def get(self, *args):
            pass
    _planets = PlanetsDouble() 

class Test(unittest.TestCase):


    def test_calc_force(self):
        universe = UniverseDouble()

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
        prediction = Prediction(UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 25), winner)

    def test_two_forces_battle(self):
        forces = {NOBODY: 10, ME: 25}
        prediction = Prediction(UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 15), winner)

    def test_three_forces_battle(self):
        forces = {NOBODY: 10, ME: 25, PLAYER2: 5}
        prediction = Prediction(UniverseDouble())
        winner = prediction._battle(forces)
        self.assertEquals((ME, 15), winner)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_calc_force']
    unittest.main()