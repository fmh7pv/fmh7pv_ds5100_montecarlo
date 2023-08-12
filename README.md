# Metadata

Project: Monte Carlo Dice Game Simulation

Version: 1.0

Author: Fadumo 

License: MIT

# Synopsis
## Installation

Use pip to install montecarlo.

pip install montecarlo

Using Classes

from montecarlo import Die, Game, Analyzer


### creates a six-sided die 
'''
die = Die(np.array([1,2,3,4,5,6])
'''
### creates a game out of a list of Die objects
'''
game = Game([die])
game.play(1000)
'''
### analyzes a given Game that has rolled its Die
'''
game.play(100)
analysis = Analyzer(game)
'''
