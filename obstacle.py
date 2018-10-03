import config


class Obstacle ():
    def __init__(self, matrix):
        self._height = len(matrix)
        self._width = len(matrix[0])
        self.matrix = matrix

        self._destroyable = None
        self._health = None
        self._score = 0

        self.position = config.positionVector()
        self.oldPosition = config.positionVector()
        self.newPosition = config.positionVector()

    def setPosition(self, x, y):
        self.oldPosition = self.newPosition
        self.newPosition.x = x
        self.newPosition.y = y
        self.position = self.newPosition

    def drawOntoBoard(self, board):
        for i in range(self.position.y, self.position.y + self._height):
            for j in range(self.position.x, self.position.x + self._width):
                board.matrix[i][j] = self.matrix[i -
                                                 self.position.y][j - self.position.x]

    def width(self):
        return self._width

    def height(self):
        return self._height

    def score(self):
        return self._score

    def isDestroyable(self):
        return self._destroyable


class Ground (Obstacle):
    def __init__(self, matrix=config.ground):
        Obstacle.__init__(self, matrix)
        self._destroyable = False


class Ground2 (Obstacle):
    def __init__(self, matrix=config.ground2):
        Obstacle.__init__(self, matrix)
        self._destroyable = False


class Cloud (Obstacle):
    def __init__(self, matrix=config.cloud):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class L (Obstacle):
    def __init__(self, matrix=config.L):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class E (Obstacle):
    def __init__(self, matrix=config.E):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class V (Obstacle):
    def __init__(self, matrix=config.V):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class One (Obstacle):
    def __init__(self, matrix=config.One):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class Two (Obstacle):
    def __init__(self, matrix=config.Two):
        Obstacle.__init__(self, matrix)
        self._destroyable = False
        self.type = None


class Pipe (Obstacle):
    def __init__(self, matrix=config.pipe):
        Obstacle.__init__(self, matrix)
        self._destroyable = False


class unDestroyableBlock (Obstacle):
    def __init__(self, matrix=config.blocks1):
        Obstacle.__init__(self, matrix)
        self._destroyable = False


class destroyableBlock (Obstacle):
    def __init__(self, matrix=config.blocks2):
        Obstacle.__init__(self, matrix)
        self._destroyable = True

    def checkForHit(self, board):
        for i in range(self.position.y):
            if board.matrix[self.position.y + self.height()][self.position.x + i] is 'A':
                self.matrix = config.blocks1
                return True
        return False

# class mushroom (Obstacle):
#   def __ init__ ()
