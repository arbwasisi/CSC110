# Author: Arsene Bwasisi
# Description: Using graphics.py, this program will display
#              a canvas with 3 shapes, a triangle, a rectangle
#              and a square, all with different colors. Each
#              shape will move across the screen at the same
#              speed and rap around when they exit the screen.

from graphics import graphics
import random

def main():
    gui = graphics(800, 800, 'Three Shapes')
    x = 0
    rec_y = random.randint(100, 700)
    elp_y = random.randint(100, 700)
    tri_y = random.randint(100, 700)

    while True:
        gui.clear()
        gui.rectangle(x, rec_y, 100, 100, 'blue')
        gui.ellipse(x + 50, elp_y, 100, 100, 'green')
        gui.triangle(x + 50, tri_y - 100, x, tri_y, x + 100, tri_y, 'red')
        gui.update_frame(30)

        if x > 800:
            x = -100
            rec_y = random.randint(100, 700)
            elp_y = random.randint(100, 700)
            tri_y = random.randint(100, 700)

        x += 10

main()
