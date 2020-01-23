import unittest
from Sudoku import Sudoku

board1 = [[5, [3, 6], 0, 0, 1, 0, 0, 0, 4],
         [2, 7, 4, 0, 0, 0, 6, 0, 0],
         [0, 8, 0, 9, 0, 4, 0, 0, 0],
         [8, 1, 0, 4, 6, 0, 3, 0, 2],
         [0, 0, 2, 0, 3, 0, 1, 0, 0],
         [7, 0, 6, 0, 9, 1, 0, 5, 8],
         [0, 0, [3, 1], 5, 0, 3, 0, 1, 0],
         [0, 0, 5, 0, 0, 0, 9, 2, 7],
         [1, 0, 0, 0, 2, 0, 0, 0, 3]]

board2 = [[5, 3, 0, 0, 1, 0, 0, 0, 4],
         [2, 7, 4, 0, 0, 0, 6, 0, 0],
         [0, 8, 0, 9, 0, 4, 0, 0, 0],
         [8, 1, 0, 4, 6, 0, 3, 0, 2],
         [0, 0, 2, 0, 3, 0, 1, 0, 0],
         [7, 0, 6, 0, 9, 1, 0, 5, 8],
         [0, 0, [3, 1], 5, 0, 3, 0, 1, 0],
         [0, 0, 5, 0, 0, 0, 9, 2, 7],
         [1, 0, 0, 0, 2, 0, 0, 0, 3]]

class TestSudoku(unittest.TestCase):
    def test_check_row_unqiue(self):
        board = Sudoku(board1)
        board.check_row_unique(0,1)
        board.check_row_unique(6,2)
        board.print_board()
        self.assertEqual(board.board, board2)