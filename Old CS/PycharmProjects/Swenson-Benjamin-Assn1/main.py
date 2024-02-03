import math

M = .065
K = 25
G = 9.8

Distance = eval(input("What is the distance to the professor?"))
Angle = eval(input("What is the angle of elevation?"))

X = math.sqrt((M * G * Distance)/(K * math.sin(2 * math.radians(Angle))))

print("You need to pull back", X, "meters")

#cs-1400-MW1 Benjamin Swenson