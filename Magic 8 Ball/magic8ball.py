# Title:  	Magic 8 Ball
# Author: 	Thomas Luong
# Purpose:	Simulate a magic 8-ball
# Usage:	To practice displaying random responses

# Notes:	Allow user to enter question
#			Display an inprogress message ("i.e. 'thinking..")
#			Create 20 responses and show random response
#			Allow user to ask another question or quit
# Bonus: add gui with box to enter question with 4 buttons
#		ask, clear (text box), play again, quit (closes window)

from random import randint
from time import sleep
from easygui import *
import sys

def showFortune():
	responses = ["Yes I believe so", "No I don't think so", "Anything is possible", "If you truely believe so, it will become true",
		"Only on Tuesdays", "Please ask later when I feel like answering", "No",
		"Yes", "What would your mother say?", "Please consult the Magic 9 Ball about this matter, I'm not qualified enough",
		"Does a turtle have a shell?", "Does an ant have muscles?", "I think so",
		"Yeah, I'm sure of it", "No, it will never happen", "Reconsider your life choices",
		"Do I look like a miracle worker?", "Impossible", "Never say never - 'Justin Beiber'",
		"I think Google is better qualified on this matter"]

	indexResponse = randint(0,19)
	fortune = "The Magic 8 Ball says: " + responses[indexResponse]

	msgbox("Thinking...")
	sleep(2)
	msgbox(fortune)

def displayPrompt()

def magicEightBall():
	msg = "State your question to the Magic 8 Ball:  "

	choices = ["Ask", "Clear", "Play Again", "Quit"]
	reply = buttonbox(msg, choices=choices)

	if (reply == "Ask"):
		

	elif (reply == "Clear"):


magicEightBall()





