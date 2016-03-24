# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.

import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break

def askUserChoice():
    while true:
    	choice = int(input('How many sticks would you like to pick up? (1-4) :'))
	if int(choice) > 4 
        	choice = int(input('Please enter a number between 1 and 4'))
        elif int(choice) <1:
        	choice = int(input('Please enter a number between 1 and 4'))
        else:
        	return int(choice)

def subtractSticks( number ):
    global sticks 
    sticks -= number
    if sticks <= 0:
    	return True
    else:
        return False

def determineComputerChoice():
    return random.randrage(1,5)