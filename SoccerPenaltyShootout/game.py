import sys
import math
import re
import random
import time
import print_game as print_game


def check_selection(selection):
    if selection == 1:
        start_game(False) #PvP
    elif selection == 2:
        start_game(True) #PvC
    elif selection == 3:
        print_game.print_rules()
    elif selection == 4:
        print("Exiting the game...")
        sys.exit(0)
    else:
        print("Exiting the game...")
        sys.exit(0)
        
        
def start_game(bot_enable):
    if bot_enable == True:
        print("You have selected PvC Mode:")
        play_game(bot_enable)
    else:
        print("You have selected PvP Mode:")
        play_game(bot_enable)
    

def play_game(bot_enable):
    options = [1, 2, 3, 4, 5]
    player = False #Player1
    player1_goals = 0
    player2_goals = 0
    tries = 0 #five for each player, means ten in total
    extension = False
    
    while True:
        if player == False:
            print_game.print_goal()
            print("--> Player1 Shooter Choice:")
            shooter_choice = print_game.print_and_select_options()
            
            print("--> Player2 Goalkeepers Choice:")
            if (bot_enable == True):
                keeper_choice = random.choice(options)
                print("CPU making an entry...")
                time.sleep(0.3)
            else:
                keeper_choice = print_game.print_and_select_options()
                
            print_game.print_shot(shooter_choice)
            print_game.print_goalkeeper_jump(keeper_choice)
            
            if (shooter_choice == keeper_choice):
                print("Player2 Goalkeeper HOLDS!\n")
            else:
                player1_goals += 1
                print("Player1 Shooter scores a GOAL!\n")
            
            print_game.print_score(player1_goals, player2_goals)
            player = True
            extension = False
        else:
            print_game.print_goal()
            print("--> Player2 Shooters Choice:")
            if (bot_enable == True):
                shooter_choice = random.choice(options)
                print("CPU making an entry...")
                time.sleep(0.3)
            else:
                shooter_choice = print_game.print_and_select_options()
                
            print("--> Player1 Goalkeepers Choice:")
            keeper_choice = print_game.print_and_select_options()
            print_game.print_shot(shooter_choice)
            print_game.print_goalkeeper_jump(keeper_choice)
            
            if (shooter_choice == keeper_choice):
                print("Player1 Goalkeeper HOLDS!\n")
            else:
                player2_goals += 1
                print("Player2 Shooter scores a GOAL!\n")
            
            print_game.print_score(player1_goals, player2_goals)
            player = False
            extension = True
        
        tries += 1
        if (tries == 10):
            draw = check_winner(player1_goals, player2_goals)
            if (draw == False):
                break
            else:
                continue

        if (tries > 10 and extension == True): #going into extension and checking the winner
            draw = check_winner(player1_goals, player2_goals)
            if (draw == False):
                break
            else:
                continue

        if (check_winner_diff(player1_goals, player2_goals, tries) == True):
            break
        else:
            continue
            

def check_winner(player1_goals, player2_goals): #after five shots for each player
    if (player1_goals > player2_goals):
        print_game.print_winner(False)
        return False
    elif (player1_goals < player2_goals):
        print_game.print_winner(True)
        return False
    else:
        return True


def check_winner_diff(player1_goals, player2_goals, tries): #for best of five
    #for score 3:0
    if ((player1_goals - player2_goals) >= 3):
        print_game.print_winner(False)
        return True
    elif ((player2_goals - player1_goals) >= 3):
        print_game.print_winner(True)
        return True
    #for score 4:2 and 5:3 
    elif (tries == 8 or tries == 9):
        if ((player1_goals - player2_goals) == 2):
            print_game.print_winner(False)
            return True
        elif ((player2_goals - player1_goals) == 2):
            print_game.print_winner(True)
            return True
        else:
            return False
    else:
        return False
