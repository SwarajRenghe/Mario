import config
import time
import sys


class Person ():
    def __init__(self, matrix):
        self._height = len(matrix)
        self._width = len(matrix[0])
        self.matrix = matrix
        self._downwardVelocity = 1
        self._gravity = None
        self._direction = None

        self._moveByHowMuch = None

        self._health = None
        self._livesRemaining = None
        self._score = None

        self._position = config.positionVector()
        self.oldPosition = config.positionVector()
        self.newPosition = config.positionVector()

    def setPosition(self, x, y):
        self.oldPosition = self.newPosition
        self.newPosition.x = x
        self.newPosition.y = y
        self._position = self.newPosition

    def drawOntoBoard(self, board):
        for i in range(self._position.y, self._position.y + self._height):
            for j in range(self._position.x, self._position.x + self._width):
                board.matrix[i][j] = self.matrix[i -
                                                 self._position.y][j - self._position.x]

    def width(self):
        return self._width

    def height(self):
        return self._height

    def applyGravity(self, board):
        if self._downwardVelocity > 0:
            flag = 0
            for i in range(self._downwardVelocity):
                for i in range(self._width):
                    if board.matrix[self._position.y + self.height()][self._position.x + i] not in config.allowedCharacters:
                        flag = 1
                        break
                if flag is 0:
                    self._position.y += 1
                else:
                    self._downwardVelocity = 1
                    break
            self._downwardVelocity += self._gravity
        else:
            if self.position().y + self._downwardVelocity < 0:
                self._downwardVelocity = 1
                return
            flag = 0
            for i in range(self._downwardVelocity, 0):
                for i in range(self._width):
                    if board.matrix[self._position.y - 1][self._position.x + i] not in config.allowedCharacters:
                        flag = 1
                        break
                if flag is 0:
                    self._position.y -= 1
                else:
                    self._downwardVelocity = 1
                    break
            self._downwardVelocity += self._gravity

    def moveRight(self, board):
        flag = 0
        for i in range(self.height()):
            if (self._position.x + self.width() + 1) >= board.width():
                return False
            if board.matrix[self._position.y + i][self._position.x + self.width()] not in config.allowedCharacters:
                flag = 1
                break
        for i in range(self.height()):
            if (self._position.x + self.width() + 1) >= board.width():
                return False
            if board.matrix[self._position.y + i][self._position.x + self.width() + 1] not in config.allowedCharacters:
                flag = 1
                break
        if flag is 0:
            self._position.x += self._moveByHowMuch
            return True
        return False

    def moveLeft(self, board):
        flag = 0
        if self._position.x - 2 >= board.leftLimit():
            for i in range(self.height()):
                if board.matrix[self._position.y + i][self._position.x - 1] not in config.allowedCharacters:
                    flag = 1
                    break
            for i in range(self.height()):
                if board.matrix[self._position.y + i][self._position.x - 2] not in config.allowedCharacters:
                    flag = 1
                    break
            if flag is 0:
                self._position.x -= self._moveByHowMuch
                return True
        return False

    def jumpUp(self, board):
        self._downwardVelocity = -5

    def position(self):
        return self._position

    def direction(self):
        return self._direction

    def score(self):
        return self._score

    def health(self):
        return self._health

    def increaseScore(self, byHowMuch):
        self._score += byHowMuch

    def decreaseScore(self, byHowMuch):
        self._score -= byHowMuch

    def increaseHealth(self, byHowMuch):
        self._health += byHowMuch

    def decreaseHealth(self, byHowMuch):
        self._health -= byHowMuch

    def changeDirection(self):
        # Right = 1. Left = 0
        if self._direction is 1:
            self._direction = 0
        else:
            self._direction = 1


class Mario (Person):
    def __init__(self, matrix=config.mario):
        Person.__init__(self, matrix)
        self._health = 100
        self._livesRemaining = 3
        self._downwardVelocity = 1
        self._gravity = 1
        self._score = 100
        self._moveByHowMuch = 2


class miniEnemy1 (Person):
    def __init__(self, matrix=config.enemy):
        Person.__init__(self, matrix)
        self.health = 100
        self._livesRemaining = 1
        self._downwardVelocity = 1
        self._gravity = 1
        self._direction = 1
        self._moveByHowMuch = 1

    def checkIfPlayerAbove(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)

        # If Player is In Range
        for i in range(player.width()):
            if (player.position().y + player.height()) == self.position().y:
                if (player.position().x) == self.position().x + i:
                    return True
        return False

    def checkIfPlayerLeft(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False

        # If Player is in Range
        for i in range(player.height()):
            if (player.position().x + player.width()) == (self.position().x - 1):
                if (player.position().y + i) == (self.position().y):
                    return True
        return False

    def checkIfPlayerRight(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)

        # If Player is in Range
        for i in range(player.height()):
            if (self.position().x + self.width() + 1) == player.position().x:
                if (player.position().y + i) == self.position().y:
                    return True
        return False


class miniEnemy2 (Person):
    def __init__(self, matrix=config.enemy2):
        Person.__init__(self, matrix)
        self.health = 100
        self._livesRemaining = 1
        self._downwardVelocity = 1
        self._gravity = 1
        self._direction = 1
        self._moveByHowMuch = 2

    def checkIfPlayerAbove(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)

        # If Player is In Range
        for i in range(player.width()):
            if (player.position().y + player.height()) == self.position().y:
                if (player.position().x) == self.position().x + i:
                    return True
        return False

    def checkIfPlayerLeft(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        print(player.position().x + player.width(), self.position().x,
              player.position().y, self.position().y)

        # If Player is in Range
        for i in range(player.height()):
            if (player.position().x + player.width() + 1) == (self.position().x):
                if (player.position().y + i - 1) == (self.position().y):
                    return True
        return False

    def checkIfPlayerRight(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)
        print(player.position().x + player.width(), self.position().x,
              player.position().y, self.position().y)
        # If Player is in Range
        for i in range(player.height()):
            if (self.position().x + self.width() + 1) == player.position().x:
                if (player.position().y + i - 1) == self.position().y:
                    return True
        return False


class bossEnemy (Person):
    def __init__(self, matrix=config.bossEnemy):
        Person.__init__(self, matrix)
        self._health = 1000
        self._livesRemaining = 1
        self._downwardVelocity = 1
        self._gravity = 1
        self._direction = 1
        self._moveByHowMuch = 2

    def checkIfPlayerAbove(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)

        # If Player is In Range
        for i in range(player.width()):
            if (player.position().y + player.height()) == self.position().y:
                if (player.position().x) == self.position().x + i:
                    return True
        return False

    def checkIfPlayerLeft(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        print(player.position().x + player.width(), self.position().x,
              player.position().y, self.position().y)

        # If Player is in Range
        for i in range(player.height()):
            if (player.position().x + player.width()) == (self.position().x):
                if (player.position().y + i) == (self.position().y):
                    return True
        return False

    def checkIfPlayerRight(self, player):
        # If Player is too far Left
        if (player.position().x + player.width()) < self.position().x - 1:
            return False
        # If Player is too far Right
        if (player.position().x) > (self.position().x + self.width() + 1):
            return False
        # print (player.position().y + player.height(), self.position().y, player.position().x, self.position().x)
        print(player.position().x + player.width(), self.position().x,
              player.position().y, self.position().y)
        # If Player is in Range
        for i in range(player.height()):
            if (self.position().x + self.width()) == player.position().x:
                if (player.position().y + i) == self.position().y:
                    return True
        return False
