# Santiago Torres
# assignment6
# 10/15/23
# CISW 24


import sys
import os
import datetime

timestamp = datetime.datetime.now()
timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

def myLogger(s):
    logEntry = timestamp + " " + s + "\n"
    logFile = open('log.txt', 'a+')
    logFile.write(logEntry)
    logFile.close()

player_name = input("Player: What is your name? ")
games_played = 0
wins = 0
losses = 0

player_entry = "New Player Entry: " + player_name
myLogger(player_entry)

lets_play = input('Would you like to play a game? (y/n/q): ')
if lets_play == 'n':
    print('Thank you for playing. Good bye.')
    player_stats = "Totals: wins - {} losses - {}".format(wins,losses)
    myLogger(player_stats)
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
            player_game_choice = player_name + " chose bagels."
            myLogger(player_game_choice)
            games_played = games_played + 1
            winlose = input('Did you win or lose your game? (w/l)')
            if winlose == 'w' :
                wins = wins + 1
            elif winlose == 'l' :
                losses = losses + 1

        elif game_choice == '2':
            print('You chose Rock, Paper, Scissors! Have a nice game.')
            player_game_choice = player_name + " chose Rock, Paper, Scissors"
            myLogger(player_game_choice)
            games_played = games_played + 1
            winlose = input('Did you win or lose your game? (w/l)')
            if winlose == 'w' :
                wins = wins + 1
            elif winlose == 'l' :
                losses = losses + 1

        elif game_choice == '3':
            print('You chose The Game 21! Have a nice game. ')
            player_game_choice = player_name + " chose The Game 21."
            myLogger(player_game_choice)
            games_played = games_played + 1
            winlose = input('Did you win or lose your game? (w/l)')
            if winlose == 'w' :
                wins = wins + 1
            elif winlose == 'l' :
                losses = losses + 1

        elif game_choice not in [1,2,3,'q']:
            print('oops')
        
        
        if game_choice.lower() == 'q':
            print('Thank you for playing. Good bye.')
            player_stats = "Totals: wins - {} losses - {}".format(wins,losses)
            myLogger(player_stats)
            sys.exit()