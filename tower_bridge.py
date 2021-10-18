# Author: Arsene Bwasisi	
# Description: A program to print out ASCII art of the famous
#			   landmarks using user input.

bridge_length = int(input("enter bridge length:\n"))
lower_tower = int(input("lower tower height length:\n"))
upper_tower = int(input("upper tower height length:\n"))
tower_width = int(input("enter tower width:\n"))
bt_tower = "     |u" + "."*tower_width + "u|   " + " "*bridge_length + "   |u" + "."*tower_width + "u|\n"
tp_tower = "    |||" + "^"*tower_width + "uu|  " + " "*bridge_length + "  |uu" + "^"*tower_width + "|||\n"

print("    +  " + " "*tower_width + "  +  " + " "*bridge_length + "  +  " + " "*tower_width + "  +")
print(tp_tower*upper_tower, end='')
print("     \\u" + "^"*tower_width +"u/===" + "="*bridge_length + "===\\u" + "^"*tower_width + "u/")
print(bt_tower*lower_tower, end='')
print("_____|u" + "."*tower_width + "u|___" + "_"*bridge_length + "___|u" + "."*tower_width + "u|_____")
print("====HHH" + "H"*tower_width + "HH===" + "="*bridge_length + "===HHH" + "H"*tower_width + "HH====")
print(("    HHH" + "H"*tower_width + "HH   " + " "*bridge_length + "   HHH" + "H"* tower_width + "HH\n")*3, end='')