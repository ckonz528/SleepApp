"""This program is designed to help improve CPAP usage adherance for sleep apnea patients"""

from menus import *
import treasure_hunt as TH
import sys

GAMES = 0

def showMainMenu():
    print('\nMain Menu')
    print('What would you like to do?')
    main_selection = get_menu_selection(main_options)
    
    if main_selection == 1:
        showLogMenu()
    elif main_selection == 2:
        showTHMenu()
    else:
        sys.exit()

def showLogMenu():
    print('\nMain Menu > Log Adherance')
    while True:
        log_selection = get_menu_selection(log_options)

        if log_selection == 1:
            date = input("Enter today's date (MM-DD-YYYY): ")
            hours = maskHours()
            with open('Mask_Hours.txt', 'a') as fo:
                fo.write(date + ': ' + str(hours) + ' hours')

            if hours >= 4:
                print("Great job! You've earned 1 game of Treasure Hunt!")
                print("It's important to use your CPAP machine for at least 4 hours per night.")
                #GAMES += 1
            else:
                print("Darn! No games awarded.")
                print("Tonight, try to use your CPAP machine for at least 4 hour to earn a game of Treasure Hunt1 tomorrow!")
        
        elif log_selection == 2:
            showCleaningMenu()
        
        else:
            showMainMenu()


def showTHMenu():
    print('\nMain Menu > Play Treasure Hunt')
    while True:
        TH_selection = get_menu_selection(TH_options)
    
        if TH_selection == 1:
            print('You have earned XX games of Treasure Hunt.')
        elif TH_selection == 2:
            TH.playTreasureHunt()
        else:
            showMainMenu()

def showCleaningMenu():
    while True:
        print('\nMain Menu > Log Adherance > Clean Parts')
        cleaning_selection = get_menu_selection(clean_options)

        print('Great job! You earned 1 game of Treasure Hunt.')
        if cleaning_selection == 1:
            print('Wiping down your face mask can help prevent sores.')
        elif cleaning_selection == 2:
            print('Replacing the water in your CPAP helps ensure proper humidification.')
        elif cleaning_selection == 3:
            print("Clean tubing helps make sure air is correctly delivered while you're sleeping.")
        elif cleaning_selection == 4: 
            print("It's important to clean your water tank regularly to prevent bacterial growth.")
        elif cleaning_selection == 5:
            print("Cleaning your face mask helps prevent residue build up.")
        else:
            showLogMenu()

def maskHours():
    while True:
        hours = input('Enter the number of hours you slept with your mask on: ')

        if hours.isdigit:
            hours = int(hours)
            return hours
        else:
            print('***ERROR: Please enter an integer.')


### BEGIN PROGRAM    
print('Welcome to SleepAPPnea, where the real treasure is better sleep.')

showMainMenu()