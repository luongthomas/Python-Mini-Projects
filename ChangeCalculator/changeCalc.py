# Title:  	Change Calculator
# Author: 	Thomas Luong
# Purpose:	Calculates number of coins types that add up to an inputted amount
# Usage:	Practice logic

# Notes:	If inputs $1.47, the program will say 5 quarters, 2 dimes, 0 nickels and two pennies

# Subgoals:	Allows input of price, and money given to calculate change.
#			Loop program until they don't need

from math import floor

def calcChange(amountRecieved, itemPrice):
	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0

	change = round(amountRecieved - itemPrice, 2)
	print("change: ", change)

	quarters = floor(change / 0.25)
	amountWithoutQ = round(change - (quarters * 0.25), 2)

	dimes = floor(amountWithoutQ / 0.10)
	amountWithoutQD = round(amountWithoutQ - (dimes * 0.10), 2)

	nickels = floor(amountWithoutQD / 0.05)
	amountWithoutQDN = round(amountWithoutQD - (nickels * 0.05), 2)

	pennies = floor(amountWithoutQDN / 0.01)
	amountwithoutQDNP = round(amountWithoutQDN, 2)

	print("You need to give: ")
	print("		", quarters, " quarters")
	print("		", dimes, " dimes")
	print("		", nickels, " nickels")
	print("		", pennies, " pennies")


loop = True
while (loop == True):
	cost = float(input("\n\nWhat is the total cost? : "))
	amountGiven = float(input("What is the amount of money given? : "))

	calcChange(amountGiven, cost)
	answer = input("\n\nWould you like to quit (Y/N)? : ")
	if (answer == "N"):
		loop = True
	else:
		loop = False

