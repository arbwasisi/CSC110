# Author: Arsene Bwasisi
# Description: This programs displays several shapes that are seleceted
#              by the user. They include an hourlass, plumbbob, house.
#              Users will provide a character to use for the shape as well
#              the shapes height.

def line(height):
    '''
    This function will determine the height of the row_area line
    with the input provided by the user.
    '''
    line = '|'+'-'*9+'|\n' # line = |---------|
    print(line*height, end='')

def upward_arrow(character):
    '''
    This function will display the upwards arrow of the selected
    shape witt the provided character.
    '''
    # Defines the index, scalar to determine number of
    # characters and space to determine number of space.
    index = 0
    scalar = 1
    space = 5
    
    # Loopt through to print upward arrow by multiplying 
    # space string with a space variable and character 
    # argument with scalar variable.
    while index < 6:
        print(' '*space + character*scalar)
        scalar += 2 # index each variable.
        space -= 1
        index += 1

def downward_arrow(character):
    '''
    This function will display the downward arrow of the selected
    shape with the provided character.
    '''
    # Reverses the upward_arrow function.
    index = 6
    scalar = 11
    space = 0
    
    while index > 0:
        print(' '*space + character*scalar)
        scalar -= 2
        space += 1
        index -= 1

def main():
    
    # Stores user input in to variables 
    shape = input("Enter shape to display:\n")
    if shape != 'hourglass' and shape != 'plumbbob' and shape != 'house':
        print('Not valid option.') # Prints message if input is invalid.
    else:
        character = input("Enter arrow character:\n")
        height = int(input("Enter row-area height:\n")) # wrap input into int. 
        print()
    
    # Will check input of shape and display an image by calling 
    # the line, upward, and downward function.
    if shape == 'hourglass':
        line(height)
        downward_arrow(character)
        upward_arrow(character)
        line(height)
    elif shape == 'plumbbob':
        upward_arrow(character)
        line(height)
        downward_arrow(character)
    elif shape == 'house':
        upward_arrow(character)
        line(height)

main()

