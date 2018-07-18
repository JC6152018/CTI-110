#This program will run a random number guessing game
#With the user until they guess correctly.
#July 6th, 2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Jessica Washington

#Start the random module.
import random

#Create the game.
number = random.randint(1, 100)

#Ask the user to guess the number.
def main():
    print('You will get 10 guesses.')
    game_loop(number)
    exit
    

#Create the game loop.
def game_loop(number):
    tries = 10
    count = 0
    for attempts in range(tries):
        i = (int(input('Guess a number 1 - 100:')))
        count = count + 1        
        #Set what happens if the guesses are incorrect.
        if i < number:
            print('Too low, try again.')
        elif i > number:
            print('Too high, try again.')
        #Set what happens if correct.
        if i == number:
            break
    if i == number:
        print('That is correct. Great job!')
        #Show attempts.
        print('You guessed it in', count, 'guesses!')
        print()
        exit
    if i != number:
        print('You did not guess the number.')
        print()
        exit             
#Call the main function.
main()
#Ask user if they would like to play again.
play = input('Would you like to play again? Y or N: ')
while play == 'Y' or play == 'y':
    print()
    main()
    #Initiate play
    #End game.
if play == 'n' or play == 'N':
    print('Thanks for playing!')

    
        
    
