'''
Hiba Khan
CS 5001, Spring 2023
Final Project

This program tests the functions in game.py.
'''

import game
import unittest
from test_helper import count_tiles

class GameTest(unittest.TestCase):

    def test_new_number(self):
        '''
        Test for the new_number function.
        '''

        # add one new number to empty board
        game.board = [[0] * 4 for i in range(4)]
        game.new_number()
        new_board = (any(2 in row for row in game.board) or \
                    any(4 in row for row in game.board)) and \
                    count_tiles() == 1
        self.assertTrue(new_board)

        # add no new number to full board
        game.board = [[2, 16, 8, 4], [4, 32, 64, 2], [2, 2, 4, 8],
                      [128, 2, 4, 8]]
        game.new_number()
        new_board = [[2, 16, 8, 4], [4, 32, 64, 2], [2, 2, 4, 8],
                      [128, 2, 4, 8]]
        self.assertEqual(game.board, new_board)

        # add two new numbers to partially full board
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.new_number()
        game.new_number()
        new_board = count_tiles() == 12
        self.assertTrue(new_board)

    def test_start_board(self):
        '''
        Test for the start_board function.
        '''

        # new board of length 4 with two numbers
        game.size = 4
        game.start_board()
        new_board = (count_tiles() == 2) and (len(game.board) == 4)
        self.assertTrue(new_board)

        # new board to replace old one
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.start_board()
        new_board = count_tiles() == 2
        self.assertTrue(new_board)

    def test_reset_merged(self):
        '''
        Test for the reset_merged function.
        '''

        # check if merged tiles reset for empty board
        game.board = [[0] * 4 for i in range(4)]
        game.size = 4
        game.reset_merged()
        new_board = [[False] * 4 for i in range(4)]
        self.assertEqual(game.merged_cells, new_board)

        # check if merged tiles reset for partially full board
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.reset_merged
        new_board = [[False] * 4 for i in range(4)]
        self.assertEqual(game.merged_cells, new_board)

    def test_up(self):
        '''
        Test for the up function.
        '''

        # check if tiles move up
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.size = 4
        game.score = 0
        game.reset_merged()
        game.up()
        new_board = [[4, 2, 8, 4], [128, 0, 64, 2], [0, 0, 8, 0],
                     [0, 0, 0, 0]]
        self.assertEqual(game.board, new_board)

        # check if any change for empty board
        game.board = [[0] * 4 for i in range(4)]
        game.up()
        new_board = [[0] * 4 for i in range(4)]
        self.assertEqual(game.board, new_board)

    def test_down(self):
        '''
        Test for the down function.
        '''

        # check if tiles move down
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.size = 4
        game.score = 0
        game.reset_merged()
        game.down()
        new_board = [[0, 0, 0, 0], [0, 0, 8, 0], [4, 0, 64, 4],
                     [128, 2, 8, 2]]
        self.assertEqual(game.board, new_board)

        # check if any change for empty board
        game.board = [[0] * 4 for i in range(4)]
        game.down()
        new_board = [[0] * 4 for i in range(4)]
        self.assertEqual(game.board, new_board)

    def test_left(self):
        '''
        Test for the left function.
        '''

        # check if tiles move left
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.size = 4
        game.score = 0
        game.reset_merged()
        game.left()
        new_board = [[2, 8, 4, 0], [64, 2, 0, 0], [4, 4, 0, 0],
                     [128, 4, 0, 0]]
        self.assertEqual(game.board, new_board)

        # check if any change for empty board
        game.board = [[0] * 4 for i in range(4)]
        game.left()
        new_board = [[0] * 4 for i in range(4)]
        self.assertEqual(game.board, new_board)

    def test_right(self):
        '''
        Test for the right function.
        '''

        # check if tiles move right
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        game.size = 4
        game.score = 0
        game.reset_merged()
        game.right()
        new_board = [[0, 2, 8, 4], [0, 0, 64, 2], [0, 0, 4, 4],
                     [0, 0, 128, 4]]
        self.assertEqual(game.board, new_board)

        # check if any change for empty board
        game.board = [[0] * 4 for i in range(4)]
        game.right()
        new_board = [[0] * 4 for i in range(4)]
        self.assertEqual(game.board, new_board)

    def test_check_win(self):
        '''
        Test for the check_win function.
        '''

        # check if win is True
        game.board = [[2, 0, 8, 4], [2048, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        win = game.check_win()
        self.assertTrue(win)

        # check if win is False
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        win = game.check_win()
        self.assertFalse(win)

    def test_check_lose(self):
        '''
        Test for the check_lose function.
        '''

        # check if lose is True
        game.board = [[2, 64, 8, 4], [4, 16, 32, 8], [2, 8, 4, 2],
                      [4, 16, 8, 128]]
        lose = game.check_lose()
        self.assertTrue(lose)

        # check if lose is False with empty spaces
        game.board = [[2, 0, 8, 4], [0, 0, 64, 2], [2, 2, 4, 0],
                      [128, 0, 4, 0]]
        lose = game.check_lose()
        self.assertFalse(lose)

        # check if lose is False with ability to merge
        game.board = [[2, 2, 8, 4], [4, 2, 64, 2], [2, 2, 4, 16],
                      [128, 32, 4, 64]]
        lose = game.check_lose()
        self.assertFalse(lose)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
