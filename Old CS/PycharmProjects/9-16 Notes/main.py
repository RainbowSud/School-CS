import random

numberOfQuestions = 5

while numberOfQuestions > 0:
    print("You have", numberOfQuestions, "questions remaining.")
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    sum = number1 + number2

    print("what is ",number1, "+ ", number2,"?")
    response = eval(input())

    if response == sum:
        print("Good job!", sum, "is the correct answer!")
    else:
        print("Sorry that's not right ):", sum, "was the correct answer, try again later :D")

    numberOfQuestions -= 1
if numberOfQuestions == 0:
    print("Yay! You are done with the Questions")




