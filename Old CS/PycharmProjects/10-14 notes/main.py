

class TallyCounter:

    def __init__(self, name = "nobody", resetDisabled = False):
        self.__count = 0
        self.__handHeld = True
        self.__name = name
        self.__resetDisabled = resetDisabled

    def reset(self):
        if self.__resetDisabled = True: return
        self.__count = 0

    def getCount(self):
        return self.__count

    def getName(self):
        return self.__name

    def click(self, numClicks = 1):
        self.__count += numClicks
        if self.__count > 9999:
            self.__count -= 9999


def main():
    busCount = TallyCounter()
    stadiumCount = TallyCounter(name="martin")

    for i in range(1,10):
        busCount.click()
        print(busCount.getCount())
    stadiumCount.click(100000)
    busCount.reset()
    print(stadiumCount.getName())
    print(busCount.getCount())
    print(stadiumCount.getCount())


main()