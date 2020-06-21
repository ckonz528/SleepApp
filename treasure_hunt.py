## Treasure hunt game

import random as r
from game_board import GameBoard

def getChests(numChests, width, height):
    chests = []
    for i in range(numChests):
        newChest = [r.randint(0, width), r.randint(0, height)]
        if newChest not in chests:
            chests.append(newChest)
    return(chests)

def collectGuess(detectors, chests):
    print(f'You have {detectors:d} metal detectors left.')
    print(f'There are still {chests} remaining.')
    x, y = input('Where would you like to deploy your next device? (or type quit) ').split

### BEGIN PROGRAM
print('Welcome to Treasure Hunt!')

instructions = input('Would you like to view the instructions? (Y/N): ')

if instructions == 'N':
    detectors = 10
    board = GameBoard()
