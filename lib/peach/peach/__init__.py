# -*- coding: utf-8 -*-
################################################################################
# Peach - Computational Intelligence for Python
# Jose Alexandre Nalon
#
# This file: __init__.py
# Makes the peach directory a package and initializes it.
################################################################################

# Doc string, reStructuredText formatted:
__doc__ = """
*Peach* is a pure-Python package with aims to implement techniques of machine
learning and computational intelligence. It contains packages for

- Neural Networks, including, but not limited to, multi-layer perceptrons and
  self-organizing maps;
- Fuzzy logic and fuzzy inference systems, including Mamdani-type and
  Sugeno-type controllers;
- Optimization packages, including multidimensional optimization;
- Stochastic Optimizations, including genetic algorithms, simulated annealing,
  particle swarm optimization;
- A lot more.

:Authors:
  José Alexandre Nalon
"""

# Variables and information about the system
__version__ = "0.1.0"


# __all__ = [ 'nn', 'fuzzy', 'optm', 'ga' ]


################################################################################
# Imports sub-packages
from nn import *        # Neural network package
from fuzzy import *     # Fuzzy logic package
from optm import *      # Optimization package
from ga import *        # Genetic Algorithms package

