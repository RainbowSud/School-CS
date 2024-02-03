
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():

    for i in range(101):
        print(i, ":", fact(i))

    for i in range(101):
        print(i, ":", fib(i))


main()

