import random

l1 = []

for i in range(8):
    l1.append([])

for i in range(8):
    for j in range(8):
        l1[i].append("X")


for i in range(8):
    for j in range(8):
        print(l1[i][j],end="  ")
    print()