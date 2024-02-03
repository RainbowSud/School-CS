import random
import time


# write all your code below this line
class Card:
    def __init__(self, num=1, suit="S"):
        self.__num = num
        self.__suit = suit

    def __lt__(self, other):
        if ord(self.__suit) < ord(other.__suit):
            return True
        elif ord(self.__suit) > ord(other.__suit):
            return False
        elif ord(self.__suit) == ord(other.__suit):
            return True

    def print(self):
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
            print(str("A") + suit, end=" ")
        elif self.__num == 11:
            print(str("J") + suit, end=" ")
        elif self.__num == 12:
            print(str("Q") + suit, end=" ")
        elif self.__num == 13:
            print(str("K") + suit, end=" ")
        else:
            print(str(self.__num) + suit, end=" ")

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
    def __init__(self):
        self.__deck = []
        for i in range(9827, 9823, -1):
            for j in range(1, 14):
                if j == 1:
                    j = "A"
                elif j == 11:
                    j = "J"
                elif j == 12:
                    j = "Q"
                elif j == 13:
                    j = "K"
                self.__deck.append(Card(i, j))

    def print(self):
        for d in self.__deck:
            print(d)

    def shuffle(self):
        random.shuffle(self.__deck)

    def arrange(self):
        self.__deck.sort()

    def restore(self):
        self.__deck = []
        for i in range(9827, 9823, -1):
            for j in range(1, 14):
                if j == 1:
                    j = "A"
                elif j == 11:
                    j = "J"
                elif j == 12:
                    j = "Q"
                elif j == 13:
                    j = "K"
                self.__deck.append(str(j) + chr(i))

    def deal(self):
        return self.__deck.pop()

    def numCards(self):
        return len(self.__deck)

class Hand:
    def __init__(self):
        self.__hand = []

    def addCard(self, card):
        self.__hand.append(card.print())

    def numCards(self):
        return len(self.__hand)

    def print(self):
        for d in self.__hand:
            print(d)


    def printBlackJackDealer(self):
        for d in self.__hand:
            print(d)
    # print the cards currently in the hand, without newlines
    # replace the first card with "??" to hide it
    # see example output for details

    def blackJackValue(self):
        print("gay")

# return the blackjack value of this hand
# aces are worth 11 unless that causes a bust.
# then the minimum number of aces are counted as 1s
# so that no bust occurs. ("bust" == any value over 21)


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
    #    game = BlackJackGame()
    #    game.play()

    test()


main()
