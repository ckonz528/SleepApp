## Treasure hunt game

import random as r
from math import sqrt
import sys
from game_board import GameBoard
from Instructions import showInstructions

def getChests(numChests, width, height):
    chests = []
    for i in range(numChests):
        newChest = [r.randint(0, width), r.randint(0, height)]
        if newChest not in chests:
            chests.append(newChest)
    return(chests)

def getMove(previous_moves, width, height):
    """Allows the player to enter the coordinates of their guess"""
    print('Where would you like to deploy your next device?')
    while True:
        move = input('Enter the x coordinate, a space, then the y coordinate of your guess (or type quit): ')

        #validate move
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) != 2:
            print('***ERROR: wrong number of inputs.')
        elif not move[0].isdigit() or not move[1].isdigit():
            print('***ERROR: both inputs must be integers.')
        elif not isOnBoard(int(move[0]), int(move[1]), width, height):
            print('***ERROR: invalid move. That space is not on the board.')
        elif [int(move[0]), int(move[1])] in previous_moves:
            print('***ERROR: You have already tried that space.')
        else:
            return(int(move[0]), int(move[1]))

def isOnBoard(x, y, width, height):
        if x not in range(width) or y not in range(height):
            return(False)
        else:
            return(True)

def makeMove(game, chests, x, y):
    """React to the user's coordinate selection"""
    smallest_dist = 100
    for cx, cy in chests:
        dist = sqrt((cx - x)**2 + (cy - y)**2)

        # check for the closest chest
        if dist < smallest_dist: 
            smallest_dist = dist

    smallest_dist = round(smallest_dist)
        
    if smallest_dist == 0:
        print('You found a treasure chest!!!')
        chests.remove([x, y]) # remove found chest from list
        game.board[y][x] = 'C'
        return('Chest')
    else:
        if smallest_dist < 10: 
            game.board[y][x] = str(smallest_dist)
            print(f'Treasure detected {smallest_dist} paces from the detector.')
            return False
        else:
            game.board[y][x] = 'X'
            print('The detector did not find anything. All chests must be out of range')
            return False

def playTreasureHunt():
    print('Welcome to Treasure Hunt!\n')

    while True:
        instructions = input('Would you like to view the instructions? (Y/N): ')
        if instructions not in ['y', 'n', 'Y', 'N']:
            print('***ERROR: Invalid response. Please enter Y or N.')
        elif instructions.lower == 'y':
            showInstructions()
        else:
            break

    while True:
        # Game setup
        detectors = 20
        board = GameBoard()
        width = board.width
        height = board.height
        chests = getChests(3, width, height)
        board.displayBoard()
        previous_moves = []

        while detectors > 0:
            # show status
            print(f'You have {detectors:d} detectors left and {len(chests)} chests remaining.')

            x, y = getMove(previous_moves, width, height)
            previous_moves.append([x, y])

            result = makeMove(board, chests, x, y)
            if result == False:
                continue
            else: 
                if result == 'Chest':
                    # Update previously placed detectors
                    for x, y in previous_moves:
                        makeMove(board, chests, x, y)
            board.displayBoard()

            if len(chests) == 0:
                print('Congratulations! You found all the chests!')
                break

            detectors -= 1

        if detectors == 0:
            print('Darn! You ran out of detectors :(')
            print('I guess that treasure will stay hidden!')
            print('The remaining chests were here:')
            for x, y in chests:
                print(f'    {x}, {y}')