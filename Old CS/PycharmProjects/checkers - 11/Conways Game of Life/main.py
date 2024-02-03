import random
import time

class Game:
    def __init__(self):
        self.__size = 22  # Used to calculate the size of the board
        self.__CGBoard = []  # Current Generation Board
        self.__NGBoard = []  # Next Generational Board

    def boardCreation(self):
        for i in range(0, self.__size):
            self.__CGBoard.append([])
            self.__NGBoard.append([])

    def NGboardAddition(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__NGBoard[i].append(" ")

    def CGboardAddition(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if i == 0 or i == self.__size - 1:
                    self.__CGBoard[i].append(" ")
                elif j == 0 or j == self.__size - 1:
                    self.__CGBoard[i].append(" ")
                else:
                    n = random.randint(1, 3)
                    if n == 3:
                        self.__CGBoard[i].append("X")
                    else:
                        self.__CGBoard[i].append(" ")

    def CGboardPrinting(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print(self.__CGBoard[i][j], end=" ")
            print()


    def NGequalCG(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__NGBoard[i][j] = self.__CGBoard[i][j]

    def CGequalNG(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                self.__CGBoard[i][j] = self.__NGBoard[i][j]

    def nextGeneration(self):
        for i in range(1, self.__size - 1):
            for j in range(1, self.__size - 1):
                n = 0
                if self.__CGBoard[i + 1][j] == "X":
                    n += 1
                if self.__CGBoard[i - 1][j] == "X":
                    n += 1
                if self.__CGBoard[i][j + 1] == "X":
                    n += 1
                if self.__CGBoard[i][j - 1] == "X":
                    n += 1
                if self.__CGBoard[i-1][j-1] == "X":
                    n += 1
                if self.__CGBoard[i-1][j+1] == "X":
                    n += 1
                if self.__CGBoard[i+1][j-1] == "X":
                    n += 1
                if self.__CGBoard[i+1][j+1] == "X":
                    n += 1
                if n == 0 and self.__CGBoard[i][j] == "X":
                    self.__NGBoard[i][j] = " "
                if n == 1 and self.__CGBoard[i][j] == "X":
                    self.__NGBoard[i][j] = " "
                if n == 3 and self.__CGBoard[i][j] == " ":
                    self.__NGBoard[i][j] = "X"
                if n >= 4 and self.__CGBoard[i][j] == "X":
                    self.__NGBoard[i][j] = " "


def main():
    gol = Game()
    gol.boardCreation()
    gol.CGboardAddition()
    gol.NGboardAddition()
    gol.NGequalCG()
    gol.CGboardPrinting()
    print("Generation: 1")
    gen = 1
    while True:
        gol.nextGeneration() # CG is gen 2 , NG is gen 3
        gol.CGequalNG() # CG is gen 2, NG is gen 2
        gol.CGboardPrinting()
        gen += 1
        print("Generation:", gen)
        time.sleep(.3)


main()
