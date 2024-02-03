import math

class Circle:

    def __init__(self, radius = 1):
        if radius < 0: radius *= -1
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getCircumference(self):
        return self.__radius*2*math.pi

def main():
    circle1 = Circle(5)
    print(circle1.getRadius())
    print(circle1.getCircumference())


main()