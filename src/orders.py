'''
Created on Nov 8, 2010

@author: dmitry.serdyuk
'''

class Order:
    source = None
    destination = None
    ship_count = None

    def __init__(self, source, destination, ship_count):
        self.source = source
        self.destination = destination
        self.ship_count = ship_count