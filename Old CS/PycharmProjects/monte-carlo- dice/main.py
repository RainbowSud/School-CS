import random

POINTS = 10000000

def main():
    inCircle = 0

    for i in range(0, POINTS):
        x = random.random()
        y = random.random()
        if (x*x + y*y) <1:
            inCircle += 1

        pi = float(inCircle)/POINTS * 4.0

    print(pi)


main()