import random
import time

def main():
    DIM = 20
    board = []
    board2 = []

    for i in range(0, DIM):
        board.append([])
        board2.append([])

    for i in range(0, DIM):
        for j in range(0, DIM):
            board[i].append(random.randint(0, 1))
            board2[i].append(0)

    for i in range(0, DIM):
        for j in range(0, DIM):
            print(board[i][j], end=" ")
        print()

    print("--------")

    for i in range(0, DIM):
        for j in range(0, DIM):
            print(board2[i][j], end=" ")
        print()

    for i in range(0, DIM):
        for j in range(0, DIM):
            board2[i][j] = board[i][j]

    print("--------")

    for i in range(0, DIM):
        for j in range(0, DIM):
            print(board2[i][j], end=" ")
        print()


main()