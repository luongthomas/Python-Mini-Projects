# Title:  	Mean, Median and Mode
# Author: 	Thomas Luong
# Purpose:	Finds mean (average), mode and median in a set of numbers without built-in functions for mean, median and mode

# Notes:	Create three functions that allow user to find mean, median, and mode
#			No built-in functions

# Subgoals:
#			In mean functions, give user option for how many decimal places to round to
#			If even numbers in list, return both middle numbers for median
#			If multiple modes, return all of them

class Statistics():
	def __init__(self, numbers, decimalPlaces):
		self.numbers = numbers
		self.numbers.sort()
		self.decimalPlaces = decimalPlaces
		self.mean = None
		self.median = None
		self.mode = None

	def print_mean(self):
		sum = 0
		for num in self.numbers:
			sum += num
		self.mean = sum / len(self.numbers)
		print("The mean is ", self.mean)

	def print_mode(self):
		modes = []
		currentStreak = 0
		highestStreak = 0
		uniqueNums = set(self.numbers) # Eliminates repeating elements

		for i, num in enumerate(uniqueNums):
			currentStreak = self.numbers.count(num)
			if (currentStreak > highestStreak):
				highestStreak = currentStreak
				modes.clear()
				modes.append(num)

			elif (currentStreak == highestStreak):
				modes.append(num)

		print("Modes:")
		for mode in modes:
			print(mode, end=' ')
		print("")


	def print_median(self):
		length = len(self.numbers)
		middle = int(length / 2)
		if (length % 2 == 0):
			print(self.numbers[middle - 1], self.numbers[middle]) 
		else:
			print(self.numbers[middle])



	def print_list(self):
		print("The list is: ")
		for i, num in enumerate(self.numbers):
			print(num, end=' ')
		print("")




user_array = input("Please input an array of numbers separated by spaces: \n\t")
user_array = user_array.split(" ")
user_array = [int(x) for x in user_array]

decimals = 2
newList = Statistics(user_array, decimals)

choice = input("Type '1' for finding mean, '2' for mode, or '3' for median:\n\t")
if (choice == '1'):
	newList.print_mean()
elif (choice == '2'):
	newList.print_mode()
elif (choice == '3'):
	newList.print_median()
else:
	print("Sorry I didn't understand your choice.  Goodbye\n")

