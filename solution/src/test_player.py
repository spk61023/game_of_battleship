import unittest
from player import Player

class Test(unittest.TestCase):

    player1 = Player("PLAYER 1",5,5,5)
    player2 = Player("PLAYER 2",5,5,5)

    def test_setup_board(self):
        self.player1.setup_board(5)
        self.player2.setup_board(5)

    def test_strike(self):
        guess_row,guess_col = 2,2
        self.player1.strike(guess_row,guess_col)
        self.player2.strike(guess_row,guess_col)

    def test_strike_invalid_cases(self):
        #Check Index Error
        guess_row,guess_col = 20,20
        self.player1.strike(guess_row,guess_col)
        self.assertRaises(Exception)
        #Check str
        guess_row,guess_col = 'a','b'
        self.player1.strike(guess_row,guess_col)
        self.assertRaises(Exception)

    def test_calculate_score(self):
        player1_score =self.player1.calculate_score()
        self.assertEqual(player1_score,0)


if __name__ == '__main__':
    unittest.main()
