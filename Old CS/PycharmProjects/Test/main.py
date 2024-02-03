import random

class Domino:
    def __init__(self, a=0, b=0):
        if a < 0 or a > 6:
            a = 0
        if b < 0 or b > 6:
            b = 0
        self.__a = a
        self.__b = b

    def __lt__(self, other):
        if self.__a < other.__a:
            return True
        if self.__a > other.__a:
            return False
        return self.__b < other.__b

    def value(self):
        return self.__a, self.__b

    def print(self):
        print(str(self.__a)+":"+str(self.__b))

class Boneyard:
    def __init__(self):
        self.__yard = []
        for i in range(7):
            for j in range(i, 7):
                self.__yard.append(Domino(i, j))

    def print(self):
        for d in self.__yard:
            d.print()

    def size(self):
        return len(self.__yard)

    def shuffle(self):
        random.shuffle(self.__yard)

    def arrange(self):
        self.__yard.sort()




def main():
    yard = Boneyard()
    yard.print()
    print("---------------------------------")
    yard.shuffle()
    yard.print()
    print("---------------------------------")
    yard.arrange()
    yard.print()

main()