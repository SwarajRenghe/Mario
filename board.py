import config
from colorama import Fore, Back


class Board ():
    def __init__(self, height=config.boardHeight, width=config.boardWidth, visibleWidth=config.visibleBoardWidth, background1=config.boardBackground1, background2=config.boardBackground2):
        self._height = height
        self._width = width
        self._background1 = background1
        self._background2 = background2

        self.matrix = []
        self.x = 0
        self.visibleWidth = visibleWidth
        self._levelOneLength = config.levelOne

        self._position = config.positionVector()
        self._bottomCorner = config.positionVector()

        tempMatrix = []
        for i in range(self._height):
            temp = []
            for j in range(self._width):
                if j < self._levelOneLength:
                    temp.append(self._background1)
                else:
                    temp.append(self._background2)
            tempMatrix.append(temp)
            del temp
        self.matrix = tempMatrix
        del tempMatrix

    def clearMatrix(self):
        tempMatrix = []
        for i in range(self._height):
            temp = []
            for j in range(self._width):
                if j < self._levelOneLength:
                    temp.append(self._background1)
                else:
                    temp.append(self._background2)
            tempMatrix.append(temp)
            del temp
        self.matrix = tempMatrix
        del tempMatrix

    def printMatrix(self):
        for i in range(self._height):
            for j in range(self.x, self.x + self.visibleWidth):
                if self.matrix[i][j] in ['/', '|', '-', '\\', '_', 'V']:
                    # print (Back.WHITE, end='')
                    print(Fore.YELLOW, end='')
                elif self.matrix[i][j] in ['A', '|', 'E', 'M', '}']:
                    # print (Back.BLUE, end='')
                    print(Fore.WHITE, end='')
                elif self.matrix[i][j] is 'X':
                    print(Back.BLUE, end='')
                    print(Fore.WHITE, end='')
                elif self.matrix[i][j] is '?':
                    print(Back.RED, end='')
                    print(Fore.WHITE, end='')
                elif self.matrix[i][j] in ['H', 'O']:
                    # print (Back.BLUE, end='')
                    print(Fore.CYAN, end='')
                elif self.matrix[i][j] is ' ':
                    # print (Back.BLUE, end='')
                    print(Fore.GREEN, end='')
                elif self.matrix[i][j] is 'I':
                    # print (Back.GREEN, end='')
                    print(Fore.GREEN, end='')
                elif self.matrix[i][j] is '{':
                    # print (Back.BLUE, end='')
                    print(Fore.MAGENTA, end='')
                elif self.matrix[i][j] is '{':
                    # print (Back.BLUE, end='')
                    print(Fore.MAGENTA, end='')
                else:
                    # print (Back.BLUE, end='')
                    print(Fore.RED, end='')
                print(self.matrix[i][j], end='')
                print(Back.RESET, end='')
            print('')

    def width(self):
        return self._width

    def height(self):
        return self._height

    def leftLimit(self):
        return self.x

    def levelOne(self):
        return self._levelOneLength

    def setLevelOne(self):
        self._levelOneLength = 200

    def changeBackground(self, background):
        self._background = background
        # self._background2 = background
