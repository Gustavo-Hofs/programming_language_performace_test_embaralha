package main

/*
Desafio:
1. Cria um baralho de N cartas;
2. A carta do topo é removida e separada do baralho;
3. A próxima carta é movida para a base do baralho;
4. Repete até que sobre uma carta;

INPUT: número de cartas (int);
OUTPUT: array com cartas removidas na sequência
    e última carta que restou ([]int,int);
*/

func Embaralha(n int) ([]int, int) {
	initial_deck := make([]int, n)
	for i := 0; i < n; i++ {
		initial_deck[i] = i + 1
	}
	remaning_cards := []int{}
	for len(initial_deck) > 1 {
		remaning_cards = append(remaning_cards, initial_deck[0])
		initial_deck = append(initial_deck[2:], initial_deck[1])
	}
	return remaning_cards, initial_deck[0]
}

func Embaralha2(n int) ([]int, int) {
	initial_deck := make([]int, n)
	for i := 0; i < n; i++ {
		initial_deck[i] = i + 1
	}
	remaning_cards := make([]int, n-1)
	i := 0
	for len(initial_deck) > 1 {
		remaning_cards[i] = initial_deck[0]
		i += 1
		initial_deck = append(initial_deck[2:], initial_deck[1])
	}
	return remaning_cards, initial_deck[0]
}
