'''
Hiba Khan
CS 5001, Spring 2023
Final Project

This program runs a 2048 game that a user can play.
'''

import draw_game

def main():
    '''
    Purpose:
        This function runs a 2048 game that a user can play.
    '''
    
    draw_game.create_turtle()
    draw_game.start_game()
    draw_game.create_keys()

if __name__ == "__main__":
    main()
