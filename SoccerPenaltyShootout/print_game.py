import sys
import math
import re
import time
from getpass import getpass


def print_rules():
    print("You've selected Rules:")
    print("The game rules are similar to real life soccer penalties after the game extension. Each player has five chances to score a goal by enetering the position of the shot. In that turn the other player has the chance to hold the shot by entering the position of the goalkeeper. After the try the players will change their roles and the other will shoot where the other will try to hold. The score will be printed. The game ends after best of five or if one player scores more goals then the other. If the players have the same socre after the five tries the panalties will be extended with one try until there is a winner. You can choose wich player starts to shoot and which to hold. All your inputs will be hidden. The choice entry are always from the - looking frontal at the goal - perspective. If you wanna play alone you can play against the CPU. Good luck and have fun.\n")


def print_winner(player):
    if player == False:
        print("Player1 WINS!\n\n")
    else:
        print("Player2 WINS!\n\n")


def print_and_select_options():
    print("[1] Top Left")
    print("[2] Buttom Left")
    print("[3] Middle")
    print("[4] Top Right")
    print("[5] Buttom Right")
    
    while True:
        try:
            choice = int(getpass("Select from Number [1] - [5]: "))
        except ValueError:
            print("Not a correct Value!")
            continue
        else:
            if check_choice(choice) == False:
                print("Not a correct Value!")
                continue
            else:
                return choice
    

def check_choice(choice):
    if (choice < 1 or choice > 5):
        return False
    else:
        return True


def print_score(player1_goals, player2_goals):
    print("-----------------------")
    print("| Player1: " + str(player1_goals))
    print("| Player2: " + str(player2_goals))
    print("-----------------------\n")
    
def print_goal():
    print("     ________________________________     ")
    print("     |                              |     ")
    print("     |              O               |     ")
    print("     |           ---|---            |     ")
    print("     |              -               |     ")
    print("_____|_____________/_\______________|_____\n")


def print_goalkeeper_jump(keeper_choice):
    time.sleep(0.8)
    if(keeper_choice == 1):
        print("     ________________________________     ")
        print("     |\                             |     ")
        print("     | \_O_                         |     ")
        print("     |    \\                        |     ")
        print("     |     -___                     |     ")
        print("_____|_____\________________________|_____")
        print("Keeper jumps to the TOP LEFT!\n")
    elif(keeper_choice == 2):
        print("     ________________________________     ")
        print("     |                              |     ")
        print("     |                              |     ")
        print("     |   \  ___                     |     ")
        print("     |  O--|                        |     ")
        print("_____|___/__---_____________________|_____")
        print("Keeper jumps to the BUTTOM LEFT!\n")
    elif(keeper_choice == 3):
        print("     ________________________________     ")
        print("     |                              |     ")
        print("     |              O               |     ")
        print("     |           ---|---            |     ")
        print("     |              -               |     ")
        print("_____|_____________/_\______________|_____")
        print("Keeper stays in the MIDDLE!\n")
    elif(keeper_choice == 4):
        print("     ________________________________     ")
        print("     |                             /|     ")
        print("     |                         _O_/ |     ")
        print("     |                        //    |     ")
        print("     |                     ___-     |     ")
        print("_____|________________________/_____|_____")
        print("Keeper jumps to the TOP RIGHT!\n")
    elif(keeper_choice == 5):
        print("     ________________________________     ")
        print("     |                              |     ")
        print("     |                              |     ")
        print("     |                     ___  /   |     ")
        print("     |                        |--O  |     ")
        print("_____|_____________________---__\___|_____")
        print("Keeper jumps to the BUTTOM RIGHT!\n")
    else:
        print("An Failure happend")
        sys.exit(1)


def print_shot(shooter_choice):
    if(shooter_choice == 1):
        print("\nBall gets shot to the TOP LEFT!")
    elif(shooter_choice == 2):
        print("\nBall gets shot to the BUTTOM LEFT!")
    elif(shooter_choice == 3):
        print("\nBall gets shot to the MIDDLE!")
    elif(shooter_choice == 4):
        print("\nBall gets shot to the TOP RIGHT!")
    elif(shooter_choice == 5):
        print("\nBall gets shot to the BUTTOM RIGHT!")
    else:
        print("An Failure happend")
        sys.exit(1)
