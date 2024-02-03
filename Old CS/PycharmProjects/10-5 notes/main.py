
class Worm:

    def __init__(self, weight=5, name="generic worm"):
        self.__weight = weight
        self.odometer = 0
        self.name = name

    def getWeight(self):
        return self.__weight

    def getOdometer(self):
        return self.odometer

    def getName(self):
        return self.name

    def crawl(self, inches):
        if self.__weight <= 5:
            return
        oldOdometer = self.odometer
        self.odometer += inches
        self.poop(self.odometer//5-oldOdometer//5)

    def eat(self, kibbles):
        self.__weight += kibbles

    def poop(self, nugget):
        self.__weight -= nugget
        if self.__weight < 5:
            self.__weight = 5

    def status(self):
        print(self.name, ":\t", end="")
        print("weight =", self.__weight, "\todometer =", self.odometer)

def feedWorm(myWorm):
    myWorm.eat(10)

def main():
    mable = Worm(weight=15, name="mable")
    oliver = Worm(weight=25, name="oliver")
    daphney = Worm(3343, "daphney")

    mable.status()
    mable.crawl(12)
    mable.status()

    oliver.status()
    feedWorm(oliver)
    oliver.status()

    
main()
