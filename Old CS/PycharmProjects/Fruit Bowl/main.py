import random

class Fruit:
    def __str__(self):
        return "I am some kind of ... fruit. Maybe a papaya?"

    def whatAmI(self):
        return "I am a fruit"

class Apple(Fruit):
    def __str__(self):
        return "I am an Apple"

class Orange(Fruit):
    def __str__(self):
        return "I am an Orange"

def main():
    fruitBasket = []

    for i in range(10):
        r =  random.randint(1,3)
        if r == 1:
            fruitBasket.append(Fruit())
        if r == 2:
            fruitBasket.append(Apple())
        if r == 3:
            fruitBasket.append(Orange())

    for i in range(10):
        print(fruitBasket[i])


main()
