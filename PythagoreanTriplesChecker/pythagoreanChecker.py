# Title:  	Pythagorean Triples Checker
# Author: 	Thomas Luong
# Purpose:	Returns whether the triangle is a Pythagorean Triple or not
# Usage:	Practice logical number checking and using exponents

# Notes:	Allows the user to input the sides of any triangle in any order
#			Returns whether the triangle is a Pythagorean Triple or not
#			Loops the program so user can use it more than once without restarting


def pythagoreanCheck():
	a = int(raw_input("Side A Length: "))
	b = int(raw_input("Side B Length: "))
	c = int(raw_input("Side C Length: "))

	if (a**2 + b**2) == c**2:
		print("Yes, this triplet is a Pythagorean Triple")
	else:
		print("No, this triplet is not a Pythagorean Triple")

pythagoreanCheck()
