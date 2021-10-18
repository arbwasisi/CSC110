###
### Author: Arsene Bwasisi
### Description: This program creates a CSC 110 version of 1D chess with a singel
###              dimension board with 3 chess piece for each player, one king and 
###              two knights. A knight can move 2 indexes left or right and replace
###              the piece in that position. King moves to the next index occupied
###              by another piece, black or white, and replace it.

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    ''' 
    This function validates a move made by the player. A move is valid if
    it's with in the board range and if the selected position is of the current 
    player.
    '''
    if position < len(board): # Checks if position is with in the board range(8)

        # Checks who the current player is and assess if the position selected
        # holds a piece that belongs to that particular player.
        if player == WHITE:
            if board[position] == W_KNIGHT or board[position] == W_KING:
                return True
        elif player == BLACK:
            if board[position] == B_KNIGHT or board[position] == B_KING:
                return True
    return False

def move_knight(board, position, direction):
    ''' This functions moves the knight piece by 2 indexes. '''

    index = position # Allows us to increment on the position without changing its value
    if direction == 'r' and index < 7: # Move piece only if index is less than 7
        index += 2 # Moves piece right by 2 index
        board[index] = board[position]
        board[position] = EMPTY 
    elif direction == 'l' and index > 1: # Move piece only if index is greater than 1
        index -= 2 # Moves piece left by 2 index
        board[index] = board[position]
        board[position] = EMPTY
    return board

def move_king(board, position, direction):
    ''' This functions moves the king piece left or right till it meets another piece. '''

    index = position

    if direction == 'r':
        while index < len(board):
            index += 1 

            # If an index in board does not have an empty string replaces it
            # with the piece king, and puts an empty string where the king was
            if board[index] != EMPTY or index == len(board)-1:
                board[index] = board[position]
                board[position] = EMPTY
                return board
    elif direction == 'l':
        while index >= 0:
            index -= 1
            if board[index] != EMPTY or index == 0:
                board[index] = board[position]
                board[position] = EMPTY
                return board

def print_board(board):
    ''' This function displays the board where the game is played. '''

    print('+' + '-'*53 + '+')
    for index in board:
        print('| ' + index + ' ', end='')
    print('|', '\n+' + '-'*53 + '+')

def draw_board(board, gui):
    ''' This function will display a graphically representation of the chess board. '''
    
    index = 0
    point = 75
    
    gui.clear()
    gui.text(225, 50, '1 Dimensional Chess', 'green4', 25)
    
    # Loops through and displays rectangles that form the board
    while index < len(board):
        gui.rectangle(point, 115, 60, 60, 'red4')
        
        # If statements that customize each peace to represent
        # a white or black king and a white or black knight
        if board[index] == W_KING or board[index] == B_KING:
            if board[index] == W_KING:
                gui.text(point+5, 140, 'King', 'white', 14)
            else:
                gui.text(point+5, 140, 'King', 'black', 14)
        elif board[index] != EMPTY:
            if board[index] == W_KNIGHT:
                gui.text(point+5, 140, 'Knight', 'white', 14)
            else:
                gui.text(point+5, 140, 'Knight', 'black', 14)
        gui.update_frame(75)
        
        index += 1
        point += 60

def is_game_over(board):
    ''' This function signals if the game is over or not. '''

    # Checks if black/white king is in board
    # if not returns true ti end game
    if B_KING not in board:
        print_board(board)
        print('White wins!')
        return True
    elif W_KING not in board:
        print_board(board)
        print('Black wins!')
        return True
    return False

def move(board, position, direction):
    ''' This function moves the pieces in the board. '''

    # Calls the move_king function if the position contains a king piece
    # And cales the move_knight function, if the position has a knight piece
    if board[position] == W_KING or board[position] == B_KING:
        move_king(board, position, direction)
    elif board[position] == W_KNIGHT or board[position] == B_KNIGHT:
        move_knight(board, position, direction)

def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)

main()
