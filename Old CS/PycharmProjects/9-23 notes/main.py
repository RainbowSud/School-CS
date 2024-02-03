
def max(a,b):
    if a>b: return a

    return b

def print1tox(x):
    for i in range (1,x):
        print(i)

def add1(x):
    return x+1

def main():
    myAnswer = max(2,3)
    print(myAnswer)

    print("+++++++++++++++++++")

    print(max(40,100))

    print("+++++++++++++++++++")

    print1tox(7)
    print("+++++++++++++++++++")
    print1tox(5)

    print("+++++++++++++++++++")

    x = 1
    print(add1(x))
    print(x)

main()
