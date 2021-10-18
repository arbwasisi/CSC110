# Author: Arsene Bwasisi
# Description: This program will read in a CSV file that's inputed by the
#              user. The user will determine an operation to peform on the
#              data in the file, either compute the minimum, maximum or 
#              the average, of a particular column, then display the results.              

def find_max(numbers_list, column):
    ''' 
    Finds the maximum value of a column in the numbers list.
    numbers_list: A 2D list of numbers.
    column: The column to perform the operation on
    '''

    maximum = 0 # set maximum to 0 
    # Iterate through the value of the provided column in the list
    for row in numbers_list:
        number = row[column-1] # Take away one to adjust the index
        # Set maximum to number if number greater than maximum
        if float(number) > maximum:
            maximum = float(number)

    print('The maximum value in column', column, 'is:', str(maximum))

def find_min(numbers_list, column):
    ''' 
    Finds the minimum of a column in the numbers list.
    numbers_list: A 2D list of numbers.
    column: The column to perform the operation on
    '''

    minimum = 100 # set minimum to 100 
    for row in numbers_list:
        number = row[column-1]
        if float(number) < minimum: # check for minimum value
            minimum = float(number)

    print('The minimum value in column', column, 'is:', str(minimum))

def find_avg(numbers_list, column):
    ''' 
    Finds the average from a column in the numbers list.
    numbers_list: A 2D list of numbers.
    column: The column to perform the operation on
    '''

    number_sum = 0 # a sum of all the number in the column
    for row in numbers_list:
        number = row[column-1]
        number_sum += float(number) # add each number to number_sum
    
    # Divide the sum of numbers by the length of numbers_list
    # to obtain the average
    average = number_sum/len(numbers_list)

    print('The average for column', column, 'is:', str(average))

def main():
    
    # Get the needed information from users
    csv_file = input('Enter CSV file name:\n')
    column = int(input('Enter column number:\n')) 
    operation = input('Enter column operation:\n')
    open_file = open(csv_file, 'r') # Open csv file
    
    # Process the data in csv_file and create
    # 2D list
    float_list = list()
    for line in open_file:
        split_line = line.strip('\n').split(',')
        float_list.append(split_line)
    
    # Call each function depending on the operation
    if operation == 'max':
        find_max(float_list, column)
    elif operation == 'min':
        find_min(float_list, column)
    elif operation == 'avg':
        find_avg(float_list, column)

main()
