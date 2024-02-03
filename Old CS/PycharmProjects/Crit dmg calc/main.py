def calc(cr, cd):
    crits = int(cr)
    noncrits = 100 - int(cr)
    dmg = 100 + int(cd)
    output = (dmg * crits) + ( 100 * noncrits)
    return output

def main():
    cr1 = eval(input("What is your first Crit Rate %?"))
    cd1 = eval(input("What is your first Crit DMG %?"))
    cr2 = eval(input("What is your second Crit Rate %?"))
    cd2 = eval(input("What is your second Crit DMG %?"))
    print("Your total DMG assuming 100 hits, with 100 base dmg is:", calc(cr1, cd1))
    print("Your total DMG assuming 100 hits, with 100 base dmg is:", calc(cr2, cd2))

main()