# Benjamin Swenson - CS 1400 - Section 1
import random

# the chess piece super class
class ChessPiece:
    def __init__(self, color, x, y):
        self.__color = color
        self.__x = x
        self.__y = y

    def color(self):
        return self.__color

    def location(self):
        return self.__x, self.__y

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# TODO: write all your code below this line
# Every one of these next 6 classes is essentially the same.
# There is an innit function to set up all the variables
# A pic function that determines what the piece should look like based on it's color
# A valid move function that returns true if the move is valid
# The valid move function logic is different for each piece
# The logic calculates based off of that chess pieces valid moves based on the rules of the game
class Pawn(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9823)
        elif self.__c == "w":
            return chr(9817)

    def validMove(self, x, y):
        if self.__c == "b":
            if self.__x == x and self.__y == y + 1:
                return True
            else:
                return False
        elif self.__c == "w":
            if self.__x == x and self.__y == y - 1:
                return True
            else:
                return False

class Queen(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9819)
        elif self.__c == "w":
            return chr(9813)

    def validMove(self, x, y):
        for i in range(8):
            if x == self.__x + i and y == self.__y + i:
                return True
            if x == self.__x + i and y == self.__y - i:
                return True
            if x == self.__x - i and y == self.__y + i:
                return True
            if x == self.__x - i and y == self.__y - i:
                return True
        if self.__x == x:
            return True
        if self.__y == y:
            return True

class King(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9818)
        elif self.__c == "w":
            return chr(9812)

    def validMove(self, x, y):
        if x == self.__x + 1 and y == self.__y + 1:
            return True
        if x == self.__x + 1 and y == self.__y:
            return True
        if x == self.__x + 1 and y == self.__y - 1:
            return True
        if x == self.__x and y == self.__y + 1:
            return True
        if x == self.__x and y == self.__y - 1:
            return True
        if x == self.__x - 1 and y == self.__y + 1:
            return True
        if x == self.__x - 1 and y == self.__y:
            return True
        if x == self.__x - 1 and y == self.__y - 1:
            return True

class Rook(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9820)
        elif self.__c == "w":
            return chr(9814)

    def validMove(self, x, y):
        if self.__x == x:
            return True
        if self.__y == y:
            return True

class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9822)
        elif self.__c == "w":
            return chr(9816)

    def validMove(self, x, y):
        if x == self.__x + 1 and y == self.__y + 2:
            return True
        if x == self.__x + 2 and y == self.__y + 1:
            return True
        if x == self.__x + 2 and y == self.__y - 1:
            return True
        if x == self.__x + 1 and y == self.__y - 2:
            return True
        if x == self.__x - 1 and y == self.__y - 2:
            return True
        if x == self.__x - 2 and y == self.__y - 1:
            return True
        if x == self.__x - 2 and y == self.__y + 1:
            return True
        if x == self.__x - 1 and y == self.__y + 2:
            return True

class Bishop(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.__c = Pawn.color(self)
        self.__x = Pawn.x(self)
        self.__y = Pawn.y(self)

    def pic(self):
        if self.__c == "b":
            return chr(9821)
        elif self.__c == "w":
            return chr(9815)

    def validMove(self, x, y):
        for i in range(8):
            if x == self.__x + i and y == self.__y + i:
                return True
            if x == self.__x + i and y == self.__y - i:
                return True
            if x == self.__x - i and y == self.__y + i:
                return True
            if x == self.__x - i and y == self.__y - i:
                return True

# TODO: write all your code above this line

# print a nice picture of the valid moves
# white pawns only move "up" one space
# black pawns only move "down" one space
# other chess pieces move normally
def printValidMoves(cp):
    print("\t  ", cp.pic(), "at", cp.location())
    for i in range(7, -1, -1):
        print("\t" + str(i) + " ", end="")
        for j in range(0, 8):
            if cp.x() == j and cp.y() == i:
                print(cp.pic() + " ", end="")
            elif cp.validMove(j, i): print("* ", end="")
            else:
                print(". ", end="")
        print()
    print("\t  ", end="")
    for i in range(0, 8):
        print(str(i) + " ", end="")
    print()
    print()


# returns a random chess piece at a random location
# each of these types must inherit from ChessPiece
def randomChessPiece():
    if random.randint(0, 1) == 0:
        c = "w"
    else:
        c = "b"
    t = random.randint(1, 6)
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    if t == 1:
        return Pawn(c, x, y)
    if t == 2:
        return Queen(c, x, y)
    if t == 3:
        return King(c, x, y)
    if t == 4:
        return Rook(c, x, y)
    if t == 5:
        return Knight(c, x, y)
    else:
        return Bishop(c, x, y)

def main():
    clist = []

    # make a list of random chess pieces
    for i in range(0, 10):
        clist.append(randomChessPiece())

    # display their valid moves
    for i in range(0, len(clist)):
        # behold! polymorphism works!
        printValidMoves(clist[i])


main()
