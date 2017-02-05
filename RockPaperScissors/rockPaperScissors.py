# Title:  	Rock Paper Scissors game
# Author: 	Thomas Luong
# Purpose:	Allow user to play RPS against a computer
# Usage:	Practice creating a good user experience and object oriented programming

# Notes:	Ask player to pick rock, paper or scissors
#			Have the computer chose its move.
#			Compare the choices and decide who wins.
#			Print the results

# Subgoals:	Give the player the option to play again
#			Keep a record of the score (e.g. Player: 3 / Computer: 6)

from random import randint

class Player:
	def __init__(self):
		self.score = 0
		self.choice = None

human = Player()
computer = Player()

def game(player1, player2):
	choices = ["rock", "paper", "scissors"]

	computerChoice = randint(0, 2)
	player2.choice = choices[computerChoice]

	while (player1.choice == None):
		print("********************************************")
		humanChoice = raw_input("What is your decision: Rock, Paper or Scissors: ").lower()
		if (humanChoice not in choices):
			print("Please spell or enter a correct option.\n")
		else:
			player1.choice = humanChoice

	print "Human chooses: " + player1.choice 
	print "Computer chooses: " + player2.choice + "\n"

	result = whoWon(player1, player2)
	if (result == 0):
		print("Draw")
	elif (result == 1):
		print("Human wins")
		player1.score += 1
	elif (result == 2):
		print("Computer wins")
		player2.score += 1
	else:
		print("Error: No result applicable to the match")

	print "Player: " + str(player1.score) + " / Computer: " + str(player2.score) + "\n"

	player1.choice = None

# return 0 if draw.
# return 1 if player1 won, 
# return 2 if player2 won, 
def whoWon(player1, player2):
	if (player1.choice == player2.choice):
		return 0
	elif (player1.choice == "rock") and (player2.choice == "scissors"):
		return 1
	elif (player1.choice == "rock") and (player2.choice == "paper"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "scissors"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "rock"):
		return 1
	elif (player1.choice == "scissors") and (player2.choice == "rock"):
		return 2
	elif (player1.choice == "scissors") and (player2.choice == "paper"):
		return 1
	else:
		return 3


playAgain = True

while (playAgain == True):
	game(human, computer)

	request = raw_input("Would you like to play again? (Y/N) : ").lower()
	if (request == 'y'):
		playAgain = True
		print("Playing again\n")
	elif (request == 'n'):
		playAgain = False
		print("Let's stop\n")
	else:
		print("Didn't understand either Y or N, playing again by default.\n")
	



