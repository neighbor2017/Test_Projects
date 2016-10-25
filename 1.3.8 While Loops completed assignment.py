from __future__ import print_function

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

import random

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''A winner is chosen between four names.
    The user then guesses the winner and the program keeps asking them until
    they get it correctly.
    '''
    winner = random.choice(players) # Winner is chosen at random.

    ####
    # This block of code prints the first line of the program.
    # It states the names that can win.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # the index corresponds to a name in the list to be printed, up until the very last name
        print(p+', ', end='')
    print(players[len(players)-1]) # prints the last name in the players list without a comma

    ####
    # Asks for guesses of the winner until the winner is chosen. Returns the number of guesses it took.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
    
def goguess():
    '''Program picks a number and user tries to guess it'''
    
    ####
    # Variable initialization
    ####
    guess_count = 0
    secret = random.randint(1,20)
    current_guess = ''
    print('I have a number between 1 and 20 inclusive.')
    
    ####
    # First guess processing
    ####
    current_guess = int(raw_input('Guess the number: '))
    guess_count += 1
    
    ####
    # Guessing loop
    ####
    while secret != current_guess:
        if current_guess > secret: # High-low printout controller
            print(current_guess,'is too high.')
        else: 
            print(current_guess, 'is too low.')
        
        current_guess = int(raw_input('Guess again: ')) 
        guess_count += 1
        
        if current_guess == -1: # Loop breaker
            break
    ####
    # Final printout and function end
    ####    
    print('Correct! My number was', secret, end='.\n')
    print('You guessed my number in', guess_count, 'tries.')    
    return guess_count  
        
        
        
        