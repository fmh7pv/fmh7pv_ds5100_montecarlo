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
# API description

## Die Class
### change weight 

   """
        This method changes the weight for a specific face value.

        Arguments:
            side_face: takes str (like letters) or numeric (integer or float) in an array. 
            side_weight: takes valid type, i.e. if it is numeric (integer or float) or castable as numeric.

        Raises:
            IndexError: If the face value is not in an array. 
            TypeError: If the weight is not a numeric value (integer or float).
        """
### roll_dice
""
      This method simulates rolling of die one or more times.

        Argument:
            rolls (int): A parameter of how many times the die is to be rolled; defaults to 1.

        Returns:
           outcomes: a Python list of outcomes.
        """
### current state
        """
        This method returns a copy of the  data frame.

        Returns:
          die  pandas.DataFrame: A copy of the data frame.
        """



