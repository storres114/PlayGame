# Santiago Torres
# bagles.py
# September 17th, 2023
# CISW 24

import random
 
# (!) Try setting this to 1 or 10
NUM_DIGITS = 4
 
# (!) Try setting this to 1 or 10
MAX_GUESSES = 12
 
def main():
    print('''Bagels, a deductive logic game.
     
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
 
When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
 
For example, if the secret number was 2481 and your guess was 8439,
the clue would be Fermi Pico.'''.format(NUM_DIGITS))
     
    # main game loop
    while True:
        # This stores the secret number the plaer needs to guess:
        secretNum = getSecretNum()
 
        print('I have thought up a number')
        print(' You have {} guesses to get it right'.format(MAX_GUESSES))
 
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
 
            # keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
 
            clues = getClues(guess, secretNum)
            print(clues)
 
            numGuesses += 1
 
            if guess == secretNum:
                # There are correct, so break out of this loop
                break
            if numGuesses > MAX_GUESSES:
                print('You have run out of guesses')
                print('The answer was {}.'.format(secretNum))
         
        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
         
    print('Thanks for playing!')
 
def getSecretNum():
    """ Returns a string made up of NUM_DIGITS unique random digits. """
    # create a list of digits 0 to 9
    numbers = list('0123456789')
    # shuffle them into random order
    random.shuffle(numbers)
 
    # get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
     
    return secretNum
 
def getClues(guess, secretNum):
    """ Returns a string with the Pico, Fermi, Bagels clues for a guess and secret number pair """
    if guess == secretNum:
        return 'You got it!'
     
    clues = []
 
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong place
            clues.append('Pico')
    if(len(clues) == 0):
        # There are no correct answers
        return 'Bagels'
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information way
        clues.sort()
 
        # Make a single string from the list of string clues
        return ' '.join(clues)
 
# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
