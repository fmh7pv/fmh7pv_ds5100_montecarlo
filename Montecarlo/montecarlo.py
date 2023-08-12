
import pandas as pd
import numpy as np

class Die():
    """ Created a 'die' class that has faces and weights.
    Attributes:
    self.die (pandas.DataFrame): This is the dataframe that stores face values and weights.
    """
    def __init__(self, sides=np.arange(1,7)):
        """
        Initializes the Die class with specified 'sides'.

        Argument:
            sides (numpy.ndarray): An array containing distinct face values of the die.

        Raises:
            ValueError: If faces values do not have distinct values.
            TypeError: If faces values are not a NumPy array.
        """
        self.sides = sides
        if len(set(sides)) != len(sides): 
            raise ValueError("Values must be distinct")
        if not isinstance(sides, np.ndarray):
            raise ValueError("Values must be a NumPy array")
        self.sides = sides
        self.die = pd.DataFrame(dict(
            face = sides, 
            weight = np.ones(len(sides), dtype = float)))
        self.die = self.die.set_index('face')
        self.die.index_name = 'side_id' 
    def change_weight(self, side_face, side_weight):
        """
        This method changes the weight for a specific face value.

        Arguments:
            side_face: takes str (like letters) or numeric (integer or float) in an array. 
            side_weight: takes valid type, i.e. if it is numeric (integer or float) or castable as numeric.

        Raises:
            IndexError: If the face value is not in an array. 
            TypeError: If the weight is not a numeric value (integer or float).
        """
        if not np.isin(side_face, self.sides):
            raise IndexError("Value must be in the die array")
        if type(side_weight) != int and type(side_weight) != float:
            raise ValueError("Values must be numeric")
        self.die['weight'][side_face] = float(side_weight)
    def roll_dice(self, rolls = 1):
        """
        This method simulates rolling of die one or more times.

        Argument:
            rolls (int): A parameter of how many times the die is to be rolled; defaults to 1.

        Returns:
           outcomes: a Python list of outcomes.
        """
        sum_weight = sum(self.die['weight'])
        outcomes = np.random.choice(self.sides,rolls,p=self.die['weight']/sum_weight)
        return outcomes.tolist()  
    def current_state(self):
        """
        This method returns a copy of the  data frame.

        Returns:
          die  pandas.DataFrame: A copy of the data frame.
        """
        return (self.die.copy())
    
    
class Game:
    """
    The game class consists of rolling of one or more similar dice (Die objects) one or more times.
    Attributes:
    dice: A list of Die objects representing the dice in the game.
    play_outcome: Data frame that shows the user the results of the most recent play.
    """
    def __init__(self, dice):
        """
        Initializes the Game class with a list of similar dice.
        Argument:
        dice (list): A list of already instantiated similar dice
        """
        self.dice = dice
        self.play_outcome = pd.DataFrame()
    def play(self, rolls = 1):
        """
        This method takes an integer parameter to specify how many times the dice should be rolled and saves the result of the play to a private data frame.

        Argument:
            rolls (int): integer parameter to specify how many times the dice should be rolled
        """
        outcome = {}
        for index, die in enumerate(self.dice):
            outcome[f"Die_{index}"] = die.roll_dice(rolls)
        self.play_outcome = pd.DataFrame(outcome)
    def  recent_play(self, form = 'wide'):
        """ This method returns a copy of the private play data frame to the user.
        Argument: Format options ('form'): 'wide' (default) or 'narrow'
        Returns: self.play_outcome.copy  pandas.DataFrame: The play results data frame.
        Raises: ValueError: Passed an invalid option for narrow or wide.
        """
        if form == 'wide':
            df = self.play_outcome.copy()
            return df
        elif form == "narrow":
            return self.play_outcome.melt(ignore_index=False, var_name="Die", value_name="Results")
        else:
            raise ValueError("Passed an invalid option for narrow or wide")
    
class Analyzer:
    """ This class analyzes takes the results of a single game and computes various descriptive statistical properties about it.
     Attributes: game (Game): A Game object whose results will be analyzed.
     """
    def __init__(self, game):
        """ Initializes and takes a game object as its input parameter.
         Arguments: game (Game): A Game object, data frame which will be analyzed
         Raises: ValueError: Expected a Game object
         """
        if not isinstance(game, Game):
            raise ValueError("Expected a Game object")
        self.game = game
    def jackpot(self):
        """ This method creates a jackpot. A jackoput is a result in which all faces are the same, e.g. all ones for a six-sided die. 
        This method computes how many times the game resulted in a jackpot. 

        Returns:
           jackpots int: Returns an integer for the number of jackpots.
        """
        if self.game.play_outcome is None:
            raise ValueError("No game has been played yet!")
        jackpots = 0
        for _, row in self.game.play_outcome.iterrows():
            if row.nunique() == 1:
                jackpots += 1
        return jackpots


    def face_counts_per_roll(self):
            
        """
       This method how many times a given face is rolled in each event.

        Returns: A data frame of results. Included in the df is: index of the roll number, face values as columns, and count values in the cells (i.e. it is in wide format)
        """
        if self.game.play_outcome is None:
            raise ValueError("No game has been played yet!")

        face = self.game.play_outcome.apply(lambda x: x.value_counts()).fillna(0)
        face = face.astype(int)
        return face

    def combo_count(self):
        """
        This method commputes the distinct combinations of faces rolled, along with their counts

        Returns: combo, pandas DataFrame with a MultiIndex of distinct combinations and a column for the associated counts..
        """
        
        combo = self.game.play_outcome.apply(lambda x: tuple(sorted(x))).value_counts().reset_index()
        return combo

    def permutation_count(self):
        
        """
        This method computes the distinct permutations of faces rolled, along with their counts.

        Returns: permutation, pandas DataFrame with a MultiIndex of distinct permutations and a column for the associated counts.
        """
        permutation = self.game.play_outcome.apply(lambda x: tuple(x.tolist())).value_counts().reset_index()
        return permutation
         