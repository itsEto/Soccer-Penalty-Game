import sys
import math
import re
import time
import menu as menu
import game as game


def main():
    while True:
        selection = menu.start_menu()
        game.check_selection(selection)
        time.sleep(0.5)
    

if __name__=='__main__':
    main()
