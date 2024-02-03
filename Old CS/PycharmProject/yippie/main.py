
def hanoi(n, s, d, x):
    if n == 0: return
    hanoi(n-1, s, x, d)
    print("move disc from", s, "to", d)
    hanoi(n-1, x, d, s)





def main():

    hanoi(5, "A", "B", "C")

main()