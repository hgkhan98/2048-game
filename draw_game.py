'''
Hiba Khan
CS 5001, Spring 2023
Final Project

This program draws a board for a 2048 game using Turtle and logic from
game.py.
'''

import turtle
import game

def round_square(center_x, center_y, length, color):
    '''
    Purpose:
        This function creates a square with rounded edges at a certain
        coordinate position with a certain length and color. 
    Parameters:
        center_x: x-coordinate equal to the center of the square.
        center_y: y-coordinate equal to the center of the square.
        length: length of the square.
        color: color of the square.
    Results:
        square with rounded edges, of the specified length and color. The
        center is at the specified x- and y-coordinates.
    '''

    t.up()
    t.goto(center_x - (length / 2) + 5, center_y - length / 2)
    t.down()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.fd(length - 2 * 5)
        t.circle(5, 90)
        t.fd(length - 2 * 5)
        t.circle(5, 90)
    t.end_fill()

def draw_board():
    '''
    Purpose:
        This function creates a board on the screen with cells of a
        certain color based on the number in the cell.
    Parameters:
        none
    Results:
        board with cells of different colors based on the number.
    '''

    color_dict = {0: "light coral", 2: "hot pink", 4: "deep pink",
                  8: "pale violet red", 16: "medium violet red",
                  32: "purple", 64: "violet", 128: "medium orchid",
                  256: "dark violet", 512: "medium purple",
                  1024: "medium slate blue", 2048: "dark slate blue"}
    
    round_square(0, 0, 410, "misty rose")
    cell_size = 400 / size
    for y in range(1, size + 1):
        center_y = (cell_size / 2) + 200 - (y * cell_size)
        for x in range(size):
            center_x = (cell_size / 2) - 200 + (x * cell_size)
            color = color_dict[game.board[y - 1][x]]
            round_square(center_x, center_y, cell_size - 10, color)

def write_numbers():
    '''
    Purpose:
        This function writes numbers in each of the cells on the screen.
    Parameters:
        none
    Results:
        numbers written in each cell.
    '''
   
    cell_size = 400 / len(game.board)
    font_size = int(cell_size / 3)
    for y in range(1, len(game.board) + 1):
        lower_y = (cell_size / 5) + 200 - (y * cell_size)
        for x in range(len(game.board)):
            center_x = (cell_size / 2) - 200 + (x * cell_size)        
            t.up()
            t.goto(center_x, lower_y)
            t.down()
            t.color("white")
            t.write(game.board[y - 1][x], align="center",
                    font=("Futura", font_size, "bold"))

def update_board():
    '''
    Purpose:
        This function updates the screen with the board and numbers in it.
        If the player wins or loses, update the board accordingly.
    Parameters:
        none
    Results:
        updated board.
    '''

    t.clear()
    draw_board()
    write_numbers()
    write_rules()
    update_score()
    write_rules()
    win_screen()
    lose_screen()

def update_score():
    '''
    Purpose:
        This function updates the score on the screen.
    Parameters:
        none
    Results:
        updated score.
    '''
    
    t.up()
    t.goto(- 500, 0)
    t.color("medium violet red")
    t.down()
    t.write(f"Score: {game.score}", font=("Future", 30, "bold"))

def write_rules():
    '''
    Purpose:
        This function writes the rules of the game on the screen.
    Parameters:
        none
    Results:
        rules written.
    '''
    
    t.up()
    t.goto(300, 0)
    t.color("medium violet red")
    t.down()
    t.write(f"New game: n\nEnd game: e", font=("Future", 20, "bold"))

def win_screen():
    '''
    Purpose:
        This function updates the screen with a message if the player wins
        the game.
    Parameters:
        none
    Results:
        winning message written.
    '''

    if game.check_win() == True:
        t.up()
        t.goto(0, 220)
        t.color("medium violet red")
        t.down()
        t.write(f"You win!", align="center", font=("Future", 50, "bold"))

def lose_screen():
    '''
    Purpose:
        This function updates the screen with a message if the player loses
        the game/
    Parameters:
        none
    Results:
        losing message written.
    '''

    if game.check_lose() == True:
        t.up()
        t.goto(0, 220)
        t.color("medium violet red")
        t.down()
        t.write(f"You lose!", align="center", font=("Future", 50, "bold"))

def up_key():
    '''
    Purpose:
        This function updates the screen after the up button is pressed.
    Parameters:
        none
    Results:
        board with cells shifted up.
    '''

    if game.check_win() == False:
        game.up()
        game.new_number()
        update_board()    

def down_key():
    '''
    Purpose:
        This function updates the screen after the down button is pressed.
    Parameters:
        none
    Results:
        board with cells shifted down.
    '''

    if game.check_win() == False:
        game.down()
        game.new_number()
        update_board()

def left_key():
    '''
    Purpose:
        This function updates the screen after the left button is pressed.
    Parameters:
        none
    Results:
        board with cells shifted left.
    '''

    if game.check_win() == False:
        game.left()
        game.new_number()
        update_board()

def right_key():
    '''
    Purpose:
        This function updates the screen after the right button is pressed.
    Parameters:
        none
    Results:
        board with cells shifted right.
    '''

    if game.check_win() == False:
        game.right()
        game.new_number()
        update_board()

def new_key():
    '''
    Purpose:
        This function creates a new game after the "n" button is pressed.
    Parameters:
        none
    Results:
        new board.
    '''

    t.clear()
    start_game()

def create_turtle():
    '''
    Purpose:
        This function creates a global Turtle and Screen.
    Parameters:
        none
    Results:
        global Turtle object and global Screen object
    '''
    
    global sc
    global t

    sc = turtle.Screen()
    sc.bgcolor("pink")
    sc.setup(width=1.0, height=1.0)

    t = turtle.Turtle()
    t._tracer(False)

def start_game():
    '''
    Purpose:
        This function starts the game and creates a board on the screen.
    Parameters:
        none
    Results:
        starting board.
    '''

    global size

    size = 4
    game.size = 4
    game.start_board()
    draw_board()
    write_numbers()
    write_rules()
    update_score()

def create_keys():
    '''
    Purpose:
        This function takes input from the keyboard to call functions
        associated with those keys.
    Parameters:
        none
    Results:
        function associated with key is called.
    '''

    sc.listen()
    sc.onkey(up_key, "Up")
    sc.onkey(down_key, "Down")
    sc.onkey(left_key, "Left")
    sc.onkey(right_key, "Right")
    sc.onkey(sc.bye, "e")
    sc.onkey(new_key, "n")

    sc.mainloop()
    
