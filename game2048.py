import numpy
import random
import sys
import os


class Game(object):
    def __init__(self):
        self.dimension = 4
        self.matrix = numpy.zeros((self.dimension, self.dimension))
        self.score = 0
        self.hasMoved = True

    def isFull(self):
        if numpy.any(self.matrix == 0):
            return False
        return True

    def isOver(self):
        if not self.isFull():
            return False
        for row in range(4):
            for column in range(3):
                if self.matrix[row][column] == self.matrix[row][column + 1]:
                    return False
        for column in range(4):
            for row in range(3):
                if self.matrix[row][column] == self.matrix[row + 1][column]:
                    return False

        return True

    def isWin(self):
        if max(self.matrix) == 2048:
            return True
        return False

    def setNewNum(self):
        if self.hasMoved:
            zeroList = []
            for row in range(4):
                for column in range(4):
                    if self.matrix[row][column] == 0:
                        zeroList.append([row, column])
            if len(zeroList) != 0:
                x = random.sample(zeroList, 1)
                self.matrix[x[0][0]][x[0][1]] = random.randrange(2, 5, 2)

    def leftMove(self):
        lastMatrix = self.matrix.copy()
        for i in range(4):
            rowList = list(self.matrix[i])
            while 0 in rowList:
                rowList.remove(0)
            x = 0
            while x < len(rowList) - 1:
                if rowList[x] == rowList[x + 1]:
                    rowList[x] = 2 * rowList[x]
                    self.score = self.score + rowList[x]
                    rowList[x + 1] = 0
                    x = x + 2
                else:
                    x = x + 1
            while 0 in rowList:
                rowList.remove(0)
            while len(rowList) < 4:
                rowList.append(0)
            self.matrix[i] = rowList
        if (lastMatrix == self.matrix).all():
            self.hasMoved = False
        else:
            self.hasMoved = True

    def rightMove(self):
        self.matrix = numpy.flip(self.matrix, axis=1)
        self.leftMove()
        self.matrix = numpy.flip(self.matrix, axis=1)

    def upMove(self):
        self.matrix = numpy.transpose(self.matrix)
        self.leftMove()
        self.matrix = numpy.transpose(self.matrix)

    def downMove(self):
        self.matrix = numpy.transpose(self.matrix)
        self.rightMove()
        self.matrix = numpy.transpose(self.matrix)

    def restart(self):
        self.__init__()
        self.setNewNum()
        self.setNewNum()
        self.printMatrix()
        self.printScore()

    def Operation(self):
        while True:
            operation = input("W(up) S(down) A(left) D(right) Q(quit) R(restart)")
            if operation == "w":
                self.upMove()
                break
            elif operation == "s":
                self.downMove()
                break
            elif operation == "a":
                self.leftMove()
                break
            elif operation == "d":
                self.rightMove()
                break
            elif operation == "q":
                sys.exit()
            elif operation == "r":
                self.restart()
            else:
                print("Wrong input!")
                continue

    def printMatrix(self):
        print(self.matrix)

    def printScore(self):
        print('Score:', self.score)

    def isWin(self):
        if self.matrix.max() == 2048:
            return True
        return False


if __name__ == "__main__":
    game = Game()
    game.setNewNum()
    game.setNewNum()
    game.printMatrix()
    while True:
        game.Operation()
        os.system("clear")
        if game.isWin():
            print('You WIN!!')
            break
        if game.isOver():
            print('Game Over!')
            break
        game.setNewNum()
        game.printMatrix()
        game.printScore()
