# Author: Arsene Bwasisi
# Description: This program calculates the deflection of a
#              simulated bridge by taking various user inputs including,
#              bridge length and weight of object.

length = int(input("Bridge length:\n"))
distance = int(input("Distance to calculate deflection at:\n"))
weight = int(input("Weight:\n"))

deflection = ((weight*distance)/(48*210*500))*((3*length**2)-(4*distance**2))
print('\ndeflection =', round(deflection, 5))

