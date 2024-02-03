# Benjamin Swenson - CS1400 - Section 1 - Assignment 9
import random
import time

# write all your code below this line
class Card:
    # Defines my two variables for Card
    def __init__(self, num=1, suit="S"):
        self.__num = num
        self.__suit = suit

    # Overrides the < operator and defines it in this way, allows my sort function to work
    def __lt__(self, other):
        t1 = self.__suit, self.__num
        t2 = other.__suit, other.__num
        return t1 < t2

    # I added this function in to make the blackjack hand total so much easier, by creating a getter
    # I was able to sum everything up much easier then any other way I could think of
    def getNum(self):
        return self.__num

    # This is my print function - It prints my card in the way I want it to look
    def print(self):
        # This set of blocks converts the suit as a letter into the suit character itself
        if self.__suit == "S":
            suit = chr(9824)
        elif self.__suit == "D":
            suit = chr(9826)
        elif self.__suit == "H":
            suit = chr(9825)
        elif self.__suit == "C":
            suit = chr(9827)
        else:
            suit = chr(63)
        # This set of blocks converts numbers into letters for aces, jacks, queens, and kings - Also prints everything
        if self.__num == 1:
            print(str("A") + suit, end=" ")
        elif self.__num == 11:
            print(str("J") + suit, end=" ")
        elif self.__num == 12:
            print(str("Q") + suit, end=" ")
        elif self.__num == 13:
            print(str("K") + suit, end=" ")
        else:
            print(str(self.__num) + suit, end=" ")

    # Okay so this is like, in order to get my output to match what was given I added this function only for when
    # I am printing out the deck itself, I can't have the end=" " part because then it won't closely match the output
    # Given to me, I personally like it better printing out every card on the same line, but I added this to match
    # The given output. (Exact same as ^ but without end=" "
    def print2(self):
        if self.__suit == "S":
            suit = chr(9824)
        elif self.__suit == "D":
            suit = chr(9826)
        elif self.__suit == "H":
            suit = chr(9825)
        elif self.__suit == "C":
            suit = chr(9827)
        else:
            suit = chr(63)
        if self.__num == 1:
            print(str("A") + suit)
        elif self.__num == 11:
            print(str("J") + suit)
        elif self.__num == 12:
            print(str("Q") + suit)
        elif self.__num == 13:
            print(str("K") + suit)
        else:
            print(str(self.__num) + suit)

    # This function gives the value of 10 to all face cards, and the value of 11 to Ace
    def blackJackValue(self):
        if self.__num == 1:
            return 11
        elif self.__num == 11:
            return 10
        elif self.__num == 12:
            return 10
        elif self.__num == 13:
            return 10
        else:
            return self.__num


class Deck:
    # Here I make the deck, The first for loop defines the suit, the second one adds the value, then the append
    # Adds a card object to the list, the reason the numbers are so high is I was first trying out a way
    # That wasn't working by changing the number into the suit character, this was before I understood
    # A lot of what I know now, and I'm too lazy to change those numbers to like 1-4 so it's just weird numbers
    # But it works the same, so yeah.
    def __init__(self):
        self.__deck = []
        for i in range(9827, 9823, -1):
            if i == 9827:
                i = "C"
            elif i == 9826:
                i = "D"
            elif i == 9825:
                i = "H"
            elif i == 9824:
                i = "S"
            for j in range(1, 14):
                self.__deck.append(Card(j, i))

    # Really simple - prints out the deck (print2 is to get rid of end=" ")
    def print(self):
        for d in self.__deck:
            d.print2()

    # Shuffles the deck given the importation of random
    def shuffle(self):
        random.shuffle(self.__deck)

    # Sorts the deck via the < override I did
    def arrange(self):
        self.__deck.sort()

    # This copies the first creation of the deck - just recreates the deck to restore it. quick and simple
    def restore(self):
        self.__deck = []
        for i in range(9827, 9823, -1):
            if i == 9827:
                i = "C"
            elif i == 9826:
                i = "D"
            elif i == 9825:
                i = "H"
            elif i == 9824:
                i = "S"
            for j in range(1, 14):
                self.__deck.append(Card(j, i))

    # This just pops out the top card of the deck and returns it
    def deal(self):
        return self.__deck.pop()

    # Returns the length of the deck - simple function
    def numCards(self):
        return len(self.__deck)


class Hand:
    # Creates the hand as an empty list
    def __init__(self):
        self.__hand = []

    # Appends the hand with a card object
    def addCard(self, card):
        self.__hand.append(card)

    # Returns the length of the string
    def numCards(self):
        return len(self.__hand)

    # Prints out the card objects that are in the hand, calls the card print function
    def print(self):
        for d in self.__hand:
            d.print()

    # I need to print the first card as ??, so what I came up with was to just print those ??, then remove that
    # Corresponding card from the deck, print the rest of the deck out, and then add that card back in,
    # In the same position I took it out from, to restore the hand to the proper cards
    def printBlackJackDealer(self):
        print("??", end=" ")
        s = self.__hand.pop(0)
        for d in self.__hand:
            d.print()
        self.__hand.insert(0, s)

    # This is where I use my getter, I just get the number of that card, then the first line assumes A is a 11
    # But the line 190 shows that if that A being 11 busts, then it choses A to be 1 and reruns all the calculations
    def blackJackValue(self):
        print(end="")
        sum = 0
        sum2 = 0
        for d in self.__hand:
            c = d.getNum()
            if c == 1:
                c = 11
            elif c == 11:
                c = 10
            elif c == 12:
                c = 10
            elif c == 13:
                c = 10
            sum += c
        if sum > 21:
            for d in self.__hand:
                c = d.getNum()
                if c == 1:
                    c = 1
                elif c == 11:
                    c = 10
                elif c == 12:
                    c = 10
                elif c == 13:
                    c = 10
                sum2 += int(c)
                sum = sum2
        return sum

# write all your code above this line


class BlackJackGame:
    def __init__(self):
        self.__d = Deck()
        self.__d.shuffle()

    def displayLine(self, who, hand):
        # print a "hand" line of the output
        print(who + ": ", end="")
        print(" (" + str(hand.blackJackValue()) + ")\t", end="")
        hand.print()
        if hand.numCards() <= 5: print("\t", end="")
        if hand.numCards() <= 3: print("\t", end="")

    def pickWinner(self, n, dn, b, db, pf, df):
        # print out the winner of the hand
        print()
        if n and not dn:
            print("\t\tyou win!")
        elif n and dn:
            print("\t\t(push)")
        elif not n and dn:
            print("\t\tdealer wins.")
        elif b and not db:
            print("\t\tdealer wins.")
        elif not b and db:
            print("\t\tyou win!")
        elif pf == df:
            print("\t\t(push)")
        elif pf > df:
            print("\t\tyou win!")
        else:
            print("\t\tdealer wins.")
        print()

    def play(self):
        print()
        print("        Welcome to Simple BlackJack")
        print()

        # the main event loop
        while True:
            # dealer reshuffles cards when 75% dealt
            if self.__d.numCards() < 14:
                print("\t\t\t\t\tDealer shuffles the deck")
                self.__d.restore()
                self.__d.shuffle()

            # dealer and player each have a hand
            dealer = Hand()
            player = Hand()

            # flags used to determine the eventual winner
            natural = False
            dnatural = False
            busted = False
            dbusted = False
            playerfinal = 0
            dealerfinal = 0

            # dealer gets a hand
            dealer.addCard(self.__d.deal())
            dealer.addCard(self.__d.deal())

            # dealer hand displayed with one card hidden
            print("dealer" + ": ", end="")
            print(" (??)\t", end="")
            dealer.printBlackJackDealer()
            print()

            # player gets a hand
            player.addCard(self.__d.deal())
            player.addCard(self.__d.deal())

            # check for player natural
            if player.blackJackValue() == 21:
                self.displayLine("player", player)
                print("natural blackjack!")
                natural = True

            # player get more cards if desired
            while player.blackJackValue() < 21:
                self.displayLine("player", player)
                response = input("hit? [y/n] ")
                if response == "n": break
                player.addCard(self.__d.deal())

            # find final player status for hand
            self.displayLine("player", player)
            playerfinal = player.blackJackValue()
            if playerfinal == 21 and not natural:
                print("blackjack!")
            elif playerfinal > 21:
                print("you busted.")
                busted = True
            else:
                print("you hold.")

            time.sleep(1)

            # now it is the dealers turn
            if dealer.blackJackValue() == 21:
                self.displayLine("dealer", dealer)
                print("dealer blackjack!")
                dnatural = True

            # if player busted, dealer does nothing
            if busted:
                self.displayLine("dealer", dealer)
                print()

            # dealer gets to add cards if no naturals
            if not natural and not busted:
                while dealer.blackJackValue() <= 15 and not busted:
                    self.displayLine("dealer", dealer)
                    print("dealer hits.")
                    time.sleep(1)

                    dealer.addCard(self.__d.deal())

                # find final dealer status for hand
                self.displayLine("dealer", dealer)
                dealerfinal = dealer.blackJackValue()
                if dealerfinal == 21 and not dnatural:
                    print("dealer blackjack!")
                elif dealerfinal > 21:
                    print("dealer busted.")
                    dbusted = True
                else:
                    print("dealer holds.")
            time.sleep(1)

            # find the winner for this hand
            self.pickWinner(natural, dnatural, busted, dbusted, playerfinal, dealerfinal)

            response = input("\t\t\t\t\tplay again? [y/n] ")
            if response == "n": break

        print("\t\t\t\t\tso long!")
        print()


def cardTest():
    print()
    print("Card Test")
    print()
    c1 = Card()
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    c4 = Card(3, "D")

    c1.print()
    c2.print()
    c3.print()
    c4.print()
    print()
    print(format(c1.blackJackValue(), "3.0f"), end=" ")
    print(format(c2.blackJackValue(), "3.0f"), end=" ")
    print(format(c3.blackJackValue(), "3.0f"), end=" ")
    print(format(c4.blackJackValue(), "3.0f"), end=" ")
    print()
    print()

    c0 = Card(13, "C")
    c1 = Card(1, "D")
    c2 = Card(2, "D")
    c3 = Card(3, "D")
    c4 = Card(10, "D")
    c5 = Card(11, "D")
    c6 = Card(12, "D")
    c7 = Card(13, "D")
    c8 = Card(1, "H")
    c9 = Card(1, "S")
    c0.print()
    c1.print()
    c2.print()
    c3.print()
    c4.print()
    c5.print()
    c6.print()
    c7.print()
    c8.print()
    c9.print()
    print()
    print(c0 < c1)
    print(c1 < c2)
    print(c2 < c3)
    print(c3 < c4)
    print(c4 < c5)
    print(c5 < c6)
    print(c6 < c7)
    print(c7 < c8)
    print(c8 < c9)
    print(c9 < c0)


def deckTest():
    print()
    print("Deck Test")
    print()
    d = Deck()
    d.print()
    print()
    d.shuffle()
    d.print()
    print()
    d.arrange()
    d.print()
    print()
    c0 = d.deal()
    c1 = d.deal()
    c0.print()
    c1.print()
    print()
    print()
    d.print()
    print()
    print(d.numCards())
    d.restore()
    print(d.numCards())
    print()
    d.print()
    print()


def handTest():
    print()
    print("Hand Test")
    print()
    c1 = Card(1, "S")
    c2 = Card(13, "H")
    c3 = Card(3, "C")
    h = Hand()
    h.addCard(c1)
    h.addCard(c2)
    h.print()
    print()
    print(h.numCards())
    h.addCard(c3)
    h.print()
    print()
    print(h.numCards())
    print()

    h2 = Hand()
    h2.addCard(c1)
    h2.addCard(c2)
    h2.printBlackJackDealer()
    print()
    h2.print()
    print("=", h2.blackJackValue())
    print()
    h2.addCard(c3)
    h2.print()
    print("=", h2.blackJackValue())
    print()


def test():
    cardTest()
    deckTest()
    handTest()


def main():
    # game = BlackJackGame()
    # game.play()

    test()


main()
