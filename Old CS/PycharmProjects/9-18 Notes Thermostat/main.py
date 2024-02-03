setTemp = 60
currentTemp = 65

for i in range(90,50,-5):
    if (setTemp>=i) and (setTemp<i+5):
        print("    ", setTemp,"=>  ",end="")
    print(i)



