def getMeOuttaHere(x, y):
    y = x*2
    return x, y


def main():
    a = 5
    b = 6
    a, b = (getMeOuttaHere(a, b))
    print(a, b)


main()
