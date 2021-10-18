# Author: Arsene Bwasisi
# Description: This program will display a bridge structure using
#              letters and characters when given input, such as the
#              width of the bridge and the spacing of the support.

length = int(input("Bridge length:\n"))
spacing = int(input("Spacing between supports:\n"))

beam = ''
support = ''
count = 1
index = 0
height = 3

while count <= length:
    beam += '#'
    if index < spacing:
        support += ' '
        index += 1
    else:
        support += '#'
        index = 0
    count += 1

print("\nEEE" + beam + "EEE")

while height > 0:
    print("EEE" + support + "EEE")
    height -= 1
    
