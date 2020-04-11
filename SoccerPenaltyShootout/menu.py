import sys
import math
import re


def print_logo():
    print("     ________________________________     ")
    print("     |                              |     ")
    print("     |                              |     ")
    print("     |    Soccer Penalty Shootout   |     ")
    print("     |             Menu             |     ")
    print("_____|______________________________|_____\n")


def print_menu():
    print("[1] Player vs Player")
    print("[2] Player vs CPU")
    print("[3] Rules")
    print("[4] Exit")
    
    
def select():
    while True:
        try:
            choice = int(input("Select from Number [1] - [4]: "))
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
    if (choice < 1 or choice > 4):
        return False
    else:
        return True


def start_menu():
    print_logo()
    print_menu()
    return select()
    
