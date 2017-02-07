# Title:  	Mad Libs
# Author: 	Thomas Luong
# Purpose:	Creates a story based on verbs, adjectives and nouns that the user inputs
# Usage:	Practice python functions and reusability

# Notes:	Create Mad Libs style game where user inputs certain types of words
#			Story doesn't have to be too long but should have some sort of story line.

# Subgoals:
#			If user puts in a name, change first letter to capital letter
#			Change the word "a" to "an" when next word in sentence begins with a vowel



'''

Your hands feel warm.  You wake up and open your eyes slowly.  While lying down you raise your head.  Glancing down
at your hands and see a frog licking your fingers.  It croaks.  Suddenly it jumps onto your chest.  It stares at your 
forehead.  You decide to kiss it.  The frog is enveloped by an intense white light.  It flickers for a while and is 
now only flickering.  Once the light is gone, the frog that was there before is a beautiful human looking back at you.  
The person says, "Hello my name is J, and I love you."  

You married this person and now you have 8 kids.  And a pet frog.

'''

'''

Your hands feel __(adjective describing touch)__.  You wake up and open your eyes slowly.  
While lying down you raise your head.  Glancing down at your __(body part)__ and see [a] __(animal*)__ licking your fingers.  
It __(animal sound)__.  Suddenly it __(verb describing movement and ends in s)__ onto your chest.  It stares at your 
__(body part)__.  You decide to kiss it.  The __(animal*)__ is enveloped by an intense __(color)__ light.  
It flickers for a while and is now only flickering dimly.  Once the light is gone, the __(animal*)__ that was there before 
is a __(a word to describe your crush)__ human looking back at you.  

The person says, "__(greeting)__ my name is __(name of your crush/lover)__, and I love you."  

You married this person and now you have __(number)__ kids.  And a pet __(animal*)__.

'''

from time import sleep
def madlibs():
	print("Madlibs starting, please enter the words below: ")
	print("------------------------------------------------")
	touchAdj = input("An adjective describing touch: ")
	bodyPart = input("A body part: ")
	animal = input("An animal: ")
	animalSound = input("A sound an animal makes: ")
	color = input("A color: ")
	name = input("The name someone you like: ")
	adjective = input("An adjective to describe someone you like: ")
	number = input("A number from one to 50: ")
	greeting = input("A greeting to your good friend: ")

	print("\n------------------------------------------------")
	print("Word gathering complete.  Creating story...")
	sleep(5)
	print("\n\nYour hands feel " + touchAdj + ".  You wake up and open your eyes slowly. ")
	sleep(2)
	print("While lying down you raise your head.")
	sleep(2)
	print("Glancing down at your " + bodyPart + ", you then see a " + animal + " licking your fingers.  ")
	sleep(2)
	print("It says " + animalSound + ".")
	sleep(2)
	print("You decide to kiss it.")
	sleep(1)
	print("The next thing you know, the " + animal + " is enveloped by an intense "+ color + " light.  ")
	sleep(2)
	print("It flickers for a while and is now only flickering dimly.")	
	sleep(2)
	print("Once the light is gone, the " + animal + " that was there before... ")
	sleep(2)
	print("...is now a " + adjective + " human looking back at you.")
	sleep(2)
	print("The person says, \"" + greeting + " my name is " + name + ", and I love you.\"")
	sleep(2)
	print("You married this person and now you have " + number + " kids.  And a pet " + animal + ".")
	sleep(2)

	print("\nThe end.\n\n")

madlibs()



