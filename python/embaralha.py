#!/usr/bin/env python3


import sys


def embaralha(n):
    initial_deck = [i + 1 for i in range(n)]
    remaning_cards = []
    while len(initial_deck) > 1:
        remaning_cards.append(initial_deck.pop(0))
        initial_deck = initial_deck[1:] + initial_deck[:1]
    return remaning_cards, initial_deck[0]


if __name__ == "__main__":
    deck, card = embaralha(int(sys.argv[1]))
    print("[[" + ','.join([str(i) for i in deck]) + "]," + str(card) + "]")
