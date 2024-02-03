print("\n\n\nLet us answer the question \"Are you Meat Loaf?\"\n\n")
response = input("Would you do anything for love? [y/n]")

if response == 'n':
    print("\nYou are not Meat loaf\n")
else:
    response = input("Even that? [y/n]")
    if response == 'y':
        print("\nYou are not Meat loaf")
    else:
        print("\nYou are Meat Loaf")