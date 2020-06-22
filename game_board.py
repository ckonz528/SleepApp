import random as r

class GameBoard():

    def __init__(self):
        """Initialize the game board"""
        self.width = 31 
        self.height = 10
        self.board = []

        # create a new board
        for y in range(self.height):
            self.board.append([]) 
            for x in range(self.width):
                self.board[y].append(r.choice(['~', '`', '*', '.']))
    
    def displayBoard(self):
        """function to display the current state of the game board"""
        # construct tens line for grid labels
        tensLine = '     '
        for i in range(self.width // 10):
            tensLine += ('  ' * 9) + str(i + 1) + ' '
        
        # construct ones line for grid labels
        onesLine = '   ' + ('0 1 2 3 4 5 6 7 8 9 ' * (self.width // 10))
        for i in range(self.width % 10):
            onesLine += str(i) + ' '
        
        # display game board with grid labels
        print(tensLine)
        print(onesLine)

        for row in range(self.height):
            print(f'{row:2d} {" ".join(self.board[row])} {row:<2d}')

        print(onesLine)
        print(tensLine)