DIM = 5
numbers = []
sum = 0

for i in range(DIM):
    value = eval(input("enter a number:"))
    numbers.append(value)
    sum += value

for i in range(DIM):
    print(numbers[i])

print("sum is", sum)