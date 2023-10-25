#!/usr/local/bin/python3
# The Game of 21
# Guess a number 1, 2, or 3 and try to get to 21
# Sable Cantus
# http://cantus.us/mtsac

import random

total = 0
turn = 0

while True:
    if turn == 0:
        print()
        print('The total is', total)
        print('>>> Players turn <<<')
        if 0 <= total < 21:
            number = int(input('Choose a number 1, 2, or 3: '))
        else:
            number = int(input('cannot go above 21. choose again:'))
        total = total + number
        if total == 21:
            print('You win!')
            break
        else:
            turn = 1
    else:
        print()
        print('The total is', total)
        print('>>> computers turn <<<')
        computerChoice = random.randint(1,3)
        if total + computerChoice > 21:
            print('You win')
            break
        print('I choose {}.'.format(computerChoice))
        total = total + computerChoice
        if total == 21:
            print('I win!')
            break
        else:
            print('Your turn')
            turn = 0