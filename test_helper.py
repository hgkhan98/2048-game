'''
Hiba Khan
CS 5001, Spring 2023
Final Project

This program contains a helper function for test_game.py.
'''

import game

def count_tiles():

    count = 0

    for i in range(len(game.board)):

        for j in range(len(game.board)):

            if game.board[i][j] != 0:
                count += 1

    return count
