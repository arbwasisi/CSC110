44# Author: Arsene Bwasisi
# Description: This program will use inputs from users to display a bridge
#              structure using different charachters and will calculate the
#              deflection of the bridge structure with those inputs.

# We grap input from users and convert them in integers.
bridge_length = int(input("Bridge length:\n"))
support_spacing = int(input("Spacing between supports:\n"))
points_spacing = int(input("Spacing between points to measure deflection at:\n"))
weight = int(input("Weight:\n"))

# Variables that define counters, indexs, and strings
measure_points = ''
beam = ''
support = ''
points = 0
count = 0
index = 0
index_2 = 0

# This while loop will add charachters to the empty strings if the conditions are true.
while count < bridge_length:
    beam += '#'

    # if the index is less than the inputed point spacing
    # and a space and increment index, else turn points to string
    # and add it to measure_points string, reset index.
    if index < points_spacing:
        measure_points += ' '
        index += 1
    else:
        measure_points += str(points)
        points += 1
        index = 0

    # if the index_2 is less than the inputed point spacing
    # and a space and increment index_2, else and # charachter and
    # reset index.
    if index_2 < support_spacing:
        support += ' '
        index_2 += 1
    else:
        support += '#'
        index_2 = 0

    count += 1

print("   " + measure_points + "   ")
print("EEE" + beam + "EEE")
print("EEE" + support + "EEE")
print("EEE" + support + "EEE")
print("EEE" + support + "EEE")

# Define extra index after support_spacing and scalar used to multiply
# points_spacing and support_spacing depending on number of points and supports
index = 1
scalar = 1
count = 0

print()
print('DEFLECTIONS:')

# This While loop will iterate through the code depending on number of points.
# It will calculate the distance of point from support and plug it in to the
# equation to calculate the delfection, then print out the result.
while count < points:
    # if there is no support or the point spacing is greater than support spacing,
    # it will run a different formula for distance than if there was support pylons.
    if support_spacing >= bridge_length or points_spacing > support_spacing:

        # This will calculate the distance(x) from point(p) spacing to its neares support(s).
        # By using modulus we find the remainder of p/s
        distance = (scalar*points_spacing+index)%(scalar*support_spacing+index)
        if distance > (support_spacing + 1) - distance: # This checks if x is > s - x.
            distance = (support_spacing + 1) - distance # If it is, it sets x to the smaller value.
    else:
        # Calculates the remainder of s/p if support is there
        distance = (scalar*support_spacing+index)%(scalar*points_spacing+index)
        if distance > (support_spacing + 1) - distance: # Performs same function as line 73
            if distance > support_spacing + 1: # Checks if x is greater than s+i
                distance = distance - (support_spacing + 1) # if true x - s+1, else s+1 - x
            else:
                distance = (support_spacing + 1) - distance

    # Caluclates the deflection with x and given input and displays results.
    deflection = ((weight*distance)/(48*210*500))*((3*support_spacing**2)-(4*distance**2))
    print('    point', count, '=', round(deflection, 5))
    scalar+=1
    index+=1
    count+=1
    