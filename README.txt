Hiba Khan
CS 5001, Spring 2023
Final Project

Files included:

    game:
        Contains the logic for the game.
    draw_game:
        Draws the game using Turtle and logic from game.py.
    main:
        Runs the game.
    test_game:
        Tests the functions in game.py.
    test_helper:
        Contains a helper function for test_game.

Collectively, these files run a 2048 game that the user can play using the
keyboard.

How to run the program:

    Run main.py

    Keys:
        Up: shifts the numbers up on the board.
        Down: shifts the numbers down on the board.
        Left: shifts the numbers left on the board.
        Right: shifts the numbers right on the board.
        "n": creates a new game.
        "e": ends the program.

Features that work:

    - The screen shows the board with numbers clearly.
    - The player can use the arrow keys on the keyboard to play the game.
    - The game keeps track of the score and displays it on the board at all
    times.
    - The game can be ended at any time and the directions to end it is
    visible on the board at all times.
    - A new game can be started at anu time without having to exit and re-run
    the program, and the directions are visible on the board at all times.
    - If the user presses any keys other than what the game uses, the game is
    not affected.
    - The program does not crash.
    - When the cells merge, they are highlighted using a different color.

