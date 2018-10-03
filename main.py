import input
import config
import board
import obstacle
import character
import time
import os
from colorama import Fore

totalScore = 0
totalLives = 3
canProgressToLevel2 = 0


def level1():
    import input
    import config
    import board
    import obstacle
    import character

    groundList = []
    cloudList = []
    pipeList = []
    enemyList1 = []
    enemyList2 = []
    blockList = []

    test = 0

    L1 = obstacle.L()
    E1 = obstacle.E()
    V1 = obstacle.V()
    E2 = obstacle.E()
    L2 = obstacle.L()
    One1 = obstacle.One()

    L1.setPosition(5, 2)
    E1.setPosition(10, 2)
    V1.setPosition(15, 2)
    E2.setPosition(20, 2)
    L2.setPosition(25, 2)
    One1.setPosition(30, 2)

    getCharacter = input.inputFunctionClass()
    board = board.Board()
    board.clearMatrix()
    mario = character.Mario()

    mario.setPosition(5, 5)
    mario.drawOntoBoard(board)

    for i in range(0, board.width() - 4, 4):
        tempGround1 = obstacle.Ground()
        tempGround1.setPosition(i, board.height() + 1 - board.height() // 6)
        groundList.append(tempGround1)
        del tempGround1

    count = 0
    for i in range(60, board.levelOne() - len(config.cloud[0]), 60):
        tempCloud = obstacle.Cloud()
        tempCloud.setPosition(i, config.randomInteger(0, 10))
        cloudList.append(tempCloud)
        del tempCloud
    del count

    for i in range(60, board.levelOne(), 80):
        tempPipe = obstacle.Pipe()
        tempPipe.setPosition(config.randomInteger(
            i + 0, i + 15), board.height() - groundList[0].height() - tempPipe.height())
        pipeList.append(tempPipe)
        del tempPipe

    for i in range(70, board.levelOne() - 25, 80):
        tempEnemy = character.miniEnemy1()
        tempEnemy.setPosition(config.randomInteger(
            i, i + 30), board.height() - groundList[0].height() - tempEnemy.height())
        enemyList1.append(tempEnemy)
        del tempEnemy

    for i in range(150, board.levelOne() - 25, 80):
        tempEnemy = character.miniEnemy2()
        tempEnemy.setPosition(config.randomInteger(
            i, i + 30), board.height() - groundList[0].height() - tempEnemy.height())
        enemyList2.append(tempEnemy)
        del tempEnemy

    for i in range(80, board.levelOne() - 20, 50):
        tempBlock = obstacle.unDestroyableBlock()
        tempBlock2 = obstacle.unDestroyableBlock()
        tempBlock3 = obstacle.destroyableBlock()
        height = config.randomInteger(7, 17)
        tempBlock.setPosition(i, height)
        tempBlock2.setPosition(i+6, height)
        tempBlock3.setPosition(i+3, height)
        blockList.append(tempBlock)
        blockList.append(tempBlock2)
        blockList.append(tempBlock3)
        del tempBlock, tempBlock2, tempBlock3

    while (config.gameLoop):
        # tempBlock = obstacle.unDestroyableBlock ()
        # tempBlock2 = obstacle.unDestroyableBlock ()
        # tempBlock3 = obstacle.destroyableBlock ()
        # tempBlock.setPosition (45, 17)
        # tempBlock2.setPosition (51, 17)
        # tempBlock3.setPosition (48, 17)

        # print (board.height(), board.width (), mario._downwardVelocity)

        board.clearMatrix()

        L1.drawOntoBoard(board)
        E1.drawOntoBoard(board)
        V1.drawOntoBoard(board)
        E2.drawOntoBoard(board)
        L2.drawOntoBoard(board)
        One1.drawOntoBoard(board)

        for i in groundList:
            i.drawOntoBoard(board)

        for i in cloudList:
            i.drawOntoBoard(board)

        for i in pipeList:
            i.drawOntoBoard(board)
            if i.position.x < board.x:
                pipeList.pop(0)

        mario.drawOntoBoard(board)

        for i in range(len(enemyList1)):
            if enemyList1[i].checkIfPlayerAbove(mario) is True:
                enemyList1.pop(i)
                break
                mario.increaseScore(10)

            if enemyList1[i].checkIfPlayerLeft(mario) is True:
                mario.decreaseHealth(10)
                enemyList1.pop(i)
                break

            if enemyList1[i].checkIfPlayerRight(mario) is True:
                mario.decreaseHealth(10)
                enemyList1.pop(i)
                break

        for i in range(len(enemyList2)):
            if enemyList2[i].checkIfPlayerAbove(mario) is True:
                enemyList2.pop(i)
                mario.increaseScore(10)
                break

            if enemyList2[i].checkIfPlayerLeft(mario) is True:
                mario.decreaseHealth(50)
                enemyList2.pop(i)
                break

            if enemyList2[i].checkIfPlayerRight(mario) is True:
                mario.decreaseHealth(50)
                enemyList2.pop(i)
                break

        # if board.x > 20:
        # 	config.boardBackground = '/'
        # 	board.changeBackground (config.boardBackground)

        for i in enemyList1:
            if i.position().x < board.x:
                enemyList1.pop(0)
            else:
                if i.direction() is 1:
                    if i.moveRight(board) is True:
                        pass
                    else:
                        i.changeDirection()
                elif i.direction() is 0:
                    if i.moveLeft(board) is True:
                        pass
                    else:
                        i.changeDirection()
                i.applyGravity
                # if test % 5 is 0:
                i.drawOntoBoard(board)

        for i in enemyList2:
            if i.position().x < board.x:
                enemyList2.pop(0)
                break
            else:
                if i.direction() is 1:
                    if i.moveRight(board) is True:
                        pass
                    else:
                        i.changeDirection()
                elif i.direction() is 0:
                    if i.moveLeft(board) is True:
                        pass
                    else:
                        i.changeDirection()
                i.applyGravity
                # if test % 5 is 0:
                i.drawOntoBoard(board)

        # tempBlock.drawOntoBoard (board)
        # tempBlock2.drawOntoBoard (board)
        # tempBlock3.drawOntoBoard (board)
        # if tempBlock3.checkForHit (board) is True:
        # 	mario.increaseScore (1)

        for i in blockList:
            i.drawOntoBoard(board)
            check = i.isDestroyable()
            if i.isDestroyable() is True:
                if i.checkForHit(board) is True:
                    mario.increaseScore(10)

        # tempGround.drawOntoBoard (board)

        # tempCloud.drawOntoBoard (board)
        # tempCloud2.drawOntoBoard (board)
        # tempCloud3.drawOntoBoard (board)

        # mario.applyGravity (board)

        # tempGround1.drawOntoBoard (board)
        # time.sleep (0.1)
        board.printMatrix()
        mario.applyGravity(board)

        # if enemy.direction () is 1:
        # 	if enemy.moveRight (board) is True:
        # 		pass
        # 	else:
        # 		enemy.changeDirection ()
        # elif enemy.direction () is 0:
        # 	if enemy.moveLeft (board) is True:
        # 		pass
        # 	else:
        # 		enemy.changeDirection ()

        # if enemy.direction () is 1 and enemy.moveRight(board) is True:
        # 	enemy.changeDirection ()
        # else:
        # 	enemy.moveRight (board)
        # 	enemy.changeDirection ()
        # if enemy.direction () is 0 and enemy.moveLeft (board) is False:
        # 	# enemy.changeDirection ()
        # 	enemy.moveLeft (board)

        # print (enemy.moveRight(board))

        # if enemy.moveRight(board) is False:
        # 	enemy.changeDirection()

        enteredKey = input.getInput(getCharacter)

        if enteredKey is 'q':
            # time.sleep (0.1)
            config.clear()
            print(Fore.RED, "Thank you for playing!")
            print(Fore.RESET)
            return 'Quit'
        elif enteredKey is 'd':
            # time.sleep (0.1)
            if mario.position().x < ((board.visibleWidth) / 2):
                config.clear()
                mario.moveRight(board)
            else:
                config.clear()
                if mario.moveRight(board) is True:
                    board.x += 2
        elif enteredKey is 'a':
            config.clear()
            mario.moveLeft(board)
        elif enteredKey is 'w':
            # time.sleep (0.1)
            os.system('aplay ./Sounds/jump.wav -q &')
            config.clear()
            mario.jumpUp(board)
        else:
            # time.sleep (0.1)
            config.clear()

        print("Score -", mario.score(), "//", "Health -",
              mario.health(), "//", "Lives Remaining - ", totalLives)

        if mario.health() <= 0:
            config.clear()
            print(Fore.RED, "You Died!!!")
            os.system('aplay ./Sounds/dying.wav -q &')
            break

        if mario.position().x > 280:
            config.clear()
            print("You Cleared Level 1! Congratulations!")
            print("Level 2 will start in 5 seconds!")
            time.sleep(5)
            return True
    return False


def level2():
    import input
    import config
    import board
    import obstacle
    import character

    groundList = []

    L1 = obstacle.L()
    E1 = obstacle.E()
    V1 = obstacle.V()
    E2 = obstacle.E()
    L2 = obstacle.L()
    Two2 = obstacle.Two()

    L1.setPosition(5, 2)
    E1.setPosition(10, 2)
    V1.setPosition(15, 2)
    E2.setPosition(20, 2)
    L2.setPosition(25, 2)
    Two2.setPosition(30, 2)

    board = board.Board()
    board.changeBackground(' ')
    board.clearMatrix

    mario = character.Mario()
    mario.setPosition(5, 5)
    mario.drawOntoBoard(board)

    bossEnemy = character.bossEnemy(config.bossEnemy)
    bossEnemy.setPosition(80, 0)
    bossEnemy.drawOntoBoard(board)

    for i in range(0, board.width() - 4, 4):
        tempGround1 = obstacle.Ground()
        tempGround1.setPosition(i, board.height() + 1 - board.height() // 6)
        groundList.append(tempGround1)
        del tempGround1

    getCharacter = input.inputFunctionClass()

    while True:
        board.clearMatrix()

        L1.drawOntoBoard(board)
        E1.drawOntoBoard(board)
        V1.drawOntoBoard(board)
        E2.drawOntoBoard(board)
        L2.drawOntoBoard(board)
        Two2.drawOntoBoard(board)

        for i in groundList:
            i.drawOntoBoard(board)

        mario.drawOntoBoard(board)
        bossEnemy.drawOntoBoard(board)

        if bossEnemy.checkIfPlayerAbove(mario) is True:
            bossEnemy.decreaseHealth(100)
            mario.jumpUp(board)
            for i in range(25):
                mario.moveRight(board)
        if bossEnemy.checkIfPlayerRight(mario) is True:
            mario.decreaseHealth(25)
        if bossEnemy.checkIfPlayerLeft(mario) is True:
            mario.decreaseHealth(25)

        if mario.position().x < bossEnemy.position().x:
            bossEnemy.moveLeft(board)
        else:
            bossEnemy.moveRight(board)

        board.printMatrix()
        mario.applyGravity(board)
        bossEnemy.applyGravity(board)

        enteredKey = input.getInput(getCharacter)

        if enteredKey is 'q':
            config.clear()
            print(Fore.RED, "Thank you for playing!")
            print(Fore.RESET)
            break
        elif enteredKey is 'd':
            if mario.position().x < ((board.visibleWidth) / 2):
                config.clear()
                mario.moveRight(board)
            else:
                config.clear()
                if mario.moveRight(board) is True:
                    board.x += 2
        elif enteredKey is 'a':
            if mario.position().x < ((board.visibleWidth) / 2):
                config.clear()
                mario.moveLeft(board)
            else:
                config.clear()
                if mario.moveLeft(board) is True:
                    board.x -= 2
        elif enteredKey is 'w':
            os.system('aplay ./Sounds/jump.wav -q &')
            config.clear()
            mario.jumpUp(board)
        else:
            config.clear()

        print("Score -", mario.score(), "//", "Health -", mario.health())
        print("Enemy Score =", bossEnemy.health())

        if bossEnemy.health() < 0:
            config.clear()
            print('YOU WIN!')


while totalLives > 0:
    if canProgressToLevel2 is 1:
        if level2() is False:
            totalLives -= 1
            # level2 ()
    else:
        a = level1()
        if a is False:
            totalLives -= 1
            level1()
        elif a is 'Quit':
            break
        else:
            canProgressToLevel2 = 1
