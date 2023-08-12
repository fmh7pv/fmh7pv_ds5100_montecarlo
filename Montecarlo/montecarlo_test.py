import pandas as pd
import numpy as np
import unittest 
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):
    def test_1_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertIsNotNone(die)

    def test_2_change_weight(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        die.change_weight(1,100)
        self.assertEqual(die.current_state().loc[1].item(), 100)
        
    def test_3_roll_dice(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        outcomes = die.roll_dice(4)
        self.assertTrue(isinstance(die.roll_dice(), list))
    
    def test_4_current_state(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertTrue(isinstance(die.current_state(), pd.DataFrame))
    
    def test_5_game_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        g = Game([die1, die2])
        self.assertTrue(isinstance(g, Game))
        
    def test_6_play(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        g = Game([die1, die2])
        self.assertTrue(len(g.dice), 2)
        
    def test_7_recent_play(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        g = Game([die1, die2])
        results = g.play(5)
        results = g.recent_play()
        self.assertTrue(isinstance(results, pd.DataFrame))
                    
    def test_8_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertTrue(isinstance(die.current_state(), pd.DataFrame))
        
    def test_9_jackpot(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        g = Game([die])
        g.play(10)
        analyzer = Analyzer(g)
        self.assertEqual(analyzer.jackpot(), 10)
        
    def test_10_face_counts_per_roll(self):
        faces = np.array([1, 2, 3, 4, 5])
        die1 = Die(faces)
        die2 =Die(faces)
        g = Game([die1, die2])
        analyzer = Analyzer(g)
        self.assertIsInstance(analyzer.face_counts_per_roll(), pd.DataFrame)
        
    def test_11_combo_count(self):
        faces = np.array([1, 2, 3, 4, 5])
        die1 = Die(faces)
        die2 =Die(faces)
        g = Game([die1, die2])
        analyzer = Analyzer(g)
        self.assertIsInstance(analyzer.combo_count(), pd.DataFrame)
        
    def test_12_perm_count(self):
        faces = np.array([1, 2, 3, 4, 5])
        die1 = Die(faces)
        die2 =Die(faces)
        g = Game([die1, die2])
        analyzer = Analyzer(g)
        self.assertIsInstance(analyzer.permutation_count(), pd.DataFrame)
        
    
        
        

        
    
        
 
    
if __name__ == '__main__':
    
        unittest.main(verbosity=3) 