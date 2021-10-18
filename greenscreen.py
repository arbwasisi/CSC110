###
### Author: Arsene Bwasisi
### Description: This program will take several inputs, including a color
###              channel(r,g,b), the channel difference, a greenscreen
###              image, a background image, and a file name to create.
###              From these inputs, the program will combine a still image
###              from the greenscreen, with the background image.

from os import _exit as exit

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def generate_image(gs_pixels, fi_pixels, cd, color):
    '''
    This function will create a 3D list of pixels for the new image
    using the greenscreen algorithm.
    gs_pixels: 3D pixel list of the greenscreen image
    fi_pixels: 3D pixel list of the background fill image
    cd: A floating number representing the channel difference
    color: A string representing the channels r, g, b
    '''

    new_pixels = []
    i = 0 # Row index
    j = 0 # Individual pixel index

    for row in gs_pixels:
        rows = [] # Reset rows list every iteration

        # Use the greenscreen algorithm to determine which
        # pixel to use
        for pixel in row:
            if color == 'r':
                # if channel r, multiply channel difference to
                # the other channels
                # c1, c2: first and second channel product
                c1, c2 = pixel[1]*cd, pixel[2]*cd
                if pixel[0] > c1 and pixel[0] > c2:
                    # use pixels from fill image if r values
                    # is greater then c1 and c2
                    rows.append(fi_pixels[i][j])
                else:
                    rows.append(pixel)
            elif color == 'g':
                c1, c2 = pixel[0]*cd, pixel[2]*cd
                if pixel[1] > c1 and pixel[1] > c2:
                    rows.append(fi_pixels[i][j])
                else:
                    rows.append(pixel)
            elif color == 'b':
                c1, c2 = pixel[0]*cd, pixel[1]*cd
                if pixel[2] > c1 and pixel[2] > c2:
                    rows.append(fi_pixels[i][j])
                else:
                    rows.append(pixel)
            j += 1
        j = 0 # reset index with new row
        i += 1
        new_pixels.append(rows)

    return new_pixels

def write_new_file(file_name, pixels, out_file):
    '''
    This function will take the data from the pixels list and write
    it to out_file.
    file_name: Greenscreen inputed file
    pixels: Pixel list of new image
    out_file: Name of file to write data to
    '''

    image_file = open(file_name, 'r')

    first_line = image_file.readline()
    second_line = image_file.readline()
    third_line = image_file.readline()

    write_data = []

    i = 0 # row index
    # iterates through pixels and creates the structure
    # for the new file
    for row in pixels:
        for pixel in row:
            for index in range(len(pixel)):
                rgb = pixel[index]
                if i == len(row)-1 and index == 2:
                    rgb = str(rgb) + '\n'
                    write_data.append(rgb)
                else:
                    rgb = str(rgb) + ' '
                    write_data.append(rgb)
            i += 1
        i = 0 # reset row index

    new_file = open(out_file, 'w')

    new_file.write(first_line)
    new_file.write(second_line)
    new_file.write(third_line)

    # Write data to file and close file
    for data in write_data:
        new_file.write(data)

    new_file.close()

def main():

    # Get the 5 input values from the user, as described in the PA specification
    # These input values will be validated later in main
    colors = ['r', 'g', 'b']

    channel = input('Enter color channel\n')
    if channel not in colors:
        print('Channel must be r, g, or b. Will exit.')
        exit(0)

    channel_difference = float(input('Enter color channel difference\n'))
    if channel_difference < 1.0 or channel_difference > 10.0:
        print('Invalid channel difference. Will exit.')
        exit(0)

    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')

    wh1 = get_image_dimensions_string(gs_file)
    wh2 = get_image_dimensions_string(fi_file)
    wh1, wh2 = wh1.split(' '), wh2.split(' ')
    w1, h1 = int(wh1[0]), int(wh1[1])
    w2, h2 = int(wh2[0]), int(wh2[1])

    if w1 != w2 and h1 != h2:
        print('Images not the same size. Will exit.')
        exit(0)
    out_file = input('Enter output file name\n')

    # Next, Do some valiation of the input values
    # The PA specification tells you what you need to validate

    # If the the input is valid, implement the greenscreen.
    # You should:
    #    * Load in the image data from the two input image files.
    #      Use the provided load_image_pixels functions for this!
    #    * Generate a NEW image based on the two input values,
    #      using the greenscreen algorithm described in the specification
    #    * Save the newly-generated image to a file
    # You probably will want to create other function(s) that you call from here.

    gs_pixels = load_image_pixels(gs_file)
    fi_pixels = load_image_pixels(fi_file)

    pixels = generate_image(gs_pixels, fi_pixels, channel_difference, channel)
    write_new_file(gs_file, pixels, out_file)
    print('Output file written. Exiting.')

main()
