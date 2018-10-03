import os
import random

# Position Vector : Defines a co-ordinate and an abscissa


class positionVector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


"""
	Miscellaneous Important Functions
"""

# def randomIntegerBetween (a1, a2):
#     return random.randint (a1, a2)


def clear():
    _ = os.system('clear')


def reset():
    _ = os.system('tput reset')


def randomInteger(x, y):
    return random.randint(x, y)


"""
	Miscellaneous Important Objects
"""

# These following are default values; can be changed as per requirement and scale
gameLoop = True

boardHeight = 30
boardWidth = 400
visibleBoardWidth = 130
levelOne = 300
boardBackground1 = ' '
boardBackground2 = ']'


# # Colors
# colors = {
#     "BLACK": "\033[00;30m",
#     "RED": "\033[00;31m",
#     "GREEN": "\033[00;32m",
#     "YELLOW": "\033[00;33m",
#     "BLUE": "\033[00;34m",
#     "PURPLE": "\033[00;35m",
#     "CYAN": "\033[00;36m",
#     "LIGHT_GREY": "\033[00;37m",

#     "DARK_GREY": "\033[01;30m",
#     "BOLD_RED": "\033[01;31m",
#     "BOLD_GREEN": "\033[01;32m",
#     "BOLD_BLUE": "\033[01;33m",
#     "BOLD_PURPLE": "\033[01;34m",
#     "BOLD_CYAN": "\033[01;35m",
#     "BOLD_YELLOW": "\033[01;36m",
#     "WHITE": "\033[01;31m"
# }

# Items to Draw
# class Ground

allowedCharacters = ['{', ' ', '/', 'E']


ground = [['I', 'I', 'I', 'I'], ['I', 'I', 'I', 'I'],
          ['I', 'I', 'I', 'I'], ['I', 'I', 'I', 'I']]
ground2 = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
mario = [[' ', 'A', ' '], ['M', 'M', 'M'], ['E', 'E', 'E'], ['}', ' ', '}']]

cloud = [[boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1], [boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1, boardBackground1], [boardBackground1, boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1, boardBackground1, boardBackground1], [
    boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1], [boardBackground1, boardBackground1, boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1, boardBackground1, boardBackground1], ['{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{'], [boardBackground1, boardBackground1, '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', '{', boardBackground1, boardBackground1]]

pipe = [['O', 'O', 'O', 'O', 'O'],
        [' ', 'H', 'H', 'H', ' '],
        [' ', 'H', 'H', 'H', ' '],
        [' ', 'H', 'H', 'H', ' ']]

blocks1 = [['X', 'X', 'X'],
           ['X', 'X', 'X'],
           ['X', 'X', 'X']]

blocks2 = [['?', '?', '?'],
           ['?', '?', '?'],
           ['?', '?', '?']]

# enemy2 = [['|', '*', '|', '|', '*', '|'],
# ['-', '-', '-', '-', '-', '-'],
# ['[', ']', ' ', ' ', '[', ']']]

enemy = [[' ', '_', '_', '_', ' '],
         ['/', '-', '-', '-', '\\'],
         ['|', '\\', ' ', '/', '|']]

enemy2 = [[' ', '_', '_', '_', '_', '_', ' '],
          ['/', '-', '-', '-', '-', '-', '\\'],
          ['H', 'H', ' ', ' ', ' ', 'H', 'H'],
          ['H', 'H', ' ', ' ', ' ', 'H', 'H'],
          ['O', 'O', ' ', ' ', ' ', 'O', 'O']]

L = [['|', ' ', ' '],
     ['|', ' ', ' '],
     ['|', '_', '_']]

E = [[' ', '_', '_'],
     ['|', '_', '_'],
     ['|', '_', '_']]
V = [['|', ' ', '|'],
     ['\\', ' ', '/'],
     [' ', 'V', ' ']]
One = [['/', '|', ' '],
       [' ', '|', ' '],
       ['_', '|', '_']]
Two = [[' ', '_', '_', ' ', ' ', ' '],
       ['/', ' ', ' ', '\\', ' ', ' '],
       [' ', ' ', '/', '_', '_', '_']]

bossEnemy = [['|', ' ', '\\', ' '],
             ['|', ' ', ' ', '\\'],
             ['|', ' ', '\\', ' '],
             ['|', ' ', ' ', '\\'],
             ['|', ' ', '\\', ' '],
             ['|', ' ', ' ', '\\'],
             ['|', ' ', '\\', ' '],
             ['|', ' ', ' ', '\\']]
