# Author: Arsene Bwasisi	
# Description: A program to print out ASCII art of the Bodiam
#			   castle using user input of castle width.

width = int(input(" castle width:\n "))
space = width + 3
print("")
print(" "*space,  ".-.-.",  " "*space)
print(" [-]" + " "*width + "|-.-|" + " "*width + "[-]")
print(" | |" + "_"*width + "| H |" + "_"*width + "| |")
print(" | |" + " "*width + "| H |" + " "*width + "| |")
print(" | |" + " "*width + "| H |" + " "*width + "| |")
print(" |_|" + "_"*width + "||^||" + "_"*width + "|_|")