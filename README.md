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

"""
die = Die(np.array([1,2,3,4,5,6])
"""
### creates a game out of a list of Die objects

"""
game = Game([die])
game.play(1000)
"""
### analyzes a given Game that has rolled its Die

"""
      game.play(100)
      analysis = Analyzer(game)
"""
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
      """
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
## Game Class
     """
    The game class consists of rolling of one or more similar dice (Die objects) one or more times.
    
    Attributes:
        dice: A list of Die objects representing the dice in the game.
### play
      """
        This method takes an integer parameter to specify how many times the dice should be rolled and saves the result of the play to a private data frame.

        Argument:
            rolls (int): integer parameter to specify how many times the dice should be rolled
        """
### recent_play
      """
        This method returns a copy of the private play data frame to the user..

        Argument:
            Format options ('form'): 'wide' (default) or 'narrow'

        Returns:
          self.play_outcome.copy  pandas.DataFrame: The play results data frame.

        Raises:
            ValueError: Passed an invalid option for narrow or wide.
        """
## Analyzer Class
      """
    This class analyzes takes the results of a single game and computes various descriptive statistical properties about it.

    Attributes:
        game (Game): A Game object whose results will be analyzed.
    """

### jackpot 
      """
        This method creates a jackpot. A jackoput is a result in which all faces are the same, e.g. all ones for a six-sided die. 
        This method computes how many times the game resulted in a jackpot. 

        Returns:
           jackpots int: Returns an integer for the number of jackpots.
        """
### face_counts_per_roll
      """
       This method how many times a given face is rolled in each event.

        Returns: A data frame of results. Included in the df is: index of the roll number, face values as columns, and count values in the cells (i.e. it is in wide format)
        """
###  combo_count
        """
        This method commputes the distinct combinations of faces rolled, along with their counts

        Returns: combo, pandas DataFrame with a MultiIndex of distinct combinations and a column for the associated counts..
        """
### permutation_count
        
        """
        This method computes the distinct permutations of faces rolled, along with their counts.

        Returns: permutation, pandas DataFrame with a MultiIndex of distinct permutations and a column for the associated counts.
        """

        
        



