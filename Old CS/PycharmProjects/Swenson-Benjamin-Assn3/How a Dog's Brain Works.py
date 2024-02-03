print("        Today we will explore how a dogs brain works,\n"
      "        pretend you are a dog and respond to each question with either a \"y\" or a \"n\"\n"
      "        and you will see just how a dogs brain works. ")

response = input("Start: \nIs it an object?")

if response == 'n':
    response = input("Is it a sound?")
    if response == 'n':
        print("Ignore it")
        print("This has concluded the dog brain test")
    else:
        print("Bark at it")
        print("This has concluded the dog brain test")
else:
    response = input("Can you eat it?")
    if response == 'n':
        response = input("Is it a tennis ball?")
        if response == 'n':
            print("Bark at it")
            print("This has concluded the dog brain test")
        else:
            print("Pick it up")
            print("Return to owner")
            print("This has concluded the dog brain test")
    else:
        print("Eat it")
        response = input("Was it good?")
        if response == 'n':
            print("Puke it out")
            print("Re-eat it")
            print("This has concluded the dog brain test")
        else:
            print("Wag your tail")
            print("This has concluded the dog brain test")


