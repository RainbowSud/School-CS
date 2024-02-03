def linePattern(n):
    print("--------------")
    print("Line Pattern")
    for i in range(1, n+1):
        print("*", end="")
    print()

def squarePattern(n):
    print("--------------")
    print("Square Pattern")
    for j in range(1, n+1):
        for i in range(1, n+1):
            print("*", end="")
        print()

def wedgePatternLeft(n):
    print("--------------")
    print("Wedge Pattern - Left Bound")
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            print("*", end="")
        print()

def wedgePatternRight(n):
    print("--------------")
    print("Wedge Pattern - Right Bound")
    for j in range(1, n+1):
        for i in range(n-j, 0, -1):
            print(" ", end="")

        for i in range(1, j+1):
            print("*", end="")
        print()

def treePattern(n):
    print("--------------")
    print("Tree Pattern")
    for j in range(1, n + 1):
        for i in range(n - j, 0, -1):
            print(" ", end="")

        for i in range(1, 2*j):
            print("*", end="")
        print()

def boxPattern(n):
    print("--------------")
    print("Box Pattern")
    for j in range(1, n + 1):
        if j == 1 or j == n:
            for i in range(1, n + 1):
                print("*", end="")
        else:
            for i in range(1, n + 1):
                if i == 1 or i == n:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()


def main():
    response = eval(input("choose a number "))
    print("n=", response)
    linePattern(response)
    squarePattern(response)
    wedgePatternLeft(response)
    wedgePatternRight(response)
    treePattern(response)
    boxPattern(response)



main()