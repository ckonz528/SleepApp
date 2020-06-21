import random as r

class GameBoard():

    def __init__(self):
        self.width = 22 
        self.height = 10
        self.board = []

        # create a new board
        for y in range(self.height):
            self.board.append([]) 
            for x in range(self.width):
                self.board[y].append(r.choice(['~', '`', '*', '.']))
    
    def displayBoard(self):
        # construct tens line for grid labels
        tensLine = '   '
        for i in range(self.width // 10):
            tensLine += ('_ ' * 9) + str(i + 1) + ' '
        
        # construct ones line for grid labels
        onesLine = '   ' + ('1 2 3 4 5 6 7 8 9 0 ' * (self.width // 10))
        for i in range(self.width % 10):
            onesLine += str(i + 1) + ' '
        
        # display game board with grid labels
        print(tensLine)
        print(onesLine)

        for row in range(self.height):
            print(f'{row + 1:2d} {" ".join(self.board[row])} {row + 1:2d}')

        print(onesLine)
        print(tensLine)
        

test = GameBoard()
test.displayBoard()