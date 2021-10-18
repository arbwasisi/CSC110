# Author: Arsene Bwasisi
# Description: Using graphics.py, this program will display
#              a canvas with 3 shapes, a triangle, a rectangle
#              and a square, all with different colors. Each
#              shape will move across the screen at the same
#              speed and rap around when they exit the screen.

from graphics import graphics
import random

def sun(gui):
    ''' A function that displays the sun on the canvas.'''
    
    # Set mouse_x and mouse_y to move sun with low motion
    x = (gui.mouse_x/38)
    y = (gui.mouse_y/38)
    gui.ellipse(x+600, y+75, 100, 100, 'gold')

def foreground(gui):
    ''' This function will display the foreground of the landscape.'''
    
    # Set mouse_x and mouse_y to move foreground with fast motion
    x = (gui.mouse_x/6)
    y = (gui.mouse_y/6)
    gui.rectangle(x-150, y+550, 900, 900, 'lawn green')
    
    # Iterate through and display grass blade
    i = -50
    while i < 950:
        offset = i * 3
        if offset % 2 == 0: # Diplay grass for every other iteration
            gui.line(x + offset, y + 550, x + offset, y + 525, 'lime green', 2)
        i += 1

    gui.rectangle(x + 525, y + 500, 25, 100, 'brown4')
    gui.ellipse(x + 537, y + 475, 100, 150, 'forest green')

def mountain(gui, color1, color2, color3):
    ''' A function to display the side mountains and back mountain.'''
    
    # Set mouse_x and mouse_y to move middle mountain and side mountain
    # with moderate motion, middle mountain moves slower than side mountain
    x = gui.mouse_x
    y = gui.mouse_y
    gui.triangle((x/28) + 375, (y/28) + 150, (x/28) - 25, (y/28) + 750, (x/28) + 775, (y/28) + 750, color1)
    gui.triangle((x/22) + 175, (y/22) + 250, (x/22) - 175, (y/22) + 750, (x/22) + 600, (y/22) + 750, color2)
    gui.triangle((x/22)+ 575, (y/22) + 250, (x/22) + 175, (y/22) + 750, (x/22) + 975, (y/22) + 750, color3)

def birds(gui, x, y):
    ''' A function that displays birds across the canvas.'''
    
    # Iterate through loop to display 5 birds
    i = 0
    while i < 10:
        if i * 5 % 2 == 0: # Display only if divisble by 2
            gui.line(x, y, x + 15, y + 10, 'black', 2) # Add to x so birds are displayed across the screen
            gui.line(x + 15, y + 10, x + 30, y, 'black', 2) # Also add to y so birds are slightly slanting
        i += 1
        x += 50
        y += 10

def main():

    gui = graphics(750, 750, 'Landscape')
    red_1 = random.randint(0, 255)
    green_1 = random.randint(0, 255)
    blue_1 = random.randint(0, 255)
    red_2 = random.randint(0, 255)
    green_2 = random.randint(0, 255)
    blue_2 = random.randint(0, 255)
    red_3 = random.randint(0, 255)
    green_3 = random.randint(0, 255)
    blue_3 = random.randint(0, 255)
    
    # Set color for mountain, different color will display when program is run
    color_1 = gui.get_color_string(red_1, green_1, blue_1)
    color_2 = gui.get_color_string(red_2, green_2, blue_2)
    color_3 = gui.get_color_string(red_3, green_3, blue_3)
    
    x = -500 
    y = 200
    while True:
        gui.clear() # Clear canvas through each iteration
        gui.rectangle(-10, -10, 800, 800, 'sky blue')
        sun(gui)
        mountain(gui, color_1, color_2, color_3)
        foreground(gui)
        birds(gui, x, y)
        gui.update_frame(50) # Update frame for motion
        
        # Move birds across the canvas by adding to x value
        # If birds exit the screen, reset value of x
        if x > 750: 
            x = -500
        x += 5
main()


