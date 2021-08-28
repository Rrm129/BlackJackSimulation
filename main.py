from datastructures import *
import random


def readDeck(deck, filename):
    car = open(filename, 'r')
    for i in car:
        card = i.rstrip()
        deck.push(Cards(card))


def shuffle(deck):

    deck1 = Deck()
    deck2 = Deck()
    decksize = deck.size()

    for i in range(decksize):
        if deck.size() == decksize/2:
            break
        deck1.push(deck.top())
        deck.pop()

    for i in range(decksize):
        if deck.isEmpty():
            break
        deck2.push(deck.top())
        deck.pop()

    for i in range(deck1.size() + deck2.size()):
        if deck2.isEmpty():
            break
        deck.push(deck1.top())
        deck1.pop()
        deck.push(deck2.top())
        deck2.pop()


def FisherYates(deck):
    # Much better than the regular sorting because this is true random.
    # The other algorithm has a pattern so it is not efficient as the Fisher Yates that
    # changes the order o each node with a completely random node of the stack.
    # It should not be used for a trading card game.

    deck2 = Deck()
    n = deck.size()
    for i in range(deck.size()-1, 0, -1):

        loc = random.randint(0, n-1)
        deck2.push(deck.getInnerNode(loc))
        deck.deleteInnerNode(loc)
        n -= 1
        if n == 1:
            deck2.push(deck.top())
            deck.pop()
            break

    deck.copyStack(deck2)


def main():

    file = "Cards.txt"
    playerDeck = Deck()
    dealerDeck = Deck()
    mainDeck = Deck()

    # Three decks used
    readDeck(mainDeck, file)
    readDeck(mainDeck, file)
    readDeck(mainDeck, file)

    g = Game(playerDeck, dealerDeck, mainDeck)
    FisherYates(g.mainDeck)

    n = 1
    while g.mainDeck.size() > 5:

        print('Game #', n)
        g.start()
        g.results()

        n += 1

    g.showScore()


if __name__ == '__main__':
    main()
