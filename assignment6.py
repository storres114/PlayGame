# Santiago Torres
# assignment6
# 10/3/23
# CISW 24


import sys

lets_play = input('Would you like to play a game? (y/n/q): ')
if lets_play == 'n':
    print('Thank you for playing. Good bye.')
    sys.exit()

if lets_play == 'y':
    while True:
        game_choice=input('''
    Choose a game or quit:
                      
    1) Bagels
    2) Rock, Paper, Scissors
    3) The Game 21
    q) to quit
                      
    Enter your choice: ''')
        
        if game_choice == '1':
            print('You chose bagels! Have a nice game.')
        elif game_choice == '2':
            print('You chose Rock, Paper, Scissors! Have a nice game.')
        elif game_choice == '3':
            print('You chose The Game 21! Have a nice game. ')
        elif game_choice not in [1,2,3,'q']:
            print('oops')
        
        
        if game_choice.lower() == 'q':
            print('Thank you for playing. Good bye.')
            sys.exit()