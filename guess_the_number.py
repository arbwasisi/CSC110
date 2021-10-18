# Author: Arsene Bwasisi    
# Description: This prompts users to input a number between 10 and 100,
#              a second user will have to guess the inputed number. User
#              has 2 shots to get it right. A message will print if guess
#              if incorrect and if guess is correct.

num = int(input("Enter number to be guessed between 10 and 100, inclusive:\n"))

if num < 10 or num > 100:
	print(num, "is not 10-100, inclusive.")
else:
    first_guess = int(input("First guess:\n"))

    if first_guess != num:
        print(first_guess, "is incorrect.")
        second_guess = int(input("Second guess:\n"))
        if second_guess != num:
            print(second_guess, "is incorrect.")
            print("You did not guess the number within 2 attempts.")
            print("The target number was {}".format(num))
            print("Your guesses were {} and {}".format(first_guess, second_guess))
        else:
            print(second_guess, "is correct! Ending game.")
    else:
        print(first_guess, "is correct! Ending game.")

