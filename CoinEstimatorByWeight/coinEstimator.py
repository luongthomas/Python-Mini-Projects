# Title:  	Coin Estimator By Weight
# Author: 	Thomas Luong
# Purpose:	Allows user to calculate an estimated total from an input of the 
#				total coin weight of each type as well as number of coin 
#				wrappers they need.
# Usage:	Practice creating a good user experience and object oriented programming

# Notes:	Allows user to input total weight of each type of coin they have
#				pennies, nickels, dimes and quarters
#			Print out how many of each type of coin wrapper they would need
#				how many coins they have, and an estimated total value of their money


# Subgoals:	Round all numbers printed to the nearest whole number
#			Allow user to select whether they want to submit weight in grams or pounds

# Coin Info:
#			Penny, 	$0.01, 1982-present mass is 2.50g, 50 fit into wrapper (total $0.50), 0.00551156 pounds
#				
#			Nickel, $0.05, mass is 5.00 g, 	40 fit into wrapper (total, $2.00), 0.0110231 pounds
#				
#			Dime, 	$0.10, mass is 2.268 g,	50 fit into wrapper (total, $5.00), 0.0050000841 pounds
#				
#			Quarter,$0.25, mass is 5.67 g,  40 fit into wrapper (total $10.00), 0.01250021 pounds
#				

from math import floor

class Coin:
	def __init__(self, value, massGram, massPound, wrapperCapacity, name, numberOfCoins = 0, totalWeight = 0, wrappers = 0):
		self.value = value
		self.massGram = massGram
		self.massPound = massPound
		self.wrapperCapacity = wrapperCapacity
		self.name = name
		self.numberOfCoins = 0
		self.totalWeight = 0
		self.wrappers = 0

class Penny(Coin):
	def __init__(self):
		super().__init__(value = 0.01, massGram = 2.50, massPound = 0.00551156, wrapperCapacity = 50, name = "pennies")

class Nickel(Coin):
	def __init__(self):
		super().__init__(value = 0.05, massGram = 5.00, massPound = 0.0110231, wrapperCapacity = 40, name = "nickels")

class Dime(Coin):
	def __init__(self):
		super().__init__(value = 0.10, massGram = 2.268, massPound = 0.0050000841, wrapperCapacity = 50, name = "dimes")

class Quarter(Coin):
	def __init__(self):
		super().__init__(value = 0.25, massGram = 5.67, massPound = 0.01250021, wrapperCapacity = 40, name = "quarters")

def weight(coin, units):
	if (units == 'grams'):
		return coin.massGram
	elif (units == 'pounds'):
		return coin.massPound
	else:
		return "Error, cannot return weight"

def coinEstimate():
	
	repeat = True
	unitShorthand = "g"

	# -- USER INPUT --
	# TODO: Ask if want to enter weight in pounds or grams
	while (repeat == True):
		units = int(input("Enter 1 to enter coin weight in grams, enter 2 for pounds: "))

		if (units == 1):
			
			units = "grams"
			unitShorthand = "g"
			repeat = False
			print("Units selected: ", units)
		elif (units == 2):
			
			repeat = False
			units = "pounds"
			unitShorthand = "lbs"
			print("Units selected: ", units)
		else:
			print("Please enter 1 or 2.\n")


	penny = Penny() 
	nickel = Nickel()
	dime = Dime()
	quarter = Quarter()

	print(penny.value)
	print("number of pennies: " + str(penny.numberOfCoins))

	# TODO: Ask for weight of pennies, nickels, dimes and quarters separately
	# TODO: Store as value
	penny.totalWeight = input("Enter the weight of pennies you have in " + units + ": ")
	nickel.totalWeight = input("Enter the weight of nickels you have in " + units + ": ")
	dime.totalWeight = input("Enter the weight of dimes you have in " + units + ": ")
	quarter.totalWeight = input("Enter the weight of quarters you have in " + units + ": ")
	
	print(penny.totalWeight, nickel.totalWeight, dime.totalWeight, quarter.totalWeight)

	

	# -- CALCULATIONS --
	# TODO: For each coin type, divide input mass by coin mass to get number of coins
	penny.numberOfCoins = round(float(penny.totalWeight) / weight(penny, units))
	nickel.numberOfCoins = round(float(nickel.totalWeight) / weight(nickel, units))
	dime.numberOfCoins = round(float(dime.totalWeight) / weight(dime, units))
	quarter.numberOfCoins = round(float(quarter.totalWeight) / weight(quarter, units))
	print('number of pennies ', penny.numberOfCoins)
	print('number of dimes ', dime.numberOfCoins)
	

	# TODO: With number of coins, divide by wrapper capacity for each coin type
	penny.wrappers = floor(penny.numberOfCoins / penny.wrapperCapacity)
	nickel.wrappers = floor(nickel.numberOfCoins / nickel.wrapperCapacity)
	dime.wrappers = floor(dime.numberOfCoins / dime.wrapperCapacity)
	quarter.wrappers = floor(quarter.numberOfCoins / quarter.wrapperCapacity)
	print('number of penny wrappers: ', penny.wrappers)
	print('number of dime wrappers: ', dime.wrappers)

	# TODO: Calculate total value of all coins
	totalValue = (penny.numberOfCoins * penny.value +
		nickel.numberOfCoins * nickel.value +
		dime.numberOfCoins * dime.value +
		quarter.numberOfCoins * quarter.value )

	

	# -- DISPLAY RESULTS --
	# TODO: Print how many coin wrappers they need for each coin
	print("\nYou have these many coins for each coin type: ")
	print("		penny: ", penny.numberOfCoins)
	print("		nickel: ", nickel.numberOfCoins)
	print("		dime: ", dime.numberOfCoins)
	print("		quarter: ", quarter.numberOfCoins)

	# TODO: Print how many coins they have for each coin
	print("\nThe number of wrappers needed for: ")
	print("		penny: ", penny.wrappers)
	print("		nickel: ", nickel.wrappers)
	print("		dime: ", dime.wrappers)
	print("		quarter: ", quarter.wrappers)

	# TODO: Print an estimated total value of their money
	print('\nThe total value of all your money is: $', totalValue)
	


coinEstimate()











