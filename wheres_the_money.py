# Author: Arsene Bwasisi    
# Description: This program takes in various user input including
#              annual income, monthly rent and bills and forms a chart
#              that shows the users annual spending including taxes.

from os import _exit as exit

print('-'*29, '\n' + '-'*5, "WHERE'S THE MONEY", '-'*5, '\n' + '-'*29)

salary = input("What is your annual salary?\n")
if salary.isnumeric():
    salary = int(salary)
else:
    print("Must enter positive integer for salary.")
    exit(0)
    
rent = input("How much is your monthly mortgage or rent?\n")
if rent.isnumeric():
    rent = int(rent)
else:
    print("Must enter positive integer for mortgage or rent.")
    exit(0)
    
bill = input("What do you spend on bills monthly?\n")
if bill.isnumeric():
    bill = int(bill)
else:
    print("Must enter positive integer for bills.")
    exit(0)
    
food_expense = input("What are your weekly grocery/food expenses?\n")
if food_expense.isnumeric():
    food_expense = int(food_expense)
else:
    print("Must enter positive integer for food.")
    exit(0)
    
travel = input("How much do you spend on travel annually?\n")
if travel.isnumeric():
    travel = int(travel)
else:
    print("Must enter positive integer for travel.")
    exit(0)

annual_rent = rent*12
annual_bill = bill*12
annual_food_expense = food_expense*52

rent_percentage = (annual_rent/salary)*100
bill_percentage = (annual_bill/salary)*100
food_expense_percentage = (annual_food_expense/salary)*100
travel_percentage = (travel/salary)*100

if salary <= 15000:
    tax_percentage = 10
elif salary <= 75000:
    tax_percentage = 20
elif salary <= 200000:
    tax_percentage = 25
else:
    tax_percentage = 30
    
tax = salary * ( tax_percentage / 100.0)
if tax > 50000:
    tax = 50000
    
extra = salary - (annual_rent + annual_bill + annual_food_expense + travel + tax)
extra_percentage = (extra/salary)*100

max_dash = max(rent_percentage, bill_percentage, food_expense_percentage, travel_percentage, tax_percentage, extra_percentage)

print('')
print('-'*42 + '-'*int(max_dash), '\nSee the financial breakdown below, based on a salary of ${}\n'.format(salary) 
    + '-'*42 + '-'*int(max_dash))
print("| {:>13} | $ ".format("mortgage/rent") + 
    format(annual_rent, '10,.2f'), '| {:5.1f}% |'.format(rent_percentage), '#'*int(rent_percentage))
print("| {:>13} | $ ".format("bills") + 
    format(annual_bill, '10,.2f'), '| {:5.1f}% |'.format(bill_percentage), '#'*int(bill_percentage))
print("| {:>13} | $ ".format("food") + 
    format(annual_food_expense, '10,.2f'), '| {:5.1f}% |'.format(food_expense_percentage), '#'*int(food_expense_percentage))
print("| {:>13} | $ ".format("travel") + 
    format(travel, '10,.2f'), '| {:5.1f}% |'.format(travel_percentage), '#'*int(travel_percentage))
print("| {:>13} | $ ".format("tax") + 
    format(tax, '10,.2f'), '| {:5.1f}% |'.format(tax_percentage), '#'*int(tax_percentage))
print("| {:>13} | $ ".format("extra") + 
    format(extra, '10,.2f'), '| {:5.1f}% |'.format(extra_percentage), '#'*int(extra_percentage))
print('-'*42 + '-'*int(max_dash))

if extra < 0:
    print(">>> WARNING: DEFICIT <<<")
if tax == 50000:
    print(">>> TAX LIMIT REACHED <<<")

