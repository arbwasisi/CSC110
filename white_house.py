# Author: Arsene Bwasisi	
# Description: A program to print out ASCII art of the famous
#			   landmarks using user input.

side_width = int(input("Specify side width:\n"))
middle_width = int(input("Specify middle width:\n"))
flag_height = int(input("Specify flag height:\n"))

space = (side_width * 3) + (middle_width * 4)
height = ((side_width + middle_width)//4) + 1

pole = " "* space + " |\n"
top = "|" + "II "* side_width + "||II"* middle_width + "HH" + "II||"* middle_width + " II"* side_width + "|"
bottom = "\n|" + ".. "* side_width + "||.."* middle_width + "||" + "..||"* middle_width + " .."* side_width + "|"
wall = top + bottom + '\n'

print("")
print(" "* space, "|##")
print(pole*flag_height, end='')
print("   "* side_width + " " + ".-.-"* middle_width + "''" + "-.-."* middle_width, "   "* side_width)
print("   "* side_width + " " + ";.__"* middle_width + "--" + "__.;"* middle_width, "   "* side_width)
print("." + "___"* side_width + "[---"* middle_width + "--" + "---]"* middle_width + "___"* side_width + ".")
print(wall*height, end='')