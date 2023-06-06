use json;
use std::{collections::VecDeque, env};

fn main() {
    let args: Vec<_> = env::args().collect();
    let n = args[1].parse::<i32>().unwrap();
    let (deck, card) = embaralha(n);
    print_result(deck, card);
}

fn print_result(a: Vec<i32>, b: i32) {
    let mut data = json::JsonValue::new_array();
    _ = data.push(a);
    _ = data.push(b);
    println!("{}", data.dump());
}

fn embaralha(n: i32) -> (Vec<i32>, i32) {
    let mut initial_deck = VecDeque::with_capacity(n as usize);
    for i in 0..n {
        initial_deck.push_back(i + 1)
    }
    let mut remaning_cards = vec![];
    while initial_deck.len() > 1 {
        remaning_cards.push(initial_deck.pop_front().unwrap());
        let front_card = initial_deck.pop_front().unwrap();
        initial_deck.push_back(front_card);
    }
    let last_card = initial_deck[0];
    (remaning_cards, last_card)
}
