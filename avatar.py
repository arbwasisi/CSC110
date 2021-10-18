# Author: Arsene Bwasisi
# Description: This program allows user to build their own custom avatar
#              or select from 3 pre-desgined avatars. The user will be prompt
#              to give different input imcluding characters and size the will
#              determine the look and feature of the avatar.

def avatar_hat(direction):
    ''' 
    This function will print a specified hat, either a top hat,
    a cam hat facing right, left or forward.
    '''
    
    # Defines the crown and brim of hat
    crown = '       ~-~\n' + '     /-~-~-\\'
    brim = '___'
    
    # A conditon to check where user wants brim placed
    if direction == 'left':
        print(crown)
        print(' '+ brim + '/_______\\')
    elif direction == 'right':
        print(crown)
        print('    /_______\\' + brim)
    elif direction == 'both':
        print(crown)
        print(' ' + brim + '/_______\\' + brim)
    else:
        print(crown)
        print('    /_______\\')
        
def avatar_face(hair, eyes):
    ''' 
    This function will display the avatars face with some features like 
    the hair and eyes being determine by the user.
    '''
    # An if statement to determine if hair is shaggy or not
    if hair == 'True':
        hair = '"""""""'
    else:
        hair = "'''''''"
        
    print('    |' + hair + '|')
    print('    | ' + eyes + '   ' + eyes + ' |')
    print('    |   V   |')
    print('    |  ~~~  |')
    print('     \\_____/')
    
def avatar_arms(character):
    ''' A function that display the avatar's arm using user input.'''
    
    arm = ''
    index = 0
    
    # Loops through to add character input to arm variable
    while index < 4:
        arm += character
        index += 1
        
    print(' 0' + arm, end='')
    print('|---|', end='')
    print(arm + '0')

def avatar_torso(height):
    ''' A function that controls the height of the avatar's torso from user input.'''
    
    torso = '      |-X-|'
    index = 0
    
    while index < height:
        print(torso)
        index += 1
        
def avatar_legs(height):
    ''' A function that controls the height of the avatar's legs from user input.'''
    
    # Set starting number of space for outside and inside the leg
    # outside will decrease, while inside increase.
    out_space = '     '
    in_space = ' '
    index = 4
    count = 0
    
    print('      HHHHH')
    while count < height:
        print(out_space + '///' + in_space + '\\\\\\')
        in_space += '  ' # adds 2 spaces with each loop
        # index decrease with each loop, so less space is printed with each loop
        out_space = out_space[:index]
        index -= 1
        count += 1 
        
def jeff():
    ''' This function builds the avatar Jeff.'''
    
    avatar_hat('both')
    avatar_face('True', '0')
    avatar_arms('=')
    avatar_torso(2)
    avatar_legs(2)
    print('#HHH#       #HHH#')
    
def adam():
    ''' This function builds the avatar Adam.'''
    
    avatar_hat('right')
    avatar_face('False', '*')
    print('      |-X-|')
    avatar_arms('T')
    avatar_torso(3)
    avatar_legs(3)
    print('<|||>       <|||>')
 
def chris():
    ''' This function builds the avatar Chris.'''
    
    avatar_hat('forward')
    avatar_face('True', 'U')
    print('      |-X-|')
    avatar_arms('W')
    avatar_torso(1)
    avatar_legs(4)
    print('<>-<>       <>-<>')

def custom():
    ''' This function builds an avatar designed by the user, using user input.'''
    
    print('Answer the following questions to create a custom avatar')
    hat_style = input('Hat style ?\n')
    eye_char = input('Character for eyes ?\n')
    hair_style = input('Shaggy hair (True/False) ?\n')
    arm_char = input('Arm style ?\n')
    torso_length = int(input('Torso length ?\n'))
    leg_length = int(input('Leg length (1-4) ?\n'))
    shoe_style = input('Shoe look ?\n')
    
    print()
    avatar_hat(hat_style)
    avatar_face(hair_style, eye_char)
    avatar_arms(arm_char)
    avatar_torso(torso_length)
    avatar_legs(leg_length)
    print(shoe_style, '     ', shoe_style)

def create_avatar(choice):
    ''' Builds the avatar based on the input provided.'''
    
    if choice == 'Jeff':
        print()
        jeff()
    elif choice == 'Adam':
        print()
        adam()
    elif choice == 'Chris':
        print()
        chris()
    elif choice == 'custom':
        custom()

def main():
    print('----- AVATAR -----')
    choice = input('Select an Avatar or create your own:\n')

    while choice != 'exit':
        if choice != 'Jeff' and choice != 'Adam' and choice != 'Chris' and choice != 'custom':
            choice = input('Select an Avatar or create your own:\n')
        else:
            return create_avatar(choice) # Returns the created avatar to function
main()  
