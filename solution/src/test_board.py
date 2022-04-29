import unittest

import numpy as np
import numpy.testing as npt

from board import Board


class Test(unittest.TestCase):

    board1 = Board(player_name="PLAYER1",grid_size=5)
    board2 = Board(player_name="PLAYER2",grid_size=5)

    def test_display_board(self):
        self.valid_result = []
        for value in range(0,5):
            self.valid_result.append([str(value+1)]*5)
        self.assertEqual(self.board1.display_board(self.board1),self.board2.display_board(self.board2))

    def test_set_player_board(self):
        self.board1.set_player_board(board=self.board1.board,no_of_ships=5)
        self.board2.set_player_board(board=self.board2.board,no_of_ships=5)

    def test_set_miss_ship(self):
        self.board1.set_miss_ship(guess_row=1,guess_col=1)
        self.assertEqual(self.board1.board[1][1],"O")
        self.board2.set_miss_ship(guess_row=1,guess_col=1)
        self.assertEqual(self.board2.board[1][1],"O")

    def test_set_dead_ship(self):
        self.board1.set_dead_ship(guess_row=2,guess_col=2)
        self.assertEqual(self.board1.board[2][2],"X")
        self.board2.set_dead_ship(guess_row=2,guess_col=2)
        self.assertEqual(self.board2.board[2][2],"X")

if __name__ == '__main__':
    unittest.main()
