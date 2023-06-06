package main

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
