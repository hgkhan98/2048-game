'''
Hiba Khan
CS 5001, Spring 2023
Final Project

This program creates the logic for running a 2048 game through Turtle.
'''

import random

def new_number():
    '''
    Purpose:
        This function adds a new number to the global board at a random
        position. The number is either 2 or 4 and is chosen randomly. It
        replaces a 0 on the board. If there are no 0s present on the
        board, no change is made.
    Parameters:
        none
    Result:
        global board updated with 2 or 4 if there is an empty cell.
    '''
    
    added = False

    # while new number not added and there are empty cells on the board,
    # add 2 or 4 to random empty position on board
    while added == False and any(0 in row for row in board) == True:

        row = random.randint(0, len(board) - 1)
        column = random.randint(0, len(board) - 1)

        if board[row][column] == 0:
            board[row][column] = random.randrange(2, 5, 2)
            added = True   
        
def start_board():
    '''
    Purpose:
        This function creates a global board of a certain size, which
        dictates the length and width of the board. All the numbers are
        0 aside from two numbers which are either 2 or 4. The function
        initializes other global variables, including score set to 0 and
        win set to False.
    Parameters:
        none
    Result:
        global board created in which all the numbers are 0 aside from
        two numbers that are either 2 or 4.
    '''
    
    global board
    global score
    global win

    # create empty board   
    board = [[0] * size for i in range(size)]

    # add two numbers
    new_number()
    new_number()
    score = 0
    win = False
    reset_merged()

def reset_merged():
    '''
    Purpose:
        This function creates a global variable merged_cells to check
        if cells have been merged. It is equal to the board in size, but
        the elements are True and False rather than numbers. This
        function resets the all the elements in merged_cells to False.
    Parameters:
        none
    Result:
        global merged_cells equal to the board in size and with all
        elements equal to False.
    '''

    global merged_cells

    # create board with cells containing False
    merged_cells = [[False] * size for i in range(size)]

def up():
    '''
    Purpose:
        This function shifts all the numbers in the board up. If an
        element is 0, it is considered an empty cell. If two numbers are
        shifted next to each other and are the same, they are merged,
        which means adding the two together. The new number is placed in
        the upper cell. At the end, merged_cells is reset.
    Parameters:
        none
    Result:
        board with numbers shifted up and merged if possible.
    '''

    global score
    
    for j in range(len(board)):

        for i in range(1, len(board)):

            count = 1
            non_zero = 0
           
            if board[i][j] != 0:
                
                while board[i - count][j] == 0 and (i - count) >= 0:

                    non_zero = i - count
                    count += 1

                if non_zero == 0:

                    if board[i - 1][j] != 0:
                        
                        if board[i - 1][j] == board[i][j] and \
                           merged_cells[i - 1][j] == False:
                            board[i - 1][j] *= 2
                            score += board[i - 1][j]
                            board[i][j] = 0
                            merged_cells[i - 1][j] = True
                    
                    elif board[non_zero][j] == 0:
                        board[non_zero][j] = board[i][j]
                        board[i][j] = 0
                        
                    else:
                        if board[non_zero][j] == board[i][j] and \
                           merged_cells[non_zero][j] == False:
                            board[non_zero][j] *= 2
                            score += board[non_zero][j]
                            board[i][j] = 0
                            merged_cells[non_zero][j] = True

                elif board[non_zero - 1][j] == board[i][j] and \
                     merged_cells[non_zero - 1][j] == False:
                    board[non_zero - 1][j] *= 2
                    score += board[non_zero - 1][j]
                    board[i][j] = 0
                    merged_cells[non_zero - 1][j] = True

                else:
                    board[non_zero][j] = board[i][j]
                    board[i][j] = 0
    
    reset_merged()

def down():
    '''
    Purpose:
        This function does the opposite of the up function. It shifts
        all the numbers in the board down. If an element is 0, it is
        considered an empty cell. If two numbers are shifted next to each
        other and are the same, they are merged, which means adding the
        two together. The new number is placed in the lower cell. At the
        end, merged_cells is reset.
    Parameters:
        none
    Result:
        board with numbers shifted down and merged if possible.
    '''

    board.reverse()

    up()

    board.reverse()

def left():
    '''
    Purpose:
        This function shifts all the numbers in the board left. If an
        element is 0, it is considered an empty cell. If two numbers are
        shifted next to each other and are the same, they are merged,
        which means adding the two together. The new number is placed in
        the upper cell. At the end, merged_cells is reset.
    Parameters:
        none
    Result:
        board with numbers shifted left and merged if possible.
    '''

    global score

    for i in range(len(board)):

        for j in range(1, len(board)):

            count = 1
            non_zero = 0
            
            if board[i][j] != 0:
                
                while board[i][j - count] == 0 and (j - count) >= 0:

                    non_zero = j - count
                    count += 1

                if non_zero == 0:

                    if board[i][j - 1] != 0:
                        
                        if board[i][j - 1] == board[i][j] and \
                           merged_cells[i][j - 1] == False:
                            board[i][j - 1] *= 2
                            score += board[i][j - 1]
                            board[i][j] = 0
                            merged_cells[i][j - 1] = True
                    
                    elif board[i][non_zero] == 0:
                        board[i][non_zero] = board[i][j]
                        board[i][j] = 0
                        
                    else:
                        if board[i][non_zero] == board[i][j] and \
                           merged_cells[i][non_zero] == False:
                            board[i][non_zero] *= 2
                            score += board[i][non_zero]
                            board[i][j] = 0
                            merged_cells[i][non_zero] = True

                elif board[i][non_zero - 1] == board[i][j] and \
                     merged_cells[i][non_zero - 1] == False:
                    board[i][non_zero - 1] *= 2
                    score += board[i][non_zero - 1]
                    board[i][j] = 0
                    merged_cells[i][non_zero - 1] = True

                else:
                    board[i][non_zero] = board[i][j]
                    board[i][j] = 0
   
    reset_merged()

def right():
    '''
    Purpose:
        This function does the opposite of the left function. It shifts
        all the numbers in the board down. If an element is 0, it is
        considered an empty cell. If two numbers are shifted next to each
        other and are the same, they are merged, which means adding the
        two together. The new number is placed in the lower cell. At the
        end, merged_cells is reset.
    Parameters:
        none
    Result:
        board with numbers shifted down and merged if possible.
    '''

    for row in board:
        row.reverse()

    left()

    for row in board:
        row.reverse()

def check_win():
    '''
    Purpose:
        This function checks if the player wins the game. If any of the
        cells in the board contain the number 2048, the player wins and
        the function returns True.
    Parameters:
        none
    Results:
        boolean. True if 2048 is present in the board, else False.
    '''
    
    win = False
    
    if any(2048 in row for row in board) == True:
        win = True

    return win

def check_lose():
    '''
    Purpose:
        This function checks if the player loses the game. If there are
        no empty cells and no more shifts possible, then the player loses
        and the function returns True.
    Parameters:
        none
    Results:
        boolean. False if any cell contains 0 or two equal numbers are
        next to each other, else True.
    '''
    
    lose = True

    if any(0 in row for row in board) == True:
        lose = False

    for i in range(len(board) - 1):

        for j in range(len(board) - 1):

            if board[i][j] == board[i + 1][j] or board[i][j] == \
               board[i][j + 1]:
                lose = False

    for j in range(len(board) - 1):

        if board[len(board) - 1][j] == board[len(board) - 1][j + 1]:
            lose = False

    for i in range(len(board) - 1):

        if board[i][len(board) - 1] == board[i + 1][len(board) - 1]:
            lose = False

    return lose

