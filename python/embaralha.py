#!/usr/bin/env python3

'''
Desafio:
1. Cria um baralho de N cartas;
2. A carta do topo é removida e separada do baralho;
3. A próxima carta é movida para a base do baralho;
4. Repete até que sobre uma carta;

INPUT: número de cartas (int);
OUTPUT: array com cartas removidas na sequência
    e última carta que restou ([]int,int);

Inspiração: https://www.youtube.com/live/PP8NazoBjHU?feature=share
'''

import sys
#import json
#from numba import njit


#@njit
def embaralha(n):
    '''
    Recebe número de cartas a serem criadas e embaralhadas "n",
    retorna lista removida "remaning_cards" e ultima carta do baralho.
    '''
    initial_deck = [i + 1 for i in range(n)]
    remaning_cards = []
    while len(initial_deck) > 1:
        remaning_cards.append(initial_deck.pop(0))
        initial_deck = initial_deck[1:] + initial_deck[:1]
    return remaning_cards, initial_deck[0]


if __name__ == "__main__":
    deck, card = embaralha(int(sys.argv[1]))
    # print(deck, card)
    # print("["+' '.join([str(i) for i in deck])+"]", card)
    #print(json.dumps([deck, card], separators=(',', ':')))
    print("[["+','.join([str(i) for i in deck])+"],"+str(card)+"]")
