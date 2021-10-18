# Author: Arsene Bwasisi
# Description: encrypter.py will take in a file as input, and it will read
#              the contents in the file and shuffle the lines to encrypte
#              the content. It will write the shuffled lines in a different,
#              along with a key file containing the index of the original file.

import random

def read_file(file_name):
    ''' 
    This functions will open and read the inputed file and
    organize the data in to a list.
    '''

    indexes = []
    lines = []

    file = open(file_name, 'r')
    
    # Apppends each line in the file to the lines list
    for line in file:
        if '\n' not in line:
            line += '\n'
        lines.append(line)

    # Create a list of the indexes form the range of the lines list
    for index in range(1, len(lines)+1):
        indexes.append(index)

    return lines, indexes

def encrypter(file_list, file_indexes):
    '''
    This function will use a shuffling algorithm to move the content
    of the list around by using the random module. 
    '''
    
    limit = len(file_list) * 5 # the number of time the list will be shuffled
    count = 0

    while count < limit:

        # Define 2 random number with the file_list range
        num_1 = random.randint(0, len(file_list)-1)
        num_2 = random.randint(0, len(file_list)-1)

        # Swap the indexes in the list with the random numbers
        file_list[num_1], file_list[num_2] = file_list[num_2], file_list[num_1]
        file_indexes[num_1], file_indexes[num_2] = file_indexes[num_2], file_indexes[num_1]

        count += 1

    return file_list, file_indexes

def write_to_file(file_list, file_indexes):
    ''' 
    This function will write the content in the file_list into encrypted.txt,
    and file_indexes into index.txt
    '''

    # Open encrypted.txt and index.txt in write mode
    encrypted_file = open('encrypted.txt', 'w')
    index_file = open('index.txt', 'w')

    # write in the info from file_list and file_indexes into the files
    for index in range(len(file_list)):
        encrypted_file.write(file_list[index])
        index_file.write(str(file_indexes[index]) + '\n')

    encrypted_file.close() # close files
    index_file.close()

def main():
    
    random.seed(125)
    get_file = input("Enter a name of a text file to mix:\n")
    
    lines_list, index_list = read_file(get_file)
    shuffled_lines, shuffled_indexes = encrypter(lines_list, index_list)
    write_to_file(shuffled_lines, shuffled_indexes)

main()
